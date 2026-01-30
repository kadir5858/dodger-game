# ============================================
# HINDERNIS-MODUL
# ============================================
# Dieses Modul verwaltet alle Hindernisse,
# die von oben nach unten fallen.
# ============================================

import pygame
import random
from config import (
    HINDERNIS_GESCHWINDIGKEIT,
    HINDERNIS_BREITE,
    HINDERNIS_HOEHE,
    HINDERNIS_SPAWN_RATE,
    BILDSCHIRM_BREITE,
    BILDSCHIRM_HOEHE,
    HINDERNIS_BILD_PFAD,
    ROT
)


def hindernis_bild_laden():
    """
    Lädt das Hindernis-Bild aus der Datei.
    
    Falls das Bild nicht gefunden wird, wird ein
    einfaches rotes Rechteck als Ersatz erstellt.
    """
    try:
        bild = pygame.image.load(HINDERNIS_BILD_PFAD)
        bild = pygame.transform.scale(bild, (HINDERNIS_BREITE, HINDERNIS_HOEHE))
        print("Hindernis-Bild erfolgreich geladen!")
        return bild
    except (pygame.error, FileNotFoundError):
        print("Hinweis: Hindernis-Bild nicht gefunden. Verwende Platzhalter.")
        bild = pygame.Surface((HINDERNIS_BREITE, HINDERNIS_HOEHE))
        bild.fill(ROT)
        return bild


def neues_hindernis_erstellen():
    """
    Erstellt ein neues Hindernis an einer zufälligen X-Position.
    
    Das Hindernis startet oberhalb des Bildschirms (y = negative Höhe)
    und fällt dann nach unten.
    
    Gibt ein Dictionary zurück mit:
    - x: Zufällige X-Position
    - y: Startposition (oberhalb des Bildschirms)
    - breite: Breite des Hindernisses
    - hoehe: Höhe des Hindernisses
    - geschwindigkeit: Wie schnell das Hindernis fällt
    """
    hindernis = {
        "x": random.randint(0, BILDSCHIRM_BREITE - HINDERNIS_BREITE),
        "y": -HINDERNIS_HOEHE,  # Startet oberhalb des Bildschirms
        "breite": HINDERNIS_BREITE,
        "hoehe": HINDERNIS_HOEHE,
        "geschwindigkeit": HINDERNIS_GESCHWINDIGKEIT
    }
    return hindernis


def hindernis_spawnen(hindernisse, frame_zaehler):
    """
    Entscheidet, ob ein neues Hindernis erscheinen soll.
    
    Parameter:
    - hindernisse: Die Liste aller aktuellen Hindernisse
    - frame_zaehler: Der aktuelle Frame (wird für das Timing verwendet)
    
    Diese Funktion soll:
    1. Prüfen, ob genug Frames vergangen sind (HINDERNIS_SPAWN_RATE)
    2. Falls ja, ein neues Hindernis erstellen
    3. Das neue Hindernis zur Liste hinzufügen
    """
    # TODO: Spawne in regelmäßigen Abständen ein neues Hindernis.
    # Tipp: Verwende den Modulo-Operator (%) um zu prüfen, ob frame_zaehler
    #       durch HINDERNIS_SPAWN_RATE teilbar ist
    # Tipp: Wenn ja, rufe neues_hindernis_erstellen() auf
    # Tipp: Füge das neue Hindernis mit append() zur Liste hinzu
    #
    # Beispiel für Modulo: if frame_zaehler % 60 == 0 prüft alle 60 Frames
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst


def hindernisse_bewegen(hindernisse, geschwindigkeits_faktor=1.0):
    """
    Bewegt alle Hindernisse nach unten.
    
    Parameter:
    - hindernisse: Liste aller Hindernisse
    - geschwindigkeits_faktor: Multiplikator für die Geschwindigkeit
                               (für Slow-Motion Power-Up)
    """
    for hindernis in hindernisse:
        # Bewege das Hindernis nach unten
        # Der geschwindigkeits_faktor kann die Bewegung verlangsamen
        hindernis["y"] += hindernis["geschwindigkeit"] * geschwindigkeits_faktor


def hindernisse_entfernen(hindernisse):
    """
    Entfernt alle Hindernisse, die den Bildschirm verlassen haben.
    
    Dies ist wichtig, damit die Liste nicht unendlich groß wird!
    
    Parameter:
    - hindernisse: Liste aller Hindernisse
    
    Gibt eine neue Liste zurück, die nur die sichtbaren Hindernisse enthält.
    """
    # Behalte nur Hindernisse, die noch auf dem Bildschirm sind
    sichtbare_hindernisse = []
    for hindernis in hindernisse:
        if hindernis["y"] < BILDSCHIRM_HOEHE:
            sichtbare_hindernisse.append(hindernis)
    return sichtbare_hindernisse


def hindernisse_zeichnen(bildschirm, hindernisse, hindernis_bild):
    """
    Zeichnet alle Hindernisse auf den Bildschirm.
    
    Parameter:
    - bildschirm: Das pygame Display
    - hindernisse: Liste aller Hindernisse
    - hindernis_bild: Das geladene Hindernis-Bild
    """
    for hindernis in hindernisse:
        bildschirm.blit(hindernis_bild, (hindernis["x"], hindernis["y"]))


def kollision_pruefen(spieler_rect, hindernisse):
    """
    Prüft, ob der Spieler mit einem Hindernis kollidiert.
    
    Parameter:
    - spieler_rect: Das pygame.Rect des Spielers
    - hindernisse: Liste aller Hindernisse
    
    Diese Funktion soll:
    1. Durch alle Hindernisse iterieren
    2. Für jedes Hindernis ein Rect erstellen
    3. Prüfen, ob das Spieler-Rect das Hindernis-Rect berührt
    4. True zurückgeben, wenn eine Kollision gefunden wurde
    5. False zurückgeben, wenn keine Kollision gefunden wurde
    
    Rückgabe: True wenn Kollision, sonst False
    """
    # TODO: Prüfen Sie, ob der Spieler mit einem Hindernis kollidiert.
    # Tipp: Verwende eine for-Schleife um durch alle Hindernisse zu gehen
    # Tipp: Erstelle für jedes Hindernis ein Rect:
    #       hindernis_rect = pygame.Rect(hindernis["x"], hindernis["y"], 
    #                                    hindernis["breite"], hindernis["hoehe"])
    # Tipp: Verwende spieler_rect.colliderect(hindernis_rect) um Kollision zu prüfen
    # Tipp: Wenn colliderect() True zurückgibt, gib True zurück
    
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst
    
    # Wenn keine Kollision gefunden wurde, gib False zurück
    return False
