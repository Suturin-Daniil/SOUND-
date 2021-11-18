from math import sqrt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size


temperature = 297 # Температура в трубе, которая остается постоянной в ходе эксперимента
Mair = 28.97e-3 # Молярная масса смеси азота, кислорода и аргона
Mco2 = 44.01e-3 # Молярная масса углекислого газа
Mh2o = 18.01e-3 # Молярная масса водянного пара, содержащегося в воздухе
Cpair = 1.0036 # Молярная теплоемкость смеси АКА при постоянном давлении
Cvair = 0.7166 # Молярная теплоемкость смеси АКА при постоянном объеме
Cph2o = 1.863
Cvh2o = 1.403
Cpco2 = 0.838
Cvco2 = 0.649
Xh2o = 0.0105 # Объемная доля молекул водяного пара в воздухе
Xair = 0.9892 # Объемная доля молекул газа АКА
R = 8.31

Q = np.linspace(1.05, 5.43, 101) # Создаем массив объемных долей углекислого газа

s = [] # массив для значений скорости звука при различных объемных долях углекислого газа


#             ____________________________________________________________________________________________________________________
#            /           R * temperature * (Mair * Cpair * (Xair - Q) + Mh2o * Cph2o * Xh2o + Mco2 * Cpco2 * Q)                  /
# v   =  _  /--------------------------------------------------------------------------------------------------------------------
#         \/ (Mair * Cvair * (Xair - Q) + Mh2o * Cvh2o * Xh2o + Mco2 * Cvco2 * Q) * (Mair * (Xair - Q) + Mh2o * Xh2o + Mco2 * Q)

# Формула расчета скорости звука в зависимости от объемной доли углекислого газа при фиксированной влажности и температуре


for i in range(101):
    s.append(  sqrt(  (  R * temperature * (Mair * Cpair * (Xair - Q[i] * 0.01) \ 
    + Mh2o * Cph2o * Xh2o + Mco2 * Cpco2 * Q[i] * 0.01)  ) \
    / (  (Mair * Cvair * (Xair - Q[i] * 0.01) + Mh2o * Cvh2o * Xh2o + Mco2 * Cvco2 * Q[i] * 0.01) \
    * (Mair * (Xair - Q[i] * 0.01) + Mh2o * Xh2o + Mco2 * Q[i] * 0.01) )  )  ) # Использую перенос
# сроки \


fig, ax = plt.subplots(figsize=(16,10), dpi = 400)
ax.plot(Q, s, label = 'линия интерполяции') 
ax.set_xlabel('Q, %', fontsize = 20)
ax.set_ylabel('V(Q), м/c', fontsize = 20)
ax.set_title("Зависимость скорости звука V от объемной доли Q ( в %) углекислого газа", fontsize = 20)
ax.legend(fontsize = 15)
ax.grid()

mpl.rcParams.update({'font.size': 13})

plt.scatter(1.295, 344.648, marker='8', s = 150)
plt.text(1.420, 344.648, 'Воздух в комнате: Q=1,42%, V=344,6м/c')
plt.scatter(5.113, 340.595, marker='8', s = 150)
plt.text(5.153, 340.895, 'Воздух при выдохе:')
plt.text(5.033, 340.695, 'Q=5,253%, V=340,595м/c')


plt.xlim([1, 6]) # Устанавливем пределы измерений по оси Ох
plt.ylim([340, 345.5]) # Устанавливаем пределы измерений по оси Оу
ax.minorticks_on()


ax.grid(which='major',
    color = 'k', 
    linewidth = 2)

ax.grid(which='minor', 
    color = 'k', 
    linestyle = ':')

fig.savefig("V(Q) зависимость.png") # Cохраняем получившийся график
