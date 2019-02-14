import random
 
r = "Red"
o = "Orange"
y = "Yellow"
g = "Green"
b = "Blue"
p = "Purple"
m = "Maroon"
u = "Ultramarine"
liste = [r,o,y,g,b,p,m,u]
print("Renklerin listesi: \n\n", liste)
liste2 = random.sample(liste, 4)
#print(liste2)
#Showing answer.

count = 0

while count < 10:
  bcount = 0
  count += 1  # This is the same as count = count + 1
  a2 = input("tahminizi girin: ")
  a3 = input("tahminizi girin: ")
  a4 = input("tahminizi girin: ")
  a5 = input("tahminizi girin: ")
  liste3 = [a2,a3,a4,a5]

  print(liste3)

  if a2 == liste2[0]:
    print("Siyah pul")
    bcount += 1
  elif a2 == liste2[1]:
    print("Beyaz pul")
  elif a2 == liste2[2]: 
    print("Beyaz pul")
  elif a2 == liste2[3]:
    print("Beyaz pul")
  else:
      print("Doğru yok")


  if a3 == liste2[1]:
    print("Siyah pul")
    bcount += 1
  elif a3 == liste2[0]:
    print("Beyaz pul")
  elif a3 == liste2[2]: 
    print("Beyaz pul")
  elif a3 == liste2[3]:
    print("Beyaz pul")
  else:
    print("Doğru yok")


  if a4 == liste2[2]:
    print("Siyah pul")
    bcount += 1
  elif a4 == liste2[0]:
    print("Beyaz pul")
  elif a4 == liste2[1]: 
    print("Beyaz pul")
  elif a4 == liste2[3]:
    print("Beyaz pul")
  else:
    print("Doğru yok")


  if a5 == liste2[3]:
    print("Siyah pul")
    bcount += 1
  elif a5 == liste2[0]:
    print("Beyaz pul")
  elif a5 == liste2[1]: 
    print("Beyaz pul")
  elif a5 == liste2[2]:
    print("Beyaz pul")
  else:
    print("Doğru yok")
  if bcount == 4:
    print("Tebrikler! ")
    count = 222
  else:
    if count < 10:
      print("Hit or miss i guess they never miss\n________________________________")
    else:
      print("Başaramadın.")

#Ceyhun "CengizDegilim" Gülbaş: "Nesne yükseltmesi başarıyla tamamlandı."
#Buğra "Sasu" Marsak: "Ya hek!"
#Oğuzhan "Susa" Dublezeks: "Pipimiz küçük kodumuz düşük."
