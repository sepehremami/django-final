#! /usr/bin/bash

find . -path "*/venv/*" -prune -o -path "*/migrations/*" ! -name "__init__.py" -exec rm -rf {} +
