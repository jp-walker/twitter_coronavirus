#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs="+",required=True)
parser.add_argument('--keys',nargs="+",required=True)
args = parser.parse_args()

import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            if k in args.keys:
                total[k][path[21:26]] += sum(tmp[k].values())
for k in total.keys():
    x = total[k].keys()
    y = total[k].values()
    plt.plot(x,y)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Keys")
    plt.savefig(f"plot{args.keys}.png")
