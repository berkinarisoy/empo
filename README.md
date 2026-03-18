# EMPO

## Requirements
- Python 3.10 (3.11+ not supported due to NMMO dependencies)
- [pyenv](https://github.com/pyenv/pyenv) recommended for managing Python versions

## Setup

# Install pyenv (mac)
brew install pyenv
echo 'eval "$(pyenv init -)"' >> ~/.zshrc && source ~/.zshrc

# Install the right Python
pyenv install 3.10.14

# Clone and enter the repo
git clone https://github.com/berkinarisoy/empo
cd empo  

# Create venv and install
make setup

# Verify
python -c "import nmmo; print('nmmo OK')"