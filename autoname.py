  
name = input ("Введите имя нового пользователя: ")
surname == input ("Введите фамилиюнового пользователя: ")

print ("Выберите компанию, в которую добавите пользователя \n 1 RNDS \n 2 Winwestor")
company_name = int (input())
if company_name == 1:
    company = "RNDS"
elif company_name == 2:
    company = "Winwestor"
else:
    print ("Введите компанию")



print (name, company, surname)