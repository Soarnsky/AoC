#!/usr/bin/python

import sys
import re
import time

with open("input.txt", "r") as f:
    lines = f.readlines()

count = 0
events = {}
for line in lines:
    p = "^\[\d{4}-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] \w+ #?(\S+).*$"
    month = int(re.match(p, line).group(1))
    day = int(re.match(p, line).group(2))
    hour = int(re.match(p, line).group(3))
    minute = int(re.match(p, line).group(4))
    detail = re.match(p, line).group(5)
    dt = "%s/%s %s:%s" % (month, day, hour, minute)
    events[dt] = [minute, detail]

timestamps = sorted(events, key=lambda x:time.mktime(time.strptime(x, '%m/%d %H:%M')))
guards = {}
guard = ""
time_asleep = 0
min_asleep = 0
for timestamp in timestamps:
    if events[timestamp][1] == "up":
        min_asleep = events[timestamp][0] - time_asleep
        if guards.has_key(guard):
            guards[guard][0] += min_asleep
        else:
            guards[guard] = [min_asleep]
            guards[guard].append({i:0 for i in range(60)})
        for i in range(time_asleep, events[timestamp][0]):
            guards[guard][1][i] += 1
    elif events[timestamp][1] == "asleep":
        time_asleep = events[timestamp][0]
    else:
        guard = events[timestamp][1]

max_asleep = 0
sleepy_min = -1
sleepy_guard = ""
for guard in guards:
    asleep_count, asleep_min = max(zip(guards[guard][1].values(), guards[guard][1].keys()))
    if asleep_count > max_asleep:
        max_asleep = asleep_count
        sleepy_min = asleep_min
        sleepy_guard = guard

print max_asleep, sleepy_min
print sleepy_guard, int(sleepy_guard) * sleepy_min
