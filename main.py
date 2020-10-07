name = "bacdefghijklmnopqrstuvwxyz0123456789"
key = input("Enter you text : ")
mass = len(key)
result = ""
mats = ""
for x in range(mass):
    index = 0
    for y in name:
        if key[x] == y:
            result += str(index + 1)
        index += 1
for p in range(len(result)):
    mats += "9"
lass = int(result)
# print(result)
mats = int(mats)
result = mats - lass
# print(result)
code = str(result)
codeOutput = ""
index = 0
for x in code:
    codeOutput += name[int(x)]
print(codeOutput)
