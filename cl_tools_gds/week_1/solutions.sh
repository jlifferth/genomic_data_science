#!/bin/bash
echo "Hello World!"

echo "#1 How many chromosomes are there in the genome?"
grep ">" apple.genome | wc -l

# or 
grep -c ">" apple.genome

echo "#2 How many genes?"
cut -f1 apple.genes | uniq | wc -l

echo "#3 How many transcript variants?"
cut -f2 apple.genes | sort -u | wc -l

echo "#4 How many genes have a single splice variant?"
cut -f1 apple.genes | uniq -c | grep " 1 " | wc -l

echo "#5 How may genes have 2 or more splice variants?"
cut -f1 apple.genes | uniq -c | grep -v " 1 " | wc -l

echo "#6 How many genes are there on the ‘+’ strand?"
grep "+" apple.genes | cut -f1 | uniq | wc -l

echo "#7 How many genes are there on the ‘-’ strand?"
grep "	-	" apple.genes | cut -f1 | uniq | wc -l

echo "#8 How many genes are there on chromosome chr1?"
grep "chr1" apple.genes | cut -f1 | uniq | wc -l

echo "#9 How many genes are there on each chromosome chr2?"
grep "chr2" apple.genes | cut -f1 | uniq | wc -l

echo "#10 How many genes are there on each chromosome chr3?"
grep "chr3" apple.genes | cut -f1 | uniq | wc -l

echo "#11 How many transcripts are there on chr1?"
grep "chr1" apple.genes | cut -f1 | wc -l

echo "#12 How many transcripts are there on chr2?"
grep "chr2" apple.genes | cut -f1 | wc -l

echo "#13 How many transcripts are there on chr3?"
grep "chr3" apple.genes | cut -f1 | wc -l

echo "#14 How many genes are in common between condition A and condition B?"
cut -f1 apple.conditionA | sort -u > genesA
cut -f1 apple.conditionB | sort -u > genesB
comm -1 -2 genesA genesB | wc -l

# or another solution to #14:
cat genesA genesB | sort | uniq -c | grep " 2 " | wc -l

echo "#15 How many genes are specific to condition A? "
comm -2 -3 genesA genesB | wc -l

echo "#16 How many genes are specific to condition B?"
comm -1 -3 genesA genesB | wc -l

echo "#17 How many genes are in common to all three conditions?"
cut -f1 apple.conditionC > genesC
comm -1 -2 genesB genesC > genesBC
comm -1 -2 genesBC genesA | wc -l

cut -f1 apple.conditionC | sort -u > genesC
cat genes{A,B,C} | sort | uniq -c | grep -c " 3 "

