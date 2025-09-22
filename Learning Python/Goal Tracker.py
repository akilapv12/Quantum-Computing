# Goal Tracker

tasks=input("Enter your tasks separated by commas: ").split(', ')
print("Your tasks are:")
for index, task in enumerate(tasks):  #enumerate() adds a counter to the iterable
    print(index, "-", task)

done=input("Enter the numbers of the tasks you have completed (separated by commas):  ").split(', ')
if  len(done) < len(tasks):
    print("You have completed:", [tasks[int(i)] for i in done])
    for i in sorted(map(int, done), reverse=True): #map() makes the contents of done into int.
        tasks.pop(i)                               #sorted() reverse=true makes it in descending order.
    print("Remaining tasks are:", tasks)           #tasks.pop(1) removes each number.