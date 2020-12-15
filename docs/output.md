# qbic-pipelines/sradownloader: Output

This document describes the output produced by the pipeline. Most of the plots are taken from the MultiQC report, which summarises results at the end of the pipeline.

## Introduction

This document describes the output produced by the pipeline. Most of the plots are taken from the MultiQC report, which summarises results at the end of the pipeline.

The directories listed below will be created in the results directory after the pipeline has finished. All paths are relative to the top-level results directory.

## Pipeline overview

The pipeline is built using [Nextflow](https://www.nextflow.io/)
and processes data using the following steps:

* [Prefetch](#prefetch) - download of SRA data
* [Fasterq-dump](#fasterq-dump) - converts SRA files to FastQ files
* [sort_fastq_files](#sort_fastq_files) - sorts fastq files into single-end and paired-end
* [Download Metadata](#get_metadata) - downloads metadata for SRA files

## Prefetch

[Prefetch](https://github.com/ncbi/sra-tools) is a tool of the SRA-tools package. It downloads and saves a .sra file for each SRA run accession.

For further reading and documentation see the [SRA-Tools documentation](https://ncbi.github.io/sra-tools/).

<!-- > **NB:** The FastQC plots displayed in the MultiQC report shows _untrimmed_ reads. They may contain adapter sequence and potentially regions with low quality. To see how your reads look after trimming, look at the FastQC reports in the `trim_galore` directory. -->

## Fasterq-dump

[fasterqdump](https://github.com/ncbi/sra-tools) is another tool of the SRA-tools package. It converts .sra files to FastQ files in a multithreaded manner. The files are automatically split during the conversion process into forward and reverse reads according to the sequencing strategy. The FastQ files are compressed to .fastq.gz files by pigz, to reduce the file size of the output.

For further reading and documentation see the [SRA-Tools documentation](https://ncbi.github.io/sra-tools/).

## sort_fastq_files

[sort_fastq_files](https://github.com/ncbi/sra-tools) sorts the reads according to their orientation, which is either singleEnd or pairedEnd. During the conversion step to FastQ files in paired-end experiments, in some cases, unmatched reads are produced, which are sorted into a separate directory called `pairedEnd/unmatched_reads`.

**Output directory: `results/sorted_output_files`**

## get_metadata

This process downloads metadata for each SRA run accession in XML format into a separate directory called `results/metadata`.
