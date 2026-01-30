# ============================================
# KONFIGURATION - Dodger Game
# ============================================
# Hier kannst du alle wichtigen Einstellungen
# für das Spiel anpassen. Experimentiere mit
# den Werten und schau, wie sich das Spiel
# verändert!
# ============================================
import os

# Basisverzeichnis (Projekt-Root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------
# BILDSCHIRM-EINSTELLUNGEN
# --------------------------------------------
BILDSCHIRM_BREITE = 800   # Breite des Spielfensters in Pixeln
BILDSCHIRM_HOEHE = 600    # Höhe des Spielfensters in Pixeln
FPS = 60                   # Bilder pro Sekunde (Frames per Second)

# --------------------------------------------
# FARBEN (RGB-Werte: Rot, Grün, Blau)
# --------------------------------------------
# Jede Farbe besteht aus 3 Zahlen von 0-255
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
GELB = (255, 255, 0)
HINTERGRUND_FARBE = (30, 30, 50)  # Dunkles Blau-Grau

# --------------------------------------------
# SPIELER-EINSTELLUNGEN
# --------------------------------------------
SPIELER_GESCHWINDIGKEIT = 7  # Wie schnell sich der Spieler bewegt
SPIELER_BREITE = 48          # Breite des Spielers in Pixeln
SPIELER_HOEHE = 48           # Höhe des Spielers in Pixeln
SPIELER_START_Y = 500        # Startposition (Abstand von oben)

# --------------------------------------------
# HINDERNIS-EINSTELLUNGEN
# --------------------------------------------
HINDERNIS_GESCHWINDIGKEIT = 4    # Wie schnell Hindernisse fallen
HINDERNIS_BREITE = 40            # Breite eines Hindernisses
HINDERNIS_HOEHE = 40             # Höhe eines Hindernisses
HINDERNIS_SPAWN_RATE = 45        # Alle X Frames erscheint ein neues Hindernis
                                  # (Kleinere Zahl = mehr Hindernisse)

# --------------------------------------------
# POWER-UP-EINSTELLUNGEN
# --------------------------------------------
POWERUP_BREITE = 32              # Breite eines Power-Ups
POWERUP_HOEHE = 32               # Höhe eines Power-Ups
POWERUP_GESCHWINDIGKEIT = 2      # Wie schnell Power-Ups fallen
POWERUP_SPAWN_CHANCE = 300       # Alle X Frames Chance auf Power-Up
                                  # (Größere Zahl = seltener)

# Schild Power-Up
SCHILD_DAUER = 5                 # Wie lange das Schild aktiv ist (in Sekunden)

# Slow-Motion Power-Up
SLOW_MOTION_DAUER = 4            # Wie lange Slow-Motion aktiv ist (in Sekunden)
SLOW_MOTION_FAKTOR = 0.5         # Geschwindigkeits-Multiplikator (0.5 = halb so schnell)

# --------------------------------------------
# SCORE-EINSTELLUNGEN
# --------------------------------------------
PUNKTE_PRO_SEKUNDE = 10          # Wie viele Punkte man pro Sekunde bekommt
SCHRIFT_GROESSE = 36             # Größe der Schrift für den Score

# --------------------------------------------
# DATEIPFADE
# --------------------------------------------
# Diese Pfade zeigen auf die Grafik-Dateien
SPIELER_BILD_PFAD = os.path.join(BASE_DIR, "assets", "player", "player.png")
HINDERNIS_BILD_PFAD = os.path.join(BASE_DIR, "assets", "obstacles", "obstacle.png")
SCHILD_BILD_PFAD = os.path.join(BASE_DIR, "assets", "powerups", "shield.png")
SLOW_BILD_PFAD = os.path.join(BASE_DIR, "assets", "powerups", "slow.png")
