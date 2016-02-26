
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD, Adadelta
import numpy as np

X_train = [[0, 1],
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1],
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1],
            [0, 0],
            [1, 0],
            [1, 1]]

X_train = np.array(X_train)
Y_train = [1, 0, 1, 0,1, 0, 1, 0,1, 0, 1, 0]
Y_train = np.array(Y_train)

X_test = [[0, 1],
            [0, 0],
            [1, 0],
            [1, 1]]
X_test = np.array(X_test)

Y_test = [1, 0, 1, 0]
Y_test = np.array(Y_test)

np.random.seed(9337)
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# "class_mode" defaults to "categorical". For correctly displaying accuracy
# in a binary classification problem, it should be set to "binary".
model.compile(loss='mean_squared_error',
              optimizer='Adadelta',
              class_mode='binary')

model.fit(X_train, Y_train, nb_epoch=5,
          show_accuracy=True, verbose=1, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, show_accuracy=True, verbose=0)
print(score)