from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    size = models.PositiveSmallIntegerField(unique=True)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.size} gm - Rs. {self.price}"

    class Meta:
        verbose_name = _("Sku")
        verbose_name_plural = _("Skus")