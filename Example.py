# coding=utf-8
# la linea de arriba es necesaria porque chinga tu madre

# importar de Tensor Flow
from tensorflow.examples.tutorials.mnist import input_data

# importar Tensor Flow y lo guardamos en la variable "tf"
import tensorflow as tf

# Cargar los datos en variable
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

# Un placeholder 28px * 28px (Tamaño de las imagenes) = 784
x = tf.placeholder(tf.float32, [None, 784])

# Las imagenes son en Blanco y Negro
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Inicializar el modelo

# Indicar el Algoritmo (Softmax regression)
y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ *
                                              tf.log(y), reduction_indices=[1]))

# Entrenar nuestro algoritmo
# "GradientDescentOptimizer" es un optimizador de datos, para poder aumentar la precision de
# nuestros datos, el valor "0.05" nos va a ayudar que todos los valores en nuestro
# data set sean consistentes
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)

# estamos iniciando una session interactiva de TensorFlow
session = tf.InteractiveSession()

# Inicializar variables
tf.global_variables_initializer().run()
# Cambiar el inicio de variables por esta línea de codigo si tira errorde modulo:
# tf.initialize_all_variables().run()

# Entrenamiento
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    session.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Muestra la presicion
print(session.run(accuracy, feed_dict={ x:mnist.test.images, y_:mnist.test.labels } ))