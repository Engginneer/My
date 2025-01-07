import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import holoviews as hv
from holoviews import dim, opts
import panel as pn
import hvplot.pandas
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score,f1_score


df = pd.read_excel('predictive_maintenance.xlsx')
df = df.drop(['UDI', 'Product ID', 'Type', 'Target'], axis=1)
list_target = []
for i in df['Failure Type']:
    if i == 'Heat Dissipation Failure':
        list_target.append(1)
    elif i == 'Power Failure':
        list_target.append(2)
    elif i == 'Tool Wear Failure':
        list_target.append(3)
    else:
        list_target.append(0)
df['Target_num'] = list_target
df = df.loc[df['Target_num']>0]
df=df.drop('Failure Type', axis=1)
print(df)

colors = [ 'red', 'blue', 'green']
sns.set_palette(colors)
sns.pairplot(df, hue='Target_num', palette=sns.color_palette())
plt.show()

columns=['Air temperature [K]','Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]','Tool wear [min]']
target_names=['Heat Dissipation Failure', 'Power Failure', 'Tool Wear Failure']
X=df[columns]
y = df['Target_num']
y = y-1
y.value_counts()




scaler = preprocessing.StandardScaler()
scaled_features = scaler.fit_transform(X)
X = pd.DataFrame(scaled_features, index=X.index, columns=X.columns)
X.describe()



X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=123, stratify=y)
print(f"Количество строк в y_train по классам: {np.bincount(y_train)}")
print(f"Количество строк в y_test по классам: {np.bincount(y_test)}")



cmap_light = ListedColormap(colors)

X1_label = 'Air temperature [K]'
X2_label = 'Tool wear [min]'

plot_df_train = X_train.copy()
plot_df_train['Target_num'] = y_train

plot_df_test = X_test.copy()
plot_df_test['Target_num'] = y_test

X1 = pn.widgets.Select(name='X1', options=columns, value=X1_label)
X2 = pn.widgets.Select(name='X2', options=columns, value=X2_label)


def draw(x1, x2):
    plot_train = plot_df_train.hvplot.scatter(x1, x2, by='Target_num', marker='o', size=100, color=colors, alpha=0.25)
    plot_test = plot_df_test.hvplot.scatter(x1, x2, by='Target_num', marker='o', size=100, color=colors, alpha=1)

    plot = (plot_train * plot_test)
    plot.opts(width=600, height=500, tools=['hover'],
              title="Predictive Dataset", legend_position='top', show_grid=True)
    return (plot)


pn.Row(
    pn.pane.HoloViews(
        pn.bind(draw, X1, X2)
    ).servable(),

    pn.WidgetBox(
        pn.Column(
            "Пространство признаков",
            X1, X2
        ).servable(target='sidebar')
    ),
)


names = ["Linear Discriminant Analysis", "Random Forest", "SVM Poly"]
classifiers = [
    LinearDiscriminantAnalysis(solver="svd"),
    RandomForestClassifier(n_estimators=25, random_state = 123),
    svm.SVC(kernel='poly', C=6, gamma=0.8),
   ]

scoring = make_scorer(f1_score, zero_division=0, average='macro')
scores=dict( {'fit_time': pd.DataFrame(), 'score_time': pd.DataFrame(), 'test_score': pd.DataFrame(), 'train_score': pd.DataFrame()})
num_folds = 5
for name, clf in zip(names, classifiers):
    clf.fit(X_train.values, y_train)
    res = cross_validate(clf, X_test.values, y_test, scoring=scoring, cv=num_folds, return_train_score=True)
    score=pd.DataFrame.from_dict(res)
    for key in scores.keys():
      scores[key][name]=score[key]

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=2, store_covariance=True)
lda.fit(X, y)
X_lda = lda.transform(X)

lda_df=pd.DataFrame(X_lda, index=df.index)
lda_df['Target'] = y
sns.pairplot(lda_df,hue='Target', palette=sns.color_palette())
plt.show()

lda2 = LinearDiscriminantAnalysis(solver="svd")

lda2.fit(X, y)
X_lda2 = lda2.transform(X)

X_lda_df=pd.DataFrame(X_lda2, index=df.index)

X_train, X_test, y_train, y_test = train_test_split(X_lda_df,y,test_size=0.3,random_state=123, stratify=y)

plot_df_train=X_train.copy()
plot_df_train['Target_num']=y_train

plot_df_test=X_test.copy()
plot_df_test['Target_num']=y_test

lda2.fit(X_train, y_train)
y_pred = lda2.predict(X_test)

plot_df_pred=plot_df_test[plot_df_test['Target_num'] != y_pred]

x1, x2 = ('0' , '1')


h = .005  # step size in the mesh
# create a mesh to plot in
x_min, x_max = X_lda_df[0].min() - 0.1, X_lda_df[0].max() + 0.1
y_min, y_max = X_lda_df[1].min() - 0.1, X_lda_df[1].max() + 0.1
bounds=(x_min,y_min,x_max,y_max)
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h), indexing='xy')
Z = lda2.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
image=hv.Image(np.flipud(Z), bounds=bounds).opts(cmap=colors, alpha=0.3)
image