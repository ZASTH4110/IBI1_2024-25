import re

tata_pattern = re.compile(r'TATA[AT]A[AT]')
gene_pattern = re.compile(r'gene:([^\s]+)')

valid_splice_signals = ['GTAG', 'GCAG', 'ATAC']
splice_signal = input("please input splice signal (GTAG / GCAG / ATAC) :").strip().upper()

if splice_signal not in valid_splice_signals:
    print("error, you can only input GTAG、GCAG or ATAC")
    exit()

output_filename = f"{splice_signal}_spliced_genes.fa"
tata_genes = {}

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    current_gene = None
    current_seq = ""

    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_gene and splice_signal in current_seq:
                #current_gene has content and splice_signal is in current_seq
                tata_matches = tata_pattern.findall(current_seq)
                if tata_matches:
                    tata_genes[current_gene] = (current_seq, len(tata_matches))
            match = gene_pattern.search(line)
            current_gene = match.group(1) if match else None
            current_seq = ""
        else:
            current_seq += line

if current_gene and splice_signal in current_seq:
    tata_matches = tata_pattern.findall(current_seq)
    if tata_matches:
        tata_genes[current_gene] = (current_seq, len(tata_matches))

with open(output_filename, "w") as out:
    for gene, (seq, count) in tata_genes.items():
        out.write(f">{gene}\nTATA_boxes:{count}\n")
        out.write(seq + "\n")

print(f" Done! Found {len(tata_genes)} spliced genes containing TATA box and the splice signal {splice_signal}. Results written to {output_filename}")

