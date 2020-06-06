#!/bin/bash
# install virtual environment
apt-get install -y --force-yes python3-pip
pip3 install virtualenvwrapper
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.AmantyaEnvs
#export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
. /usr/local/bin/virtualenvwrapper.sh
#. $HOME/.local/bin/virtualenvwrapper.sh
mkvirtualenv FrameworkEnvs
apt-get install python3 python-dev python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip python3-mysqldb libmysqlclient-dev 
pip3 install -r required_python3_packages.txt 
