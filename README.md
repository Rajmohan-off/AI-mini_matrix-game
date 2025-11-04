# 🤖 AI Number Arrange Game — 9×9 Matrix

A Python-based console puzzle game where **you or an AI agent** arrange shuffled numbers (1–81) into ascending order on a 9×9 grid.

---

## 🧠 Features
- **Manual Play Mode:** Swap any two tiles to reorder numbers.
- **AI Solve Mode:** Watch an AI agent automatically sort the grid using a greedy search algorithm.
- **Dynamic Board:** Randomly shuffled each run.
- **Smart Output:** Displays the grid and updates move counts step-by-step.

---

## ⚙️ Setup

### Clone and run
```bash
git clone https://github.com/Rajmohan-off/ai-number-arrange-game.git
cd ai-number-arrange-game
python main.py
No external libraries are required.

🎮 Commands
Command	Description
swap r1 c1 r2 c2	Swap two tiles by their coordinates
ai	Activate AI solver
show	Display solved reference board
quit	Exit the game

Example:

bash
Copy code
swap 1 1 1 2
🤖 AI Strategy
The AI uses a greedy correction algorithm:

Scans the board for misplaced numbers.

Finds where the correct number currently is.

Swaps the two tiles.

Repeats until all tiles are in ascending order.

It demonstrates basic search logic and position correction, ideal for showcasing algorithmic reasoning in AI coursework or interviews.

🧩 Example Output
csharp
Copy code
=== 🤖 AI Number Arrange Game (9×9) ===
Arrange numbers 1–81 in ascending order.
Commands: 'swap r1 c1 r2 c2' | 'ai' | 'show' | 'quit'

------------------------------------------------------------
 17 |  2 |  9 | 10 | ...
------------------------------------------------------------
Moves: 0
Enter command: ai
🤖 AI is solving step-by-step...
AI Move 1
AI Move 2
...
✅ AI finished sorting the matrix!
🧱 Project Structure
css
Copy code
ai-number-arrange-game/
├── main.py
├── README.md
└── requirements.txt
✨ Future Ideas
Upgrade AI to A* or reinforcement learning.

Add GUI using Tkinter.

Enable adjustable grid sizes (3×3 to 9×9).


👨‍💻 Author
Rajmohan P
MBA Business Analytics | Project Manager | AI Enthusiast
