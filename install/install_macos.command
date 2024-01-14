echo "Ce script utilise python3.11"
git clone https://github.com/Athrax/Analyse-CGE-Francais.git
cd Analyse-CGE-Francais
python3.11 -m venv .venv
source .venv/bin/activate && export PYTHONPATH=./:$PYTHONPATH
python -m pip install matplotlib
python -m pip install customtkinter
python analyse_cge/main.py -nogui