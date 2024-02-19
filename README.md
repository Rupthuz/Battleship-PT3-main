# Battleship Challenge
The Battleship Challenge presents a timeless blend of strategic planning and deduction, placing you within a 10x10 grid environment, set within a Terminal interface. Your objective is to pinpoint and destroy four adversary battleships cunningly concealed across the grid. Immerse yourself in a tactical solo confrontation against the computer opponent and strive to claim triumph.


![Facebook post - 1](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/4e3b5358-a366-4f9e-b131-d1de1e60ec3e)

Click Here to Heroku [live app](https://batlleshipcodep3-ebe6d13f5332.herokuapp.com/)

Click Here to [Github Repository](https://github.com/Rupthuz/Battleship-PT3-main)



<!--ts-->
* [How to Play](#How_to_Play) 
* [User Experience UX](#User_Experience_UX)
* [User Stories](#User_Stories)
  * [Code Structure](#Code_Structure)
  * [Comments and Documentation](#Comments_and_Documentation)
   * [Variable and Function Naming](#Variable_and_Function_Naming)
   * [Code Formatting](#Code_Formatting)
  * [Error Handling](#Error_Handling)
  * [Additional Considerations](#Additional_Considerations)
  * [Owner Stories](#Owner_Stories)
* [Game Rules](#Game_Rules)
  * [Legend](#Legends)
* [Design Choice](#Design_Choice)
* [Features](#Features)
* [Additional upcoming features](#Additional_upcoming_features)
* [Hit and Miss Feedback](#Hit_and_Miss_Feedback)
* [Utilized Technologies](#Utilized_Technologies)
* [Utilized Libraries](#Utilized_Libraries)
* [Testing](#Testing)
* [Credits](#Credits)
* [Acknowledgements](#Acknowledgements)
* [Deployment](#Deployment)
<!--te-->


# How to Play 
- Firstly, you will be asked to input the placement of your ships, totaling 5 in number, with varying lengths (the length will be displayed for you).

![Captura de tela 2024-02-18 093926](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/0746643e-c9ff-4ea4-a987-c103e2ad78b9)

- After completing the placement of your ships, your own battlefield will be displayed, showing the final position of your ships.

![Captura de tela 2024-02-18 093946](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/59579e63-5a26-4008-8617-c9bb883dd318)

- Immediately after, the actual game begins, and you can input the number you believe will hit the enemy ship. The guess number should be in the following format (0,12,13,14,15), with the first number corresponding to the height and the following to the width of the grid.

![Captura de tela 2024-02-18 094747](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/92c376b0-ae99-407a-b61e-7035e228c6a9)

-Both battlefields will be displayed together, with the enemy's field directly below yours.

![Captura de tela 2024-02-18 094944](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/d91457f6-3357-44cf-b665-8e0e7ead2849)

-The game is concluded when you manage to sink all 5 enemy ships or when the enemy sinks all of yours.


# User Experience UX
## User Stories:
- As a user, I wish to be able to visualize my own ships on my grid.
- As a user, I wish to see the letters or numbers above the columns and rows so that I can accurately decide which cell to target.
- As a user, I want to receive notifications about the turns, whether it's my turn or the computer's turn.
- As a user, I want to receive visual cues and text updates that inform me whether I've scored a hit or a miss.
- As a user, I want to be informed which grid is for which purpose if there are more than one.
- As a user, I want to have the option to exit the game at any time.
- As a user, I want to receive a brief introduction to the game and its rules.

# User Story 2: Enhancing Code Clarity and Maintainability for Developers

- As a developer, I aim for code that adheres to readability and maintainability standards.

## Acceptance Criteria:

## Code Structure:

- Given that I'm reviewing the codebase,
- When I navigate through project directories and files,
- Then the code should be logically organized, with clear separation of concerns and a consistent folder structure.

## Comments and Documentation:

- Given that I'm reading the code,
- When I encounter complex or non-trivial sections,
- Then the code should contain helpful comments and documentation elucidating the purpose and functionality of those sections.

## Variable and Function Naming:

- Given that I'm inspecting variable and function names,
- When I come across a variable or function,
- Then the names should be descriptive, following a consistent naming convention, and offering a clear understanding of their purpose.

## Code Formatting:

- Given that I'm scrutinizing the code,
- When I review the formatting,
- Then the code should adhere to a consistent style guide, with proper indentation, spacing, and alignment to enhance readability.

## Avoidance of Magic Numbers:

- Given that I'm analyzing numeric values in the code,
- When I encounter numeric constants lacking clear context,
- Then the code should refrain from employing magic numbers and instead use named constants or variables to enhance readability.

## Error Handling:

- Given that I'm examining error-handling mechanisms,
- When I encounter sections addressing potential errors,
- Then the code should incorporate appropriate error handling with descriptive messages to facilitate issue diagnosis during development and maintenance.


## Additional Considerations:

- Refactoring should be conducted when necessary to elevate code quality.
- The application of design patterns and best practices should be considered where relevant.
- Code should be crafted with future maintainers in mind, anticipating potential project changes and updates.
- Continuous integration and automated code analysis tools should be employed to detect potential issues early in the development lifecycle.


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

- To emulate the traditional Battleship game experience, the design incorporates two grids: the player's grid and the opponent's grid. The player's grid is situated below the opponent's grid. This arrangement mirrors the layout seen in - physical Battleship games, where players typically have their own grid beneath their opponent's. This setup requires the player to record their attacks on their grid while tracking the opponent's strikes on the grid above.
- The screenshot provided demonstrates the alignment of the grids, showcasing the positioning as described.

![Captura de tela 2024-02-12 141633](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/9db950b5-6157-411e-b93a-32c6d4045bb7)

- Player's Grid
  
![Captura de tela 2024-02-12 142028](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/9be93c69-5070-4db7-9923-db3c7a296ce1)

- Enemy's Grid

# Features:

## Grid Presentation:
- The grid for the player and the opponent is showcased.
- The player's vessels are discernible on their grid.
- Alphabets and numerals atop columns and rows for convenient identification.

# Additional upcoming features

- Manual deployment of battleships - Gives players the option to manually position their battleships on the game board.
- Game timer functionality - Introduces a timer for time-based gameplay.
- Screen-clearing capability - Utilizes the os.system import to implement a function for clearing the screen.
- Multiplayer mode activation - Enables player-versus-player battles for a multiplayer gaming experience.

## Hit and Miss Feedback:
- Visual signs and text updates indicate hits ('o') and misses ('X'):

# Utilized Technologies
- Python: Predominant programming language employed in the application.
- GitHub: Platform utilized for repository hosting.
- VS Code: Selected as the primary code editor for composing and modifying the website's code.

## Utilized Libraries:
The Battleship game relies solely on one core library, the random library

# Testing
The code underwent testing, uncovering no significant errors. Despite attempting to utilize PEP8 for code validation, the site's functionality was inaccessible to me. In its place, I utilized Pylint, which offers insights into syntax errors.

![Captura de tela 2024-02-13 134159](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/6191baed-6686-4648-b25b-e7b2dfa0b928)

-I know the test was successful because after choosing the numerical position on the grid, it was displayed on the battle grid.
- ![Captura de tela 2024-02-13 140357](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/56799c96-a925-4206-bab0-9930dd086ea7)
- ![Captura de tela 2024-02-13 140405](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/26ec680a-c908-43dc-b9f1-269aabe1333a)

- I know the test was successful because after choosing the numerical position on the grid where a ship was located, it appeared with the chosen symbol for (hit).

- ![Captura de tela 2024-02-13 140532](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/054a6d62-4576-4e65-9975-9cb0c8a0c8dd)
- ![Captura de tela 2024-02-13 140613](https://github.com/Rupthuz/Battleship-PT3-main/assets/74190717/c8e0f2c5-2a7e-4b03-8edc-74f5af8219e8)

- The same applies when the ship is sunk, making it possible to verify the symbol for (sunk)

# Deployment
- The Battleship project was deployed with Code Institute's mock terminal for Heroku.

## Deployment Steps
- Fork or Clone Repository:
- Fork the repository or clone it to your local machine using the following command: git clone https://github.com/Rupthuz/Battleship-PT3-main
- Create a New Heroku App:
- Log in to your Heroku account.
- Click on the "New" button and select "Create new app."
- Choose a unique app name and set your preferred region.
- Set Buildpacks:
- In the Heroku app dashboard, navigate to the "Settings" tab.
- Scroll down to the "Buildpacks" section.
- Add the following buildpacks in order:
- Python
- NodeJS
- Link Heroku App to Repository:
- In the "Deploy" tab, connect your Heroku app to your GitHub repository.
- Enable automatic deploys if desired. Deploy:
- Manually deploy your app by clicking the "Deploy Branch" button.
- Alternatively, enable automatic deploys for future updates.
- Open App:
- Once the deployment is successful, click on the "Open App" button to view your live application.

# Credits
## Python:
- The Battleship Game is inspired by the tutorial article authored by Mark Anthony Llego /
- Franklin Nascimento (https://www.youtube.com/watch?v=uoG17lg2WCg).
- This project was constructed utilizing a template provided by Code Institute to establish the necessary environment for deployment on Heroku.
- Credits are given to the Code Institute projects, curriculum and previous projects in Python.
- GeeksforGeeks - Python Programming Examples
- PythonDex - Python Battleship Game

# Acknowledgements

- I am grateful for my wife's patience as I allocate significant time to coding.
- Special thanks to my mentor, Daniel Hamilton, for consistently providing valuable feedback.

