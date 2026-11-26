"""Local checks for the One Emoji, One Smile entry program.

Run: python3 -m pytest tests/  (or python3 tests/test_entry.py)
"""
import os
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUT = "/tmp/one-emoji-test-output"


def run_program():
    subprocess.run(["rm", "-rf", OUT], check=True)
    env = dict(os.environ, OUTPUT_DIR=OUT)
    r = subprocess.run(
        [sys.executable, "main.py"], cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        env=env, capture_output=True, text=True, check=True,
    )
    assert r.returncode == 0, r.stderr
    with open(os.path.join(OUT, "entry.txt"), encoding="utf-8") as f:
        return f.read()


def test_entry_is_exactly_one_emoji():
    text = run_program()
    assert 1 <= len(text) <= 8, f"gate: 1-8 chars, got {len(text)}"
    assert text.strip() == text and text.strip(), "gate: not only whitespace"
    assert len(text) == 1, f"exactly one character, got {len(text)}"
    assert unicodedata.category(text[0]).startswith("So"), "must be a symbol (emoji)"
    assert text == "\U0001fae0", f"expected melting face, got {text!r}"


def test_entry_is_deterministic():
    first = run_program()
    second = run_program()
    assert first == second, "program must be deterministic"


if __name__ == "__main__":
    test_entry_is_exactly_one_emoji()
    test_entry_is_deterministic()
    print("all local checks passed")
