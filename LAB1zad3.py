def zadanie3(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x["reward"]/x["time"], reverse=True)
    total_wait_time = 0
    current_time = 0
    for task in sorted_tasks:
        current_time += task["time"]
        total_wait_time += current_time
    return sorted_tasks, total_wait_time




tasks = [
    {"id":1,"time":3,"reward":50},
    {"id":2,"time":1,"reward":20},
    {"id":3,"time":23,"reward":50},
    {"id":4,"time":1,"reward":56},
    {"id":5,"time":43,"reward":5000}
]

sorted_tasks, total_wait_time = zadanie3(tasks)
print("Posortowane zadania:", sorted_tasks)
print("Całkowity czas oczekiwania:", total_wait_time)