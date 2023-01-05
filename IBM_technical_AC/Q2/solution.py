file = open('data.txt')
record_num = 0
records = list()
allValid = True
errorCodes = []
for line in file.readlines():
    current_line = line.strip().split(" ")
    if len(current_line) == 1:
        record_num = current_line[0]
    else:
        if current_line[1] == 'false':
            allValid = False
            errorCodes.append(current_line[2])
            
if allValid:
    print('Yes')
else:
    print('No')
    for error in errorCodes:
        print(error, end=" ")
