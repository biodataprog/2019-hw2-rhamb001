#!/#!/usr/bin/env python

# this is a python script template
# this next line will download the file using curl

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,sys,csv,re


# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence

#download the file
if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz") 

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
with gzip.open(gff,"rt") as ecoligff: #unzipping and opening
    gene_count = 0
    total_gene_length=0
    str1=" "
    reader = csv.reader(ecoligff,delimiter="\t") #converting to csv file 
    
    for row in reader: #count up number of genes and find total length
        str2 = str1.join(row) #covert row to string
        mylist = str2.strip().split(" ") #split string by spaces
        if len(mylist) >= 5: #ignore first lines without 5 or more list parts
            if mylist[2] == "gene": #search for gene in list 2
                gene_count = gene_count +1  #count number of genes         
                start = int(mylist[3]) # convert string to number with int()
                end   = int(mylist[4])
                genelen = end - start + 1
                total_gene_length += genelen           

    print("There are",gene_count,"genes")

with gzip.open(fasta,"rt") as ecolifa: 
    seqs = aspairs(ecolifa)
    for seq in seqs:
        seqname  = seq[0]
        seqstring= seq[1]
        #print("The length of",seqname,"is",len(seqstring))
        genome_len=len(seqstring)
total_gene_length_float = float(total_gene_length) #make integers floats for division
genome_len_float = float(genome_len)

percent_coding=((total_gene_length_float/genome_len_float)*100)

print(percent_coding,"percent of the E. coli genome is coding.")
    usr/bin/env python

# this is a python script template
# this next line will download the file using curl

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,sys,csv,re


# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence

#download the file
if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz") 

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
with gzip.open(gff,"rt") as ecoligff: #unzipping and opening
    gene_count = 0
    total_gene_length=0
    str1=" "
    reader = csv.reader(ecoligff,delimiter="\t") #converting to csv file 
    
    for row in reader: #count up number of genes and find total length
        str2 = str1.join(row) #covert row to string
        list = str2.strip().split(" ") #split string by spaces
        if len(list) >= 5: #ignore first lines without 5 or more list parts
            m = re.search('gene',list[2]) #only search for gene in list 2
            if m:
                gene_count = gene_count +1  #count number of genes         
                start = int(list[3]) # convert string to number with int()
                end   = int(list[4])
                genelen = end - start + 1
                total_gene_length += genelen
               

    print("There are",gene_count,"genes")

with gzip.open(fasta,"rt") as ecolifa: 
    seqs = aspairs(ecolifa)
    for seq in seqs:
        seqname  = seq[0]
        seqstring= seq[1]
        #print("The length of",seqname,"is",len(seqstring))
        genome_len=len(seqstring)
total_gene_length_float = float(total_gene_length) #make integers floats for division
genome_len_float = float(genome_len)

percent_coding=((total_gene_length_float/genome_len_float)*100)

print(percent_coding,"percent of the E. coli genome is coding.")
