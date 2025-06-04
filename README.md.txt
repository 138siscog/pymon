# Simon Game (Text-Based Version)

This is a work-in-progress Python implementation of the classic **Simon** memory game. The goal is to mimic the CPU-generated sequence of numbers (representing button presses) by typing them correctly. Each level adds one more item to the pattern, increasing the difficulty.

---

## How It Works (Intended Functionality)

- The game starts at **level 1**.
- A random sequence of numbers from 1 to 4 is generated to simulate Simon’s pattern.
- The player inputs numbers one at a time, trying to match the CPU's pattern.
- If the full pattern is matched correctly:
  - The level increases.
  - A new pattern (1 number longer) is generated.
- If the player makes a mistake:
  - The game ends.
  - The final score (highest level reached) is shown.

---

## Debugging Notes

- The line `print(cpu)` is included **temporarily** for debugging purposes, so the developer can verify the CPU's pattern during testing.  
- This line will be removed or hidden from the player once the core logic is stable.

---

## Current Bugs / Issues

1. **Pattern Comparison Logic Is Flawed**  
   - `cpu` is a list containing the pattern as another list (i.e., `cpu = [[4, 2, 1]]`)  
   - But `pattern` is compared directly to `cpu`, which always fails (`pattern != cpu`)  
   - **Fix**: Remove the extra `cpu` list and work directly with `pattern`.

2. **Level Increment Bug**  
   - The line `level =+ 1` is a typo. It should be `level += 1`.  
   - As written, `level` is always set to positive 1, preventing level progression.

3. **Incomplete Player Input Matching**  
   - The game checks `if player == pattern` after just **one input**, which will almost always fail unless the pattern is only 1 number long.  
   - **Fix**: Collect all user inputs for the full pattern before checking equality.

---

## TODO

- [ ] Fix pattern logic and remove unnecessary wrapping list.
- [ ] Collect full player input before comparing to CPU pattern.
- [ ] Add a delay between levels with screen clear for better UX.
- [ ] Add visual representation of 1–4 buttons (e.g., text-based colors or symbols).
- [ ] Add input validation (only accept numbers 1–4).
- [ ] Allow player to exit mid-game (e.g., by typing `q`).

---

## Example (Expected Game Flow)

```text
Level 1:
CPU: [3]  <-- (Visible only during debugging)
Your turn: 3
Correct!

Level 2:
CPU: [3, 1]
Your turn: 3
Your turn: 1
Correct!

Level 3:
CPU: [3, 1, 4]
Your turn: 3
Your turn: 1
Your turn: 2
Incorrect. You Lose.
Score: 3
