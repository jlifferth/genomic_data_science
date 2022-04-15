

def has_stop_codon(dna,frame=0):
    "This function chekcs if given gna sequence has in frame stop codons"
    stop_codon_found = False
    stop_codons=['tga','tag','taa']
    for i in range(frame,len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found

dna = 'aaatgagcggccggct'


print(has_stop_codon(dna,1))

