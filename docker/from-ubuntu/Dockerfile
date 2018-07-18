FROM ubuntu:latest

LABEL Description="image with MCViNE installed with conda"

SHELL ["/bin/bash", "-c"]


RUN apt-get update --fix-missing && apt-get install -y locales apt-utils wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 git time make

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8  

ENV PATH /opt/conda/bin:$PATH

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -bfp /opt/conda \
    && rm ~/miniconda.sh \
    && source /opt/conda/etc/profile.d/conda.sh \
    && conda create -n mcvine python=2.7 \
    && source activate mcvine \
    && conda config --add channels conda-forge \
    && conda config --add channels mantid \
    && conda config --add channels mcvine \
    && conda install numpy \
    && conda install mcvine \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "source activate mcvine" >> ~/.bashrc

CMD [ "/bin/bash" ]

