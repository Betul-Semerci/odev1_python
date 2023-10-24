#Girilen sayılar arasından en büyüğünü bulma./tamsayı kabul ettim
x=int(input("1. Sayıyı Giriniz: "))
y=int(input("2. Sayıyı Giriniz: "))
z=int(input("3. Sayıyı Giriniz: "))

if (x>=y and x>=z):
     buyuk=x
elif (y>=x and y>=z):
     buyuk=y  
else:
     buyuk=z
print("Girilen en büyük sayı: ",buyuk)             
