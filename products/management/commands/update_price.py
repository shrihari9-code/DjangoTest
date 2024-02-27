from django.core.management.base import BaseCommand
from django.db.models import F
from products.models import Sku

class Command(BaseCommand):
    help = 'Update Sku prices'

    def handle(self, *args, **options):
        # Update platform commission to 25% of selling price
        Sku.objects.update(platform_commission=F('selling_price') * 0.25)

        # Update cost price to selling price - platform commission
        Sku.objects.update(cost_price=F('selling_price') - F('platform_commission'))

        # Update selling price in Sku model
        for sku in Sku.objects.all():
            sku.save()