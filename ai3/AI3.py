import nn1
import numpy as np
import matplotlib.pyplot as plt
#     non so cosa succede qui
input_vector = np.array([2, 1.5])
learning_rate = 0.01
neural_network = nn1.NeuralNetwork(learning_rate)
neural_network.predict(input_vector)

# gli imput devono essere proporzionali ai target
input_vectors = np.array([[3, 1.5],[2, 1],[4, 1.5],[3, 4],[3.5, 0.5],[2, 0.5],[5.5, 1],[1, 1],])
targets = np.array([0, 1, 0, 1, 0, 1, 1, 0, ])

neural_network = nn1.NeuralNetwork(learning_rate)
training_error = neural_network.train(input_vectors, targets, 10000)
plt.plot(training_error)
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
plt.savefig("ai3/cumulative_error.png")