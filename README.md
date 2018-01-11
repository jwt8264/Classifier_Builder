# Classifier Builder
This was a homework assignment for my Data Mining class. 
## Summary
The goal is to build a data classifier. Data points have 4 numerical attributes and belong to either class 1 or 0. I need to create a decision tree that will determine if a data point belongs in class 1 or 0. 

I am given a set of training data, that has a bunch of data points and the class that they belong to. The decision tree that I build will be based off of this data.
## The Trainer
It would be foolish to build the decision tree by hand, it's better to make the computer do it instead. I'll build a training program that will build the best decision tree for me. 

The training program recursively builds a decision tree. It looks for the best way to split the initial data set using [mixed entropy](https://en.wikipedia.org/wiki/Entropy_of_mixing) as a measure of bestness (a split that creates the two most homogenous subsets is best). This first split is the first if statement. The same process is recursively applied to each subset and the result is placed in each respective branch of the previous decision. 	

In this case, we already know from the assignment that 3 decisions (3 nested if-statements) are all that's needed, but this process could be done as much as needed. Generally, however, it's best to use a few decisions as possible to avoid over-training, which would hamper the decision tree on any data that is not training data. 

## The Classifier
The output of the training program is the classifier program. The classifier will read a bunch of un-classified data points and determine the class that they belong to. 

## How do I know it worked
After building the classifier with the trainer, you can use `accuracy.py` to show the success rate of the classifier on the testing and training data. 





