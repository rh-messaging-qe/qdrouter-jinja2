#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from Jinja2Writer import Jinja2Writer
from qpid_dispatch_internal.management.qdrouter import QdSchema

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
args = parser.parse_args()


def main():
    """Generate Jinja2 qdrouterd.conf template"""
    if args.output is not None:
        sys.stdout = open(args.output, 'w')

    Jinja2Writer(sys.stdout, QdSchema()).entity_types_extending("configurationEntity")
