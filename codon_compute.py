#!/usr/bin/env python
import os, gzip, itertools
s_dict= {'AAA':0}
m_dict= {'AAA':0}
codon=""
scodon_number=0
mcodon_number=0

def m_codon_handle(codon):
    if codon not in m_dict.keys():
        m_dict[codon] = 1
    else:
        m_dict[codon] += 1

def s_codon_handle(codon):
    if codon not in s_dict.keys():
        s_dict[codon] = 1
    else:
        s_dict[codon] += 1


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

url1="ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2/cds/Salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2.ASM694v2.cds.all.fa.gz"
url2="ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/mycobacterium_tuberculosis_h37rv/cds/Mycobacterium_tuberculosis_h37rv.ASM19595v2.cds.all.fa.gz"
file1="Salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2.ASM694v2.cds.all.fa.gz"
file2="Mycobacterium_tuberculosis_h37rv.ASM19595v2.cds.all.fa.gz"

if not os.path.exists(file1):
    os.system("curl -O %s"%(url1))

if not os.path.exists(file2):
    os.system("curl -O %s"%(url2))

with gzip.open(file1,"rt") as sp1: 
    c = 0
    g = 0
    seqs = aspairs(sp1)
    total_len = 0
    gene_count = 0
    for seq in seqs:
        seqname  = seq[0]
        seqstring= seq[1]
        gene_count = gene_count+1 
        gen_len = len(seqstring)
        total_len = gen_len + total_len
        for n in seqstring:
            if len(codon)<2:
                codon = codon+n
            else:
                codon = codon+n
                s_codon_handle(codon)
                codon=""
            
            
            if n == 'C':
                c += 1
            elif n == 'G':
                g = g + 1
        
    
    scodon_number = total_len/3
    gc_total = g+c
    fgc = float(gc_total)
    ftl = float(total_len)        
    gc_content = (fgc/ftl)*100

    print("1. The number of predicted genes in Salmonella enterica is:",gene_count)
    print("2. The total length of the Salmonella enterica gene sequences is:",total_len)
    print("3. The GC content of the Salmonella enterica genome is:",gc_content,"%")
    print("4. The total number of codons in the Salmonella enterica genome is:",scodon_number)

with gzip.open(file2,"rt") as sp2: 
    c = 0
    g = 0
    seqs = aspairs(sp2)
    total_len = 0
    gene_count = 0
    for seq in seqs:
        seqname  = seq[0]
        seqstring= seq[1]
        gene_count = gene_count+1 
        gen_len = len(seqstring)
        total_len = gen_len + total_len
        for n in seqstring:
            if len(codon)<2:
                codon = codon+n
            else:
                codon = codon+n
                m_codon_handle(codon)
                codon=""
            
            
            if n == 'C':
                c += 1
            elif n == 'G':
                g = g + 1
    
    mcodon_number = total_len/3
    gc_total = g+c
    fgc = float(gc_total)
    ftl = float(total_len)        
    gc_content = (fgc/ftl)*100

    print("1. The number of predicted genes in Mycobacterium tuberculosis is:",gene_count)
    print("2. The total length of the M. tuberculosis gene sequences is:",total_len)
    print("3. The GC content of the M. tuberculosis genome is:",gc_content,"%")
    print("4. The total number of codons in the M. tuberculosis genome is:",mcodon_number)
    
    print()
    print("Codon               Mycobacterium                  Salmonella")
for key in m_dict:
    m= float(m_dict[key])/mcodon_number*100
    s= float(s_dict[key])/scodon_number*100
    print(key,"      ",m,"%      ",s,"%")
    
    
      
