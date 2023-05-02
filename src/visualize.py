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
import numpy as np
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

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# creating the dataset
keys = sorted(list(counts["_all"].keys())[:10])
values = sorted(list(counts["_all"].values())[:10])
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(keys, values, width = 0.4)

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Keys")
plt.savefig('plot.png')
plt.show()
