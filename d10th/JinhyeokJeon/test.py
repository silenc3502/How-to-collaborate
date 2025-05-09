from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    shuffle=True, stratify=y)
model = RandomForestClassifier(n_estimators=200, max_depth=10)
model.fit(X_train, y_train)
pred_train = model.predict(X_train)
pred_test = model.predict(X_test)
print(f'train set : {accuracy_score(pred_train, y_train)}')
print(f'test set : {accuracy_score(pred_test, y_test)}')