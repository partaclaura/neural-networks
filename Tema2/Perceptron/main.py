import gzip
import pickle

from perceptron import test_step


def get_data():
    fd = gzip.open('mnist.pkl.gz', 'rb')
    return pickle.load(fd, encoding='latin')


if __name__ == '__main__':
    train_set, valid_set, test_set = get_data()
    test_step(train_set, test_set)

