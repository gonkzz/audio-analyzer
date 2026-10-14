import sys

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

from audio_painter.spectral import stft

MAX_FREQUENCY = 4000


def main():
    audio_path = sys.argv[1]
    audio, sample_rate = sf.read(audio_path)

    # Mix stereo down to mono
    if audio.ndim == 2:
        audio = np.mean(audio, axis=1)

    magnitudes, frequencies, times = stft(audio, sample_rate)

    # Decibels, so quiet harmonics stay visible
    decibels = 20 * np.log10(magnitudes.T + 1e-6)

    # Only keep the range where melodies live
    visible = frequencies <= MAX_FREQUENCY

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(times, frequencies[visible], decibels[visible], shading="auto")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title("Spectrogram")
    plt.colorbar(label="Magnitude (dB)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
