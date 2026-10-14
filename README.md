# audio-painter

<img src="assets/icon.png" alt="" width="140">

This started as a tool for learning music by ear. Then I plotted a spectrogram of Charlie Parker warming up and kept staring at it, so now it's turning into something that paints music instead.

So far it's a short-time Fourier transform in Python with [NumPy](https://numpy.org/) and [SciPy](https://scipy.org/), and a script that plots the result.

I wrote about it here: [Getting Lost in Bird's Lines](https://goncalo-soares.com/blog/seeing-bird/).

## Running

Requires [uv](https://docs.astral.sh/uv/) and an audio file.

```sh
uv run scripts/plot_spectrogram.py path/to/clip.wav

uv run pytest
```

To see the Charlie Parker clip from the post:

```sh
mkdir -p clips
curl -o clips/bird.mp3 https://goncalo-soares.com/blog/seeing-bird/bird-practice-clip.mp3
uv run scripts/plot_spectrogram.py clips/bird.mp3
```

## What's next

Some kind of visualizer: you give it a recording and watch a painting being made in real time. I don't know yet what it looks like.
