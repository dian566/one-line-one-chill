# One Line, One Chill

[![Bounty](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/dian566/one-line-one-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/dian566/one-line-one-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

Entry for the [One Line, One Chill](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488) bounty on [make.fun](https://make.fun): one line of horror, a single sentence under 200 characters, meant to frighten a reader in one breath.

## The line

> The baby monitor whispered my name in my dead grandmother's voice — and I live alone.

87 characters, one sentence, no setup, no second chance.

## How it works

`main.py` writes that exact line to `/output/entry.txt`. It is fully
deterministic — the same bytes on every run, with no randomness, no clock,
no network access and no input files. An optional `ONE_CHILL_OUTPUT`
environment variable overrides the output path (used for local testing).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
