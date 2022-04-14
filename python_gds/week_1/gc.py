#!/usr/bin/python

dna = 'acgctcgcgcggcgatatgccgtagctgacgttttaaaag'

no_c = dna.count('c')

no_g = dna.count('g')

dna_length = len(dna)

gc_percent = (no_c + no_g) * 100.0 / dna_length

print(gc_percent)
