class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        tmp = bin(n)[2:].zfill(32)
        tmp = tmp[::-1]
        return int(tmp,base=2)