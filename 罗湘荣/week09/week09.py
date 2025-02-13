import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical

#标准化
def z_score(a):
    x_mean = np.mean(a)
    s2 = sum([(i - np.mean(a)) * (i - np.mean(a)) for i in a]) / len(a)
    return [(i - x_mean) / s2 for i in a]

l=[-10, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]
l1=[]
cs=[]
for i in l:
    c=l.count(i)
    cs.append(c)
z=z_score(l)
plt.plot(l,cs)
plt.plot(z,cs)
plt.show()

#实现简单神经网络
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#打印第三张图片
digit = test_images[2]
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy',
               metrics=['accuracy'])

#归一化
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255

#更改标记
print("before change:" ,test_labels[2])
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
print("after change: ", test_labels[2])

#训练
network.fit(train_images, train_labels, epochs=5, batch_size = 128)
#测试
test_loss, test_acc = network.evaluate(test_images, test_labels, verbose=1)
#实验效果
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
digit = test_images[1]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
test_images = test_images.reshape((10000, 28*28))
res = network.predict(test_images)

for i in range(res[1].shape[0]):
    if (res[1][i] == 1):
        print("the number for the picture is : ", i)
        break
