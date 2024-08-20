import numpy as np

def initialize_parameters(input_size=9, hidden_size=100, output_size=9):
    np.random.seed(0)
    w1 = np.random.randn(input_size, hidden_size) * 0.01
    b1 = np.zeros((1, hidden_size))
    w2 = np.random.randn(hidden_size, output_size) * 0.01
    b2 = np.zeros((1, output_size))
    return w1, b1, w2, b2

def forward_propagation(x, w1, b1, w2, b2):
    z1 = np.dot(x, w1) + b1
    a1 = np.maximum(0, z1)
    z2 = np.dot(a1, w2) + b2
    a2 = softmax(z2)
    return z1, a1, z2, a2

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def compute_loss(a2, y):
    m = y.shape[0]
    log_probs = -np.log(a2[range(m), np.argmax(y, axis=1)])
    loss = np.sum(log_probs) / m
    return loss

