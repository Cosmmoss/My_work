file = open('Text.txt', 'r', encoding = 'UTF-8')  # открываем файл для чтения
content = file.read()  # метод чтения
sogl = len([i for i in content if i.lower() not in 'aeuioy '])  # создаю количество согласных в предложении
glas = len([i for i in content if i.lower() in 'aeuioy'])  # создаю количество гласных букв в предложении
result = str(glas) +  str(sogl)  # числа перевожу в строковый вид (запись только в строковом виде) и соединяю
file.close()  # закрываю для сохранения
file1 = open('write.txt', 'w+')  # открываю для записи
file1.write(result)  # записываю в файл результат
file1.close
file1 = open('write.txt', 'r', encoding = 'UTF-8')  # открываю для чтения
cont = file1.read()
print(*[i for i in cont], sep='\n')  # вывод на печать
file.close()
# Тестирую