# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/0xfani/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/0xfani/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One front page of the world's news on Thursday 19 November 2026: 42 stories from
seven regions and seven fields. Three illustrated lead stories (the Trump-Xi-Putin
summit in Shenzhen, the World Court's Rohingya genocide ruling, Anthropic's record
market debut), ten illustrated cards, a world map with numbered pins, 29 briefs and
a date check naming stories left out because they were first reported on 18 November.

- `entry.png` is the picture (1024 x 1024 PNG). It was drawn with Pillow from a
  checked story list; the illustrations were made with ChatGPT image generation and
  the map uses Natural Earth land outlines.
- `main.py` is the entry program: it copies `entry.png` to the output folder.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=47qm20ar&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
