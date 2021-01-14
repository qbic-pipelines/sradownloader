# qbic-pipelines/sradownloader: Changelog

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## v1.0.0 - 15/12/2020

- First release version of steffenlem/sradownloader, created with the [nf-core](http://nf-co.re/) template.
Updated SRA-Tools to 2.10.8, which improves stability of the downloading and unpacking process.
- Now the pipeline also features an automatic user config generation, which is required for the SRA-tools package.
- Additionally, unpaired reads which are sometimes generated when splitting paired end data, are now saved in a separte directory inside the pairedEnd output directory.

### `Added`

- [#4](https://github.com/qbic-pipelines/sradownloader/pull/4) New process for automatic metadata download by [@SusiJo](https://github.com/SusiJo)
- Added runinfo metadata download [@SusiJo](https://github.com/SusiJo)

### `Fixed`

### `Dependencies`

### `Deprecated`
