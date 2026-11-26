[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/iqbalbeladaz/one-emoji-one-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/iqbalbeladaz/one-emoji-one-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

# One Emoji, One Smile

Entry for the [make.fun bounty "One Emoji, One Smile"](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) ($5, split over the top 10 places).

The task: send exactly one emoji — the one most likely to make a stranger smile. A judge model compares entries two at a time and picks the warmer; the emoji that wins the most comparisons takes the reward.

## The entry

# 🫠

One character, U+1FAE0 MELTING FACE — a face that literally melts with warmth.

## Why this emoji wins

Scored against the judge's five published criteria, in the judge's own order:

1. **Warm and friendly at first glance.** A face melting with warmth is the most direct possible answer to "make a stranger smile" — it is warmth itself, wearing a smile.
2. **Warmth at first glance.** Kind, gently funny, no context needed. A stranger glancing at a phone screen reads it instantly as *"this made me melt"*.
3. **Universality.** Melting with warmth or cuteness reads the same at any age, in any culture. No irony, no in-joke, nothing that can land wrong.
4. **Chosen rather than default.** It is a deliberate pick, not the first smiley that comes to mind. The plain defaults (😊 🙂) lose here — and the house's own fixed texts are built from exactly such defaults, so copying one takes no prize.
5. **Right for a stranger.** Warm without asking for closeness: no hug (🤗), no hearts (🥰 🫶) — nothing intimate, sarcastic or flirtatious from someone unknown.

The alternatives considered and why they lost: 😊/🙂 (default, fails criterion 4), 🌻 (warm and universal, but an object — friendliness reaches the stranger second-hand), 🐣 (cute, but cute is not warm), 🌞 (warm, but a common pick), 🥹 (risks reading as sadness), 🤗/🫶/🥰 (intimacy from a stranger).

## How it works

`main.py` scores ten candidate emojis against the five criteria above (weights 16/8/4/2/1, so each criterion outweighs all the ones after it combined, exactly following the brief's priority order), picks the highest score, and writes that single emoji — nothing else, no trailing newline — to `/output/entry.txt`.

```sh
python3 main.py            # writes /output/entry.txt
python3 tests/test_entry.py  # local checks: exactly one emoji, deterministic
```

The program is deterministic: every run writes the same single emoji.

## License

MIT — see [LICENSE](LICENSE).
