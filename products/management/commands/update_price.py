from django.core.management.base import BaseCommand
from django.db.models import F
from products.models import Sku

class Command(BaseCommand):
    help = 'Update existing Sku records to set selling_price, platform_commission, and cost_price.'

    def handle(self, *args, **kwargs):
        Sku.objects.all().update(
            platform_commission=F('selling_price') * 0.25,
            cost_price=F('selling_price') - F('platform_commission')
        )