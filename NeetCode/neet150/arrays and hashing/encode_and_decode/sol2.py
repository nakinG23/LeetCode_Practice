from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strs = ''.join(f"{len(word)}:{word}" for word in strs)
        print("Encoded List:", encoded_strs)
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = s.find(":", i)  # Find the separator ":"
            length = int(s[i:j])  # Extract length
            i = j + 1  # Move to the start of the word
            decoded_list.append(s[i:i+length])  # Extract word
            i += length  # Move to the next segment
        
        print("Decoded List:", decoded_list)
        return decoded_list



sol = Solution()
# strs = [""]
strs = ["neet","code","love","you"]
result_encode = sol.encode(strs)
result_decode = sol.decode(result_encode)