# Jason Tu
# Training program
# Mar 23, 2017

import math
import numpy

# This program creates a classifier program based on a set of training data

# compare a string to '1'
def isTrue(str):
    return str.strip() == '1'

# determine the entryopy of a list of items
def Entropy(aList) :
    ttlSum = math.fsum( aList )
    if ttlSum == 0:
        return 0
    ttlEntropy = 0
    #
    #  Go through every element in the list and compute its contribution to the total entropy:
    #
    for idx in range(0,len(aList)) :
        thisValue = aList[idx]
        thisProb  = ( thisValue / float(ttlSum) )
        if thisProb != 0:
            ttlEntropy += - thisProb * math.log( thisProb, 2 )
    return ttlEntropy

# calculate the mixed entropy of a data set
# arr - the data set as a list
# attr - the attribute in questions
# threshold - the threshold on which to split the attribute
def MixedEntropy(arr, attr, threshold):
    target = 4
    FP = 0
    TN = 0
    TP = 0
    FN = 0
    for row in arr:
        if isTrue(row[target]) :
            # target is true:
            if float(row[attr]) > threshold :
                # attr is greater than threshold:
                TP += 1
            else :
                # attr is less than threshold:
                FP += 1
        else :
            # target is false
            if float(row[attr]) > threshold :
                # attr is greater than threshold
                FN += 1
            else :
                # attr is less than threshold
                TN += 1

    sum = TN + TP + FN + FP
    class1  = Entropy([TP, FN])
    class2 = Entropy([FP, TN])
    # return mixed entropy
    return ( (TP+FN) * class1 + (FP+TN) * class2 ) / sum

# split a bunch of data on an attribute
# arr - the data to split
# attr - the attribute we're splitting on
# threshold - the threshold we're using to split
# return - a list with two items. the first is the lower half of data points,
#          the second item is the higher half of data points
def splitData(arr, attr, threshold):
    left = []
    right = []
    for item in arr:
        if float(item[attr]) < threshold:
            left.append(item)
        else:
            right.append(item)
    return [left, right]

# determine which class is most common in a bunch of data
# arr - the data set
def mostCommonClass(arr):
    target = 4 #index of target variable
    class0 = 0
    class1 = 0
    for item in arr:
        if item[target].strip() == '0':
            class0 += 1
        else:
            class1 += 1
    if class0 > class1:
        return 0
    return 1


def buildBestClassifier(tabs, data):
    aTab = '    '
    prefix = tabs * aTab # how much to tab over
    mark = '' #'#' * tabs
    increment = 0.01 # granularity of thresholds
    bestEntropy = 1
    bestThreshold = None
    bestAttr = None
    bestLeft = []
    bestRight = []
    #  stop condition
    if tabs > 3 or len(data) < 10:
        return prefix + 'print('+str(mostCommonClass(data))+')'

    for attr in range(0,3):
        for threshold in numpy.arange(0, 10, increment):
            # determine mixed entropy of classifier
            entropy = MixedEntropy(data,attr,threshold)
            if entropy < bestEntropy:
                bestEntropy = entropy
                bestThreshold = threshold
                bestAttr = attr
                bestLeft, bestRight = splitData(data, attr, threshold)

    thisclass  = prefix+'if float(item['+str(bestAttr)+']) < '+str(bestThreshold)+':'+mark+'\n'
    thisclass += buildBestClassifier(tabs+1,bestLeft)+'\n'
    thisclass += prefix+'else:'+mark+'\n'
    thisclass += buildBestClassifier(tabs+1,bestRight)+''

    return thisclass


def buildAClassifier():
    testingFile = 'HW_05B_DecTree_DataFiles/HW_05B_DecTree_Testing___v200.csv'
    trainingFile = 'HW_05B_DecTree_DataFiles/HW_05BB_DecTree_Training__v200.csv'
    validatingFile = 'HW_05B_DecTree_DataFiles/HW_05B_DecTree_validation_data___v200.csv'

    # initialize classifier with
    # header  = 'file = \''+testingFile+'\'\n'
    header  = 'file = \''+validatingFile+'\'\n'
    header += 'data = []\n'
    header += 'for line in open(file):\n'
    header += '    data.append(line.split(\',\'))\n'
    header += 'data = data[1:]\n'
    header += 'for item in data:\n'
    classifier = open('HW_NN_Tu_Jason_Classifier.py','w')
    classifier.write(header)

    # get training data
    data = []
    for line in open(trainingFile):
        data.append(line.split(','))
    data = data[1:]

    # build classifier
    classifier.write(buildBestClassifier(1, data))
    classifier.close()

def main():
    buildAClassifier()

main()