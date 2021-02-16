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
      'ю':'u','я':'ya', 'А':'a','Б':'b','В':'v','Г':'g','Д':'d','Е':'e','Ё':'yo',
      'Ж':'zh','З':'z','И':'i','Й':'i','К':'k','Л':'l','М':'m','Н':'n',
      'О':'o','П':'p','Р':'r','С':'s','Т':'t','У':'u','Ф':'f','Х':'kh',
      'Ц':'c','Ч':'ch','Ш':'sh','Щ':'sch','Ъ':'','Ы':'y','Ь':'','Э':'e',
      'Ю':'u','Я':'ya','-':'-','A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j',
      'K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}        
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
    file = open(filename, "w")
    file.write("Приветствую, ниже написаны персональные доступы к нашей корпоративной инфраструктуре.")
    file.write("\nВаша почта: "+ tfio +"@rnds.pro\nВебдоступ: https://yandex.ru\nЛогин: "+ tfio +"@rnds.pro Пароль: " +pas)
    file.write("\n\nКорпоративный гугл-аккаунт для доступа к гугл-диску, календарям, видео-переговоркам:\nЛогин: "+ tfio +"@rnds.pro Пароль: " +pas)
    file.write("\n\nhttp://br.rnds.pro — Амбар, система на базе Гитлаба для работы с версионностью кода и непрерывной доставкой и интеграцией.\nЛогин: " +tfio +"@rnds.pro Пароль: " +pas)
    file.write("\n\nhttps://zeus.rnds.pro/ - наша ЖИРА\nЛогин: " +tfio +" Пароль: " +pas +"\n\nПользователь на компьютере User Пароль: rndssdnr")
    file.close()
    print("Готово! Ищите файл ", filename, "в папке со скриптом")

elif company_name == 2: #winvestor
    file = open(filename, "w")
    file.write("Приветствую, ниже написаны персональные доступы к нашей корпоративной инфраструктуре.")
    file.write("\nВаша почта: "+ tfio +"@winvestor.ru\nВебдоступ: https://yandex.ru\nЛогин: "+ tfio +"@winvestor.ru Пароль: " +pas)
    file.write("\n\nКорпоративный гугл-аккаунт для доступа к гугл-диску, календарям, видео-переговоркам:\nЛогин: "+ tfio +"@rnds.pro Пароль: " +pas)
    file.write("\n\nhttp://br.rnds.pro — Амбар, система на базе Гитлаба для работы с версионностью кода и непрерывной доставкой и интеграцией.\nЛогин: " +tfio +"@rnds.pro Пароль: " +pas)
    file.write("\n\nhttps://jupiter.winvestor.ru - наша ЖИРА\nЛогин: " +tfio +" Пароль: " +pas +"\n\nПользователь на компьютере User Пароль: rndssdnr")
    file.close()
    print("Готово! Ищите файл ", filename, "в папке со скриптом")

else:
    print ("Выберите 1 или 2")
    exit(0)