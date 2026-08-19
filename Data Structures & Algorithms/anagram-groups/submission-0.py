class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        
        for i in strs:
            sorted_str = "".join(sorted(i))
            
            dict[sorted_str].append(i)
    
        return list(dict.values())