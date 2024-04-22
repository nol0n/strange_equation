import math as math

# поиск решения для:
# (x'')^2 = a*x + b*x^2 + c*x^3 
#
# приведенного к системе вида
#
# { (x_1)' = x_2 
# {
# { | (x_2)' =  sqrt(a*(x_1) + b*(x_1)^2 + c*(x_1)^3)
# { |
# { | (x_2)' = -sqrt(a*(x_1) + b*(x_1)^2 + c*(x_1)^3)

# __name__ чтобы метод не был виден за пределами этого файла 
def __new_value__(values: list, h: float, sign: int, a: float, b: float, c: float):
    t_1 = values[0]
    x_1 = values[1]
    x_2 = values[2]
    
    k_1_1 = x_2
    f_1 = x_1 + (h / 2) * k_1_1
    under_sqrt = a * f_1 + b * (f_1)**2 + c * (f_1)**3
    # проверка на то не отрицательное ли значение будет под корнем
    if under_sqrt < 0:
        raise Exception("попытка взятия sqrt(x), x < 0, ошибочные начальные условия")
    k_1_2 = math.sqrt(under_sqrt) * sign


    k_2_1 = x_2 + (h / 2) * k_1_2
    f_2 = x_1 + (h / 2) * k_2_1
    under_sqrt = a * f_2 + b * (f_2)**2 + c * (f_2)**3
    # проверка на то не отрицательное ли значение будет под корнем
    if under_sqrt < 0:
        raise Exception("попытка взятия sqrt(x), x < 0, ошибочные начальные условия")
    k_2_2 = math.sqrt(under_sqrt) * sign

    new_t_1 = t_1 + h
    new_x_1 = x_1 + h * k_2_1
    new_x_2 = x_2 + h * k_2_2

    return [new_t_1, new_x_1, new_x_2]

# основной метод для получаения коордиант графика
def calculate_plot(a: float, b: float, c: float, x_0: float, xd_0: float,
                   step_size: float, end_t: float):
    # если заданные условия недпоустимы, то вернется None
    if (a * x_0 + b * (x_0)**2 + c * (x_0)**3) < 0:
        return None

    # [t_0, x_1, x_2]
    # t_0 будет нужен для построения графика
    values_positive = [[0.0, x_0, xd_0]]
    values_negative = [[0.0, x_0, xd_0]]
    steps = (int)(end_t / step_size)

    for _ in range(steps):
        # добавление значения в сторону увеличения x относительно старта
        values_positive.append(__new_value__(values_positive[-1], step_size, 1, a, b, c))
        # добавление значения в сторону уменьшения x относительно старта, для этого берем отрицательный шаг
        values_positive.insert(0, __new_value__(values_positive[0], -step_size, 1, a, b, c))

        # добавление значения в сторону увеличения x относительно старта
        values_negative.append(__new_value__(values_negative[-1], step_size, -1, a, b, c))
        # добавление значения в сторону уменьшения x относительно старта, для этого берем отрицательный шаг
        values_negative.insert(0, __new_value__(values_negative[0], -step_size, -1, a, b, c))

    x_coord = [sublist[0] for sublist in values_positive]
    y_coord = [sublist[1] for sublist in values_positive]
    ret_positive = [x_coord, y_coord]

    x_coord = [sublist[0] for sublist in values_negative]
    y_coord = [sublist[1] for sublist in values_negative]
    ret_negative = [x_coord, y_coord]
    
    return ret_positive, ret_negative
