import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address.strip())
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum += int(count.text)
print(sum)