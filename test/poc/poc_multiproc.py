#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import multiprocessing as mp


def task(str, value,l ):
    print("task", str, value, os.getpid())
    value += 123
    name = "rename"
    l[0] = True
    l[1] += 123
    l[2] += "append"

def main():

    # Use mp.Value
    name = "1"
    value = 123
    l = [None, 456, "list"]

    p = mp.Process(target=task, args=[name, value, l])
    p.start()
    p.join()

    print('name', name)
    print('value', value)
    print('list', l)


if __name__ == "__main__":
    main()
