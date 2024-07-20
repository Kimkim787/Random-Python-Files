# Adding a yield statement means the loop will yield control at the specified 
# point while still maintaining its context. 
# This way, the yielding task can be restarted later.

import queue

def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total=0
        
        for x in range(count):
            total += 1
            print(f"task {name} running")
            yield
        print(f"task {name} total: {total}")

def main():
    work = queue.Queue()
    for w in [15, 10, 2]:
        work.put(w)
    
    tasks = [task("one", work), task("two", work), task("three", work)]

    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

main()