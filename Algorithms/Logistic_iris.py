from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
# 加载iris数据集
iris = datasets.load_iris()

X = iris.data
y = iris.target

print('Sample num:', len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)

clf.fit(X_train, y_train)

ans = clf.predict(X_test)

# count the accyracy of result
cnt = 0
for i in range(len(y_test)):
    if ans[i] - y_test[i] < 1e-1:
        cnt+=1
    print(ans[i], '', y_test[i])
    
print('Accuracy:', (cnt*100.0 / len(y_test)), '%')
