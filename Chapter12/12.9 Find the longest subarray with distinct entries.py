"""
Problem 12.9 Find the longest subarray with distinct entries

Items to keep track of:
1. the length of the longest subarray so far: max_len
2. the start of the longest subarray (or potentially longest): start
3. letter we have seen so far: used = {}

when we see a letter in the string one of the following situations can happen:
1. it's not in the used{} - todo: add it into used{}, and add 1 to max_len
2. it's in the used{} and the current start position is smaller or equal to this letter - todo: we discard all the
substring before and update the start to the new position, which is a  start for a potentially longer substring
3. it's in the used{} but the current start position is greater than the first occurrence of this letter so we don't
need to update the start position again

in addition, for every letter we see, we update its index in the dictionary, i.e. if we haven't seen it, we will add it;
if we saw it before, we will update the index to the new position of the same letter.
"""

def longest_sub(S):
    max_len, start = 0, 0
    used = {}
    for i, e in enumerate(S):
        if e in used and start <= used[e]:
            start = used[e] +1
        else:
            max_len = max(max_len, i - start+1)
        used[e] = i
    return max_len

def main():
    S1 = "aaabcdaafhb"
    S2 = "tmmzuxt"
    print(longest_sub(S2))
if __name__ == "__main__":
    main()
