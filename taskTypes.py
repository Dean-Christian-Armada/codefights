def tasksTypes(deadline, day):
	all = len(deadline)
	today = len([x for x in deadline if x<=day])
	upcoming = len([x for x in deadline if x>=day+1 and x<=day+7])
	later = (today+upcoming) - all
	return [today, upcoming, abs(later)] # abs is used to make sure it does not return negative


input1 = [1,2,3,4,5]
input2 = 2
print tasksTypes(input1, input2)


# You have some tasks in your Asana account. For each ith of them you know its deadlinei - the last day by which it should be completed. As you can see in your calendar, today is the day number day. Asana labels each task in accordance with its due date:

# If the task is due today or it's already overdue, it is labeled as Today;
# If the task should be completed within a week (but not today), i.e. its deadline is somewhere between day + 1 and day + 7 both inclusive, it is labeled as Upcoming;
# All other tasks are labeled as Later;
# Your goal is to find the number of tasks with each label.

# Example

# For deadline = [1, 2, 3, 4, 5] and day = 2, the output should be
# tasksTypes(deadline, day) = [2, 3, 0];
# For deadline = [1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8] and day = 1, the output should be
# tasksTypes(deadline, day) = [2, 8, 2].
# Input/Output

# [time limit] 4000ms (py)
# [input] array.integer deadline

# Constraints:
# 1 ≤ deadline.length ≤ 15,
# 1 ≤ deadline[i] ≤ 15.
