# Chess AI Game

## Overview
This is a chess game with an AI opponent implemented using Pygame and Python-Chess libraries. The AI uses the Minimax algorithm with alpha-beta pruning and piece-square tables for evaluation.

## Prerequisites
- Python 3.8+
- Pygame
- Python-Chess library

## Installation

Install dependencies:
```
pip install pygame python-chess
```

## Running the Game

### Standard Chess Mode
```
python src/main.py
```

### AI Game Mode
```
python src/main.py
```
- The game starts in AI mode by default
- Press 'r' to restart the game at any time

## Game Controls
- Click to select and move chess pieces
- 'r': Restart the game
- Close window to exit

## Project Structure and Classes

### Main Class (`main.py`)
- Main class controlling the game flow
- Handles the main game loop and player events
- Renders game interface and end game screens
- Manages AI game mode

### Game Class (`game.py`) 
- Manages game state
- Handles move sound effects
- Renders chessboard and pieces
- Displays legal moves and capture possibilities

### Board Class (`board.py`)
- Manages chess board using python-chess library
- Handles moves and validates their legality
- Checks for conditions like checkmate and stalemate
- Manages piece states and positions

### ChessAI Class (`ai.py`)
- Implements AI opponent using minimax algorithm with alpha-beta pruning
- Evaluates piece positions using position value tables
- Calculates best moves for AI
- Tracks number of moves checked and pruned branches

### Config Class (`config.py`)
- Manages game configuration and interface
- Provides different color themes for the board
- Manages fonts and display settings

### Theme Class (`theme.py`)
- Defines color themes for the chess board
- Manages colors for light/dark squares
- Defines highlight colors for legal moves

## Customizing the AI

The AI's behavior can be customized by modifying the following parameters in `src/ai.py`:

### Search Depth
- In `ai.py`, find the `get_best_move` method call in the `choose_move` method
- Modify the `depth` parameter (default is 3)
- Higher depth values make the AI look further ahead but will make it think longer
- Example: `depth=4` for stronger play, `depth=2` for faster moves

### Piece Values
You can modify the base values of pieces by changing the values in the `_get_piece_value` method:
```python
values = {
    chess.PAWN: 10.0,
    chess.KNIGHT: 30.0,
    chess.BISHOP: 30.0,
    chess.ROOK: 50.0,
    chess.QUEEN: 90.0,
    chess.KING: 900.0
}
```

### Position Evaluation
The AI uses piece-square tables to evaluate piece positions. These can be modified in the `ChessAI` class initialization:
- `pawn_eval_white`: Pawn position values
- `knight_eval_white`: Knight position values
- `bishop_eval_white`: Bishop position values
- `rook_eval_white`: Rook position values
- `queen_eval_white`: Queen position values
- `king_eval_white`: King position values

Higher values (positive) encourage pieces to move to those squares, while lower values (negative) discourage piece placement.

## Troubleshooting
- Ensure all dependencies are installed
- Check Python and Pygame versions are compatible
- Verify you're running from the project root directory
- On Windows, use Command Prompt or PowerShell to run commands

## Contributing
Feel free to open issues or submit pull requests.
