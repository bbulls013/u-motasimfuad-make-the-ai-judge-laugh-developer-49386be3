[![Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/bbulls013/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/bbulls013/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

# Make the AI Judge Laugh: Developer Excuses

A tiny deterministic program for the [make.fun bounty](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3): it writes one funny single-line excuse a developer gives when code breaks in production to `/output/entry.txt`.

## The excuse

> Production didn't break, it finally read the TODO I left in 2019 and gave up.

77 characters, one line, plain UTF-8. The joke turns on a twist every developer recognises: the bug was never a mystery — it was a TODO left in the code years ago, and production is the first environment honest enough to trip over it.

## How it works

`main.py` (Python 3, standard library only) validates the line against the competition gate — 1–200 characters, a single non-blank line — then writes it to `/output/entry.txt`. No input, no network, no randomness: every run produces byte-identical output.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # local test path
```

## License

MIT — see [LICENSE](LICENSE).
