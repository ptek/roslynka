from time import sleep
from temperatura import temperatura_teraz
from wilgotnosc import wilgotnosc_teraz
from alarm import powiadom
from historia import zapish

wilgotność:int = wilgotnosc_teraz()
temperatura = temperatura_teraz()

print("Temperatura: ", temperatura)
print("Wilgotność: ", wilgotność)

if wilgotność < 601:
   print("Jest mi za sucho")
   powiadom("podlej mnie!")

zapish(wilgotność, temperatura)
