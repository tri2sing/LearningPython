import re

#line = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'
#pattern = re.compile ("([^\\s]+) - - \\[(.+)\\] \"([^\\s]+) (/[^\\s]*) HTTP/[^\\s]+\" [^\\s]+ ([0-9]+)")

line = '12345#Toy Story (1995)#Frank Peterson'
pattern = re.compile ("([0-9]+)#(.+)\(([0-9]+)\)#(.+)")

line = line.strip()
match = pattern.match (line)
print (line)
if match is not None:
    print (match.group(1))
    print (match.group(2))
    print (match.group(3))
    print (match.group(4))
