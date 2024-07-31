# Python program to find a path from corner cell to
# middle cell in maze containing positive numbers
def printPath(maze, i, j, ans):

	# If we reach the center cell
	if (i == len(maze) // 2 and j == len(maze) // 2):

		# Make the final answer, Print
		# final answer and Return
		ans += "(" + str(i) + ", " + str(j) + ") -> MID";
		print(ans);
		return;
	
	# If the element at the current position
	# in maze is 0, simply Return as it has
	# been visited before.
	if (maze[i][j] == 0):
		return;
	
	# If element is non-zero, then note
	# the element in variable 'k'
	k = maze[i][j];

	# Mark the cell visited by making the
	# element 0. Don't worry, the element
	# is safe in 'k'
	maze[i][j] = 0;

	# Make recursive calls in all 4
	# directions pro-actively i.e. if the next
	# cell lies in maze or not. Right call
	if (j + k < len(maze)):
		printPath(maze, i, j + k, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	
	# down call
	if (i + k < len(maze)):
		printPath(maze, i + k, j, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	
	# left call
	if (j - k > 0):
		printPath(maze, i, j - k, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	
	# up call
	if (i - k > 0):
		printPath(maze, i - k, j, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	
	maze[i][j] = k;

if __name__ == '__main__':

	maze = [[ 3, 5, 4, 4, 7, 3, 4, 6, 3 ],[ 6, 7, 5, 6, 6, 2, 6, 6, 2 ],[ 3, 3, 4, 3, 2, 5, 4, 7, 2 ],
			[ 6, 5, 5, 1, 2, 3, 6, 5, 6 ],[ 3, 3, 4, 3, 0, 1, 4, 3, 4 ],[ 3, 5, 4, 3, 2, 2, 3, 3, 5 ],
			[ 3, 5, 4, 3, 2, 6, 4, 4, 3 ],[ 3, 5, 1, 3, 7, 5, 3, 6, 4 ],[ 6, 2, 4, 3, 4, 5, 4, 5, 1 ]] ;
	printPath(maze, 0, 0, "");
