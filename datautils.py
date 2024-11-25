import numpy as np

def load_arrowhead_data():
	train = np.loadtxt("datasets/ArrowHead_TRAIN.txt")
	train_labels, *train_data = train.T

	test = np.loadtxt("datasets/ArrowHead_TEST.txt")
	test_labels, *test_data = test.T
	return np.array(train_data).T, train_labels, np.array(test_data).T, test_labels