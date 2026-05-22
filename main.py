import flet as ft
from services.gestionnaire_calendrier import GestionnaireCalendrier


def main(page: ft.Page):
    page.title = "SmartCalendar"

    gestionnaire = GestionnaireCalendrier()
    seances = gestionnaire.get_all_seances()

    page.add(
        ft.Text("Calendrier des séances", size=20, weight="bold")
    )

    for s in seances:
        page.add(
            ft.Text(
                f"ID: {s['id']} | Date: {s['date']} | {s['heure']} | Salle: {s['salle']}"
            )
        )


ft.run(main)