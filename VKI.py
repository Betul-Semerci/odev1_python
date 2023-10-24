#Vücut Kitle İndeksi Hesabı
#vki<18,5 => zayıf
#18,5<vki<24,9 => normal
#25<vki<29,9 => fazla kilolu
#30<vki<39,9 => 1. derece obez
#vki>40 =>  2. derece obez

boy = float(input("Lütfen boyunuzu 'metre' cinsinden giriniz."))
kilo = float(input("Lütfen kilonuzu 'kilogram' cinsinden giriniz."))

vki = round(kilo/boy**2)
print(vki)
if vki < 18.5:
    print(f"Vücut kitle indeksiniz: {vki}, zayıfsınız")
elif vki > 18.5:
    print(f"Vücut kitle indeksiniz: {vki}, normal kilodasınız")   
elif vki > 25:
    print(f"Vücut kitle indeksiniz: {vki}, fazla kilolusunuz")
elif vki > 30:
    print(f"Vücut kitle indeksiniz: {vki}, 1.derece obezsiniz")   
else:
    print(f"Vücut kitle indeksiniz: {vki}, 2.derece obezsiniz") 

