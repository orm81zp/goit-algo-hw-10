import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np


def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа


def monte_carlo_integration(num_points):
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, f(b), num_points)
    points_under_curve = sum(random_y <= f(random_x))
    area_ratio = points_under_curve / num_points
    total_area = (b - a) * f(b)
    integral_value = total_area * area_ratio

    return integral_value


def show_graph(points, monte_carlo_result):
    # Створення діапазону значень
    x = np.linspace(a, b, 400)
    y = f(x)

    # Генерація точок
    random_x = np.random.uniform(a, b, points)
    random_y = np.random.uniform(0, max(f(x)), points)

    # Відбір точок під кривою
    below_curve = random_y < f(random_x)

    # Графік
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x) = x^2", color="red")
    plt.scatter(
        random_x[below_curve],
        random_y[below_curve],
        color="green",
        s=1,
    )
    plt.scatter(
        random_x[~below_curve],
        random_y[~below_curve],
        color="blue",
        s=1,
    )
    plt.fill_between(x, y, color="gray", alpha=0.3, label="Площа обчислення")
    plt.title(
        f"f(x) = x^2 від {str(a)} до {str(b)} на {str(points)} точок, значення Монте-Карло: {str(monte_carlo_result)}"
    )
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


result, error = spi.quad(f, a, b)
print("Значення інтегралу функції quad:", result)
print("Значення інтегралу методом Монте-Карло на різних вибірках:")
print("{:<15} | {:<18}".format("Кількість точок", "Значення інтегралу"))
for points in [10, 100, 1000, 3000, 10000, 30000, 50000]:
    monte_carlo_result = monte_carlo_integration(points)
    print(f"{points:<15} | {monte_carlo_result:<18}")
    show_graph(points, monte_carlo_result)
