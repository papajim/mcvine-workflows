From centos:latest

LABEL Description="image with MCViNE installed with conda"

SHELL ["/bin/bash", "-c"]

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN yum install -y wget which bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 git \
    && yum clean all

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -bfp /opt/conda \
    && rm ~/miniconda.sh \
    && source /opt/conda/etc/profile.d/conda.sh \
    && conda create -n mcvine python=2.7 \
    && source activate mcvine \
    && conda config --add channels conda-forge \
    && conda config --add channels mcvine \
    && conda config --add channels mantid \
    && conda install numpy \
    && conda install mcvine
#    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
#    && echo "source activate mcvine" >> ~/.bashrc

ENV PATH /opt/conda/envs/mcvine/bin:$PATH
ENV CONDA_PREFIX /opt/conda/envs/mcvine
ENV CONDA_PYTHON_EXE /opt/conda/bin/python
ENV CONDA_DEFAULT_ENV mcvine

CMD [ "/bin/bash" ]

