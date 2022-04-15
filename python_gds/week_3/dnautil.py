#!/usr/bin/python
"""
dnautil module contains a few useful functions for dna sequence
"""

def gc(dna):
    "this function computes the GC percentage fo a dna seq"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))/(len(dna)-nbases)
    return gcpercent

def has_stop_codon(dna,frame):
    pass
