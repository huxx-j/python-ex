s = """We encourage everyone to contribute to Python. If you still have questions
after reviewing the material
in this guide, then the Python Mentors group is available to help guide new
contributors through the process."""

sUpper = s.upper()
s2 = s.split()
set1 = set([])
for i in s2:
    if i.endswith('.'):
        i = i.split('.')
        del i[1]
        set1.add(i[0].upper())
    elif i.endswith(","):
        i = i.split(",")
        del i[1]
        set1.add(i[0].upper())
    else:
        set1.add(i.upper())
sortedList = sorted(set1)

for i in sortedList:
    print(i)

print()
print()
for i in sortedList:
    print("{0} : {1}".format(i, sUpper.count(i)))



