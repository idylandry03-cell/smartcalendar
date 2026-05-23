import flet as ft
from services.gestionnaire_calendrier import GestionnaireCalendrier
from vues.calendrier_view import afficher_calendrier

def main(page: ft.Page):
    page.title = "SmartCalendar"

    gestionnaire = GestionnaireCalendrier()
    seances = gestionnaire.get_all_seances()

    afficher_calendrier(page, seances)

ft.run(main)