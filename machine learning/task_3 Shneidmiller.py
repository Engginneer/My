import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import make_scorer, recall_score, f1_score
from sklearn.model_selection import cross_validate
import time
import holoviews as hv
import panel as pn
import hvplot.pandas


names = ["Logistic Regression", "Naive Bayes        ",
         "Nearest Neighbors 1", "Nearest Neighbors 3", "Nearest Neighbors 5", "Nearest Neighbors 7"]
classifiers = [
    LogisticRegression(),
    GaussianNB(),
    KNeighborsClassifier(1),
    KNeighborsClassifier(3),
    KNeighborsClassifier(5),
    KNeighborsClassifier(7)
]

df = pd.read_excel('predictive_maintenance.xlsx')
df = df[df['TargetF'] > 0]

columns = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
target_names = ['Heat Dissipation Failure', 'Power Failure', 'Overstrain Failure', 'Tool Wear Failure',
                'Random Failures']

X = df.iloc[:, 0:5]
y = df.iloc[:, 6]
scaler = preprocessing.MinMaxScaler()
scaled_features = scaler.fit_transform(X)
X = pd.DataFrame(scaled_features, index=X.index, columns=X.columns)
X.describe()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=23456, stratify=y)
# функция train_test_split по умолчанию автоматически перемешивает данные
print(f"Количество строк в y_train по классам: {np.bincount(y_train)}")
print(f"Количество строк в y_test по классам: {np.bincount(y_test)}")

# iterate over classifiers

for name, clf in zip(names, classifiers):
    clf.fit(X_train.values, y_train)
    score = clf.score(X_test.values, y_test)

    clf_pred = clf.predict(X_test.values)
    clf_acc = accuracy_score(y_test, clf_pred)
    print('%s : Score= %.05f ' % (name, clf_acc))

for name, clf in zip(names, classifiers):
    clf.fit(X_train.values, y_train)
    clf_pred = clf.predict(X_test.values)
    cm = confusion_matrix(y_test, clf_pred, labels=clf.classes_)
    disp = ConfusionMatrixDisplay.from_estimator(clf, X_test.values, y_test,
                                                 display_labels=clf.classes_,
                                                 cmap=plt.cm.Blues)
    disp.ax_.set_title(name + " Confusion Matrix")

for name, clf in zip(names, classifiers):
    clf.fit(X_train.values, y_train)
    clf_pred = clf.predict(X_test.values)
    clf_acc = accuracy_score(y_test, clf_pred)
    print(name)
    print(classification_report(y_test, clf_pred, target_names=target_names, zero_division=0))

scoring = make_scorer(f1_score, zero_division=0, average='macro')
scores = dict({'fit_time': pd.DataFrame(), 'score_time': pd.DataFrame(), 'test_score': pd.DataFrame(),
               'train_score': pd.DataFrame()})
num_folds = 5
for name, clf in zip(names, classifiers):

    clf.fit(X_train.values, y_train)
    res = cross_validate(clf, X_test.values, y_test, scoring=scoring,
                         cv=num_folds, return_train_score=True)
    score = pd.DataFrame.from_dict(res)
    for key in scores.keys():
        scores[key][name] = score[key]

scores['fit_time']
scores['train_score'].mean()
scores['test_score'].mean()

df = scores['test_score']
df.hvplot.bar().opts(xrotation=90)
df.transpose().hvplot.bar().opts(xrotation=90)

df = pd.read_excel('predictive_maintenance_3.xlsx')
x_label = 'Torque [Nm]'
y_label = 'Tool wear [min]'

X = df[[x_label, y_label]]
y = df['TargetF']
target_names = ['Heat Dissipation Failure', 'Overstrain Failure', 'Tool Wear Failure']
scaler = preprocessing.MinMaxScaler()
scaled_features = scaler.fit_transform(X)
X = pd.DataFrame(scaled_features, index=X.index, columns=X.columns)
X.describe()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=23456)
print(f"Количество строк в y_train по классам: {np.bincount(y_train)}")
print(f"Количество строк в y_test по классам: {np.bincount(y_test)}")
for name, clf in zip(names, classifiers):
    clf.fit(X_train.values, y_train)
    score = clf.score(X_test.values, y_test)
    clf_pred = clf.predict(X_test.values)
    clf_acc = accuracy_score(y_test, clf_pred)
    print('%s : Score= %.05f ' % (name, clf_acc))

h = .01  # step size in the mesh

x_min, x_max = X.min()[x_label] - 0.1, X.max()[x_label] + 0.1
y_min, y_max = X.min()[y_label] - 0.1, X.max()[y_label] + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
cmap_light = ListedColormap(['blue', 'orange', 'green'])
cmap_bold = ListedColormap(['darkblue', 'darkorange', 'darkgreen'])

fig = plt.figure(figsize=(10, 20))
# Draw dataset
ax = plt.subplot(6, 2, 1)
# Plot the training points
ax.scatter(x=X_train[x_label], y=X_train[y_label], c=y_train, cmap=cmap_bold, alpha=1.0, edgecolor="black")
ax.scatter(x=X_test[x_label], y=X_test[y_label], c=y_test, cmap=cmap_light, alpha=0.6, edgecolor="black")
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_title("PM dataset")

# iterate over classifiers
i = 3
for name, clf in zip(names, classifiers):
    ax = plt.subplot(6, 2, i)
    t0 = time.time()

    clf.fit(X_train.values, y_train)
    score = clf.score(X_test.values, y_test)

    clf_pred = clf.predict(X_test.values)
    clf_acc = accuracy_score(y_test, clf_pred)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    t1 = time.time()

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cmap_light, alpha=.8)

    # Plot the training points
    ax.scatter(x=X_train[x_label], y=X_train[y_label], c=y_train, cmap=cmap_bold, alpha=1.0, edgecolor="black")
    ax.scatter(x=X_test[x_label], y=X_test[y_label], c=y_test, cmap=cmap_light, alpha=0.6, edgecolor="black")

    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_title(name)

    dt = (t1 - t0) * 1000
    ax.text(xx.max() - .1, yy.min() + .1, ('Score=%.5f, Time=%.3f ms.' % (score, dt)).lstrip('0'),
            size=12, horizontalalignment='right', color='w')
    i += 1
plt.subplots_adjust(wspace=0.2, hspace=0.3)
plt.show()
# prepare for binary classification
y = df['TargetF']
y = np.where(y == 1, 0, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.75, random_state=111, stratify=y)
from sklearn.metrics import RocCurveDisplay

# prepare plots
fig, ax_roc = plt.subplots(figsize=(7, 7))

for name, clf in zip(names, classifiers):
    clf.fit(X_train, y_train)
    RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_roc, name=name)

ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
ax_roc.grid(linestyle="--")
