import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model

# 1. Load Dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize
X_train = X_train / 255.0
X_test = X_test / 255.0

# Flatten for traditional models
X_train_flat = X_train.reshape(-1, 28*28)
X_test_flat = X_test.reshape(-1, 28*28)

# -------------------------------
# 2. Logistic Regression Model
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_flat, y_train)
lr_preds = lr.predict(X_test_flat)
print("\n--- Logistic Regression ---")
print("Accuracy:", accuracy_score(y_test, lr_preds))
print(classification_report(y_test, lr_preds))

# -------------------------------
# 3. Random Forest Model
rf = RandomForestClassifier()
rf.fit(X_train_flat, y_train)
rf_preds = rf.predict(X_test_flat)
print("\n--- Random Forest ---")
print("Accuracy:", accuracy_score(y_test, rf_preds))
print(classification_report(y_test, rf_preds))

# -------------------------------
# 4. CNN Model
X_train_cnn = X_train.reshape(-1, 28, 28, 1)
X_test_cnn = X_test.reshape(-1, 28, 28, 1)

cnn_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
cnn_model.fit(X_train_cnn, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Evaluate CNN
cnn_preds = np.argmax(cnn_model.predict(X_test_cnn), axis=1)
print("\n--- CNN ---")
print("Accuracy:", accuracy_score(y_test, cnn_preds))
print(classification_report(y_test, cnn_preds))

# -------------------------------
# 5. Confusion Matrix for CNN
cm = confusion_matrix(y_test, cnn_preds)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("CNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# -------------------------------
# 6. Save CNN Model
cnn_model.save("mnist_cnn_model.h5")
print("CNN model saved as mnist_cnn_model.h5")
