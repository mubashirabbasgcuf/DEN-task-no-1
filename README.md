# DEN-task-no-1
Currently doing internship virtually with DEN and these are my submitted projects in python programming
just read the pdf file i have explained  all its working 
 
PYTHON INTERNSHIP
Task no 1:
 
 
#Introduction:

What is the Red   Blue Game?

The Red   Blue Nim game is a two   player game with two types of marbles: red and blue. There are two versions of the game:

1. Standard Version:
       Setup: Start with a certain number of red and blue marbles.
       Turns:   Players take turns removing marbles. They can remove any number from one pile or one marble   from each pile.
         Ending:   The game ends when a player has no marbles to remove on their turn.
         Losing Condition:   A player loses if either pile is empty on their turn.

2.   Misrere Version:  
         Setup:   Start with a certain number of red and blue marbles.
         Turns:   Players take turns removing marbles. They can remove any number from one pile or one marble from each pile.
         Ending:   The game ends when a player has no marbles to remove on their turn.
         Winning Condition:   A player wins if either pile is empty on their turn.

  Scoring:  
    Each red marble left is worth 2 points.
    Each blue marble left is worth 3 points.
    The final score is the sum of the points for each remaining marble. The player with the higher score wins.

Rules

  Command   Line Usage:  
To play the game, use the command   line tool with the following format:

python red_blue_nim.py       num   red <num>       num   blue <num>       version <version>       first   player <player>       depth <depth>

  Parameters:  
•	     num   red <num>`: Number of red marbles. Example: `      num   red 10`
•	     num   blue <num>`: Number of blue marbles. Example: `      num   blue 10`
•	     version <version>`: Game version (`standard` or `misere`). Default is `standard`.
•	     first   player <player>`: Who plays first (`human` or `computer`). Default is `computer`.
•	     depth <depth>`: Search depth for AI. Example: `      depth 5`

 Game Flow

•	1.   Initialization:   Start with a set number of marbles and determine the first player.
•	2.   Human Move:   Enter your move (e.g., "1 red" or "2 blue 1 red").
•	3.   Input Validation:   Ensure the move is valid (e.g., not more marbles than available).
•	4.   Update Game State:   Reflect the human move in the game state.
•	5.   Computer Move:   AI makes a move using MinMax algorithm with Alpha Beta Pruning.
•	6.   Update Game State:   Reflect the computer’s move in the game state.
•	7.   Game Over Check:   Check if the game has ended.
•	8.   Repeat:   Continue alternating moves until the game ends.

 Human Move Input and Validation:

When it’s your turn:
    Enter the move as "X red" or "X blue Y red".
    The program checks if the move is valid (e.g., not removing more marbles than available).

Computer Move Determination:

  MinMax Algorithm:  
•	Purpose:   Determines the best move by exploring all possible outcomes.
•	Alpha Beta Pruning:   Optimizes MinMax by reducing the number of nodes to explore.

  How It Works:  
•	Alpha and Beta:   Track the best possible scores for both players.
•	Pruning:   Avoid exploring moves that don't improve the outcome.

 Move Ordering:

  Standard Version:  
	Pick 2 red marbles
	Pick 2 blue marbles
	Pick 1 red marble
	Pick 1 blue marble

	Misère Version:  
	Pick 1 blue marble
	Pick 1 red marble
	Pick 2 blue marbles
	Pick 2 red marbles

Depth   Limited Search (Extra Credit)

  Purpose:   Improve efficiency by limiting search depth.
      Heuristic Evaluation:   Score game states based on factors like marble counts and potential moves.

 End of Game:

  Game Over Conditions:  

  Standard Version:  
    Ends when a pile is empty.

  Misere Version:  
    Ends when one player has one marble left in one pile, and the other player has no moves left.
    Can also end if a player resigns or the maximum number of moves is reached.

  Scoring Calculation:  
 	Red Marbles:   2 points each.
 	Blue Marbles:   3 points each.

 Demonstration:

  Initial Game State:  
	Red Marbles: 10
	Blue Marbles: 10
	Human Player Goes First

  Example Moves:  
o	Human Move:   2 red marbles, 1 blue marble
o	Updated Game State: Red Marbles: 8, Blue Marbles: 9
o	Computer Move:   1 red marble, 2 blue marbles
o	Updated Game State: Red Marbles: 7, Blue Marbles: 7

  Game Over Example:  
	Final State:   Red Marbles: 0, Blue Marbles: 3
	Human Score:   6 (3 blue marbles x 2 points each)
	Computer Score:   14 (7 red marbles x 2 points each + 3 blue marbles x 3 points each)

  Result:   Computer wins!

