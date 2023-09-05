from matplotlib import pyplot as plt

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "А/Б тестирование", fontsize=15, weight='bold')
plt.text(0.3, 0.9, "- это метод оценки продукта или новшевств", fontsize=15)
plt.text(0.01, 0.8, "до применения этого нового.", fontsize=15)
plt.text(0.01, 0.7, "Применяется этот метод на двух группах людей из одного сегмента", fontsize=15)
plt.text(0.01, 0.6, "(интересы, рекация, поведение), количество этих людей в обоих", fontsize=15)
plt.text(0.01, 0.5, "группах надо брать +/- равными, но так же нужно учитывать ", fontsize=15)
plt.text(0.01, 0.4, "относительный риск нового. Принцип: группа А продолжает", fontsize=15)
plt.text(0.01, 0.3, "пользоваться старым, а группа Б использует новое. Оценивается", fontsize=15)
plt.text(0.01, 0.2, "выполнение определенного действия, финансовая выгода и/или", fontsize=15)
plt.text(0.01, 0.1, "заинтересованность.", fontsize=15)
plt.text(0.01, 0.01, "Может применяться в медецине, бизнесе, IT сфере и т.д.", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()