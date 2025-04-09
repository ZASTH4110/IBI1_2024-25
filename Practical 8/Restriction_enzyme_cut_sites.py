import re

def find_restriction_sites(DNA_sequence, enzyme_sequence):
    # Uses regular expressions to find all positions where a restriction enzyme
    # recognition sequence matches within a DNA sequence.
    
    # Parameters:
    # - DNA_sequence (str): DNA string to scan
    # - enzyme_sequence (str): Recognition sequence of the enzyme
    
    # Returns:
    # - List of positions where matches start
    
    # Convert to uppercase
    DNA_sequence = DNA_sequence.upper() 
    enzyme_sequence = enzyme_sequence.upper()

    # Validate sequences: must contain only A, C, G, T
    if not re.fullmatch(r'[ACGT]+', DNA_sequence): #r'[ACGT]+' # Matches one or more A, C, G, T
        return "Error: DNA sequence contains invalid characters."
    if not re.fullmatch(r'[ACGT]+', enzyme_sequence): #r'[ACGT]+' # Matches one or more A, C, G, T
        return "Error: Enzyme sequence contains invalid characters."

    # Use re.finditer to find all match start positions
    matches = list(re.finditer(enzyme_sequence, DNA_sequence))
    if matches:
        positions = [match.start()+1 for match in matches]
        return positions
    else:
        return "No matches found."
 
     
print(find_restriction_sites("ACGTACGTAGCTAGCTAGCTAGCTAGC", "GCTAG"))  # Example usage
# Output: [9, 17] (positions where "GCTAG" starts in the DNA sequence)
print(find_restriction_sites("ACGTACGTAGCTAGCTAGCTAGCTAGC", "XYZ"))  # Invalid enzyme sequence
# Output: Error: Enzyme sequence contains invalid characters.
print(find_restriction_sites("ATGCGTACGTCGCGCGTACG", "GAATTC"))  # Example usage
