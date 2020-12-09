FROM nfcore/base:1.12
LABEL authors="Steffen Lemke" \
      description="Docker image containing all software requirements for the qbicpipelines/sradownloader pipeline"

# Install the conda environment
COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/qbic-pipelines-sradownloader-1.0.0/bin:$PATH

# Dump the details of the installed packages to a file for posterity
RUN conda env export --name qbic-pipelines-sradownloader-1.0.0 > qbic-pipelines-sradownloader-1.0.0.yml
