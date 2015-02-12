#!/usr/bin/python

import sys

if len(sys.argv) < 2:
  print "Usage: python pt-to-px.py (filename)"
  sys.exit()

file_name = sys.argv[1]
infile = open("./" + file_name)
outfile = open("./px-" + file_name, "w")

for line in infile.readlines():

  split = line.split()
  if len(split) < 2:
    outfile.write(line)
    continue

  if line.find("pt") == len(line) - 3 and split[0] == "font-size":
    l = line
    size_part = split[1]
    length = len(size_part)
    
    px_size = size_part[0:length-2]
    pt_size = int(round(int(px_size) / 72.0 * 96.0))

    l = l.replace(str(px_size), str(pt_size))
    l = l.replace("pt", "px")
    outfile.write(l)
  else:
    outfile.write(line)
