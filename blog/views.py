from django.shortcuts import render
from .forms import ModelForm
from blog.models import Produit,Promotion
from django.contrib import messages

# Create your views here.

def index(request):
    promotion = Promotion.objects.all()
    produit= Produit.objects.all()
    messages.info(request, 'Aucun resultat trouvé')
    context = {
        'produits':produit,
        'promo' :promotion
    }
    return render(request,'index.html', context)

def detail_produit(request, produit_id):
    promotion = Promotion.objects.all()
    id= int(produit_id)
    produit= Produit.objects.get(id=produit_id)
    context = {
        'produits':produit,
        'promo' :promotion
    }
    return render(request,'detail_produit.html', context)


def recherche_forms(request) :
    produit= Produit.objects.all()
    message = ''
    query = request.GET.get('query') 
    if request.method == "GET":
        type_de_produit = request.GET.get('query') 
        if type_de_produit is not None: 
            produit= Produit.objects.filter(type_de_produit__icontains=type_de_produit)    
        else:
            message = 'Aucun résultat trouvé pour %s'%query
    # query = request.GET.get('query')
    # if not query:
    #     produit = Produit.objects.all()
    # else:
    #     produit = Produit.objects.filter(type_de_produit__icontains=query)
    #     if not produit.exist() :
    #         message = 'Aucun résultat trouvé pour %s'%query
        
    context = {
				'produits':produit,
				'message':message,
			}
    return render(request, 'index.html', context)