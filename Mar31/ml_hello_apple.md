###ML Hello World

**Supervised Learning**: Create a classifier by finding patterns in examples.

```
   1                  2                   3
Collect
Training	->	  Train			->	  Make
Data			  Classifier		  Predictions
```



**Collect Training Data**

Measurments of the training data are called 'features'. Like weight, texture, size. Each row (called 'Example') has a label. Like: Weight - 150g; Texture - Bumpy; Label - Orange.

Thus, data can be look like this:

```
# Scikit-learn uses real-valued features.
# [[grams, smooth(1)/bumpy(0)], ... ]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# 0 - apple; 1 - orange.
labels = [0, 0, 1, 1]
```



**Train Classifier**

I'll take the Decision Tree classifier. Not completely correct descriptions is that classifier is basically a box of rules. There are a lot of different types of the classifiers.

```
from sklearn import tree

# At this point it is just an empty box of rules. To train it, we
# need a learning algorithm.
clf = tree.DecisionTreeClassifier()

# In scikit these training algorithms is included. fit is find patterns
# in data.
clf = clf.fit(features, labels)
```



**Make Prediction**

Input -> Output

```
# Lets predict that an orange is the orange.
a = clf.predict([[150, 0]])
```



Source [Google Developers](https://www.youtube.com/watch?v=cKxRvEZd3Mw).