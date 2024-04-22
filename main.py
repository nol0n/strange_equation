import themed_plot as myplt
import function as func

import numpy as np

values = []
names = []

# a - ??? / масса системы
# b - ??? / 2 * коэффициент сопротивления
# c - ??? / квадрат собственной частоты
# x_0 - стартовое положение
# xd_0 - стартовая скорость
# step_size - размер шага
# end_t - граничное значение t в обе стороны
results = func.calculate_plot(0, 1, 0, 
                              1, 1, 
                              0.05, 2)

values.append(results[0])
names.append("+sqrt()") 
values.append(results[1])
names.append("-sqrt()") 

myplt.build_graph(values, names, "t", "x", "", "", "")
