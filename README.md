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

