# Spot Permission Builder

Spot Permission Builder is a Python-based CLI tool to generate required permissions for the spot.io platform on the various cloud providers. The goal of this tool is to make it easier for Solutions Architects and Support Engineers to generate the appropriate permissions for customers.

> **_NOTE:_** This tool is a work in progress and currently only supports Azure. AWS and GCP permissions generation will be added next.

## Using the tool

```bash
python3 -m venv ./venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
