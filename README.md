# AI_Problem_Solving_as_Search
Single Agent Problem Solving Tasks: 8-Puzzle and Bricks World

Problem-Solving as Search
Depaul University 
CSC 480
Professor Steven Lytinen
Spring 2018


Many problem-solving tasks which use search have the following 
properties:

1.	They are single agent
2.	Sensing is perfect, at least with respect to the percepts
	that are necessary for the problem
3.	The results of actuators are deterministic
4.	Other than the effects of the actuators, the world remains
	the same
5.	The agent function is extremely limited (i.e., the agent
	function has very little domain knowledge)

Blocks world:

-	Implement the toy blocks world.
	-	The world has 3 blocks (r, o, b)
	-	Devise a way to represent state 
		-	For example, 'rob' could represent
			red-orange-blue
		-	Keep in mind that the relative position of
			a block or stack of blocks on the table is
			irrelevant
	-	The user should be able to input the start state
		and the goal state
	-	The agent must then be able to calculate the sequence
		of stacks and unstacks that it takes to solve
		the problem, using depth-first, breadth-first, and
		best-first search

8 Puzzle Game:

A simple 'estimator' function is provided which counts the number of
tiles that are in the right place (evaluates to an integer between 0
and 8).

The goal is to choose or devise a better estimator function for the 
8-puzzle.

-	Correctly implement a new best-first algorithm using an 
	estimator of choice (Note: chosen estimator is Manhattan
	distance)
-	Provide numerical evidence that the chosen estimator performs
	better than the one provided

