from django.core.management.base import BaseCommand, CommandError
from cashcall.models import Investments, Investors, Bills, Invoices 

class Command(BaseCommand):
    
    def create_investors_records(self):
        investor = Investors.objects.create(Investor_Email='example1@mail.com', Investor_Name='example1')
        investor.save()
        
        investor = Investors.objects.create(Investor_Email='example2@mail.com', Investor_Name='example2')
        investor.save()
        
        investor = Investors.objects.create(Investor_Email='example3@mail.com', Investor_Name='example3')
        investor.save()

    def create_investments_records(self):
        investor = Investors.objects.all()

        investmets = Investments(Investment_ID=1, Investment_Amount=10000, Investment_Date='2019-01-01', Investment_Fee=9, Investor_ID=investor[0])
        investmets.save()
        
        investmets = Investments(Investment_ID=2, Investment_Amount=20000, Investment_Date='2020-01-02', Investment_Fee=9, Investor_ID=investor[0])
        investmets.save()
        
        investmets = Investments(Investment_ID=3, Investment_Amount=30000, Investment_Date='2021-01-03', Investment_Fee=9, Investor_ID=investor[0])
        investmets.save()
        
        investmets = Investments(Investment_ID=4, Investment_Amount=50001, Investment_Date='2019-01-04', Investment_Fee=9, Investor_ID=investor[1])
        investmets.save()
        
        investmets = Investments(Investment_ID=5, Investment_Amount=50001, Investment_Date='2019-05-04', Investment_Fee=9, Investor_ID=investor[2])
        investmets.save()
        
        investmets = Investments(Investment_ID=6, Investment_Amount=50000, Investment_Date='2019-02-04', Investment_Fee=9, Investor_ID=investor[3])
        investmets.save()
        
        investmets = Investments(Investment_ID=7, Investment_Amount=50000, Investment_Date='2019-06-04', Investment_Fee=9, Investor_ID=investor[4])
        investmets.save()
        
    def create_invoices_records(self):  
        invoices = Invoices(Invoice_ID=1, Invoice_Date='2019-01-01', Invoice_Status='validated', Investor_ID=Investors.objects.get(Investor_ID=1))    
        invoices.save()

        invoiices = Invoices(Invoice_ID=2, Invoice_Date='2019-01-02', Invoice_Status='sent', Investor_ID=Investors.objects.get(Investor_ID=2))
        invoiices.save()

    def handle(self, *args, **options):
        self.create_investors_records()
        self.create_investments_records()
        self.create_invoices_records()
        