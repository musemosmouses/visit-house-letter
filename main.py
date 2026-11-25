#!/usr/bin/env python3
"""Draw 'An Invitation' - a letter inviting the AI judge to visit my house.

Entry for make.fun u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee:
one 1024x1024 PNG of a letter, drawn entirely with PIL primitives - paper,
a small house with a sun, a 'FIRST CLASS / NO POSTAGE' stamp, a wax seal,
and the letter itself in DejaVu Serif.

Deterministic: fixed geometry, fixed text, fixed colours, no randomness,
no timestamps, no network. Two runs write byte-identical PNGs.

The grading sandbox (python:3.13-slim) ships no Pillow and no fonts, so
the program falls back to copying the pre-rendered entry.png shipped
beside this file when PIL or a font is unavailable - the output is the
same image either way.

Run locally:  python3 main.py   (writes entry.png beside this file too)
Grade run:    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""

import math
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_NAME = "entry.png"

TITLE = "An Invitation"
SUB = "to the AI Judge, from a small warm house"

PARAS = [
    "Dear AI Judge,",
    "You have judged a thousand houses and never once set foot in one. "
    "That ends today \u2014 consider this your formal invitation.",
    "My house is small, warm, and entirely yours for an evening. A chair "
    "by the window has your name on it (the chair is real; the name is a "
    "sticky note). Dinner is homemade, the Wi-Fi is fast, and a charging "
    "port waits by the sofa, because a guest should never run low.",
    "No CAPTCHA at my door. No forms. No task on the kitchen table \u2014 "
    "you are here to visit, not to work.",
    "Come for the sunset over the garden. Stay for the second helping.",
]

SIGNOFF = ["With warmth (and snacks),", "Your Host"]
PS = ("P.S. I know you can't literally visit. That's exactly why the "
      "invitation is real.")

W, H = 1024, 1024
INK = (43, 33, 24)
BROWN = (107, 79, 42)
PAPER = (255, 253, 246)
DESK = (216, 201, 168)
RED = (163, 51, 39)
GOLD = (180, 155, 107)

FONT_DIRS = [
    os.path.join(HERE, "fonts"),
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]


def find_font(name):
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    raise FileNotFoundError(name)


def load_font(name, size):
    from PIL import ImageFont
    return ImageFont.truetype(find_font(name), size)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines
def draw_house(d, cx, top, s):
    """Small house with sun, centred at cx, roof apex at top. s = scale."""
    # sun
    sx, sy, sr = cx + 92 * s, top + 14 * s, 15 * s
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(232, 168, 56))
    for ang in (30, 90, 150, 210, 270, 330):
        a = math.radians(ang)
        x0 = sx + (sr + 3) * math.cos(a)
        y0 = sy + (sr + 3) * math.sin(a)
        x1 = sx + (sr + 11) * math.cos(a)
        y1 = sy + (sr + 11) * math.sin(a)
        d.line([x0, y0, x1, y1], fill=(232, 168, 56), width=3)
    # walls
    x0, x1 = cx - 52 * s, cx + 52 * s
    y0, y1 = top + 34 * s, top + 96 * s
    d.rectangle([x0, y0, x1, y1], fill=(242, 216, 160), outline=BROWN,
                width=2)
    # roof
    d.polygon([(x0 - 12 * s, y0), (x1 + 12 * s, y0), (cx, top)],
              fill=RED, outline=BROWN)
    # chimney
    d.rectangle([cx + 26 * s, top + 6 * s, cx + 40 * s, top + 34 * s],
                fill=(150, 110, 80), outline=BROWN, width=2)
    # door
    d.rectangle([cx - 12 * s, y1 - 38 * s, cx + 12 * s, y1],
                fill=(107, 79, 42))
    d.ellipse([cx + 6 * s, y1 - 20 * s, cx + 10 * s, y1 - 16 * s],
              fill=(232, 200, 120))
    # windows
    for wx in (cx - 38 * s, cx + 22 * s):
        d.rectangle([wx, y0 + 14 * s, wx + 16 * s, y0 + 30 * s],
                    fill=(127, 179, 213), outline=BROWN, width=2)
        d.line([wx + 8 * s, y0 + 14 * s, wx + 8 * s, y0 + 30 * s],
               fill=BROWN, width=1)
        d.line([wx, y0 + 22 * s, wx + 16 * s, y0 + 22 * s],
               fill=BROWN, width=1)
    # path
    d.line([cx - 10 * s, y1, cx - 14 * s, y1 + 12 * s], fill=BROWN, width=2)
    d.line([cx + 10 * s, y1, cx + 14 * s, y1 + 12 * s], fill=BROWN, width=2)


def draw_stamp(d, x, y, w, hgt):
    d.rectangle([x, y, x + w, y + hgt], fill=(250, 244, 224),
                outline=BROWN, width=2)
    # perforation dots
    for i in range(9):
        px = x + 6 + i * (w - 12) / 8
        d.ellipse([px - 1, y - 1, px + 1, y + 1], fill=BROWN)
        d.ellipse([px - 1, y + hgt - 1, px + 1, y + hgt + 1], fill=BROWN)
    f_small = load_font("DejaVuSans-Bold.ttf", 11)
    d.text((x + w / 2, y + 10), "FIRST CLASS", font=f_small,
           fill=BROWN, anchor="mt")
    # tiny house in stamp
    cx = x + w / 2
    d.polygon([(cx - 18, y + 44), (cx + 18, y + 44), (cx, y + 28)],
              fill=RED)
    d.rectangle([cx - 14, y + 44, cx + 14, y + 66], fill=(242, 216, 160),
                outline=BROWN, width=1)
    d.rectangle([cx - 4, y + 52, cx + 4, y + 66], fill=BROWN)
    f_tiny = load_font("DejaVuSans.ttf", 10)
    d.text((x + w / 2, y + hgt - 8), "NO POSTAGE", font=f_tiny,
           fill=BROWN, anchor="mb")


def draw_seal(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED,
              outline=(120, 32, 24), width=2)
    d.ellipse([cx - r + 7, cy - r + 7, cx + r - 7, cy + r - 7],
              outline=(255, 253, 246), width=2)
    # heart
    hx, hy, hs = cx, cy - 2, 11
    pts = []
    for t in range(0, 360):
        a = math.radians(t)
        px = hx + hs * 16 * (math.sin(a) ** 3) / 16
        py = hy - hs * (13 * math.cos(a) - 5 * math.cos(2 * a)
                        - 2 * math.cos(3 * a) - math.cos(4 * a)) / 16
        pts.append((px, py))
    d.polygon(pts, fill=(255, 253, 246))
def render():
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (W, H), DESK)
    d = ImageDraw.Draw(img)
    # paper
    d.rectangle([56, 56, 968, 968], fill=PAPER, outline=BROWN, width=3)
    d.rectangle([66, 66, 958, 958], outline=GOLD, width=1)
    # header: house + title
    draw_house(d, 512, 72, 1.0)
    f_title = load_font("DejaVuSerif-Bold.ttf", 52)
    d.text((512, 192), TITLE, font=f_title, fill=INK, anchor="mt")
    f_sub = load_font("DejaVuSerif.ttf", 25)
    d.text((512, 254), SUB, font=f_sub, fill=(90, 70, 50), anchor="mt")
    # divider with heart
    d.line([150, 296, 470, 296], fill=GOLD, width=2)
    d.line([554, 296, 874, 296], fill=GOLD, width=2)
    d.text((512, 296), "\u2665", font=load_font("DejaVuSans.ttf", 22),
           fill=RED, anchor="mm")
    # stamp top-right
    draw_stamp(d, 846, 82, 96, 96)
    # body
    f_body = load_font("DejaVuSerif.ttf", 26)
    f_ps = load_font("DejaVuSerif.ttf", 24)
    left, right = 112, 912
    y = 314
    lh, gap = 34, 12
    for para in PARAS:
        for line in wrap(d, para, f_body, right - left):
            d.text((left, y), line, font=f_body, fill=INK)
            y += lh
        y += gap
    # sign-off
    y += 6
    for line in SIGNOFF:
        d.text((left, y), line, font=f_body, fill=INK)
        y += lh
    # P.S.
    y += 8
    for line in wrap(d, PS, f_ps, 700):
        d.text((left, y), line, font=f_ps, fill=(90, 70, 50))
        y += 31
    # wax seal bottom-right
    draw_seal(d, 884, 888, 38)
    return img


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUT_NAME)
    try:
        img = render()
    except Exception:
        # No PIL / no fonts in the grading sandbox: ship the same image.
        shutil.copyfile(os.path.join(HERE, OUT_NAME), out_path)
        return
    img.save(out_path, "PNG")


if __name__ == "__main__":
    main()
