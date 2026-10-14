import sys

import numpy as np
import soundfile as sf

import matplotlib.pyplot as plt

from audio_painter.spectral import stft

def main():
    # 1. Get audio file from command line
    path = sys.argv[1]

    # 2. Load audio
    audio, sr = sf.read(path)

    # Convert stereo to mono
    if audio.ndim == 2:
        audio = np.mean(audio, axis=1)

    # 3. Compute STFT
    S, freqs, times = stft(audio, sr)

    # 4. Convert magnitudes to decibels
    S_db = 20 * np.log10(S.T + 1e-6)

    # 5. Plot spectrogram
    plt.figure(figsize=(12, 6))

    keep = freqs <= 4000
    plt.pcolormesh(times, freqs[keep], S_db[keep], shading="auto")

    plt.ylim(0, 4000)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title("Audio Spectrogram")
    plt.colorbar(label="Magnitude (dB)")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
