#!/bin/bash

echo "Ce script utilise python3.11"
git clone https://github.com/Athrax/Analyse-CGE-Francais.git
cd Analyse-CGE-Francais || exit
python3.11 -m venv .venv
source .venv/bin/activate
export PYTHONPATH=./analyse_cge:$PYTHONPATH
pip install -r requirements.txt
cd analyse_cge || exit
python main.py -nogui