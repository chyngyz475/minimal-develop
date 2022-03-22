from django.shortcuts import get_object_or_404, render
from django.http import ( 
    HttpResponse,
    HttpRequest,
    JsonResponse, 
    Http404
)
from django.utils.translation import gettext as _
from .models import * 
from django.views.decorators.csrf  import csrf_exempt
import json
@csrf_exempt 
def add_favorite(request: HttpRequest) -> JsonResponse:
 


    data = json.loads(request.body) 
    current_product = get_object_or_404(Product, pk=data['product_id'])
    if(current_product.is_public is False):
        return JsonResponse({'add':False,'errors':"Данный товар не найден"},status=200) 
    
    

    
    if request.user.is_authenticated is True:
        try:
            favorite = Favorite.objects.get_or_create(user=data['user_id'])[0]
            favorite.items.add(current_product)
            favorite.save() 
        except Exception as err: 
            return JsonResponse({'add':False,'errors':str(err)},status=200) 
    else:
        try:
            favorite = Favorite.objects.get_or_create(user_anonimus=data['user_anonimus'])[0]
            favorite.user_anonimus = data['user_anonimus']
            favorite.items.add(current_product)
            favorite.save()  
        except Exception as err: 
            return JsonResponse({'add':False,'errors':str(err)},status=200) 
        
 

    return JsonResponse({'add':True},status=200) 


@csrf_exempt 
def remove_favorite(request: HttpRequest) -> JsonResponse:
 

    data = json.loads(request.body) 
    current_product = get_object_or_404(Product, pk=data['product_id'])
    if(current_product.is_public is False):
       return JsonResponse({'add':False,'errors':"Данный товар не найден"},status=200) 
    if request.user.is_authenticated is True:
        try:
            favorite = Favorite.objects.get_or_create(user=data['user_id'])[0]
            favorite.items.remove(current_product)
            favorite.save() 
        except Exception as err: 
            return JsonResponse({'remove':False,'errors':str(err)},status=200)  
    else:
        try:
            favorite = Favorite.objects.get_or_create(user_anonimus=data['user_anonimus'])[0]
            favorite.user_anonimus = data['user_anonimus']
            favorite.items.remove(current_product)
            favorite.save()  
        except Exception as err: 
            return JsonResponse({'add':False,'errors':str(err)},status=200) 
    return JsonResponse({'remove':True},status=200) 

 
  
