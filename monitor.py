# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from temperatura import temperatura_teraz
from wilgotnosc import wilgotnosc_teraz
from alarm import powiadom

print("temp: " + str(temperatura_teraz()) + " moisture: " + str(wilgotnosc_teraz()))
