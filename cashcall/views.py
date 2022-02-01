from functools import reduce
from datetime import date, datetime

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.db.models import Count
from cashcall.models import Investments, Investors, Bills, Invoices
from cashcall.serializers import InvestmentsSerializer, InvestorsSerializer, BillsSerializer, InvoicesSerializer

# Create your views here.

@csrf_exempt
def investmentApi(request, id=0):
    try:
        if request.method == 'GET':
            investments = Investments.objects.all()
            investments_serializer = InvestmentsSerializer(investments, many=True)
            return JsonResponse(investments_serializer.data, safe=False)

        elif request.method == 'POST':
            investments_data = JSONParser().parse(request)
            investments_serializer = InvestmentsSerializer(data=investments_data)
            if investments_serializer.is_valid():
                investments_serializer.save()
                return JsonResponse(investments_serializer.data, status=201)
            return JsonResponse(investments_serializer.errors, status=400)

        elif request.method == 'PUT':
            investments_data = JSONParser().parse(request)
            investments = Investments.objects.get(Investment_ID=investments_data['Investment_ID'])
            investments_serializer = InvestmentsSerializer(investments, data=investments_data)
            if investments_serializer.is_valid():
                investments_serializer.save()
                return jsonResponse(investments_serializer.data, status=201)
            return JsonResponse(investments_serializer.errors, status=400)

        elif request.method == 'DELETE':
            investments = Investments.objects.get(Investment_ID=id)
            investments.delete()
            return JsonResponse('', status=204, safe=False)
    
    except:
        return JsonResponse('investmentsApi Bad Response', status=404, safe=False)

def billApi(request, id=0):
    try:
        if request.method == 'GET':
            if id!=0:
                bills = Bills.objects.get(Bill_ID=id)
                bills_serializer = BillsSerializer(bills, many=False)
            else: 
                bills = Bills.objects.all()
                bills_serializer = BillsSerializer(bills, many=True)
            return JsonResponse(bills_serializer.data, safe=False)

        elif request.method == 'POST':
            bills_data = JSONParser().parse(request)
            bills_serializer = BillsSerializer(data=bills_data)
            if bills_serializer.is_valid():
                bills_serializer.save()
                return JsonResponse(bills_serializer.data, status=201)
            return JsonResponse(bills_serializer.errors, status=400)

        elif request.method == 'PUT':
            bills_data = JSONParser().parse(request)
            bills = Bills.objects.get(Bill_ID=bills_data['Bill_ID'])
            bills_serializer = BillsSerializer(bills, data=bills_data)
            if bills_serializer.is_valid():
                bills_serializer.save()
                return jsonResponse(bills_serializer.data, status=201)
            return JsonResponse(bills_serializer.errors, status=400)

        elif request.method == 'DELETE':
            bills = Bills.objects.get(Bill_ID=id)
            bills.delete()
            return JsonResponse('', status=204, safe=False)
    
    except:
        return JsonResponse('billApi Bad Response', status=404, safe=False)

def billByInvestor(request, id=0):    
    try:
        if request.method == 'GET':
            if id!=0:
                bills = Bills.objects.all().filter(Investor_ID=id)
                bills_serializer = BillsSerializer(bills, many=True)
                return JsonResponse(bills_serializer.data, safe=False)    
    except:
        return JsonResponse('billByInvestor Bad Response', status=404, safe=False)


def generateMembershipBill(request, investor_id=0, year=0 ):
    if request.method == 'GET':
        amount_fixed = 3000
        investment_umbral = 50000

        investment = Investments.objects.filter( Investor_ID=investor_id )

        investment_list = list( filter( lambda item : item.Investment_Date.year == year , investment ) )        
        
        if len(investment_list) == 0 : return JsonResponse("no data" , status=404, safe=False)

        investment_amount_list = list( map( lambda x : x.Investment_Amount, investment_list))

        amount_value = reduce(lambda x, y: x + y, investment_amount_list )
        
        bill_amount_value = 0 if amount_value > investment_umbral else amount_fixed

        bills_data = {
            "Bill_Amount": bill_amount_value,
            "Bill_Date": date.today(),
            "Bill_Type": "Membership",
            "Bill_Checked": False,
            "Investor_ID": investor_id
            }

        bills_serializer = BillsSerializer(data=bills_data)
        if bills_serializer.is_valid():
            bills_serializer.save()
            return JsonResponse(bills_serializer.data, status=201)
        return JsonResponse(bills_serializer.errors, status=400)
        
def generateUpfrontBill(request, investor_id=0, investment_id=0):
    if request.method == 'GET':
        year_fixed = 5

        investment = Investments.objects.filter( Investor_ID=investor_id )
        
        investment_list = list( filter( lambda item : item.Investment_ID == investment_id , investment ) )        
        
        if len(investment_list) == 0 : return JsonResponse("no data" , status=404, safe=False)

        investment_amount_list = list( map( lambda x : x.Investment_Amount, investment_list))
        investment_fee_list = list( map( lambda x : x.Investment_Fee, investment_list))

        amount_value = reduce(lambda x, y: x + y, investment_amount_list )
        fee_percentage = reduce(lambda x, y: x * y, investment_fee_list )

        bill_amount_value = amount_value * fee_percentage * year_fixed

        bills_data = {
            "Bill_Amount": float("{:.2f}".format(bill_amount_value)),
            "Bill_Date": date.today(),
            "Bill_Type": "Upfront",
            "Bill_Checked": False,
            "Investor_ID": investor_id
            }

        bills_serializer = BillsSerializer(data=bills_data)
        if bills_serializer.is_valid():
            bills_serializer.save()
            return JsonResponse(bills_serializer.data, status=201)
        return JsonResponse(bills_serializer.errors, status=400)

def generateYearlyBill(request, investor_id=0, investment_id=0, payment_year=0):
    if request.method == 'GET':
        date_umbral = datetime( 2019, 4, 1)
    
        investment = Investments.objects.filter( Investor_ID=investor_id )
        
        investment_list = list( filter( lambda item : item.Investment_ID == investment_id , investment ) )        
        
        if len(investment_list) == 0 : return JsonResponse("no data" , status=404, safe=False)


        investment_list = list( filter( lambda item : item[investment_counter_index] == id_investment and item[investment_investor_index] == self.investor, investment ) )    
        if (len( investment_list) == 0) : return 0 
        
        item = investment_list[0]
        item_date = datetime.fromtimestamp(item[investment_date_index])
        
        investment_bought = 1
        investment_fee = item[investment_fee_index]
        discount_fee = 0
        
        if( item_date < self.date_umbral ) :
            if year == 1 : investment_bought = (365 - int(item_date.strftime("%j")) )/365

        else: 
            if ( year == 1 ):
                amounts_days_year = int ( datetime( item_date.year, 12, 31).strftime("%j"))
                investment_bought = (amounts_days_year - int(item_date.strftime("%j")) )/amounts_days_year
            if ( year == 3 ): discount_fee = 0.20
            if ( year == 4 ): discount_fee = 0.50
            if ( year > 4 ): discount_fee = 1.00
        
        return investment_bought * (investment_fee - discount_fee) * item[investment_amount_index]   

def invoiceStatus(request, id=0):
    try:
        if request.method == 'GET':
            if id!=0:
                invoices = Invoices.objects.all().filter(Invoice_ID=id)
                if len(invoices) >0 : return JsonResponse({'status':invoices[0].Invoice_Status}, safe=False) 
            return JsonResponse('No results', status=200, safe=False)
    except:
        return JsonResponse('invoice Bad Response', status=404, safe=False)
    