from Bio.Blast import NCBIWWW
import time


start = time.perf_counter()
fasta_string = open('myseq2.fa').read()
print('opening fasta')

result_handle = NCBIWWW.qblast('blastn','nt', fasta_string)
print('result_handle received')
lap = time.perf_counter()
print(f'{lap - start:0.2f} seconds')

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

print(len(blast_record.alignments))
print(f'{lap - start:0.2f} seconds')

E_VALUE_THRESH = 0.01

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print(f'{lap - start:0.2f} seconds')
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)

