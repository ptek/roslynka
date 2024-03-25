import csv
import pathlib
from datetime import datetime, timezone

HIST_DIR="/projekt/historia/"
HIST_FILE=HIST_DIR+"zapisy.csv"

def zapish(wilgotnosc: int, temperatura: float):
    pathlib.Path(HIST_DIR).mkdir(parents=True, exist_ok=True)
    fieldnames = ['czas', 'wilgotnosc', 'temperatura']
    t = datetime.now(timezone.utc)
    with open(HIST_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'czas':t.isoformat(timespec='seconds'), 'wilgotnosc':wilgotnosc, 'temperatura':temperatura})
