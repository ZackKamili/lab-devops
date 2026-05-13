from django.test import TestCase
from django.urls import reverse


class KillSwitchTest(TestCase):
    """
    Test de sécurité (Kill Switch) pour empêcher le déploiement
    si un mot critique apparaît dans la page.
    """

    def test_no_danger_keyword_in_production(self):
        """
        Règle :
        - Présence de "Attention"  -> Échec du test (blocage du déploiement)
        - Absence de "Attention"   -> Test validé (déploiement autorisé)
        """

        # Appel de la page d'accueil
        response = self.client.get(reverse('home'))

        # Vérifie que la page est accessible
        self.assertEqual(response.status_code, 200)

        # Vérifie que le mot interdit n’est PAS présent dans le contenu brut
        # On utilise response.content.decode() pour éviter le bug de copie de contexte sur Python 3.14
        self.assertNotIn("Attention", response.content.decode())