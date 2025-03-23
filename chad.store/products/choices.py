from django.db.models import TextChoices

class Currency(TextChoices):
    GEL = "gel", "₾"
    USD = "usd", "$"
    EURO = "euro", '€'

    