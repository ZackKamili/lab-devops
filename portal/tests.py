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

        # Vérifie que le mot interdit n’est PAS présent
        self.assertNotContains(response, "Attention")