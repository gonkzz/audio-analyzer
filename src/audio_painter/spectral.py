import numpy as np
from scipy.signal import get_window


def stft(audio, sample_rate, frame_size=4096, hop_size=1024):
    """Return frequency magnitudes, frequencies, and frame times."""

    window = get_window("hann", frame_size)

    magnitudes = []
    times = []

    for start in range(0, len(audio) - frame_size + 1, hop_size):

        # Extract a short piece of audio
        frame = audio[start:start + frame_size]

        # Smooth the edges
        frame = frame * window

        # Find the frequencies present in this frame
        spectrum = np.fft.rfft(frame)
        magnitudes.append(np.abs(spectrum))

        # Record the time at the centre of this frame
        centre = start + frame_size / 2
        times.append(centre / sample_rate)

    # Find the frequency represented by each FFT bin
    frequencies = np.fft.rfftfreq(frame_size, d=1 / sample_rate)

    return np.stack(magnitudes), frequencies, np.array(times)
