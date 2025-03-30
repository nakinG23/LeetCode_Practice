from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        charfreq_t = [0] * 52
        charfreq_window = [0] * 52
        n1 = len(t)
        n2 = len(s)
        t_list = list(t)
        return_char = ""
        return_char_list = list()
        max_return_char_len = 0
        for c in t:
                if c.islower():
                    charfreq_t[ord(c) - ord('a')] += 1
                else:
                    charfreq_t[ord(c) - ord('A') + 26] += 1

        for i in range(n2):
                if s[i].islower():
                    charfreq_window[ord(s[i]) - ord('a')] += 1
                else:
                    charfreq_window[ord(s[i]) - ord('A') + 26] += 1
                
                if s[i] in t:
                    k = i
                    while t_list and k<n2:
                        if s[k] in t_list:
                            print("about to remove ", s[k], "from", t_list)
                            t_list.remove(s[k])
                        return_char += s[k]
                        k += 1
                    print("return char = ", return_char)
                    if len(return_char) >= n1: 
                        return_char_list.append(return_char)
                    t_list = list(t)
                    return_char = ""
                    print(return_char_list)
                    
                # max_return_char_len = max(max_return_char_len, len(charfreq_window))    
        return return_char


                    # if (a >= b for a, b in zip(t1, t2))

                    # if i >= n1:
                    #     if s[i].islower():
                    #         charfreq_window[ord(s[i - n1]) - ord('a')] -= 1
                    #     else:
                    #         charfreq_window[ord(s[i - n1]) - ord('A') + 26] -= 1

        print(charfreq_t)


sol = Solution()
result = sol.minWindow(s="OUZODYXAZV", t="XYZ")
print(result)