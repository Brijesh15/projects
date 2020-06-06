#!/bin/bash

#set -x

python3 -m pip --version &>/dev/null
if (( $? != 0 ))
then
	sudo apt-get install -y python3-pip
fi

python3 -m venv -h &>/dev/null
if (( $? != 0 ))
then
	sudo apt-get install -y python3-venv
fi

mkdir -p udm_venv
cd udm_venv
python3 -m venv udm_venv
source udm_venv/bin/activate
cd ..
python3 -m pip show djangorestframework &>/dev/null
if (( $? != 0 ))
then
	python3 -m pip install --upgrade pip
	python3 -m pip install djangorestframework PyYAML requests django-filter django django-cors-headers jsonformatter retry-requests
	make -C framwork/testAutomationTool/apiHandler/ueAuthentication/
fi
