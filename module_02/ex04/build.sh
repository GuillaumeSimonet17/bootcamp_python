#!/bin/bash

# Mise à jour de pip
pip install --upgrade pip
pip install --upgrade setuptools

python -m build

# Construction des packages au format wheel
python setup.py sdist bdist_wheel

# Construction des packages au format egg
python setup.py bdist_egg
