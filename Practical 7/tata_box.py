import re  # Import the regular expression module

tata_box = re.compile(r'TATA[AT]A[AT]')  # Compile a regex pattern to match the TATAWAW motif
gene_name = re.compile(r'gene:([^\s]+)')  # Compile a regex pattern to extract gene names from header lines
tata_genes = {}  # Create a dictionary to store genes containing the TATAWAW motif

# Open the file containing sequences for reading
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as data:
    current_gene = None  # Initialize the current gene name to None
    current_seq = ""  # Initialize the current sequence to an empty string

    # Read the file line by line
    for line in data:
        line = line.strip()  # Remove leading and trailing whitespace from the line
        if line.startswith(">"):  # Check if the line is a header line
            if current_gene and tata_box.search(current_seq):  # If a gene is active and its sequence contains the motif
                tata_genes[current_gene] = current_seq  # Add the gene and its sequence to the dictionary
            gene_match = gene_name.search(line)  # Search for the gene name in the header line
            if gene_match:  # If a gene name is found
                current_gene = gene_match.group(1)  # Extract the gene name
            else:  # If no gene name is found
                current_gene = None  # Set the current gene to None
            current_seq = ""  # Reset the current sequence
        else:  # If the line is a sequence line
            current_seq += line  # Append the line to the current sequence

    # After reading all lines, check the last gene and its sequence
    if current_gene and tata_box.search(current_seq):  # If the last gene contains the motif
        tata_genes[current_gene] = current_seq  # Add the gene and its sequence to the dictionary

# Open an output file to write the selected genes and their sequences
with open("tata_genes.fa", "w") as out:
    for gene, seq in tata_genes.items():  # Iterate over the genes and their sequences
        out.write(f">{gene}\n")  # Write the gene name as a header line
        out.write(seq + "\n")  # Write each line of the sequence

# Print a message indicating the process is complete
print(f" Finished! A total of {len(tata_genes)} genes containing the TATAWAW motif have been selected and written to tata_genes.fa.")

