from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from pandas import read_csv


class Gaussian_Naive_Bayes:

    def select_data(self, dataset):
        data = read_csv(dataset, header=None)
        X = data.iloc[:, 0:4]
        Y = data.iloc[:, 4]
        return X, Y

    # Splitting Data for Cross Validation aka, training and testing
    def split_data(self, X, Y):
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
        return X_train, X_test, y_train, y_test

    # Training the Gaussian Naive Bayes Classifier
    def train_classifier(self, X_train, y_train):
        gnb_clf = GaussianNB(priors=None)
        gnb_clf.fit(X_train, y_train)
        return gnb_clf

    # cross Validation and test accuracy
    def get_accuracy_score(self, gnb_clf, X_test, y_test):
        y_pred = gnb_clf.predict(X_test)
        accr_scr = accuracy_score(y_test, y_pred, normalize=True, sample_weight=None)
        print("Training completed. Accuracy reached:")
        print(accr_scr)

    def predict(self, X_to_pred, gnb_clf):
        X_coated = []
        X_coated.append(X_to_pred)
        decision = gnb_clf.predict(X_coated)
        return decision

print("Training started...")
