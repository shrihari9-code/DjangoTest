from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, help_text=_("This will be displayed to user as-is"))
    price = models.PositiveSmallIntegerField(_("selling price (Rs.)"), help_text=_("Price payable by customer (Rs.)"))
    description = models.TextField(_("descriptive write-up"), unique=True, help_text=_("Few sentences that showcase the appeal of the product"))
    is_refrigerated = models.BooleanField(help_text=_("Whether the product needs to be refrigerated"), default=False)
    category = models.ForeignKey("categories.Category", related_name="products", blank=True, null=True, on_delete=models.PROTECT)
    managed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="managed_products", blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)  # New field for last edit timestamp
    ingredients = models.CharField(max_length=500, blank=True, null=True)  # New field for ingredients

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (Rs. {self.price})"

    class Meta:
        db_table = "product"
        ordering = []
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Sku(models.Model):
    product = models.ForeignKey(Product, related_name='skus', on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField()
    selling_price = models.PositiveSmallIntegerField(default=0)
    platform_commission = models.PositiveSmallIntegerField(default=0)
    cost_price = models.PositiveSmallIntegerField(default=0)
    measurement_unit_choices = [
        ('gm', _('Grams')),
        ('kg', _('Kilograms')),
        ('mL', _('Milliliters')),
        ('L', _('Liters')),
        ('pc', _('Piece')),
    ]
    measurement_unit = models.CharField(max_length=2, choices=measurement_unit_choices)
    status_choices = [
        (0, _('Pending for approval')),
        (1, _('Approved')),
        (2, _('Discontinued')),
    ]
    status = models.IntegerField(choices=status_choices, default=0)

    @property
    def markup_percentage(self):
        if self.cost_price > 0:
            return round((self.platform_commission / self.cost_price) * 100, 2)
        return 0

    def save(self, *args, **kwargs):
        self.selling_price = self.cost_price + self.platform_commission
        super().save(*args, **kwargs)

    def clean(self):
        if self.size > 999:
            raise ValidationError(_('Size must be less than or equal to 999.'))

    def __str__(self):
        return f"{self.product.name} - {self.size} {self.measurement_unit}"