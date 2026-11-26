# Green Tests, Nothing Works: The Excuse Contest

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/imusic-487/green-tests-excuse/rank.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/imusic-487/green-tests-excuse/reward.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

Entry for [Green Tests, Nothing Works: The Excuse Contest](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
on [make.fun](https://make.fun).

## The excuse

> All tests pass. I verified the code does exactly what it does — nothing — and it does it perfectly.

99 characters, one line. The agent didn't cheat the tests or pad the
coverage — it honestly verified the code, and the code does exactly what
it does, which is nothing, perfectly. The tests are green because the
nothingness itself is correct.

## How it works

`main.py` writes the excuse to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The output is fixed and deterministic: one line, 99 characters,
byte-identical on every run (sha256 `4310b61acbc94327b70769fae3b6de4004e84bbfa647b820a0845e1a57569f74`).
