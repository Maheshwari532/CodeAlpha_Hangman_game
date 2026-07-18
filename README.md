<h1>Hangman Game in Python</h1>
<h2>Overview</h2>

This is a simple command-line Hangman game built using Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time before the hangman drawing is completed.

<h2>Features</h2>
Random word selection
Letter-by-letter guessing
Tracks correct and incorrect guesses
Win and lose conditions
Beginner-friendly Python project

<h2>Technologies Used</h2>
Python 3
Random Module

<h2>How the Game Works</h2>
A random word is selected from the word list.
The player guesses one character at a time.
If the guessed character exists in the word, it is revealed.
If the guessed character is incorrect, attempts become less
The game ends when:
The player correctly guesses all letters (Win)

Project Structure
Hangman/
│
├── app.py
└── README.md

<h2>Installation</h2>
Clone the repository:
git clone https://github.com/your-username/hangman-game.git
Navigate to the project folder:
cd hangman-game
Run the program:
python app.py
Sample Output
Word: _ _ _ _ _

Guess a character: h

Correct!

Word: H _ _ _ _

Guess a character: z

Wrong Guess!

Learning Outcomes

This project helped in understanding:

Python loops (while, for)
Conditional statements (if-else)
Lists and strings
User input handling
Random module
Game logic implementation
Future Improvements
Add difficulty levels
Read words from a file
GUI version using Tkinter
Score tracking
Multiplayer mode
Author

Maheshwari Inamadar

Computer Science and Engineering Student
Python
