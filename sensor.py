import board
from adafruit_seesaw.seesaw import Seesaw

print("Podłączam się do sensora...")

i2c_bus = board.I2C() # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a microcontroller
polaczenie = Seesaw(i2c_bus, addr=0x36)
