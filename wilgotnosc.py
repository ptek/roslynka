from sensor import polaczenie

def wilgotnosc_teraz() -> int:
    return polaczenie.moisture_read()
