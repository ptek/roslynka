from time import sleep
from temperatura import temperatura_teraz
from wilgotnosc import wilgotnosc_teraz
from alarm import powiadom


wilgotność = wilgotnosc_teraz()

print("Temperatura: ", temperatura_teraz())
print("Wilgotność: ", wilgotność)

if wilgotność < 401:
   print("Jest mi za sucho")
   powiadom("podlej mnie!")
