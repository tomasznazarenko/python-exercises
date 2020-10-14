# University students are taking an oral exam at the end of the course.
# 
# They get questions simultaneously and have enough time to prepare the answer. 
# Once a student is ready, they put their name on the board in front of the class and wait for their turn to present the answer to the professor.
# 
# If the professor likes it, the student gets the grade, removes their name from the board, and leaves the exam.
# However, sometimes the professor might want to give the student an additional small task. 
# In this case, they will need to immediately put their name at the end of the current name list on the board and present the solution 
# to the extra question as soon as their turn comes. This can repeat a couple of times before the student finally gets the grade.
# 
# Given the log of the exam, print out the names of the students in the order they were leaving the exam.
# 
# The number n denotes the total number of records. READY student_name means that the student called student_name is ready to present their answer. 
# PASSED means that the student whose turn it is passed the exam, while EXTRA means that they received an extra question and will have to present again.

from collections import deque

number_of_operations = int(input())
queue = deque()

for _ in range(number_of_operations):
    operation = input().split()

    if operation[0] == 'READY':
        queue.appendleft(operation[1])
    elif operation[0] == 'EXTRA':
        name = queue.pop()
        queue.appendleft(name)
    elif operation[0] == 'PASSED':
        print(queue.pop())
