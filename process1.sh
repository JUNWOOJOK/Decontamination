wget https://raw.githubusercontent.com/JUNWOOJOK/bash_code/main/adapter
trimmomatic PE -threads 7  forward.fq reverse.fq forward_paired.fq forward_unpaired.fq reverse_paired.fq reverse_unpaired.fq adapter:TruSeq3-PE-2.fa:2:30:7 MINLEN:50 TRAILING:20 AVGQUAL:20 SLIDINGWINDOW:20:20
wait
rm adapter*
rm forward.fq reverse.fq singleton.fq
mv forward_paired.fq  f.fq
mv reverse_paired.fq  r.fq
rm forward_unpaired.fq reverse_unpaired.fq
rm single_end.fq s.fq
rm unmapped.fastq
