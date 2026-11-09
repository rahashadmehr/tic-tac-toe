# 🎮 Tic Tac Toe — Python & Pygame

A simple two-player Tic Tac Toe game built with Python and Pygame. Players enter their names, take turns placing X and O, and the game announces the winner or a draw.

## ✨ Features

- Two-player local game
- Player name input before starting
- Easy mouse-click gameplay
- Automatic winner detection
- Draw detection
- Play Again button
- Clean, dark-themed interface

## 🖼️ Screenshots

### Start Screen

Start screen where two players enter their names. Player X goes first and Player O plays second.

<p align="center">
  <img src="assets/start-game.png" alt="Tic Tac Toe start screen" width="500">
</p>

### Gameplay

Players take turns placing X and O on the board.

<p align="center">
  <img src="assets/gameplay.png" alt="Tic Tac Toe gameplay" width="500">
</p>

### Winner Screen

When a player wins, their name is displayed on the screen.

<p align="center">
  <img src="assets/winner.png" alt="Tic Tac Toe winner screen" width="500">
</p>

## 🚀 Installation & Run

1. Clone the repository:

```bash
git clone [https://github.com/YOUR_USERNAME/tic-tac-toe.git](https://github.com/YOUR_USERNAME/tic-tac-toe.git)
cd tic-tac-toe
```

2. Install Pygame:

```bash
pip install pygame
```

3. Run the game:

```bash
python tic_tac_toe.py
```

## 🎮 How to Play

1. Enter the name of Player X.
2. Enter the name of Player O.
3. Click **START GAME**.
4. Click an empty square to place your symbol.
5. The first player to get three symbols in a row, column, or diagonal wins.
6. If all squares are filled and no player wins, the game ends in a draw.

## 🏆 Winner Message

When a player wins, the game shows:

```text
Ali won!
```

If the game ends without a winner:

```text
It's a draw!
```

## 📁 Project Structure

```text
tic-tac-toe/
│
├── tic_tac_toe.py        # Main game file
├── README.md             # Project documentation
└── assets/
    ├── start-game.png    # Start screen screenshot
    ├── gameplay.png      # Gameplay screenshot
    └── winner.png        # Winner screen screenshot
```

## 🛠️ Technologies Used

- Python
- Pygame
- Git & GitHub

## 📄 License

This project is licensed under the MIT License.