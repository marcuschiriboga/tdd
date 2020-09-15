#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "marcus Chiriboga w/ JT"


import sys
import argparse


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument(
        "-l", '--lower', action="store_true", help='convert text to lowercase')
    parser.add_argument(
        "-t", "--title", action="store_true", help='convert text to titlecase')
    parser.add_argument(
        "text", help="text to be manipulated")
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    text = ns.text
    if ns.lower:  # or ns.l?
        text = text.lower()
    if ns.upper:
        text = text.upper()
    if ns.title:
        text = text.title()
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
