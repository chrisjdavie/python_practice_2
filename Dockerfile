FROM ubuntu:16.04
MAINTAINER Chris Davie

# Python stack

USER root

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y firefox


# other numerical packages

RUN apt-get install -y libblas-dev liblapack-dev
RUN apt-get install -y gfortran libatlas-dev g++ 

# pip2 packages

RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install Cython
RUN pip install numpy --upgrade
RUN pip install scipy --upgrade
RUN pip install futures --upgrade
RUN pip install psutil --upgrade

# pip3 packages

RUN apt-get install -y python3-pip

RUN pip3 install -U pip
RUN pip3 install -U numpy 
RUN pip3 install -U scipy
RUN apt-get install -y libfreetype6 libfreetype6-dev
RUN ln -s /usr/include/freetype2/ft2build.h /usr/include/
RUN apt-get install -y libpng12-0 libpng12-dev
RUN pip3 install -U matplotlib

RUN apt-get -y install sudo
RUN useradd -m chris && echo "chris:chris" | chpasswd && adduser chris sudo
RUN echo "chris ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/chris

RUN locale-gen en_US.UTF-8

RUN apt-get install -y less

# git

RUN apt-get install -y git man unzip

# iPython
RUN pip3 install -U ipython
RUN pip install -U ipython

RUN  echo "    IdentityFile /home/chris/.ssh/id_rsa" >> /etc/ssh/ssh_config

USER chris

RUN git config --global user.email "cjdavie@googlemail.com"
RUN git config --global user.name "chrisjdavie"

ENV BROWSER /usr/bin/firefox
ENV HOME /home/chris
ENV LC_ALL en_US.utf8
WORKDIR /home/chris

RUN echo "ssh-add ~/.ssh/id_rsa" >> /tmp/init
ENTRYPOINT ssh-agent /bin/bash --init-file /tmp/init
