# -*- coding: utf-8 -*-
"""
File: zantext.py
Author: Mild Z Ferdinand

This program generates random text.
"""

import random

POOL = "abcdefghijklmnopqrstuvwxyz"


def word(length=0):
    if not length or length > 26:
        length = random.randint(3, 10)
    else:
        length = abs(length)
    word = [random.choice(POOL) for i in range(length)]
    return ''.join(word)


def sentence(words=0, chars=0):
    words = abs(words)
    if not words:
        words = random.randint(3, 10)
    return " ".join([word() for i in range(words)]) + "."


def paragraph(sentences=0, words=0):
    if not sentences and not words:
        return " ".join([sentence() for i in range(5)])

