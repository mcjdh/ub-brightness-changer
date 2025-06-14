#!/bin/bash

# Simple brightness control without sudo
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/brightness_changer.py"