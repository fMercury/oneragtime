from django.contrib import admin

from .models import Investments, Investors, Bills, Invoices

admin.site.register(Investments)
admin.site.register(Investors)
admin.site.register(Bills)
admin.site.register(Invoices)
# Register your models here.
