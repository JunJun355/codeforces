# t = int(input())
# for _ in range(t):
#     a, b = [int(c) for c in input().split()]

#     res = 0
#     num = 2

#     while a % num == 0 and (b + 1) % num == 0:
#         num <<= 1
#         res += 1

#     # print(num, res)
#     if b >> res != a >> res:
#         thing = (a >> res) + (b >> res) + 1
#         # print("Thing:", thing)
#         b = False
#         while thing > 0:
#             if thing & 1 == 1:
#                 if thing == 1: b = True
#                 break
#             thing >>= 1
#         if b:
#             res += 1
#     # print(res)
#     print((1 << res) - 1)


import sys

# Increase recursion depth to handle deep splitting for large integers, 
# though ~60 depth is typical for 10^18.
sys.setrecursionlimit(2000)

def count_valid(l, r):
    """
    Recursive function to count valid x values (including 0).
    """
    if l == r:
        return 1
    
    # Find the most significant bit (MSB) where l and r differ.
    # In Python, (l ^ r).bit_length() gives the number of bits required to represent the XOR,
    # so bit_length() - 1 is the index of the MSB (0-indexed).
    diff = l ^ r
    k = diff.bit_length() - 1
    
    # Optimization: If the range [l, r] perfectly covers a power-of-2 block aligned 
    # with this MSB, then all x < size are valid permutations.
    # size is 2^(k+1)
    size = 1 << (k + 1)
    if (r - l + 1) == size:
        return size

    # The split point is the start of the block where bit k is 1.
    # This effectively clears the lower k bits of r.
    # Mask creates a sequence of 1s for bits 0 to k-1, then we invert it.
    split = r & ~((1 << k) - 1)
    
    # We now have two intervals:
    # Left (bit k is 0): [l, split - 1]
    # Right (bit k is 1): [split, r]
    
    # Case 1: The k-th bit of x is 0.
    # x must satisfy constraints for both intervals independently.
    # The valid count is the intersection (min) of valid counts for both sides.
    ans = min(count_valid(l, split - 1), count_valid(split, r))
    
    # Case 2: The k-th bit of x is 1.
    # This swaps the Left and Right intervals.
    # This is only structurally valid if both intervals have the exact same length.
    len_l = (split - 1) - l + 1
    len_r = r - split + 1
    
    if len_l == len_r:
        # If lengths are equal, the count contributed is identical to Case 1
        # because the constraints are symmetric.
        ans += count_valid(l, split - 1)
        
    return ans

def solve():
    # Fast I/O is necessary for t=10^5
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))
    results = []

    for _ in range(t):
        l = int(next(iterator))
        r = int(next(iterator))
        
        # The recursive function counts x=0 (identity), but the problem
        # asks for "positive integer x", so we subtract 1.
        results.append(str(count_valid(l, r) - 1))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()