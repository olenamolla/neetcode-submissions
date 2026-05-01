class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned_str == cleaned_str[::-1]