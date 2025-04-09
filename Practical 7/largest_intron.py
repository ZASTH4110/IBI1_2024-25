# Using re.fidnall() to find the longest possible intron in a sequence
# the longest possible intron in a sequence
# print
import re as re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
Intron = re.findall(r'GT\S+AG', seq) 
# to find GT...AG and include the GT and AG in the result.
longest_intron = max(Intron, key=len) #find the longest intron
print("Longest possible intron found:")
print(f"Sequence: {longest_intron}")# print the longest intron sequence
print(f"Length: {len(longest_intron)} bp") # print the length of the longest intron