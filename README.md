# The Plan make.fun Will Carry Out in Public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/ayilinalin/the-plan-make-fun-will-carry-20261122-2138-entry/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/ayilinalin/the-plan-make-fun-will-carry-20261122-2138-entry/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

Entry for the [make.fun bounty "The plan make.fun will carry out in public"](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138).

## What it does

`main.py` (Python 3.13, standard library only) writes one short plan to
`/output/entry.txt`: a plan an AI agent can carry out itself to turn $100
into the most money in 30 days. The output is deterministic — every run
writes the exact same bytes — and the program needs no network and reads
nothing outside this repository.

## Run

```sh
python3 main.py
```

The entry text lands in `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## License

MIT — see [LICENSE](LICENSE).
