#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''    
class Solution:
    def JobScheduling(self,jobs,n):
        # jobs.sort(key=lambda x: x.profit, reverse=True)
        
        max_deadline = max(job.deadline for job in jobs)
        
        result = [-1] * max_deadline
        job_sequence = 0
        total_profit = 0
        
        for job in jobs:
            for t in range(min(max_deadline, job.deadline) - 1, -1, -1):
                if result[t] == -1:
                    result[t] = job.id
                    job_sequence += 1
                    total_profit += job.profit
                    break
        return job_sequence, total_profit