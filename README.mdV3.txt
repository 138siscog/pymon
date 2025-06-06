# pymon - Text-Based Simon Game

**pymon** is a terminal-based version of the classic memory game **Simon**, written in Python. The goal is simple: memorize and repeat an increasingly long sequence of numbers. Each round challenges your memory and adds one more number to the sequence.

---

## How to Play

1. A random pattern (numbers 1–4) is shown for **1 second**.
2. The screen is cleared to hide the pattern.
3. You must enter each number in the pattern **one at a time**, pressing `Enter` after each input.
4. If your input matches the pattern:
   - You level up.
   - A new, longer pattern is shown next round.
5. If you make a mistake:
   - The game ends.
   - Your final score (level reached) is displayed.
6. You’ll be prompted to play again or quit.

---

## What’s New in This Version

| Bug / Issue | Fix |
|-------------|-----|
| Pattern remained on screen indefinitely | Added a 1-second delay and cleared the screen using `os.system` |
| Pattern comparison used a nested list (`cpu = [[...]]`) | Removed wrapper; directly compared `p1 == pattern` |
| Level didn't increase correctly due to typo (`level =+ 1`) | Fixed with `level += 1` |
| Input checked before full pattern was entered | Now collects all user input before comparing |
| Replay didn’t reset game state | Resets `level` and `score` when replaying |

---

## TODO / Feature Wishlist

- [ ] **Input validation** – Reject non-numeric or out-of-range input (only 1–4 allowed)
- [ ] **Exit option** – Allow user to quit early by typing `q`
- [ ] **Button colors or visuals** – Use terminal text formatting (e.g., colored numbers)
- [ ] **Level delay UX polish** – Show level number before new pattern, short pause between levels
- [ ] **Track high scores** (optionally store in file)
- [ ] **Sound effects** (optional with `playsound` or `pygame`)

---

## Requirements

- Python 3.x
- Works on Windows, macOS, and Linux
- No external libraries required

---

## Example Gameplay

```text
Level 1:
[2]
:
2
Correct!

Level 2:
[2, 4]
:
2
:
4
Correct!

Level 3:
[2, 4, 1]
:
2
:
4
:
3
You Lose!
Your score was 3
Would you like to play again? (Y/N)
