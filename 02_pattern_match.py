class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        print(words)
        
        # Step 1: Length mismatch check
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        # Step 2: Iterate together
        for char, word in zip(pattern, words):
            
            # If mapping exists, check consistency
            if char in char_to_word:
              
                if char_to_word[char] != word:
                    
                    return False
            else:
          
                char_to_word[char] = word
               
            
            # Reverse check
           
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
object = Solution()
print(object.wordPattern("abba", "dog cat cat dog"))  # True
print(object.wordPattern("abba", "dog cat cat fish"))  # False
print(object.wordPattern("aaaa", "dog cat cat dog"))  # False