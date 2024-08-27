
class Solution:
    def tour(self, lis, n):
        # Initialize variables
        total_gas = 0
        total_cost = 0
        tank = 0
        start_station = 0
        
        for i in range(n):
            gas = lis[i][0]   
            cost = lis[i][1]  
            
            total_gas += gas
            total_cost += cost
            tank += gas - cost
            
            if tank < 0:
                start_station = i + 1
                tank = 0
        
        if total_gas < total_cost:
            return -1
        
        return start_station
