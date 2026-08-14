from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        left = 0
        have = 0
        need_count = len(need)

        result = ""
        result_len = float("inf")

        for right in range(len(s)):

            # Add character to window
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Character requirement satisfied
            if char in need and window[char] == need[char]:
                have += 1

            # Shrink while window is valid
            while have == need_count:

                # Update smallest window
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result
