class GestionnaireCalendrier:
    def __init__(self):
        self.seances = [
            {
                "id": 1,
                "date": "2026-05-10",
                "heure": "08:00-10:00",
                "salle": "B12"
            },
            {
                "id": 2,
                "date": "2026-05-11",
                "heure": "10:00-12:00",
                "salle": "Labo Info"
            }
        ]

    def get_all_seances(self):
        return self.seances