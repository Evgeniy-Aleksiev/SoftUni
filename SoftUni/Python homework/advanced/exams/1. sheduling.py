from collections import deque

def clock_cycles(jobs, searched_index):
    sorted_jobs = deque(sorted([(jobs[index], index) for index in range(len(jobs))]))
    total_cycles = 0

    while True:
        number = sorted_jobs.popleft()
        total_cycles += number[0]
        if number[-1] == searched_index:
            break

    return total_cycles

number_of_jobs = [int(x) for x in input().split(', ')]
interest_job_index = int(input())
print(clock_cycles(number_of_jobs, interest_job_index))