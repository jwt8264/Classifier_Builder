file = '/Users/Jason/Documents/School/DataMining/HW05b/HW_05B_DecTree_DataFiles/HW_05B_DecTree_validation_data___v200.csv'
data = []
for line in open(file):
    data.append(line.split(','))
data = data[1:]
for item in data:
    if float(item[1]) < 7.87:
        if float(item[1]) < 4.94:
            if float(item[2]) < 5.81:
                print(1)
            else:
                print(0)
        else:
            if float(item[1]) < 4.94:
                print(1)
            else:
                print(1)
    else:
        if float(item[1]) < 7.87:
            print(1)
        else:
            if float(item[1]) < 7.87:
                print(1)
            else:
                print(0)