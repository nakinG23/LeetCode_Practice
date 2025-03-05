from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strs = ''
        for words in strs:
            if not encoded_strs:
                encoded_strs = words 
            else:
                encoded_strs = encoded_strs + "^^" + words 
        print("Encoded List:", encoded_strs)
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_list = s.split("^^")
        if decoded_list == ['']:
            decoded_list = []
        print("Decoded List: ", decoded_list)
        return decoded_list

sol = Solution()
strs = []
# strs = ["neet","code","love","you"]
result_encode = sol.encode(strs)
result_decode = sol.decode(result_encode)

# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]
