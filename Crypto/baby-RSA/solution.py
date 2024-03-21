from Crypto.Util.number import *
def egcd(a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
      raise Exception('modular inverse does not exist')
    else:
      return x % m

p=9134603967719418115466594323010802732165458951201330627768276187753738541374186814061315850627065173937441049542764833745372289688170621880387855059317003
q=11312700351393474174541747900288487954690851230142993894220687088079962770736831118288294834507649370693813886665340646824938751845384619209017109672384199
m=198207712768240546891520019104386783134494600425743667784987140646322866438703792631130565266468191526727548170
n=p*q
e=65537
c=50535063663157665383979004238307567070317963065207158488564965926732288034270597229646646365062421187103936948602965100105371731430676766057986733078898982772288476800466874449833684608893724132294570094968994646504656343654889518263573603064622387948769545736290616073781533863314233074502451942268945147684

d = modinv(e,(p-1)*(q-1))
flag=''
flag=long_to_bytes(m)
print ('The flag is :%s' % flag.decode())