# pymon - Text-Based Simon Game

**pymon** is a simple terminal-based version of the classic memory game **Simon**. The player must repeat an increasingly long sequence of numbers (representing button presses) correctly to advance to the next level. This version is coded entirely in Python and runs in the terminal.

---

## How to Play

1. When the game starts, it displays a pattern of numbers (from 1 to 4).
2. The player must enter each number in the sequence **one at a time**, pressing Enter after each input.
3. If the sequence is entered correctly:
   - The level increases.
   - A new, longer pattern is generated.
4. If the sequence is entered incorrectly:
   - The game ends.
   - Your score (level reached) is shown.
5. After losing, the player is asked whether they want to play again.

> **Note:** The pattern is currently shown for debugging purposes. This will be hidden in a future update.

---

## Bug Fixes in This Version

| Problem | Fix |
|--------|-----|
| Pattern comparison failed due to unnecessary list nesting (`cpu = [[...]]`) | Removed wrapper list, directly compared `p1 == pattern` |
| Level did not increase correctly (`level =+ 1`) | Fixed to `level += 1` |
| Comparison happened before full input was collected | Now collects all player input before comparing to pattern |
| Score not resetting after replay | Score and level are properly reset on replay |

---

## TODO / Feature Wishlist

- [ ] **Remove debug output** (`print(pattern)`) before release
- [ ] **Input validation** – Only allow integers 1–4, and gracefully handle invalid input
- [ ] **Exit option** – Allow player to quit mid-game by typing `q`
- [ ] **Add delay/clear screen** between levels for better UX
- [ ] **Add color or text-based visuals** to represent the buttons (e.g., Red = 1, Blue = 2)
- [ ] **Track high scores** across sessions (optional future enhancement)

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Example Gameplay (Debug Mode)

```text
Level 1:
CPU: [3]
Your turn: 3

Level 2:
CPU: [3, 2]
Your turn: 3
Your turn: 2

Level 3:
CPU: [3, 2, 1]
Your turn: 3
Your turn: 2
Your turn: 4
You Lose.
Score: 3

Play Again (Y/N)
