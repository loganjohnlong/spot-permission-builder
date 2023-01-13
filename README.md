# Spot Permission Builder

Spot Permission Builder is a Python-based CLI tool to generate required permissions for the spot.io platform on the various cloud providers. The goal of this tool is to make it easier for Solutions Architects and Support Engineers to generate the appropriate permissions for customers.

> **_NOTE:_** This tool is a work in progress and currently only supports Azure. AWS and GCP permissions generation will be added next.

## Using the tool

```
python3 main.py <options>
```

## Current Options

```
--cloud [AWS|Azure|GCP]         Cloud provider to build permissions for
                                [required]
--product [Eco|Elastigroup|Ocean]
                                Spot products that the customer wishes to
                                use. Use this flag multiple times if
                                specifying multiple products.  [required]
--readonly                      If present, ALL permissions will be set to
                                read-only.
--netapp-storage                Adds permissions for interfacing with NetApp
                                Storage.
--load-balancer                 Adds permissions for load balancers.
--dns                           Adds permissions for DNS.
--app-gateways                  Adds permissions for App Gateways. (Azure
                                only)
--application-security-groups   Adds permissions for Application Security
                                Groups. (Azure only)
--stateful                      Adds permissions for preserving state.
--subscription-id TEXT          Azure Subscription ID. Use this flag
                                multiple times to specify multiple IDs
--out PATH                      Output file for the generated JSON config
                                [required]
--help                          Show this message and exit.
```
