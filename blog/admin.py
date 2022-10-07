from django.contrib import admin

# Register your models here.

from .models import Produit
from .models import Promotion
class AdminProduit(admin.ModelAdmin):
    list_display = ['type_de_produit', 'prix', 'quantite','poids']

admin.site.register(Produit, AdminProduit) 

class AdminPromotion(admin.ModelAdmin):
    list_display = ['promo_sur', 'reduction']

admin.site.register(Promotion, AdminPromotion) 