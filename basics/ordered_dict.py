import collections

x = {">>> Tue Oct 23 22:49:46 2018": "A", ">>> Wed Oct 24 22:49:36 2018": "B", ">>> Tue Oct 23 22:49:26 2018": "C"}

od = collections.OrderedDict(sorted(x.items()))

print(od)