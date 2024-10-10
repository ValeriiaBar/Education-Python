import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func(x, y):
    """
    :parameter: x and y values
    :return  calculate Z(x,y) by analytic dependency of several variables
    """
    return x ** 2 - 2 * x * y + y ** 2 + 3 * x - 4 * y


def func_gradient(x, y):
    """ take Private derivatives for x and y separately, adding them to array
    :param x: some int
    :param y: some int
    :return: array of function gradient
    """
    return np.array([2 * x - 2 * y + 3, 2 * y - 2 * x - 4])


def plot_surface(ax):
    """Create the surface plot."""

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='coolwarm')


def gradient_descent(X_start, learning_rate=0.1, threshold=0.001, max_iterations=1000):
    """Perform gradient descent and visualize the optimization process. """

    X_start = np.array(X_start)
    X_next = X_start - learning_rate * func_gradient(X_start[0], X_start[1])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.set_size_inches(7, 5)

    plot_surface(ax)

    iteration = 0

    # Градиентный спуск
    while np.linalg.norm(X_start - X_next) > threshold and iteration < max_iterations:
        X_start = X_next
        X_next = X_start - learning_rate * func_gradient(X_start[0], X_start[1])

        ax.scatter(X_start[0], X_start[1], func(X_start[0], X_start[1]), color='red', s=80)

        ax.plot([X_start[0], X_next[0]],
                [X_start[1], X_next[1]],
                [func(X_start[0], X_start[1]),
                 func(X_next[0], X_next[1])], color='yellow')

        iteration += 1  # Увеличиваем счетчик итераций

    if iteration >= max_iterations:
        print("Достигнуто максимальное количество итераций.")

    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    ax.set_zlabel('Z')
    plt.show()


X_start = [3, 4]
# Вызов функции
gradient_descent(X_start)


