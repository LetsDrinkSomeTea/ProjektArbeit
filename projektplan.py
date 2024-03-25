import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Definiere den neuen Startzeitpunkt und das Enddatum
start_date = datetime(2024, 4, 10)
end_date = datetime(2024, 7, 27)

# Aktualisiere die Zeiträume der Hauptphasen mit dem neuen Zeitraum
phases = [
    ("Einleitung", start_date, start_date + timedelta(days=14)),
    ("Theoretische Grundlagen", start_date + timedelta(days=14), start_date + timedelta(days=28)),
    ("Erstellung von Deep Fakes", start_date + timedelta(days=28), start_date + timedelta(days=42)),
    ("Deep Fakes in der Praxis", start_date + timedelta(days=42), start_date + timedelta(days=56)),
    ("Vertiefung in die Praxis und Experimente", start_date + timedelta(days=56), start_date + timedelta(days=84)),
    ("Fazit, Ausblick und Abschluss", start_date + timedelta(days=84), start_date + timedelta(days=108)),
    ("Überarbeitung und Korrekturlesen", start_date + timedelta(days=108), start_date + timedelta(days=113)),
]
colors = plt.cm.tab10(range(len(phases)))

fig, ax = plt.subplots(figsize=(14, 7))

# Erstelle Balken für jede Phase und füge Deadlines hinzu
for i, (phase, start, end) in enumerate(phases):
    ax.barh(phase, end - start, left=start, color=colors[i])
    ax.text(end + timedelta(days=1), i, end.strftime('%Y-%m-%d'), va='center', ha='left', fontsize=8)

# Formatierung
ax.set_xlabel("Datum")
ax.set_ylabel("Phasen")
ax.set_title("Projektplan Deepfakes und Social Engineering")
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)

# Formatierung des Datums auf der x-Achse
# Datum auf deutsch anzeigen
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
# Datum alle 7 Tage anzeigen
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
# Datum vertikal anzeigen
plt.xticks(rotation=90)
# Datum auf der x-Achse anzeigen
plt.xlim(start_date - timedelta(days=0), end_date + timedelta(days=5))


plt.tight_layout()
plt.show()
