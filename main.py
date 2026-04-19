import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []

    def add_task(self, priority, task):
        heapq.heappush(self.heap, (-priority, task))

    def get_next(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]

# Misol:
scheduler = TaskScheduler()
scheduler.add_task(3, "Vazifa 1")
scheduler.add_task(1, "Vazifa 2")
scheduler.add_task(2, "Vazifa 3")

print(scheduler.get_next())  # Vazifa 2
print(scheduler.get_next())  # Vazifa 3
print(scheduler.get_next())  # Vazifa 1
