# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

f=open("key.txt",'r')
a=f.readline()
b=int(a.rstrip())

dataset = pandas.read_csv('training.csv', sep=",", header=None)
array = dataset.values
X = array[:,0:38]
Y = array[:,38]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=1)

seed = 7
scoring = 'accuracy'
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
knn = DecisionTreeClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))

print(classification_report(Y_validation, predictions))


for k in range(b):
	f=open("ip"+str(k+1)+".txt",'w')
	sample = pandas.read_csv('o'+str(k+1)+'.csv', sep=",", header=None)
	pred=knn.predict(sample)
	for p in pred:
	    f.write(p + '\n')
	f.close()
