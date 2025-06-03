#!/bin/bash

echo -n "Pip version: "
pip3 --version

INSTALL_DIR="./local_lib"
LOG_FILE="./install.log"

mkdir -p "$INSTALL_DIR"

# echo "Installing path.py in ./$INSTALL_DIR ..."
pip3 install --upgrade --force-reinstall \
  --target="$INSTALL_DIR" \
  git+https://github.com/jaraco/path.py.git > "$LOG_FILE" 2>&1

# echo "Installation complete. Logs written to $LOG_FILE"

PYTHONPATH="$INSTALL_DIR" python3 my_program.py
