from matplotlib.pyplot import *

data = [10, 15, 8, 1, 3]
labels = ['Одни пятерки', '5 и 4', 'С тройками, но без долгов', 'С закрытыми задолж.', 'Отчисл.']
explode = (0.03, 0.03, 0.03, 0.03, 0.03)
axes(aspect=1)
pie(data, labels=labels, explode=explode, autopct='%1.1f%%')
show()