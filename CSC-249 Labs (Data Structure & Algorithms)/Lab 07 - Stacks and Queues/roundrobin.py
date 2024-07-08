"""
File: roundrobin.py
Using a queue to implement a round-robin CPU job scheduling.
"""

from listqueue import ListQueue


def round_robin(job_queue):
    while len(job_queue) > 0:
        # Start by checking if the queue is empty
        if job_queue.isEmpty():
            print(f"Job queue: {job_queue}")
            break  # Break statement to stop the while loop
        else:
            print(f"Current job: {job_queue.peek()}")

        # Conditional for dealing with the exercise logic
        if job_queue.peek() > 10:
            print("Job unfinished. Return to the rear of the queue.")
            remaining_job = job_queue.pop()
            job_queue.add(remaining_job - 10)
        else:
            print("Job finished")
            job_queue.pop()

        print(f"Job queue: {job_queue}")


def main():
    job_list = [17, 5, 32, 8, 24]
    job_queue = ListQueue(job_list)
    print("Initial job queue:", job_queue)
    round_robin(job_queue)


if __name__ == "__main__":
    main()