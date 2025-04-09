import re  # Import the regular expression module

tata_pattern = re.compile(r'TATA[AT]A[AT]')  # Compile a regex pattern to match the TATAWAW motif
gene_pattern = re.compile(r'gene:([^\s]+)')  # Compile a regex pattern to extract gene names from header lines

valid_signals = {'GTAG', 'GCAG', 'ATAC'}  # Define valid splice signals
signal = input("Please input splice signal (GTAG / GCAG / ATAC): ").strip().upper()  # Prompt user for splice signal and convert to uppercase

if signal not in valid_signals:  # Check if the input signal is valid
    print("Error: only GTAG, GCAG, or ATAC are allowed.")  # Print error message if invalid
    exit()  # Exit the program

splice_patterns = {  # Define regex patterns for each splice signal
    'GTAG': re.compile(r'GT\S+AG'),  # Pattern for GTAG
    'GCAG': re.compile(r'GC\S+AG'),  # Pattern for GCAG
    'ATAC': re.compile(r'AT\S+AC')   # Pattern for ATAC
}
splice_regex = splice_patterns[signal]  # Select the regex pattern based on the input signal

tata_genes = {}  # Create a dictionary to store genes with TATA box and splice signal
current_gene = None  # Initialize the current gene name to None
current_seq = ""  # Initialize the current sequence to an empty string

# Open the file containing sequences for reading
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    for line in f:  # Read the file line by line
        line = line.strip()  # Remove leading and trailing whitespace from the line
        if line.startswith(">"):  # Check if the line is a header line
            if current_gene:  # If a gene is active
                if tata_pattern.search(current_seq) and splice_regex.search(current_seq):  # Check for TATA box and splice signal in the sequence
                    tata_matches = tata_pattern.findall(current_seq)  # Find all TATA box matches in the sequence
                    tata_genes[current_gene] = (current_seq, len(tata_matches))  # Add the gene, sequence, and TATA box count to the dictionary
            
            match = gene_pattern.search(line)  # Search for the gene name in the header line
            current_gene = match.group(1) if match else None  # Extract the gene name if found, otherwise set to None
            current_seq = ""  # Reset the current sequence
        else:  # If the line is a sequence line
            current_seq += line  # Append the line to the current sequence

output_file = f"{signal}_spliced_genes.fa"  # Define the output file name based on the splice signal
# Open the output file for writing
with open(output_file, "w") as out:
    for gene, (seq, count) in tata_genes.items():  # Iterate over the genes, sequences, and TATA box counts
        out.write(f">{gene} TATA_boxes:{count}\n{seq}\n")  # Write the gene name, TATA box count, and sequence to the file

# Print a message indicating the process is complete
print(f"Done! Found {len(tata_genes)} genes with TATA box and splice signal {signal}. Results saved to: {output_file}")
