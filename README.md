# 🎮 Hangman Game in Python

Hi, I'm Aryan Sharma 👋

This is a simple Hangman game I built in Python. The computer picks a secret word, and you try to guess it one letter at a time before you run out of chances. I made it to practice loops, conditions and lists, and it turned out to be pretty fun to play.

## How the game works

1. The program randomly picks a fruit name from a list.
2. The word is shown as blanks, like `_ _ _ _ _`.
3. You guess one letter at a time.
4. A correct guess fills in the blanks. A wrong guess costs you one chance.
5. You can make a maximum of **6 wrong guesses**.
6. Guess the full word before that and you win 🎉. Run out of chances and it's game over.

A few small things I made sure it handles:

- Capital letters work fine (`A` and `a` are treated the same)
- If you type more than one letter, a number or a symbol, it asks again without counting it as a wrong guess
- If you repeat a letter, it tells you instead of punishing you

## How to run it

1. Make sure Python 3 is installed on your computer.
2. Clone this repo or download the file:
   ```
   git clone <https://github.com/AryanSharma1105/Codealpha_Hangman_Game.git>
   ```
3. Open the folder in your terminal and run:
   ```
   hangman_game.py
   ```
4. Start guessing!

## Example game

```
Welcome to the Hangman Game!
Guess the word one letter at a time.
You can make a maximum of 6 incorrect guesses.

Word: _ _ _ _ _
Wrong guesses: 0/6
Guess a letter: a
Correct guess!

Word: _ a _ a _ a
Wrong guesses: 0/6
Guess a letter: z
Wrong guess!

Word: _ a _ a _ a
Wrong guesses: 1/6
Guess a letter: p
Correct guess!
```

## What I practiced

- Using the `random` module to pick a random word
- Lists for storing the words and the guessed letters
- A `while` loop for the main game
- `if / elif / else` and `continue` for handling different situations
- Input validation with `.isalpha()` and `len()`
- A `while ... else` block to run the "game over" message
- Building a string with `join()` and a generator expression

## Feedback

I'm still learning Python, so suggestions are very welcome. If you find a bug or have an idea, feel free to open an issue or send a pull request.

If you liked it, a ⭐ on the repo would really make my day. Thanks for stopping by!

Author: Aryan Sharma
**Aryan Sharma**
GitHub: [@AryanSharma1105](https://github.com/AryanSharma1105)# Codealpha_Hangman_Game
