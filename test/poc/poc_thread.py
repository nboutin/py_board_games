#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
from threading import Thread


def task(str, value,l ):
    print("task", str, value, threading.get_ident())
    value += 123
    name = "rename"
    l[0] = True
    l[1] += 123
    l[2] += "append"

def main():

    name = "1"
    value = 123
    l = [None, 456, "list"]

    t = Thread(target=task, args=[name, value, l])
    t.start()
    t.join()
    
    print('name', name)
    print('value', value)
    print('list', l)


if __name__ == "__main__":
    main()
