#palindrom:bir metnin yada sayının kendi tersi ile eşit olma durumu.
metin = input("Metni Giriniz: ")
ters=metin[::-1]
print ("Girilen metnin tersi:" , ters)

if ters == metin:
    print("Girilen metin polindromdur.")
else:
    print("Girilen metin polindrom değildir.")    


