f=open('myfile.fa')

seqs={}
for line in f:
    line=line.strip()

    if line[0]=='>':
        words=line.split()
        name=words[0][1:]
        seqs[name]=''
    else:
        seqs[name]=seqs[name]+line

f.close()
print(seqs)
