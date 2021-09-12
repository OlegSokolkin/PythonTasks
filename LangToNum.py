#parseInt() reloaded
#Суть проста: человек пишет число на естественном языке, а мы транслируем его в цифровой вид
#Сначала попробуем разобраться с числами до 100, поскольку там больше всего затыков. Проще всего составить словарь, где ключ - число на естественном, значение - цифра
def parse_int(string):
    #Здесь мы составляем словарь, согласно которому будет работать наш алгоритм
    lang_num = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
    'eleven':11, 'twelve':12, 'thirteen': 13, 'fourteen':14, 'fifteen': 15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
    'thirty':30, 'forty': 40, 'fifty': 50, 'sixty':60, 'seventy':70, 'eighty': 80, 'ninety': 90, 'thousand':1000, 'hundred':100, 'million':1000000}

    #Теперь надо разделить число на естественном языке на части. Нас интересует количество единиц, десятков, сотен и пока тысяч - дальше все проще. 
    list_words = []
    string = string.replace('-', ' ') #уходим от проблемы forty-six
    string = string.replace(' and ', ' ') #убираем лишнее для нас and
    list_words = string.split(' ') 

    list_thousand = [] #Здесь я буду хранить все, что связано с 1000
    summ = 0 #Сюда мы запишем итоговое число
    summ_thousand = 0 #Здесь временная переменная для хранения всего, что связано с 1000
    thousand = 0 #Индекс элемента с 1000, нас волнует только он.
    

    for i in range(len(list_words)):
        if list_words[i] == 'thousand':
            thousand = i+1
            break
        list_thousand.append(list_words[i])
        
    #print(list_thousand)
    
    i=0
    while i < len(list_thousand) and thousand>0:
        if i+1 < len(list_thousand) and list_thousand[i+1] == 'hundred':
            summ_thousand += lang_num[list_thousand[i]] * 100
            i += 2
            continue
        summ_thousand += lang_num[list_words[i]]
        i += 1

    #На этом этапе все вроде как работает корректно 
    i = thousand
    while i < len(list_words):
        #print(list_words[i])
        if list_words[i] == 'million':
            summ = lang_num[list_words[i]]
            break
        if i < (len(list_words)-1) and list_words[i+1] == 'hundred':
            summ += lang_num[list_words[i]] * 100
            i += 2
        elif i < (len(list_words)-1):
            summ += lang_num[list_words[i]]
            i += 1
        else:
            summ += lang_num[list_words[i]]
            i += 1

    summ = summ_thousand*1000 + summ
    return summ




    
    

#print(parse_int('two'))
#print(parse_int('two hundred'))
#print(parse_int('one hundred two thousand seven hundred'))
#print(parse_int('forty-six'))
#print(parse_int('one hundred and one'))
#print(parse_int('twenty nine thousand six hundred seventy four'))
#print(parse_int('seven hundred sixty one thousand seven hundred sixty one'))
print(parse_int('two'))

