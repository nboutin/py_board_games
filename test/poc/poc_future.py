#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import concurrent.futures as cf


def task(v):
    return v * v


class Foo():

    def __init__(self):
        self._value = 0

    def compute(self, param):
        self._value += param
        return self._value

    def __str__(self):
        return "val:" + str(self._value)


def main():

    futures = list()

#     with cf.ThreadPoolExecutor(max_workers=4) as executor:
#         futures.append(executor.submit(task, 1))
#         futures.append(executor.submit(task, 2))
#         futures.append(executor.submit(task, 3))
#         futures.append(executor.submit(task, 4))
#
#         for f in futures:
#             print(f.result())

    foo = Foo()

    with cf.ThreadPoolExecutor(max_workers=4) as executor:
        futures.append(executor.submit(foo.compute, 1))
        futures.append(executor.submit(foo.compute, 2))
        futures.append(executor.submit(foo.compute, 3))
        futures.append(executor.submit(foo.compute, 4))

        for f in futures:
            print(f.result())

    print(foo)


if __name__ == "__main__":
    main()
