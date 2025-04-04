import re as re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
Intron = re.findall(r'GT\S+AG', seq)
longest_intron = max(Intron, key=len)
print("Longest possible intron found:")
print(f"Sequence: {longest_intron}")
print(f"Length: {len(longest_intron)} bp")