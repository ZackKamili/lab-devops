from django.shortcuts import render
import sentry_sdk

def home(request):
    return render(request, 'portal/index.html')

def trigger_error(request):
    try:
        # Simulation d'un bug logique (ex: division par zéro)
        division_by_zero = 1 / 0
    except Exception as e:
        # On envoie l'erreur à Sentry manuellement
        sentry_sdk.capture_exception(e)

    # On renvoie l'utilisateur sur la même page avec un message discret
    return render(request, 'portal/index.html', {'error': True})
