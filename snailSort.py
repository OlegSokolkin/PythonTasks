#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#Массив всегда квадратный. Соответственно, нам нет смысла считать его длину и высоту, достаточно только одного показателя
listResult = list()
#output 1, 3, 4, 5, 3, 3, 1, 9, 2, 8, 5, 2, 4, 6, 5, 3

def snail(array):
    listResult.clear() #Важный момент, каждый новый вызов нашего алгоритма в рамках одной программы список надо чистить
    arrayTmp = array.copy() #Чтобы не заморачиваться со счетчиками циклов мы просто будем копировать первоначальный массив
    calc(array, arrayTmp)
    return listResult
   
def calc(array, arrayTmp):
    array = arrayTmp.copy()
    k=0
    j = len(array) - 1 #Немного переменных/постоянных
    listTmp = list() #Список, в который мы будем складывать значения, которые нужно будет вставить чуть позже. Как правило, это 1 и последний символы в строках, отличных от 1 и последней
   
    if len(array) == 2:
        #Когда матрица станет совсем маленькой, стало лень писать цикл. Такие ситуации того не требуют
        listResult.append(arrayTmp[0][0])
        listResult.append(arrayTmp[0][1])
        listResult.append(arrayTmp[1][1])
        listResult.append(arrayTmp[1][0])
        return listResult

    for i in range(len(array)):
        if i == 0: #Первую строку берем без изменений
      
            for y in range(len(array[i])): #Это надо только для того, чтобы посимвольно слить 2 списка. Через '+' не сработало
                listResult.append(array[i][y]) 
            del arrayTmp[i] #Строку сразу удаляем, чтобы не путаться. 
        elif i > 0 and i < len(array[i]) -1: #Задача взять первый и последний элемент списка. Первый нужно пока сохранить, последний можно сразу добавить
            listTmp.append(array[i][k]) #То самое временное хранилище для символов, которые пригодятся нам чуть позже
            
            listResult.append(array[i][j]) #последний символ строки можно сразу положить в нашу итоговую строку
            del arrayTmp[i-1][k]
            del arrayTmp[i-1][j-1]
        elif i == len(array[i]) -1 : #Последнюю строку берем в обратном порядке, но тоже целиком
      
            for y in range(len(array[i])-1, -1, -1): #Разворачиваем строку
                listResult.append(array[i][y])
            del arrayTmp[i-1]
    for y in range(len(listTmp)-1, -1, -1): #Временную строку тоже придется развернуть, поскольку нам нужны элементы в обратной последовательности
        listResult.append(listTmp[y])
    
    if len(array) <= 2:
        return listResult
    else:
        calc(array, arrayTmp)

#Тестовые прогоны                               
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))


array = [
    [1, 3, 4, 5],
    [2, 4, 6, 3],
    [5, 3, 5, 3],
    [8, 2, 9, 1]

]
expected = [1,3,4,5,3,3,1,9,2,8,5,2,4,6,5,3]
print(snail(array))

