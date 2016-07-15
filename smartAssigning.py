def smartAssigning(information):
	status_list = []
	tasks_list = []
	projects_list = []
	count = 0
	for x in information:
		_x = information[count]
		status_list.append(_x[1])
		tasks_list.append(_x[3])
		projects_list.append(_x[2])
		count += 1
	status_list = [int(x) for x in status_list]
	a = [x for x in status_list if(x)]
	if(len(a) == 1): # Conditional if only one is not in vacation
		return information[status_list.index(1)][0]
	else:
		exclude_indices = [] # This is where all the indexes of the person in vacation are stored
		exclude_indices = [_x for _x, _y in enumerate(status_list) if not _y] # _x is the index element _y = value of the element
		_tasks_list = [int(x) for x in tasks_list] # The original task list without excludes
		tasks_list = [_y for _x, _y in enumerate(_tasks_list) if _x not in exclude_indices]
		b = min(tasks_list)
		_b = _tasks_list.index(b)
		if(_tasks_list.count(b) == 1): # Conditional if only one is has the minimum task
			return information[_b][0]
		else:
			_projects_list = [int(x) for x in projects_list]
			projects_list = [_y for _x, _y in enumerate(_projects_list) if _x not in exclude_indices]
			c = min(projects_list)
			_c = _projects_list.index(c)
			if(_projects_list.count(c) == 1):
				return information[_c][0]
			else:
				return None
# input1 = ["John","1","1","2"]
# input2 = ["Martin","0","0","0"]
# input3 = ["Luke","1","2","1"]
input1 = ["John","1","1","6"]
input2 = ["Martin","1","2","6"]

# input = [input1, input2, input3]
input = [input1, input2]
print smartAssigning(input)




# Asana is exploring a smart-workload feature designed to streamline task assignment between coworkers. Newly created tasks will be automatically assigned to the team member with the lightest workload. For each person the following information is known:

# name - their name, a string containing only uppercase and lowercase letters;
# status - their vacation indicator status, which is "0" if the person is on a vacation, or "1" otherwise;
# projects - the number of projects they are currently involved in;
# tasks - the number of tasks assigned to the report.
# If a person's vacation indicator value is set to "0", this means they are on vacation and cannot be assigned new tasks. Conversely, a vacation indicator value of "1" means they are open to receive task assignments.

# Asana sorts team members according to their availability. Person A has a higher availability than person B if they have fewer tasks to do than B, or if these numbers are equal but A has fewer assigned projects than B. Put another way, we can say that person A has a higher availability than person B if their (tasks, projects) pair is less than the same pair for B.

# Your task is to find the name of the person with the highest availability. It is guaranteed that there is exactly one such person.

# Example

# Consider information about two team members:

# John, with status = "1", projects = "2" and tasks = "6", represented as ["John", "1", "2", "6"];
# Martin, with status = "1", projects = "1" and tasks = "5", represented as ["Martin", "1", "1", "5"].
# For this case, the output should be smartAssigning(information) = "Martin".

# Here John and Martin's vacation indicators are both "1", so both of them are open to new assignments. Martin is only assigned 5 tasks while John is assigned 6, so Martin has the highest availability.

# For the following employees' information:

# John, with status = "1", projects = "2" and tasks = "6", represented as ["John", "1", "2", "6"];
# Martin, with status = "0", projects = "1" and tasks = "5", represented as ["Martin", "0", "1", "5"];
# the output should be smartAssigning(information) = "John".

# In this example Martin cannot be assigned any new tasks because his vacation indicator is "0". Therefore, "John" has the highest availability.

# For the following information:

# John, with status = "1", projects = "1" and tasks = "6", represented as ["John", "1", "1", "6"];
# Martin, with status = "1", projects = "2" and tasks = "6", represented as ["Martin", "1", "2", "6"];
# the output should be smartAssigning(information) = "John".

# Both John and Martin's vacation indicators are "1", and the number of tasks each of them is assigned is 6. However, John is involved in just 1 project, while Martin is involved in 2, so John has the highest availability.

# Input/Output

# [time limit] 4000ms (py)
# [input] array.array.string information

# Array containing information about team members, where each of information[i] contains exactly 4 elements.

# Constraints:
# 1 ≤ information.length ≤ 10,
# 1 ≤ information[i][j].length ≤ 6.

# [output] string

# The name of the person with the highest availability.