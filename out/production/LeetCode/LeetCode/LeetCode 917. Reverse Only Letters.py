class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        base_str = S
        reverse_str = S[::-1]
        import string
        idx =[]
        cnt = 0
        for letter in base_str:
            if letter in string.ascii_letters:
               idx.append(cnt) 
            cnt+=1
        base_str = list(base_str) 
        for letter in reverse_str:
            if letter in string.ascii_letters:
                new_idx = idx.pop(0)
                base_str[new_idx]=letter
        return ''.join(base_str)