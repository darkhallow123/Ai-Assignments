In this repository, you will find all the programming assignments for the ICOM5015-001D course.

                         --------------------Is Python fast or slow? Report--------------------

The purpose of this assignment is to visualize the importance of using Python libraries. You should set up an experiment to compare the two cases described below:

You are going to write code in Python (using iteration) to carry out the product of 1-D and 2-D arrays whose dimensions should be compatible with the product to be carried out. You have to time the execution of your code for several cases, e.g. small arrays with dimensionalities less than 10; then try arrays with dimensionalities in the range of several tens; and then try arrays with dimensionalities in the range of several hundreds. Try it for several combinations of products of arrays.
In this second part, you should import NumPy, and use its operations to carry out the product of the same arrays used in 1. Time the execution.

For this experiment, you should compare the results and explain the reason for the difference in processing time. Use appropriate tables and graphics for your comparison. How does processing time grows with the dimensionalities of the arrays? How does processing time varies between vectors (1-D Arrays) and matrices (2-D Arrays) without NumPy vs with NumPy? Find out why the a difference. What language or languages were used for developing the NumPy library?


                         --------------------Programming assignment 2--------------------
			 
3.7) Consider the problem of finding the shortest path between two points on a plane that has convex polygonal obstacles as shown in. This is an idealization of the problem that a robot has to solve to navigate in a crowded environment.
1. Suppose the state space consists of all positions (x,y) in the plane. How many states are there? How many paths are there to the goal?
2. Explain briefly why the shortest path from one polygon vertex to any other in the scene must consist of straight-line segments joining some of the vertices of the polygons. Define a good state space now. How large is this state space?
3. Define the necessary functions to implement the search problem, including a function that takes a vertex as input and returns a set of vectors, each of which maps the current vertex to one of the vertices that can be reached in a straight line. (Do not forget the neighbors on the same polygon.) Use the straight-line distance for the heuristic function.
4. Apply one or more of the algorithms in this chapter to solve a range of problems in the domain, and comment on their performance.


3.9) The missionaries and cannibals problem is usually stated as follows. Three missionaries 
and three cannibals are on one side of a river, along with a boat that can hold one or
two people. Find a way to get everyone to the other side without ever leaving a group of missionaries 
in one place outnumbered by the cannibals in that place. This problem is famous inAI because it was 
the subject of the first paper that approached problem formulation from an analytical viewpoint 
(Amarel, 1968).
a. Formulate the problem precisely, making only those distinctions necessary to ensure a
valid solution. Draw a diagram of the complete state space.
b. Implement and solve the problem optimally using an appropriate search algorithm. Is it
a good idea to check for repeated states?
c. Whydoyouthink people have a hard time solving this puzzle, given that the state space
is so simple?	


                         --------------------Programming assignment 3--------------------
   
Generate a large number of 8-puzzle and 8-queens instances and solve them (where possible) by hill climbing (steepest-ascent and first-choice variants), hill climbing with random restart, and simulated annealing. Measure the search cost and percentage of solved problems and graph these against the optimal solution cost. Comment on your results. 





