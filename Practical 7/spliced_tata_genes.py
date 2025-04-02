import re

tata_pattern = re.compile(r'TATA[AT]A[AT]')
gene_pattern = re.compile(r'gene:([^\s]+)')

valid_signals = {'GTAG', 'GCAG', 'ATAC'}
signal = input("Please input splice signal (GTAG / GCAG / ATAC): ").strip().upper()

if signal not in valid_signals:
    print("Error: only GTAG, GCAG, or ATAC are allowed.")
    exit()

splice_patterns = {
    'GTAG': re.compile(r'GT\S+AG'),
    'GCAG': re.compile(r'GC\S+AG'),
    'ATAC': re.compile(r'AT\S+AC')
}
splice_regex = splice_patterns[signal]

tata_genes = {}
current_gene = None
current_seq = ""

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_gene:
                if tata_pattern.search(current_seq) and splice_regex.search(current_seq):
                    tata_matches = tata_pattern.findall(current_seq)
                    tata_genes[current_gene] = (current_seq, len(tata_matches))
            
            match = gene_pattern.search(line)
            current_gene = match.group(1) if match else None
            current_seq = ""
        else:
            current_seq += line

output_file = f"{signal}_spliced_genes.fa"
with open(output_file, "w") as out:
    for gene, (seq, count) in tata_genes.items():
        out.write(f">{gene} TATA_boxes:{count}\n{seq}\n")

print(f"Done! Found {len(tata_genes)} genes with TATA box and splice signal {signal}. Results saved to: {output_file}")
