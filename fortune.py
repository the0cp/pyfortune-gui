import random
import os
import sys
import codecs
import re

from optparse import OptionParser

def _random_int(start, end):
    try:
        r = random.SystemRandom()
    except:
        r = random

    return r.randint(start, end)

def _read_fortunes(fortune_file):
    with codecs.open(fortune_file, mode='r', encoding='utf-8') as f:
        contents = f.read()

    lines = [line.rstrip() for line in contents.split('\n')]

    delim = re.compile(r'^%$')

    fortunes = []
    cur = []

    def save_if_nonempty(buf):
        fortune = '\n'.join(buf)
        if fortune.strip():
            fortunes.append(fortune)

    for line in lines:
        if delim.match(line):
            save_if_nonempty(cur)
            cur = []
            continue

        cur.append(line)

    if cur:
        save_if_nonempty(cur)

    return fortunes

def get_random_fortune(fortune_file):
    fortunes = list(_read_fortunes(fortune_file))
    randomRecord = _random_int(0, len(fortunes) - 1)
    return fortunes[randomRecord]
