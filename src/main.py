# ============================================
# DODGER GAME - Hauptprogramm
# ============================================
# Willkommen zum Dodger Game!
# 
# In diesem Spiel steuerst du einen Spieler,
# der fallenden Hindernissen ausweichen muss.
# Je länger du überlebst, desto höher dein Score!
#
# Suche nach "TODO:" im Code, um die Stellen
# zu finden, an denen du programmieren sollst.
# ============================================

import pygame
import sys
import time

# Importiere unsere eigenen Module
from config import (
    BILDSCHIRM_BREITE,
    BILDSCHIRM_HOEHE,
    FPS,
    HINTERGRUND_FARBE,
    WEISS,
    ROT,
    SCHRIFT_GROESSE,
    PUNKTE_PRO_SEKUNDE
)
from player import (
    spieler_erstellen,
    spieler_bild_laden,
    spieler_bewegen,
    spieler_zeichnen,
    spieler_rechteck_holen
)
from obstacles import (
    hindernis_bild_laden,
    hindernis_spawnen,
    hindernisse_bewegen,
    hindernisse_entfernen,
    hindernisse_zeichnen,
    kollision_pruefen
)
from powerups import (
    powerup_bilder_laden,
    powerup_spawnen,
    powerups_bewegen,
    powerups_entfernen,
    powerups_zeichnen,
    powerup_kollision_pruefen,
    schild_aktivieren,
    schild_aktualisieren,
    slow_motion_aktivieren,
    slow_motion_aktualisieren
)


def pygame_initialisieren():
    """
    Initialisiert pygame und erstellt das Spielfenster.
    
    Gibt das Bildschirm-Objekt und die Uhr zurück.
    """
    pygame.init()
    
    # Erstelle das Spielfenster
    bildschirm = pygame.display.set_mode((BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE))
    pygame.display.set_caption("Dodger Game - Jugend hackt")
    
    # Erstelle eine Uhr für die Framerate
    uhr = pygame.time.Clock()
    
    return bildschirm, uhr


def score_zeichnen(bildschirm, score, schrift):
    """
    Zeichnet den aktuellen Score auf den Bildschirm.
    
    Parameter:
    - bildschirm: Das pygame Display
    - score: Der aktuelle Punktestand
    - schrift: Das pygame Font-Objekt
    """
    score_text = schrift.render(f"Score: {score}", True, WEISS)
    bildschirm.blit(score_text, (10, 10))


def game_over_zeichnen(bildschirm, score, schrift):
    """
    Zeigt den Game Over Bildschirm an.
    
    Parameter:
    - bildschirm: Das pygame Display
    - score: Der finale Punktestand
    - schrift: Das pygame Font-Objekt
    """
    # Dunkler Hintergrund
    overlay = pygame.Surface((BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(180)  # Halbtransparent
    bildschirm.blit(overlay, (0, 0))
    
    # Game Over Text
    game_over_schrift = pygame.font.Font(None, 72)
    game_over_text = game_over_schrift.render("GAME OVER", True, ROT)
    text_rect = game_over_text.get_rect(center=(BILDSCHIRM_BREITE // 2, BILDSCHIRM_HOEHE // 2 - 50))
    bildschirm.blit(game_over_text, text_rect)
    
    # Finaler Score
    score_text = schrift.render(f"Dein Score: {score}", True, WEISS)
    score_rect = score_text.get_rect(center=(BILDSCHIRM_BREITE // 2, BILDSCHIRM_HOEHE // 2 + 20))
    bildschirm.blit(score_text, score_rect)
    
    # Neustart-Hinweis
    hinweis_schrift = pygame.font.Font(None, 28)
    hinweis_text = hinweis_schrift.render("Drücke LEERTASTE zum Neustarten oder ESC zum Beenden", True, WEISS)
    hinweis_rect = hinweis_text.get_rect(center=(BILDSCHIRM_BREITE // 2, BILDSCHIRM_HOEHE // 2 + 80))
    bildschirm.blit(hinweis_text, hinweis_rect)


def score_aktualisieren(letzter_score_zeit, score):
    """
    Erhöht den Score basierend auf der vergangenen Zeit.
    
    Parameter:
    - letzter_score_zeit: Zeitpunkt der letzten Score-Erhöhung
    - score: Der aktuelle Punktestand
    
    Diese Funktion soll:
    1. Prüfen, ob mindestens 1 Sekunde vergangen ist
    2. Falls ja, den Score erhöhen
    3. Die neue Zeit und den neuen Score zurückgeben
    
    Gibt ein Tuple zurück: (neue_zeit, neuer_score)
    """
    aktuelle_zeit = time.time()
    
    # TODO: Erhöhe die Punktzahl basierend auf der verstrichenen Zeit.
    # Tipp: Prüfe, ob (aktuelle_zeit - letzter_score_zeit) >= 1 ist
    # Tipp: Wenn ja, erhöhe den score um PUNKTE_PRO_SEKUNDE
    # Tipp: Setze letzter_score_zeit auf aktuelle_zeit
    # Tipp: Gib am Ende (letzter_score_zeit, score) zurück
    
    pass  # Entferne diese Zeile, wenn du deinen Code schreibst
    
    return letzter_score_zeit, score


def powerup_einsammeln(spieler, spiel_status, powerup_typ):
    """
    Verarbeitet das Einsammeln eines Power-Ups.
    
    Parameter:
    - spieler: Das Spieler-Dictionary
    - spiel_status: Dictionary mit dem Spielstatus
    - powerup_typ: Der Typ des eingesammelten Power-Ups
    """
    if powerup_typ == "shield":
        schild_aktivieren(spieler)
    elif powerup_typ == "slow":
        slow_motion_aktivieren(spiel_status)


def spiel_zuruecksetzen(spieler, hindernisse, powerups, spiel_status):
    """
    Setzt das Spiel für einen Neustart zurück.
    """
    # Spieler zurücksetzen
    neuer_spieler = spieler_erstellen()
    spieler.update(neuer_spieler)
    
    # Listen leeren
    hindernisse.clear()
    powerups.clear()
    
    # Status zurücksetzen
    spiel_status["score"] = 0
    spiel_status["game_over"] = False
    spiel_status["slow_motion_aktiv"] = False
    spiel_status["letzter_score_zeit"] = time.time()


def hauptschleife():
    """
    Die Hauptschleife des Spiels.
    
    Hier passiert alles:
    - Events werden verarbeitet (Tastatur, Fenster schließen)
    - Spiellogik wird ausgeführt
    - Alles wird auf den Bildschirm gezeichnet
    """
    # Initialisiere pygame
    bildschirm, uhr = pygame_initialisieren()
    
    # Lade alle Bilder
    spieler_bild = spieler_bild_laden()
    hindernis_bild = hindernis_bild_laden()
    powerup_bilder = powerup_bilder_laden()
    
    # Erstelle die Schriftart für den Score
    schrift = pygame.font.Font(None, SCHRIFT_GROESSE)
    
    # Erstelle den Spieler
    spieler = spieler_erstellen()
    
    # Liste für alle Hindernisse
    hindernisse = []
    
    # Liste für alle Power-Ups
    powerups = []
    
    # Spielstatus
    spiel_status = {
        "score": 0,
        "game_over": False,
        "slow_motion_aktiv": False,
        "slow_motion_ende": 0,
        "letzter_score_zeit": time.time()
    }
    
    # Frame-Zähler (wird für das Spawnen verwendet)
    frame_zaehler = 0
    
    # ==========================================
    # HAUPTSCHLEIFE - Läuft bis das Spiel endet
    # ==========================================
    laeuft = True
    while laeuft:
        
        # ------------------------------------------
        # EVENTS VERARBEITEN
        # ------------------------------------------
        for event in pygame.event.get():
            # Fenster schließen
            if event.type == pygame.QUIT:
                laeuft = False
            
            # Tastendruck
            if event.type == pygame.KEYDOWN:
                # ESC beendet das Spiel
                if event.key == pygame.K_ESCAPE:
                    laeuft = False
                
                # Leertaste startet das Spiel neu (wenn Game Over)
                if event.key == pygame.K_SPACE and spiel_status["game_over"]:
                    spiel_zuruecksetzen(spieler, hindernisse, powerups, spiel_status)
        
        # ------------------------------------------
        # SPIELLOGIK (nur wenn nicht Game Over)
        # ------------------------------------------
        if not spiel_status["game_over"]:
            
            # Hole die aktuell gedrückten Tasten
            tasten = pygame.key.get_pressed()
            
            # Bewege den Spieler
            spieler_bewegen(spieler, tasten)
            
            # Spawne neue Hindernisse
            hindernis_spawnen(hindernisse, frame_zaehler)
            
            # TODO: Kommentar entfernen für Bonus-Aufgabe (Power-Ups aktivieren)
            # Spawne Power-Ups (seltener als Hindernisse)
            # powerup_spawnen(powerups, frame_zaehler)
            
            # Hole den Geschwindigkeitsfaktor (für Slow-Motion)
            geschwindigkeits_faktor = slow_motion_aktualisieren(spiel_status)
            
            # Bewege die Hindernisse
            hindernisse_bewegen(hindernisse, geschwindigkeits_faktor)
            
            # Bewege die Power-Ups
            powerups_bewegen(powerups)
            
            # Entferne Hindernisse und Power-Ups außerhalb des Bildschirms
            hindernisse = hindernisse_entfernen(hindernisse)
            powerups = powerups_entfernen(powerups)
            
            # Hole das Rechteck des Spielers für Kollisionen
            spieler_rect = spieler_rechteck_holen(spieler)
            
            # Prüfe Power-Up Kollisionen
            eingesammeltes_powerup = powerup_kollision_pruefen(spieler_rect, powerups)
            if eingesammeltes_powerup:
                powerup_einsammeln(spieler, spiel_status, eingesammeltes_powerup)
            
            # Aktualisiere den Schild-Status
            schild_aktualisieren(spieler)
            
            # Prüfe Kollision mit Hindernissen
            if kollision_pruefen(spieler_rect, hindernisse):
                # Kollision erkannt!
                if not spieler["hat_schild"]:
                    # Spieler hat kein Schild -> Game Over
                    spiel_status["game_over"] = True
                    print(f"Game Over! Dein Score: {spiel_status['score']}")
            
            # Score aktualisieren
            spiel_status["letzter_score_zeit"], spiel_status["score"] = score_aktualisieren(
                spiel_status["letzter_score_zeit"],
                spiel_status["score"]
            )
            
            # Frame-Zähler erhöhen
            frame_zaehler += 1
        
        # ------------------------------------------
        # ZEICHNEN
        # ------------------------------------------
        # Hintergrund füllen
        bildschirm.fill(HINTERGRUND_FARBE)
        
        # Hindernisse zeichnen
        hindernisse_zeichnen(bildschirm, hindernisse, hindernis_bild)
        
        # Power-Ups zeichnen
        powerups_zeichnen(bildschirm, powerups, powerup_bilder)
        
        # Spieler zeichnen
        spieler_zeichnen(bildschirm, spieler, spieler_bild)
        
        # Score zeichnen
        score_zeichnen(bildschirm, spiel_status["score"], schrift)
        
        # Slow-Motion Anzeige
        if spiel_status.get("slow_motion_aktiv", False):
            slow_text = schrift.render("SLOW MOTION!", True, (255, 255, 0))
            bildschirm.blit(slow_text, (BILDSCHIRM_BREITE - 200, 10))
        
        # Schild Anzeige
        if spieler["hat_schild"]:
            schild_text = schrift.render("SCHILD AKTIV!", True, (100, 100, 255))
            bildschirm.blit(schild_text, (BILDSCHIRM_BREITE - 200, 50))
        
        # Game Over Bildschirm
        if spiel_status["game_over"]:
            game_over_zeichnen(bildschirm, spiel_status["score"], schrift)
        
        # Bildschirm aktualisieren
        pygame.display.flip()
        
        # Framerate begrenzen
        uhr.tick(FPS)
    
    # Pygame beenden
    pygame.quit()
    sys.exit()


# ==========================================
# PROGRAMM STARTEN
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Willkommen zum Dodger Game!")
    print("  Steuere mit den Pfeiltasten links/rechts")
    print("  Weiche den Hindernissen aus!")
    print("=" * 50)
    hauptschleife()
