
def complement(dna):
    """Return the complementary sequence string
    """

    base_complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
    letters=list(dna)

    letters = [basecomplement[base] for base in letters]

    return ''.join(letters)


