import pandas as pd
import numpy as np
from sklearn import svm

def generate_data():
	train_data_contents =  '''class_label,distance_from_beginning,distance_from_end,contains_digit,capitalized
							B,1,10,1,0
							M,10,1,0,1
							C,2,3,0,1
							S,23,2,0,0
							N,12,0,0,1'''

	with open('train.csv','w') as output:
		output.write(train_data_contents)

def generate_test_data():
	test_data_contents = """
						class_label,distance_from_beginning,distance_from_end,contains_digit,capitalized
						B,1,10,1,0
						M,10,1,0,1
						C,2,3,0,1
						S,23,2,0,0
						N,12,0,0,1
						"""

	with open('test.csv', 'w') as output:
	    output.write(test_data_contents)


train_dataframe = pd.read_csv('train.csv')

train_labels = train_dataframe.class_label
labels = list(set(train_labels))

train_labels = np.array([labels.index(x) for x in train_labels])
train_features = train_dataframe.iloc[:,1:]
train_features = np.array(train_features)

print "train labels:\n",train_labels
print "\ntrain_features\n",train_features

classifier = svm.SVC()
classifier.fit(train_features,train_labels)


test_dataframe = pd.read_csv('test.csv')
test_labels = test_dataframe.class_label
labels = list(set(test_labels))
test_labels = np.array([labels.index(x) for x in test_labels])

test_features = test_dataframe.iloc[:,1:]
test_features = np.array(test_features)

results = classifier.predict(test_features)

num_correct = (results == test_labels).sum()
recall = num_correct / len(test_labels)
print "model accuracy (%): ", recall * 100, "%"