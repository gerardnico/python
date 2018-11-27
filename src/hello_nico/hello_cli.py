#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from clint import arguments
from clint import textui
from .hello_ip import get_my_ip


def main():
    args = arguments.Args()

    with textui.indent(4, quote='>>>'):
        textui.puts(textui.colored.red('Arguments passed in: ') + str(args.all))
        textui.puts(textui.colored.red('Flags detected: ') + str(args.flags))
        textui.puts(textui.colored.red('Files detected: ') + str(args.files))
        textui.puts(textui.colored.red('NOT Files detected: ') + str(args.not_files))
        textui.puts(textui.colored.red('Grouped Arguments: ') + str(dict(args.grouped)))
        textui.puts(textui.colored.red('Your IP: ')+str(get_my_ip()))

    print()


