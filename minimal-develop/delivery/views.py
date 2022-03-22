from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse, 
)
from django.utils.translation import gettext as _
from .models import *
from .forms import ConsultationForm
from datetime import datetime 
 