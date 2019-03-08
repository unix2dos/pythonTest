#!/usr/bin/env python3
# -*- codeing: utf-8 -*-

'i am hello module comment'
import sys

__autuor__ = "levon"


def hello():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello, %s" % args[1])
    else:
        print("too mang arguments")


if __name__ == "__main__":
    hello()
