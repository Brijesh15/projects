#!/bin/bash

#set -x

SCRIPTPATH=$(cd "$(dirname "$0")"; pwd -P)

"$SCRIPTPATH"/install_udm_pre_req.sh

mkdir -p udm_venv
cd udm_venv
python3 -m venv udm_venv
source udm_venv/bin/activate
cd ..

python3 manage_udm.py makemigrations
python3 manage_udm.py migrate

python3 manage_udm.py runserver 127.0.0.1:9000

