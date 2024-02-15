# Battleship Challenge
The Battleship Challenge presents a timeless blend of strategic planning and deduction, placing you within a 10x10 grid environment, set within a Terminal interface. Your objective is to pinpoint and destroy four adversary battleships cunningly concealed across the grid. Immerse yourself in a tactical solo confrontation against the computer opponent and strive to claim triumph.


# User Experience UX
## User Stories:
- As a user, I wish to be able to visualize my own ships on my grid.
- As a user, I wish to see the letters or numbers above the columns and rows so that I can accurately decide which cell to target.
- As a user, I want to receive notifications about the turns, whether it's my turn or the computer's turn.
- As a user, I want to receive visual cues and text updates that inform me whether I've scored a hit or a miss.
- As a user, I want to be informed which grid is for which purpose if there are more than one.
- As a user, I want to have the option to exit the game at any time.
- As a user, I want to receive a brief introduction to the game and its rules.


# Owner Stories:
- As an owner, I want to verify that the entered data is accurate and valid.
- As an owner, I want to ensure that the game is fully functional and playable from start to finish.


# Game Rules:
-The game is set on a grid of dimensions 10 by 10.
- There are four enemy battleships concealed within the grid, each with varying lengths.
- Players alternate turns selecting target coordinates (10, 12) to strike the computer's grid (1 / 0 or 1 / 2).
- Every shot taken is depicted on the grid, indicating whether it resulted in a hit or miss.
- Ships are positioned either horizontally or vertically, never diagonally.
- The grid legend features symbols representing empty spaces, ship components, hit ship components, and missed shots.

# Legend:
- '_' : Empty space on the grid.
- 'X' : Miss
- 'O': Hit
- '0' : sink Battleship

# Design Choice: Grid Arrangement

To emulate the traditional Battleship game experience, the design incorporates two grids: the player's grid and the opponent's grid. The player's grid is situated below the opponent's grid. This arrangement mirrors the layout seen in physical Battleship games, where players typically have their own grid beneath their opponent's. This setup requires the player to record their attacks on their grid while tracking the opponent's strikes on the grid above.
The screenshot provided demonstrates the alignment of the grids, showcasing the positioning as described.

![Captura de tela 2024-02-12 141633](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/9db950b5-6157-411e-b93a-32c6d4045bb7)

- Player's Grid
  
![Captura de tela 2024-02-12 142028](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/9be93c69-5070-4db7-9923-db3c7a296ce1)

- Enemy's Grid

# Features:

## Grid Presentation:
The grid for the player and the opponent is showcased.
The player's vessels are discernible on their grid.
Alphabets and numerals atop columns and rows for convenient identification.

# Additional upcoming features

- Manual deployment of battleships - Gives players the option to manually position their battleships on the game board.
- Game timer functionality - Introduces a timer for time-based gameplay.
- Screen-clearing capability - Utilizes the os.system import to implement a function for clearing the screen.
- Multiplayer mode activation - Enables player-versus-player battles for a multiplayer gaming experience.

## Hit and Miss Feedback:
Visual signs and text updates indicate hits ('o') and misses ('X'):

# Utilized Technologies
- Python: Predominant programming language employed in the application.
- GitHub: Platform utilized for repository hosting.
- VS Code: Selected as the primary code editor for composing and modifying the website's code.

## Utilized Libraries:
The Battleship game relies solely on one core library, the random library

# Testing
The code underwent testing, uncovering no significant errors. Despite attempting to utilize PEP8 for code validation, the site's functionality was inaccessible to me. In its place, I utilized Pylint, which offers insights into syntax errors.

-I know the test was successful because after choosing the numerical position on the grid, it was displayed on the battle grid.
- ![Captura de tela 2024-02-13 140357](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/56799c96-a925-4206-bab0-9930dd086ea7)
- ![Captura de tela 2024-02-13 140405](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/26ec680a-c908-43dc-b9f1-269aabe1333a)

- I know the test was successful because after choosing the numerical position on the grid where a ship was located, it appeared with the chosen symbol for (hit).

- ![Captura de tela 2024-02-13 140532](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/054a6d62-4576-4e65-9975-9cb0c8a0c8dd)
- ![Captura de tela 2024-02-13 140613](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/c8e0f2c5-2a7e-4b03-8edc-74f5af8219e8)

- The same applies when the ship is sunk, making it possible to verify the symbol for (sunk)



# Credits
## Python:
- The Battleship Game is inspired by the tutorial article authored by Mark Anthony Llego /
- Franklin Nascimento (https://www.youtube.com/watch?v=uoG17lg2WCg).
- This project was constructed utilizing a template provided by Code Institute to establish the necessary environment for deployment on Heroku.
- Credits are given to the Code Institute projects, curriculum and previous projects in Python.
- GeeksforGeeks - Python Programming Examples
- PythonDex - Python Battleship Game

