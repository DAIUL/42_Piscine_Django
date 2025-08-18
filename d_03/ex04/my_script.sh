#!/usr/bin/env bash

set -euo pipefail
command -v python3 >/dev/null
python3 -m venv django_venv
source django_venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirement.txt