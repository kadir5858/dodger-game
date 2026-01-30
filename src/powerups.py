# ============================================
# POWER-UP-MODUL
# ============================================
# Dieses Modul verwaltet alle Power-Ups im Spiel.
# Power-Ups geben dem Spieler besondere Fähigkeiten!
# ============================================

import pygame
import random
import time
from config import (
    POWERUP_BREITE,
    POWERUP_HOEHE,
    POWERUP_GESCHWINDIGKEIT,
    POWERUP_SPAWN_CHANCE,
    BILDSCHIRM_BREITE,
    BILDSCHIRM_HOEHE,
    SCHILD_BILD_PFAD,
    SLOW_BILD_PFAD,
    SCHILD_DAUER,
    SLOW_MOTION_DAUER,
    SLOW_MOTION_FAKTOR,
    BLAU,
    GELB
)


def powerup_bilder_laden():
    """
    Lädt alle Power-Up-Bilder.
    
    Gibt ein Dictionary mit den Bildern zurück.
    """
    bilder = {}
    
    # Schild Power-Up Bild laden
    try:
        bilder["shield"] = pygame.image.load(SCHILD_BILD_PFAD)
        bilder["shield"] = pygame.transform.scale(bilder["shield"], (POWERUP_BREITE, POWERUP_HOEHE))
        print("Schild-Bild erfolgreich geladen!")
    except (pygame.error, FileNotFoundError):
        print("Hinweis: Schild-Bild nicht gefunden. Verwende Platzhalter.")
        bilder["shield"] = pygame.Surface((POWERUP_BREITE, POWERUP_HOEHE))
        bilder["shield"].fill(BLAU)
    
    # Slow-Motion Power-Up Bild laden
    try:
        bilder["slow"] = pygame.image.load(SLOW_BILD_PFAD)
        bilder["slow"] = pygame.transform.scale(bilder["slow"], (POWERUP_BREITE, POWERUP_HOEHE))
        print("Slow-Motion-Bild erfolgreich geladen!")
    except (pygame.error, FileNotFoundError):
        print("Hinweis: Slow-Motion-Bild nicht gefunden. Verwende Platzhalter.")
        bilder["slow"] = pygame.Surface((POWERUP_BREITE, POWERUP_HOEHE))
        bilder["slow"].fill(GELB)
    
    return bilder


def neues_powerup_erstellen(typ):
    """
    Erstellt ein neues Power-Up.
    
    Parameter:
    - typ: Der Typ des Power-Ups ("shield" oder "slow")
    
    Gibt ein Dictionary mit den Power-Up-Informationen zurück.
    """
    powerup = {
        "x": random.randint(0, BILDSCHIRM_BREITE - POWERUP_BREITE),
        "y": -POWERUP_HOEHE,
        "breite": POWERUP_BREITE,
        "hoehe": POWERUP_HOEHE,
        "geschwindigkeit": POWERUP_GESCHWINDIGKEIT,
        "typ": typ
    }
    return powerup


def powerup_spawnen(powerups, frame_zaehler):
    """
    Entscheidet, ob ein neues Power-Up erscheinen soll.
    
    Power-Ups erscheinen seltener als Hindernisse.
    
    Parameter:
    - powerups: Die Liste aller aktuellen Power-Ups
    - frame_zaehler: Der aktuelle Frame
    """
    # Nur manchmal ein Power-Up spawnen (seltener als Hindernisse)
    if frame_zaehler % POWERUP_SPAWN_CHANCE == 0:
        # Zufällig zwischen Schild und Slow-Motion wählen
        typ = random.choice(["shield", "slow"])
        neues_powerup = neues_powerup_erstellen(typ)
        powerups.append(neues_powerup)


def powerups_bewegen(powerups):
    """
    Bewegt alle Power-Ups nach unten.
    
    Parameter:
    - powerups: Liste aller Power-Ups
    """
    for powerup in powerups:
        powerup["y"] += powerup["geschwindigkeit"]


def powerups_entfernen(powerups):
    """
    Entfernt Power-Ups, die den Bildschirm verlassen haben.
    
    Parameter:
    - powerups: Liste aller Power-Ups
    
    Gibt eine neue Liste zurück.
    """
    sichtbare_powerups = []
    for powerup in powerups:
        if powerup["y"] < BILDSCHIRM_HOEHE:
            sichtbare_powerups.append(powerup)
    return sichtbare_powerups


def powerups_zeichnen(bildschirm, powerups, powerup_bilder):
    """
    Zeichnet alle Power-Ups auf den Bildschirm.
    
    Parameter:
    - bildschirm: Das pygame Display
    - powerups: Liste aller Power-Ups
    - powerup_bilder: Dictionary mit den Power-Up-Bildern
    """
    for powerup in powerups:
        bild = powerup_bilder[powerup["typ"]]
        bildschirm.blit(bild, (powerup["x"], powerup["y"]))


def powerup_kollision_pruefen(spieler_rect, powerups):
    """
    Prüft, ob der Spieler ein Power-Up eingesammelt hat.
    
    Parameter:
    - spieler_rect: Das pygame.Rect des Spielers
    - powerups: Liste aller Power-Ups
    
    Gibt den Typ des eingesammelten Power-Ups zurück,
    oder None wenn kein Power-Up eingesammelt wurde.
    """
    for i, powerup in enumerate(powerups):
        powerup_rect = pygame.Rect(
            powerup["x"],
            powerup["y"],
            powerup["breite"],
            powerup["hoehe"]
        )
        if spieler_rect.colliderect(powerup_rect):
            # Power-Up wurde eingesammelt!
            typ = powerup["typ"]
            # Entferne das Power-Up aus der Liste
            powerups.pop(i)
            return typ
    
    return None


def schild_aktivieren(spieler):
    """
    Aktiviert das Schild Power-Up für den Spieler.
    
    Parameter:
    - spieler: Das Spieler-Dictionary
    
    Diese Funktion soll:
    1. Das Schild für den Spieler aktivieren
    2. Die Zeit speichern, wann das Schild endet
    """
    # TODO: Aktiviere die Schild-Powerup für den Spieler.
    # Tipp: Setze spieler["hat_schild"] auf True
    # Tipp: Berechne, wann das Schild endet: time.time() + SCHILD_DAUER
    # Tipp: Speichere diesen Wert in spieler["schild_ende"]
    
    print("Schild aktiviert!")  # Diese Zeile kann bleiben
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst


def schild_aktualisieren(spieler):
    """
    Prüft, ob das Schild abgelaufen ist.
    
    Parameter:
    - spieler: Das Spieler-Dictionary
    """
    if spieler["hat_schild"]:
        # Prüfe, ob die Schild-Zeit abgelaufen ist
        if time.time() > spieler["schild_ende"]:
            spieler["hat_schild"] = False
            print("Schild ist abgelaufen!")


def slow_motion_aktivieren(spiel_status):
    """
    Aktiviert das Slow-Motion Power-Up.
    
    Parameter:
    - spiel_status: Dictionary mit dem Spielstatus
    
    Diese Funktion soll:
    1. Slow-Motion aktivieren
    2. Die Zeit speichern, wann Slow-Motion endet
    """
    # TODO: Aktiviere das Slow-Motion Powerup.
    # Tipp: Setze spiel_status["slow_motion_aktiv"] auf True
    # Tipp: Berechne, wann Slow-Motion endet: time.time() + SLOW_MOTION_DAUER
    # Tipp: Speichere diesen Wert in spiel_status["slow_motion_ende"]
    
    print("Slow-Motion aktiviert!")  # Diese Zeile kann bleiben
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst


def slow_motion_aktualisieren(spiel_status):
    """
    Prüft, ob Slow-Motion abgelaufen ist und gibt den Geschwindigkeitsfaktor zurück.
    
    Parameter:
    - spiel_status: Dictionary mit dem Spielstatus
    
    Gibt den Geschwindigkeitsfaktor zurück (1.0 normal, weniger = langsamer)
    """
    if spiel_status.get("slow_motion_aktiv", False):
        # Prüfe, ob die Slow-Motion-Zeit abgelaufen ist
        if time.time() > spiel_status.get("slow_motion_ende", 0):
            spiel_status["slow_motion_aktiv"] = False
            print("Slow-Motion ist beendet!")
            return 1.0  # Normale Geschwindigkeit
        else:
            return SLOW_MOTION_FAKTOR  # Verlangsamte Geschwindigkeit
    
    return 1.0  # Normale Geschwindigkeit
