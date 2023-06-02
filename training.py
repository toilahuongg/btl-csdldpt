import numpy as np
import joblib

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from db import getAllCharacters, getFeaturesByCharacter
from utils import str_to_hog

character_list = getAllCharacters()

hog_features = []
labels = []
for character in character_list:
  image_feature_list = getFeaturesByCharacter(character.ID)
  for image in image_feature_list:
    labels.append(character.ID)
    hog_features.append(str_to_hog(image.Feature))

labels = np.array(labels)
hog_features = np.array(hog_features)
X_train, X_test, y_train, y_test = train_test_split(hog_features, labels, test_size=0.2, random_state=42)

model = svm.SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

joblib.dump(model, 'svm_model.pkl')
