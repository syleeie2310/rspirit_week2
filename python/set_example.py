bri = set(['brazil', 'russia', 'india'])

'india' in bri
'usa' in bri

bric = bri.copy()

bric.add('china')
bric.issuperset(bri)

print(bri)
print(bric)

bri.remove('russia')

print(bri & bric)
print(bri.intersection(bric))
