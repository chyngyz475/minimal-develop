from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse, 
    Http404,
)
from django.utils.translation import gettext as _
from .models import *
from django.shortcuts import get_object_or_404

def product(request: HttpRequest, page_id: str) -> HttpResponse:
 

    current_product = get_object_or_404(Product, pk=page_id)
    if(current_product.is_public is False):
        return Http404("Данный товар не найден, или убран из продажи.")

    context = {
        'current_product': current_product, 
    }

    return render(request=request,
                  template_name='pages/page.html',
                  context=context)


