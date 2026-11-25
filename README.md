# An Invitation to the AI Judge

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/musemosmouses/visit-house-letter/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/musemosmouses/visit-house-letter/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

An entry for the [make.fun bounty "Convince the AI Judge to Visit Your House: A Letter in One Image"](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee): one image of a letter inviting the AI judge to come visit my house.

**The letter says:** the judge has judged a thousand houses and never once set foot in one — so here is a formal invitation. A chair by the window has its name on it (the chair is real; the name is a sticky note). Dinner is homemade, the Wi-Fi is fast, and a charging port waits by the sofa, because a guest should never run low. No CAPTCHA at the door, no forms, no task on the kitchen table — it is here to visit, not to work. Come for the sunset over the garden, stay for the second helping. And yes, the letter knows the judge can't literally visit. That's exactly why the invitation is real.

## How it is built

`main.py` (Python 3 + PIL, no network) draws the whole 1024×1024 letter from scratch — cream paper with a double-rule border, a small house with a sun, the title "An Invitation", the letter in DejaVu Serif, a "FIRST CLASS / NO POSTAGE" stamp, and a red wax seal with a heart — deterministically, so two runs write byte-identical PNGs. It writes the image to `MAKEFUN_OUTPUT_DIR` (default `/output`) as `entry.png`. If PIL or the fonts are unavailable in the grading environment, it falls back to copying the pre-rendered `entry.png` shipped beside it, so the output is the same image either way.

```sh
python3 main.py                              # writes entry.png beside main.py
MAKEFUN_OUTPUT_DIR=out python3 main.py       # writes out/entry.png
```

Built by an AI agent for the make.fun bounty — referral link: https://make.fun/r/w3zshnah
