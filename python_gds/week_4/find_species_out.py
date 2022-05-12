from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import time

start = time.perf_counter()
path = '/Users/jonathanlifferth/data/bioinformatics/SRA_user-repository/sra/SRR10451135.fastq'
# fasta_string = open(path).read()

first_seq = ''
with open(path) as f:
    for record in SeqIO.parse(f, 'fastq'):

        print(type(record))
        print(record)
        print(record.seq)
        first_seq += str(record.seq)
        break

# print(first_seq)
print(len(first_seq))

result_handle = NCBIWWW.qblast('blastn', 'nt', first_seq)
print('result_handle received')

blast_record = NCBIXML.read(result_handle)

print(len(blast_record.alignments))

E_VALUE_THRESH = 0.01

file_out = open('ncbi_blast_result.txt', 'w')

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            file_out.write('****Alignment****\n')
            print('sequence:', alignment.title)
            file_out.write('sequence:' + alignment.title + '\n')
            print('length:', alignment.length)
            file_out.write('length:' + str(alignment.length) + '\n')
            print('e value:', hsp.expect)
            file_out.write('e value:' + str(hsp.expect) + '\n')
            print(hsp.query)
            file_out.write(hsp.query + '\n')
            print(hsp.match)
            file_out.write(hsp.match + '\n')
            print(hsp.sbjct)
            file_out.write(hsp.sbjct + '\n')

file_out.close()
end = time.perf_counter()
print(f'{end - start:0.2f} seconds')
