"""EoPI pg 24
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
For example, the parity of 1011 is 1, and the parity of 10001000 is 0. 
Parity checks are used to detect single bit errors in data storage and communication. 
It is fairly straightforward to write code that computes the parity of a single 64-bit word.
How would you compute the parity of a very large number of 64-bit words?
Hint: Use a lookup table, but don't use 2^64 entries!
"""

from test_framework import generic_test


CACHE_LEN=2**16
cache=[0, 1]


def parity(n: int) -> int:
    """generate largest number of bit length n
    
    Args:
        n: integer to get parity of
    
    Returns:
        int 0 or 1 for parity
    """
    bl = n.bit_length()
    while bl>1:
        if n<len(cache):
            return cache[n]
        if (bl % 2)==0:
            s=(bl//2)
            n=(n&((1 << s) - 1)) ^ (n>>s)
        else:
            n=(n >> 1 )^(n&1)
        bl=n.bit_length()
    return n

#dont bother with dynamic caching just cache in advance
for i in range(2,CACHE_LEN):
    cache.append(parity(i))



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
