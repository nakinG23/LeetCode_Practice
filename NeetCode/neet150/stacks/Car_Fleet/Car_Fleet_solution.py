from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed)) # to have a single list of list of positions and speed, each element is a car
        cars.sort(reverse=True) # to sort them by positiom in descending order
        print(cars)
        times = [(target-pos)/sp for pos,sp in cars]
        print(times)
        st = []

        for pos, sp in cars:
            time = (target-pos)/sp

            if not st or time > st[-1]:
                st.append(time)
                print("st", st, "time", time, "st[-1]", st[-1])
        
        return len(st)

        #     times.append((target-position[i])/speed[i])
        # counts = {}
        # for num in times:
        #     if num in counts:
        #         counts[num] += 1
        #     else:
        #         counts[num] = 1
        # print(len(counts))
        # return len(counts)

sol = Solution()
res = sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
print(res)
"""
2 arrays, speed and position
pos[i] = pos of ith car in miles
speed[i] = speed of the ith car in mile/hr
dest = target miles
target = 10, position = [1,4], speed = [3,2]
t = d/s
t = [10-1/3 , 10-4/2 ] = [3, 3]
"""