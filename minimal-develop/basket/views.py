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
from product.models import Product 

@csrf_exempt 
def add_product(request: HttpRequest) -> JsonResponse:
  
    data = json.loads(request.body) 
    current_product = get_object_or_404(Product, pk=data['product_id'])
    if(current_product.is_public is False):
        return JsonResponse({'add':False,'errors':"Данный товар не найден"},status=200) 

    if request.user.is_authenticated is True: 
        basket = Basket.objects.get_or_create(user=data['user_id'])[0] 
    else:
        basket = Basket.objects.get_or_create(user_anonimus=data['user_anonimus'])[0]
    try: 
        basket.user_anonimus = data['user_anonimus']
        item_basket = basket.get_product_in_basket(current_product)
        if(item_basket is None): 
            item_basket = ItemBasketOrOrder.objects.create(item = current_product,price = current_product.price) 
                
            item_basket.save()
            basket.items.add(item_basket)
        else:
            item_basket.count += 1
            item_basket.save() 
    except Exception as err: 
        return JsonResponse({'add':False,'errors':str(err)},status=200) 
    
    finally:
        basket.save()  

    return JsonResponse({'add':True},status=200) 



@csrf_exempt 
def remove_product(request: HttpRequest) -> JsonResponse:
  
    data = json.loads(request.body) 
    current_product = get_object_or_404(Product, pk=data['product_id'])
    if(current_product.is_public is False):
        return JsonResponse({'add':False,'errors':"Данный товар не найден"},status=200)  
    if request.user.is_authenticated is True: 
        basket = Basket.objects.get_or_create(user=data['user_id'])[0] 
    else:
        basket = Basket.objects.get_or_create(user_anonimus=data['user_anonimus'])[0]
    try:
        basket.user_anonimus = data['user_anonimus']
        item_basket = basket.get_product_in_basket(current_product)
        if(item_basket is None):  
            return JsonResponse({'remove':False,'errors':f"Продукт не найден в корзине {basket.id}"},status=200) 
        elif (item_basket.count > 1):
            item_basket.count -= 1
            item_basket.save()
        else:
            basket.items.remove(item_basket)
            basket.save()   
    except Exception as err: 
        return JsonResponse({'remove':False,'errors':str(err)},status=200) 
     
    return JsonResponse({'remove':True},status=200) 