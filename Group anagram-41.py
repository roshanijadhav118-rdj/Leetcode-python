class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for arr in strs:
            key = "".join(sorted(arr))

            if key not in groups:
                groups[key] = []

            groups[key].append(arr)

        return list(groups.values())
