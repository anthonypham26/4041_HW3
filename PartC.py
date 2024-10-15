from PartB import PriorityQueue
import math

class Task:

    def __init__(self, name, priority, time, deadline):
        self.name = name #name of task
        self.time = time #amount of time it takes to complete task, 1 being a short amount of time, 10 being being a large amount
        self.deadline = deadline #date on which the task is due, 1 being a further away deadline, 10 being a close deadline
        self.priority = priority #importance of task, 1 being not very important, 10 being very important

    def __repr__(self):
        return f"Task({self.name}, priority={self.priority}, time={self.time}, urgency={self.deadline})"

    def compare_tasks(a, b): #determines the best task, or the task to be completed first.
        best_task = Task("Best", 10, 10, 10) 
        dist_a = math.sqrt(0.5 * (a.priority - best_task.priority) ** 2 + 0.3 * (a.deadline - best_task.deadline) ** 2 + 0.2 * (a.time - best_task.time) ** 2)
        dist_b = math.sqrt(0.5 * (b.priority - best_task.priority) ** 2 + 0.3 * (b.deadline - best_task.deadline) ** 2 + 0.2 * (b.time - best_task.time) ** 2)
        
        return dist_a > dist_b

if __name__ == '__main__':

    tasks = [Task("Task 1", 5, 3, 7),
             Task("Task 2", 8, 1, 5),
             Task("Task 3", 3, 5, 9),
             Task("Task 4", 9, 2, 2),
             Task("Task 5", 4, 4, 6)]

    task_heap = PriorityQueue(Task.compare_tasks)
    task_heap.build_heap(tasks)
    task_heap.display()

    popped_task = task_heap.pop()
    print(f"Best task popped: {popped_task}")
    task_heap.display()

    

