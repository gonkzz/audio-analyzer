import numpy as np
from audio_painter.spectral import stft


def test_sine():
    sr = 44100
    n_fft = 4096
    frequency = 440

    # Generate a 1-second A4 sine wave
    t = np.arange(sr) / sr
    x = np.sin(2 * np.pi * frequency * t)

    S, freqs, times = stft(x, sr, n_fft=n_fft)

    # Find the strongest frequency in every frame
    peak_indices = np.argmax(S, axis=1)
    peak_freqs = freqs[peak_indices]

    # Every peak must be within one frequency bin of 440 Hz
    bin_width = sr / n_fft
    assert np.all(np.abs(peak_freqs - frequency) <= bin_width)


def test_shape():
    sr = 44100
    n_fft = 4096
    hop = 1024

    x = np.zeros(sr)

    S, freqs, times = stft(x, sr, n_fft=n_fft, hop=hop)

    expected_frames = 1 + (len(x) - n_fft) // hop
    expected_bins = n_fft // 2 + 1

    assert S.shape == (expected_frames, expected_bins)
    assert S.shape == (len(times), len(freqs))


def test_silence():
    sr = 44100
    x = np.zeros(sr)

    S, freqs, times = stft(x, sr)

    assert np.all(S == 0)
