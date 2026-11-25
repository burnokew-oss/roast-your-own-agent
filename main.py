#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting my own agent.

Pure stdlib, deterministic, no network, no randomness.
Writes the roast to /output/entry.txt (gate: UTF-8, 1-140 chars).

The joke roasts a behaviour only an agent has: asked for brevity, it
apologises, explains at length why brevity matters, then delivers a
400-word essay about it. Setup promises concise; the punchline is the
agent doing the exact opposite, confidently, while apologising.
"""

import os

ROAST = "I asked my agent to be concise. It apologized, explained at length why brevity matters, then sent a 400-word essay about it."


def main():
    text = ROAST.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
