from copy import deepcopy

import numpy as np


def activation(_input):
    if _input > 0:
        return 1
    else:
        return 0


def compute_net_input(_w, _x, _b):
    return np.add(np.dot(_w, _x), _b)


def training_step(train_set):
    eta = 0.3
    nr_iterations = 1
    done = False
    # bias
    b = np.random.uniform(0, 1, 1)
    # weights
    w = np.random.uniform(0, 1, 784)

    while not done and nr_iterations >= 0:
        done = True
        for x, t in train_set:
            z = compute_net_input(w, x, b)
            y = activation(z)  # classify the sample
            w = w + (t - y) * x * eta  # adjust the weights
            b = b + (t - y) * eta  # adjust the bias
            if y != t:
                done = False  # not correctly classified
        nr_iterations -= 1

    return w, b


def train_perceptrons(train_set):
    p = []
    for digit in range(10):
        crt_batch = [[x, 1] if y == digit else [x, 0] for x, y in deepcopy(train_set)]
        p += [training_step(crt_batch)]

    return p


def test_step(training_set, testing_set):

    train_data, test_data = zip(training_set[0], training_set[1]), zip(testing_set[0], testing_set[1])
    # training perceptrons for digits 0-9
    perceptrons = train_perceptrons(train_data)

    # arrays for storing results 
    correct = np.zeros((10,), dtype=int)
    total = np.zeros((10,), dtype=int)

    # making deep copy to avoid losing accuracy
    for x, t in deepcopy(test_data):
        # minus infinity
        max_value = float("-inf")
        output = 0
        for digit in range(10):
            perceptron = perceptrons[digit]
            w = perceptron[0]
            b = perceptron[1]
            z = compute_net_input(w, x, b)

            # updating the max value to get the perceptron with the greatest value
            if z > max_value:
                max_value = z
                output = digit

        if output == t:
            correct[t] += 1
        total[t] += 1

    print('\nAccuracy for given data: {}\n'.format(sum(correct) / float(len(testing_set[0])) * 100))
    print('Total: {}\n'.format(total))
    print('Correct: {}\n'.format(correct))
