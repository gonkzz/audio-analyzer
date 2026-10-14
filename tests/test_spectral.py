import numpy as np
from audio_painter.spectral import stft


def test_sine_wave_peaks_at_its_frequency():
    sample_rate = 44100
    frame_size = 4096
    frequency = 440

    # One second of an A4 sine wave
    time = np.arange(sample_rate) / sample_rate
    audio = np.sin(2 * np.pi * frequency * time)

    magnitudes, frequencies, times = stft(audio, sample_rate, frame_size=frame_size)

    # The loudest frequency in every frame
    loudest = frequencies[np.argmax(magnitudes, axis=1)]

    # Must be within one FFT bin of 440 Hz
    bin_width = sample_rate / frame_size
    assert np.all(np.abs(loudest - frequency) <= bin_width)


def test_output_shape():
    sample_rate = 44100
    frame_size = 4096
    hop_size = 1024
    audio = np.zeros(sample_rate)

    magnitudes, frequencies, times = stft(
        audio, sample_rate, frame_size=frame_size, hop_size=hop_size
    )

    frame_count = 1 + (len(audio) - frame_size) // hop_size
    bin_count = frame_size // 2 + 1

    assert magnitudes.shape == (frame_count, bin_count)
    assert magnitudes.shape == (len(times), len(frequencies))


def test_silence_gives_zeros():
    sample_rate = 44100
    audio = np.zeros(sample_rate)

    magnitudes, frequencies, times = stft(audio, sample_rate)

    assert np.all(magnitudes == 0)
