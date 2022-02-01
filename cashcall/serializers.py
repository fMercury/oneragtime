from rest_framework import serializers
from cashcall.models import Investments, Investors, Bills, Invoices

class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
         model = Investments
         fields = ('Investment_ID', 'Investment_Amount', 'Investment_Date', 'Investment_Fee', 'Investor_ID')

class InvestorsSerializer(serializers.ModelSerializer):
    class Meta:
         model = Investors
         fields = ('Investor_ID', 'Investor_Email', 'Investor_Name')

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
         model = Bills
         fields = ('Bill_ID', 'Bill_Amount', 'Bill_Date', 'Bill_Type', 'Bill_Checked', 'Investor_ID')

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
         model = Invoices
         fields = ('Invoice_ID', 'List_of_Bills', 'Invoice_Date', 'Invoice_Status', 'Investor_ID')
