# ============================================
# SPIELER-MODUL
# ============================================
# Dieses Modul enthält alles, was mit dem
# Spieler zu tun hat: Position, Bewegung,
# und Darstellung.
# ============================================

import pygame
from config import (
    SPIELER_GESCHWINDIGKEIT,
    SPIELER_BREITE,
    SPIELER_HOEHE,
    SPIELER_START_Y,
    BILDSCHIRM_BREITE,
    SPIELER_BILD_PFAD,
    GRUEN
)


def spieler_erstellen():
    """
    Erstellt einen neuen Spieler.
    
    Gibt ein Dictionary zurück mit allen Spieler-Informationen:
    - x: Die X-Position (horizontal)
    - y: Die Y-Position (vertikal)
    - breite: Die Breite des Spielers
    - hoehe: Die Höhe des Spielers
    - geschwindigkeit: Wie schnell sich der Spieler bewegt
    - hat_schild: Ob der Spieler gerade ein Schild hat
    """
    spieler = {
        "x": BILDSCHIRM_BREITE // 2 - SPIELER_BREITE // 2,  # Startet in der Mitte
        "y": SPIELER_START_Y,
        "breite": SPIELER_BREITE,
        "hoehe": SPIELER_HOEHE,
        "geschwindigkeit": SPIELER_GESCHWINDIGKEIT,
        "hat_schild": False,
        "schild_ende": 0  # Zeitpunkt, wann das Schild endet
    }
    return spieler


def spieler_bild_laden():
    """
    Lädt das Spieler-Bild aus der Datei.
    
    Falls das Bild nicht gefunden wird, wird ein
    einfaches grünes Rechteck als Ersatz erstellt.
    """
    try:
        # Versuche das Bild zu laden
        bild = pygame.image.load(SPIELER_BILD_PFAD)
        # Skaliere das Bild auf die richtige Größe
        bild = pygame.transform.scale(bild, (SPIELER_BREITE, SPIELER_HOEHE))
        print("Spieler-Bild erfolgreich geladen!")
        return bild
    except (pygame.error, FileNotFoundError):
        # Falls das Bild nicht gefunden wird, erstelle ein Ersatz-Rechteck
        print("Hinweis: Spieler-Bild nicht gefunden. Verwende Platzhalter.")
        bild = pygame.Surface((SPIELER_BREITE, SPIELER_HOEHE))
        bild.fill(GRUEN)
        return bild


def spieler_bewegen(spieler, tasten):
    """
    Bewegt den Spieler basierend auf den gedrückten Tasten.
    
    Parameter:
    - spieler: Das Spieler-Dictionary
    - tasten: Liste der gedrückten Tasten (von pygame.key.get_pressed())
    
    Diese Funktion soll:
    1. Prüfen, ob die linke Pfeiltaste gedrückt ist
    2. Prüfen, ob die rechte Pfeiltaste gedrückt ist
    3. Den Spieler entsprechend nach links oder rechts bewegen
    4. Verhindern, dass der Spieler den Bildschirm verlässt
    """
    # TODO: Bewege den Spieler nach links, wenn die linke Pfeiltaste gedrückt wird.
    # Tipp: Verwende tasten[pygame.K_LEFT] um zu prüfen, ob die Taste gedrückt ist
    # Tipp: Verringere spieler["x"] um die Geschwindigkeit
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst
    
    # TODO: Bewege den Spieler nach rechts, wenn die rechte Pfeiltaste gedrückt wird.
    # Tipp: Verwende tasten[pygame.K_RIGHT] um zu prüfen
    # Tipp: Erhöhe spieler["x"] um die Geschwindigkeit
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst
    
    # TODO: Der Spieler muss innerhalb der Bildschirmgrenzen bleiben.
    # Tipp: Die X-Position sollte nicht kleiner als 0 sein
    # Tipp: Die X-Position sollte nicht größer als BILDSCHIRM_BREITE - spieler["breite"] sein
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst


def spieler_zeichnen(bildschirm, spieler, spieler_bild):
    """
    Zeichnet den Spieler auf den Bildschirm.
    
    Parameter:
    - bildschirm: Das pygame Display
    - spieler: Das Spieler-Dictionary
    - spieler_bild: Das geladene Spieler-Bild
    """
    # Zeichne das Spieler-Bild an der aktuellen Position
    bildschirm.blit(spieler_bild, (spieler["x"], spieler["y"]))
    
    # Falls der Spieler ein Schild hat, zeichne einen Kreis drum herum
    if spieler["hat_schild"]:
        # Berechne die Mitte des Spielers
        mitte_x = spieler["x"] + spieler["breite"] // 2
        mitte_y = spieler["y"] + spieler["hoehe"] // 2
        # Zeichne einen blauen Kreis als Schild-Effekt
        pygame.draw.circle(
            bildschirm,
            (100, 100, 255),  # Hellblau
            (mitte_x, mitte_y),
            spieler["breite"] // 2 + 10,  # Etwas größer als der Spieler
            3  # Liniendicke
        )


def spieler_rechteck_holen(spieler):
    """
    Erstellt ein pygame.Rect Objekt für den Spieler.
    
    Das Rect wird für die Kollisionserkennung benötigt.
    """
    return pygame.Rect(
        spieler["x"],
        spieler["y"],
        spieler["breite"],
        spieler["hoehe"]
    )
