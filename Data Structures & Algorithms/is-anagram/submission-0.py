class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = list(s)
        arr2 = list(t)

        arr1.sort()
        arr2.sort()

        if (arr1 != arr2):
            return False

        return True
        