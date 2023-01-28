# __HI - LO__

## Welcome to HI - LO!

> __A text-based number-guessing game in true 80's retro style.__

* A number will be randomly generated depending on the chosen difficulty level.
* The goal is to guess the number in as few tries as possible, with the help
  of 'higher-than' and 'lower-than' hints.
* If the player manages to guess the correct number in few enough tries they
  will be rewarded with some classic ASCII-art.

> Try out the deployed game [__HERE__](https://hi-lo-mv.herokuapp.com/)   
> The game is best viewed in a resolution that will allow you to see the entire terminal-box.

![game](images/hi-lo.png)

---

## __The Game__

### __Starting Up__
* When the player first runs the program they are greeted with an ASCII-style game title,   
  followed by an explanation of the game rules.
* The player can then choose between 3 difficulty levels:
  - Easy: The game will pick a number between 1 - 10.
  - Normal: 1 - 100
  - Hard: 1 - 1000
* The game will not accept any other answer than 1, 2 or 3.
* The player also gets informed that they can end the game at any point by entering "E".
  - The game will accept both "e" and "E"

### __Gameplay__
* After a game mode has been selected, a number will be randomly generated within the chosen range.
* The player can now start guessing what the correct number is.
* After each guess the game will announce that their number is either higher or lower than the guessed number.
* The game will keep looping until a correct answer is given, or when the player gives up.
* After every 10'th incorrect guess the player will be asked if they wish to continue.
* When 30 incorrect guesses has been made, the game will terminate.

### __Bad Guesses__
* Only numbers in the chosen range will be accepted as a valid guess.
* The game also remembers what numbers has already been guessed on, and won't accept duplicate guesses.
* If an unacceptable guess has been entered, the game will respond with cheeky comments.

![Bad guess](images/bad-guess.png)

![Bad guess2](images/bad-guess2.png)

### __Winning__
* When the correct number has been found the player gets congratulated, and is informed of how many times they guessed.
* If the guesses are few enough, (3 on Easy, 6 on Normal and 10 on Hard) the player is rewarded with an ASCII-art dragon.
* Each difficulty level has a different image.
* The player then gets asked if they wish to play again.
  - The game will accept y, Y, yes, Yes, YES, n, N, no, No and NO.

![Win](images/win.png)

### __The End__
* When the game is over, the player is informed of this in the true old-school way.

![Game Over](images/game-over.png)

### __Easter Eggs & Cheat Codes__
* Any text-based game worth it's name needs to have easter eggs and cheats implemented.   
* So does this one.
* First, if you manage to guess the number correctly on the first try on hard mode, you will be rewarded with a unique dragon-picture that you wouldn't be able to access in any other way.
* Try to enter "<span style="color: white">Drag0n</span>" or "<span style="color: white">I am a cheater</span>" insted of guessing a number and see what happens.

---

## __Flowchart__

![chart](images/flowchart.png)

---

## __Technologies & Deployment__
