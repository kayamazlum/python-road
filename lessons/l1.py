#input ve if else

email = input("E-mail adresiniz: ")
if email:
    print("Teşekkürler")
    password = input("Şifrenizi giriniz:")
    if password:
        print("Giriş başarılı.")
    else:
        print("Şifrenizi girmediniz.")
else:
    print("E-mail adresinizi girmediniz.")



# 'l1_errors.txt' adlı dosya oluşturur / var olan bir dosyayı açar 
#Mode="w" :  write. dosyayı write modunda açar
errors = open(file="lessons/l1_errors.txt", mode="w")
print("Ekrana bir şeyler yazıyor", end= ".",file=errors) #end = sona eklenecek ifade.

#Kullanıcı form örneği
print("1.Kullanıcı sayfaya geldi.", file=errors)
print("Email: ",email, file=errors)
print("Password",password, file=errors)
print("Email ve Password girildi.",file=errors)
print("Submit butonuna bastı", file=errors)
errors.close()


email="PythonLessons@gmail.com" #string
phone=1234567890 #integer

print("Email: ",email, type(email)) #email değişkenin türünü typhe ile alırız
print("Phone number: ", phone, type(phone))