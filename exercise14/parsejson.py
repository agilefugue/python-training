import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter location: ')
uh = urllib.request.urlopen(address.strip())
data = uh.read()

info = json.loads(data.decode())

sum = 0
for item in info["comments"]:
    sum += int(item["count"])

print(sum)