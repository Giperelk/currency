"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from currency.views import (
    rate_all, rate_create, rate_details, rate_update, rate_delete,

    contactus_all, contactus_create, contactus_details, contactus_update, contactus_delete,

    source_all, source_create, source_details, source_update, source_delete,
)

'''
    DJANGO PATTERNS
'''

# django patterns
django_pattens = [
    path('admin/', admin.site.urls),
]

'''
    CURRENCY PATTERNS
'''

# rate currency patterns
rate_currency_patterns = [
    path('rate/all/', rate_all),
    path('rate/<int:pk>/', rate_details),
    path('rate/create/', rate_create),
    path('rate/<int:pk>/update/', rate_update),
    path('rate/<int:pk>/delete/', rate_delete),
]

# contact us currency patterns
contact_us_currency_patterns = [
    path('contactus/all/', contactus_all),
    path('contactus/<int:pk>/', contactus_details),
    path('contactus/create/', contactus_create),
    path('contactus/<int:pk>/update/', contactus_update),
    path('contactus/<int:pk>/delete/', contactus_delete),
]

# source currency patterns
source_currency_patterns = [
    path('source/all/', source_all),
    path('source/<int:pk>/', source_details),
    path('source/create/', source_create),
    path('source/<int:pk>/update/', source_update),
    path('source/<int:pk>/delete/', source_delete),
]

# currency patterns
currency_patterns = rate_currency_patterns + contact_us_currency_patterns + source_currency_patterns

"""
        URLPATTERNS
"""

urlpatterns = django_pattens + currency_patterns
