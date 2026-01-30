# 🎮 Jugend hackt Python Game Workshop

Willkommen zum **Python Game Workshop**! In diesem Workshop lernst du, wie man mit Python und pygame ein einfaches 2D-Spiel programmiert.

## 🎯 Welches Spiel?

Es wird das **Dodger Game** programmiert, ein einfaches Arcade-Spiel, bei dem du:
- Einen Spieler nach **links und rechts** steuerst
- **Hindernissen ausweichst**, die von oben fallen
- Versuchst, so lange wie möglich zu überleben
- Deinen **Highscore** zu verbessern!

## 📋 Voraussetzungen

- Python 3.8 oder höher
- pip (Python Paketmanager)

## 🚀 Installation

### 1. Repository herunterladen

```bash
git clone https://github.com/kadir5858/dodger-game.git
cd dodger-game
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. Spiel starten

```bash
cd src
python main.py
```

## 🎨 Eigenes Spieler-Sprite erstellen mit Pixilart

Du kannst deinen **eigenen Charakter** designen!

### Schritt-für-Schritt Anleitung:

1. **Öffne Pixilart**: Gehe zu [https://www.pixilart.com/draw](https://www.pixilart.com/draw)

2. **Erstelle eine neue Zeichnung**:
   - Klicke auf "New Drawing"
   - Wähle die Größe **48x48 Pixel** (empfohlen)
   - Du kannst auch 32x32 oder 64x64 verwenden

3. **Designe deinen Charakter**:
   - Nutze die Zeichenwerkzeuge
   - Verwende einen **transparenten Hintergrund**

4. **Exportiere als PNG**:
   - Klicke auf "Download"
   - Wähle "PNG" als Format
   - Speichere die Datei

5. **Ersetze das Spieler-Sprite**:
   - Benenne deine Datei in `player.png` um
   - Kopiere sie in den Ordner `assets/player/`
   - **Kein Code muss geändert werden!**

## 🎮 Steuerung

| Taste | Aktion |
|-------|--------|
| ← Pfeil links | Nach links bewegen |
| → Pfeil rechts | Nach rechts bewegen |
| ESC | Spiel beenden |

## 📁 Projektstruktur

```
dodger-game/
├── README.md           # Diese Datei
├── requirements.txt    # Python-Abhängigkeiten
├── assets/
│   ├── player/
│   │   └── player.png  # Dein Spieler-Sprite
│   ├── obstacles/
│   │   └── obstacle.png # Hindernis-Grafik
│   └── powerups/
│       ├── shield.png   # Schild Power-Up
│       └── slow.png     # Slow-Motion Power-Up
└── src/
    ├── main.py         # Hauptprogramm
    ├── player.py       # Spieler-Logik
    ├── obstacles.py    # Hindernis-Logik
    ├── powerups.py     # Power-Up-Logik
    └── config.py       # Einstellungen
```

## ✏️ Workshop-Aufgaben (TODOs)

In diesem Workshop wirst du folgende Funktionen selbst programmieren:

### Pflicht-Aufgaben:
1. **Spielerbewegung** - Steuere den Spieler mit der Tastatur
2. **Hindernis-Spawn** - Lass Hindernisse von oben erscheinen
3. **Kollisionserkennung** - Erkenne, wenn der Spieler getroffen wird
4. **Score-System** - Erhöhe den Punktestand über Zeit

### Bonus-Aufgaben (Power-Ups):
5. **Shield Power-Up** - Kurzzeitige Unverwundbarkeit
6. **Slow-Motion Power-Up** - Verlangsame die Hindernisse

Suche im Code nach `# TODO:` Kommentaren!

## 🔧 Konfiguration anpassen

Öffne die Datei `src/config.py` und experimentiere mit den Werten:

```python
SPIELER_GESCHWINDIGKEIT = 5   # Wie schnell bewegt sich der Spieler?
HINDERNIS_GESCHWINDIGKEIT = 3 # Wie schnell fallen Hindernisse?
SPAWN_RATE = 60               # Wie oft erscheinen neue Hindernisse?
```

**Tipp**: Ändere die Werte und schau, wie sich das Spiel anfühlt!

## 💡 Ideen für Erweiterungen

Wenn du fertig bist, kannst du das Spiel weiter verbessern:

### 🔊 Sounds hinzufügen
```python
# Sound laden
sound = pygame.mixer.Sound("sound.wav")
# Sound abspielen
sound.play()
```

### 📈 Schwierigkeit steigern
- Erhöhe die Geschwindigkeit der Hindernisse über Zeit
- Spawne mehr Hindernisse, je länger das Spiel läuft

### 💾 Highscore speichern
```python
# Highscore in Datei speichern
with open("highscore.txt", "w") as f:
    f.write(str(score))

# Highscore laden
with open("highscore.txt", "r") as f:
    highscore = int(f.read())
```

### 🎨 Verschiedene Hindernis-Typen
- Füge verschiedene Grafiken hinzu
- Manche Hindernisse sind schneller als andere

### ❤️ Leben-System
- Der Spieler hat 3 Leben
- Bei Kollision verliert man ein Leben
- Spiel endet erst, wenn alle Leben weg sind

## 🐛 Problemlösung

### "pygame nicht gefunden"
```bash
pip install pygame
```

### "Bild nicht gefunden"
- Stelle sicher, dass du im `src/` Ordner bist, wenn du `python main.py` ausführst
- Überprüfe, ob die Bilder im `assets/` Ordner liegen

### Das Fenster schließt sich sofort
- Führe das Spiel über die Kommandozeile aus, um Fehlermeldungen zu sehen

## 📚 Nützliche Links

- [Pygame Dokumentation](https://www.pygame.org/docs/)
- [Pixilart Online Editor](https://www.pixilart.com/draw)
- [Python Tutorial (Deutsch)](https://py-tutorial-de.readthedocs.io/)

## 🤝 Lizenz

Dieses Projekt ist für Bildungszwecke gedacht und steht unter der MIT-Lizenz.

---

**Viel Spaß beim Programmieren! 🚀**

*Erstellt für Jugend hackt*
