class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reversed_text = cleaned[::-1]
        
        if cleaned == reversed_text:
            return True
        
        return False