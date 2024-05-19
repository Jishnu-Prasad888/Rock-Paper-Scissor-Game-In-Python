# Rock Paper Scissors Game

A simple Rock Paper Scissors game implemented in Python.

## Introduction

This program lets you play Rock Paper Scissors against the computer.

## Instructions

1. Run the program.
2. Enter the number corresponding to your choice:
   - 1 for Scissor
   - 2 for Rock
   - 3 for Paper
3. View the result.
4. To exit the game, enter 4.
5. To view the current score, enter 5.

## Code Explanation

### Variables

- `computer_tries`: A list containing the choices of the computer and the user.
- `exit_message`: Message to display for the exit option.
- `score_message`: Message to display for the score option.
- `screen_width`: Width of the screen.
- `text_width`: Width of the text.
- `box_width`: Width of the box.
- `left_margin`: Margin for formatting the display.
- `score`: A list to store the scores. Index 0 for user's score and index 1 for computer's score.

### Functions

- `game(user_input)`: Function to play the game based on user's input.
- `input_function()`: Function to display the options and take user input.
  
### Main Program

1. Display options and take user input.
2. While the user doesn't choose to exit:
   - Play the game.
   - Display the score.
   - Take user input for the next round.

## Example

Here is how you can use the program:

```python
python main.py
