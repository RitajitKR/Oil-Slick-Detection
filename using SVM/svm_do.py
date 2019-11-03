from sklearn.svm import SVC
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class SVM_for_pixels:
    def predicter(X_to_pred):
        #X_to_pred = [2,3,4,409]
        print("got",X_to_pred)
        X_coated = []
        X_coated.append(X_to_pred)
        YHat = model.predict(X_coated)
        print(YHat)

print("svm train start")
filename = 'newset1.csv'
#filename = 'pima-indians-diabetes.data.csv'
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, header=None)
array = dataframe.values
X = array[:,0:4]
Y = array[:,4]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1234)
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
YHat = model.predict(X_test)
print(YHat)
print ("accu:::",round(accuracy_score(Y_test, YHat)*100,2))
