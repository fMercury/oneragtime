from django.urls import path, register_converter
from django.conf.urls import url
from cashcall import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns = [

    path("investment/", views.investmentApi),
    path("investment/<int:id>", views.investmentApi),
    
    path("bill/", views.billApi),
    path("bill/<int:id>", views.billApi),
    
    path("bill/investor/<int:id>", views.billByInvestor),

    path("generate/bill/membership/investor/<int:investor_id>/year/<int:year>/", views.generateMembershipBill),    
    path("generate/bill/upfront_fees/investor/<int:investor_id>/investment/<int:investment_id>/", views.generateUpfrontBill),
    path("generate/bill/yearly_fees/investor/<int:investor_id>/payment/year/<int:payment_year>/", views.generateYearlyBill),

    path("invoice/status/<int:id>", views.invoiceStatus),


    ]