import numpy as np
from scipy.signal import get_window


def stft(x: np.ndarray,
         sr: int,
         n_fft: int = 4096,
         hop: int = 1024):

    """Returns (S, freqs, times).

    S:     magnitudes, shape (n_frames, n_fft // 2 + 1)
    freqs: frequency in Hz of each column
    times: centre time in seconds of each frame
    """

    # 1. Divide audio into overlapping frames
    frames = np.lib.stride_tricks.sliding_window_view(x, n_fft)[::hop]

    # 2. Apply Hann window to each frame
    window = get_window("hann", n_fft)
    windowed = frames * window

    # 3. Compute FFT magnitudes
    S = np.abs(np.fft.rfft(windowed, axis=1))

    # 4. Compute frequency and time axes
    freqs = np.fft.rfftfreq(n_fft, d=1 / sr)
    times = (np.arange(len(frames)) * hop + n_fft / 2) / sr

    return S, freqs, times
