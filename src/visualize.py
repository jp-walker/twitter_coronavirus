#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

if len(items) > 10:
    cutoff = 9
else:
    cutoff = len(items)

names = [items[i][0] for i in range(cutoff)][::-1]
values = [items[i][1] for i in range(cutoff)][::-1]
plt.bar(names, values, width = 0.4)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Keys")
plt.savefig(f"plot{args.key}{args.input_path}.png")
plt.show()
