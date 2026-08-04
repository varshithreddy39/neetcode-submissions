class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for word in strs:
            key="".join(sorted(word))

            if key not in group:
                group[key]=[]
            group[key].append(word)
        return list(group.values())
