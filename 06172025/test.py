dict = {}
counter = 0

with open('file.txt', 'r') as file:
    for line in file:
        counter += 1
        if "WARN" in line or "ERROR" in line:
            dict[counter] = line.strip()

print(dict)