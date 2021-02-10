import random 
name = input ("Введите имя нового пользователя: ")
surname = input ("Введите фамилию нового пользователя: ")
#генерация пароля(тесовый вариант)
pas = ''
for x in range(10): #Количество символов (10)
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%&'))
#транслитерация имени и фамилии
def translit(trans):  
   #cловарь с заменами
   slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'KH',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA','-':'-'}        
   # Циклически заменяем все буквы в строке
   for key in slovar:
      trans = trans.replace(key, slovar[key])
   return trans
tfio = translit(name)[0]+translit(surname)
filename = tfio + ".txt"
#выбор компании и генерация файла
print ("Выберите компанию, в которую добавите пользователя \n 1 RNDS \n 2 Winwestor")
company_name = int (input())
if company_name == 1: #RNDS
    f = open(filename, "w")
        print ("Приветствую, ниже написаны персональные доступы к нашей корпоративной инфраструктуре.")
        print ("Ваша почта: ", tfio, "@rnds.pro\nВебдоступ: https://yandex.ru\nЛогин: ", tfio, "@rnds.pro Пароль: ", pas)
        print ("\nКорпоративный гугл-аккаунт для доступа к гугл-диску, календарям, видео-переговоркам:\nЛогин: ", tfio, "@rnds.pro Пароль: ", pas)
        print ("\nhttp://br.rnds.pro — Амбар, система на базе Гитлаба для работы с версионностью кода и непрерывной доставкой и интеграцией.\nЛогин: ", tfio, "@rnds.pro Пароль: ", pas)
        print ("\nhttps://zeus.rnds.pro/ - наша ЖИРА\nЛогин: ", tfio, " Пароль: ", pas,"\n\nПользователь на компьютере User Пароль: rndssdnr")
    f.closed

elif company_name == 2: #winvestor
    print ("Приветствую, ниже написаны персональные доступы к нашей корпоративной инфраструктуре.")
    print ("Ваша почта: ", tfio, "@winvestor.ru\nВебдоступ: https://yandex.ru\nЛогин: ", tfio, "@winvestor.ru Пароль: ", pas)
    print ("\nКорпоративный гугл-аккаунт для доступа к гугл-диску, календарям, видео-переговоркам:\nЛогин: ", tfio, "@rnds.pro Пароль: ", pas)
    print ("\nhttp://br.rnds.pro — Амбар, система на базе Гитлаба для работы с версионностью кода и непрерывной доставкой и интеграцией.\nЛогин: ", tfio, "winvestor.ru Пароль: ", pas)
    print ("\nhttps://jupiter.winvestor.ru - наша ЖИРА\nЛогин: ", tfio, " Пароль: ", pas,"\n\nПользователь на компьютере User Пароль: rndssdnr")

else:
    print ("Выберите 1 или 2")
    exit(0)

#Debug
#print (name, surname, company, tfio, pas)