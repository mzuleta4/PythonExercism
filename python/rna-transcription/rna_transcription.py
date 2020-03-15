def to_rna(dna_strand):
    dna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([dna[x] for x in dna_strand])

