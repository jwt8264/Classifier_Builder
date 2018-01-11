testingFile = '/Users/Jason/Documents/School/DataMining/HW05b/HW_05B_DecTree_DataFiles/HW_05B_DecTree_Testing___v200.csv'
trainingFile = '/Users/Jason/Documents/School/DataMining/HW05b/HW_05B_DecTree_DataFiles/HW_05BB_DecTree_Training__v200.csv'
# validatingFile = 'HW_05B_DecTree_DataFiles/HW_05B_DecTree_validation_data___v200.csv'

testing = []
for line in open(testingFile):
    testing.append(line.split(','))
testing = testing[1:]

training = []
for line in open(trainingFile):
    training.append(line.split(','))
training = training[1:]
#
# validation = []
# for line in open(trainingFile):
#     validation.append(line.split(','))
# validation = validation[1:]

# testingClassified = []
# for line in open(trainingFile):
#     testingClassified.append(line.split(','))
# testingClassified = testingClassified[1:]
#
# trainingClassified = []
# for line in open(trainingFile):
#     trainingClassified.append(line.split(','))
# trainingClassified = trainingClassified[1:]
#
# validationClassified = []
# for line in open(trainingFile):
#     validationClassified.append(line.split(','))
# validationClassified = validationClassified[1:]

mine = []
for line in open('/Users/Jason/Documents/School/DataMining/HW05b/testingResults.csv'):
    mine.append(line.split(','))
minetraining = []
for line in open('/Users/Jason/Documents/School/DataMining/HW05b/trainingResults.csv'):
    minetraining.append(line.split(','))

sum = 0
numRight = 0
for i in range(len(mine)):
    if testing[i][4].strip() == mine[i][0].strip():
        numRight += 1
    sum += 1
print(numRight/sum)

sum = 0
numRight = 0
for i in range(len(mine)):
    if training[i][4].strip() == minetraining[i][0].strip():
        numRight += 1
    sum += 1
print(numRight/sum)

