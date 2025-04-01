import re

tata_box = re.compile(r'TATA[AT]A[AT]')
gene_name = re.compile(r'gene:([^\s]+)')
tata_genes = {}
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as data:
    current_gene = None
    current_seq = ""

    for line in data:
        line = line.strip()
        if line.startswith(">"):
            if current_gene and tata_box.search(current_seq):
                tata_genes[current_gene] = current_seq
            # extract the gene name from the header line
            gene_match = gene_name.search(line)
            if gene_match:
                current_gene = gene_match.group(1)
            else:
                current_gene = None  
            current_seq = ""
        # read the sequence lines
        else:
            current_seq += line
    if current_gene and tata_box.search(current_seq):
        tata_genes[current_gene] = current_seq

# 写入筛选出的基因序列到新 FASTA 文件
with open("tata_genes.fa", "w") as out:
    for gene, seq in tata_genes.items():
        out.write(f">{gene}\n")
        for i in range(0, len(seq), 60):
            out.write(seq[i:i+60] + "\n")

print(f"✅ 完成！共筛选出 {len(tata_genes)} 条包含 TATAWAW 模式的基因，结果已写入 tata_genes.fa")
