        Planning for Autonomous Robots

Project 1

Name: Cristian Bueno

###########################################
Description: The following program has been created to solve an sliding puzzle size 3x3.
The program will apply the BFS method to calculate all the possible nodes and solutions, and using backtrack it
will return the path to solve the puzzle. This program will generate three files : Nodes, NodesInfo and nodePath which
will contain the nodes information. Additionally, the program plot_path.py will help to visualize the result.

The program has been fully written on python 3.8 and is using the libraries: numpy, copy and collections which do not
need any especial installation other than python.

In orden to run the program:

1. Open the program project1
2. On line 214 enter the goal
3. On line 215 enter the initial condition of the puzzle.

The terminal prompt will show the The Goal puzzle, the Initial condition and the nodes to solve the problem.
In case the message "This puzzle doesn't have a solution" appears, check the initial condition for possible errors.
This message indicates that the puzzle is unsolvable.
