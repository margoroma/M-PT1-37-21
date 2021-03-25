line = input("последователльность через запятую:\n")

line = line.replace(' ', '')
line = line.split(",")
print(line)

for i in range(len(line) - 1):
    for k in range(i + 1, len(line)):
        if int(line[k]) < int(line[i]):
            line[k], line[i] = line[i], line[k]
print(line)