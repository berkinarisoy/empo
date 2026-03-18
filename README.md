# EMPO

## Requirements
- Python 3.10 (3.11+ not supported due to NMMO dependencies)
- [pyenv](https://github.com/pyenv/pyenv) recommended for managing Python versions

## Setup

**Install pyenv (mac)** 

```bash
brew install pyenv
echo 'eval "$(pyenv init -)"' >> ~/.zshrc && source ~/.zshrc
```

**Install the right Python**

```bash
pyenv install 3.10.14
```

**Clone and enter the repo**

```bash
git clone https://github.com/berkinarisoy/empo
cd empo  
```

**Create venv and install**

```bash
make setup
```

**Verify setup**

```bash
make test
```