#!/bin/bash

bedtools intersect -wao -a A.bed -b B.bed | sort -u | wc -l

bedtools intersect -wo -a A.bed -b B.bed | cut -f1-3 | sort -u | wc -l

bedtools intersect -wo -a A.bed -b B.bed | cut -f4-6 | sort -u | wc -l
