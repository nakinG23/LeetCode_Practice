# Definition for a pair.
from typing import List
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        # create a list to store intermediate states
        intermediate_states = []
        
        if pairs:
            intermediate_states.append(pairs[:])
            sorted_pairs = pairs[:]
            # insertion sort now
            for i in range(1,len(sorted_pairs)):
                key = sorted_pairs[i] # we need to start from the second element
                j = i-1
                # print(sorted_pairs[j].key)
                # print(key.key)
                while j >= 0 and sorted_pairs[j].key > key.key:
                    sorted_pairs[j+1] = sorted_pairs[j]
                    j -= 1

                sorted_pairs[j+1] = key
                intermediate_states.append(sorted_pairs[:])
            
        return intermediate_states

# Sample input
# pairs = [
#     Pair(4, "apple"),
#     Pair(2, "banana"),
#     Pair(3, "cherry"),
#     Pair(1, "date")
# ]
pairs = []
# Creating Solution instance and calling insertionSort
solution = Solution()
intermediate_results = solution.insertionSort(pairs)

# Printing intermediate states
print("Intermediate States:")
for idx, state in enumerate(intermediate_results):
    print(f"Step {idx + 1}: ", [(p.key, p.value) for p in state])