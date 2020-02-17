# Stress_DB
Gene Expression analysis, Drawing boxplot
- NCBI SRA에서 A.thaliana RNA-seq data를 수집하여 처리한 Treatment에 따라 발현의 차이를 boxplot으로 시각화
- sra file을 fastq-dump, kallisto를 이용하여 tpm 값으로 normalization하여 비교
- D3 를 이용하여 boxplot을 그리고 Django를 활용하여 웹으로 출력
