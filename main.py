#word = list(input())
#len(word)
word = "биржевой"
w = list(enumerate(word))
print(w)

n = len(word)-1
count = 0
for letter in word[n]: #вместо n - индексы слова или срезы с конца
    if (letter == 'k'): #k - ссылка на таблицу окончаний (возм. окончания разделить на кол-во символов)
        count += 1
print(count, 'буквы «и» в данной строке')



