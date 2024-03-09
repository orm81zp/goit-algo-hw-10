from pulp import LpProblem, LpMaximize, LpVariable, LpStatus

# модель оптимізації
model = LpProblem("Optimization", LpMaximize)

# змінні - x Лимонад, y Фруктовий сік
x = LpVariable(name="Лимонад", lowBound=0, cat="Integer")
y = LpVariable(name="Фруктовий сік", lowBound=0, cat="Integer")

# додаємо цільову функцію
model += x + y

# Додаємо обмеження
# 100 од. "Води"
model += 2 * x + y <= 100
# 50 од. "Цукру"
model += x <= 50
# 30 од. "Лимонного соку"
model += x <= 30
# 40 од. "Фруктового пюре"
model += 2 * y <= 40

model.solve()


status = LpStatus[model.status]

statuses = {
    "Not Solved": "Задача ще не була розв'язана. Це початковий статус до виклику solve().",
    "Optimal": "Задача успішно розв'язана з оптимальним рішенням.",
    "Infeasible": "Задача не має розв'язку, тобто не існує жодного набору змінних, який би задовольняв усі обмеження.",
    "Unbounded": "Задача має необмежений розв'язок, тобто цільова функція може бути покращена нескінченно.",
    "Undefined": "Статус розв'язку не визначено, часто виникає, коли в моделі є помилки.",
}

if status in statuses:
    print(statuses[status])

print("Оптимальна кількість:")
for variable in model.variables():
    print(f" - {variable.name}: {variable.varValue}")

print(f"Максимальна продуктивність: {int(model.objective.value())}")
