pharse = "Don't panic!"
plist = list(pharse)
print(pharse)


plist.pop(0)

for index in range(4):
    plist.pop()

plist.pop(2)

plist.insert(3,'a')

plist.pop()

plist.pop(4)

plist.insert(2," ")


new_pharse = "".join(plist)
print(plist)
print(new_pharse)


