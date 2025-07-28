#!/bin/bash

# Fail if any command fails
set -e

# Process all PDFs in /app/input using main.py
python3 src/main.py
