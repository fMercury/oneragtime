from django.db import models

# Create your models here.

class Investors(models.Model):
    Investor_ID = models.AutoField(primary_key=True)
    Investor_Email = models.EmailField()
    Investor_Name = models.CharField(max_length=50)

class Investments(models.Model):
    Investment_ID = models.AutoField(primary_key=True)
    Investment_Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Investment_Date = models.DateField()
    Investment_Fee = models.DecimalField(max_digits=10, decimal_places=2)
    Investor_ID = models.ForeignKey(Investors, on_delete=models.CASCADE)

class Bills(models.Model):
    Bill_ID = models.AutoField(primary_key=True)
    Bill_Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Bill_Date = models.DateField()
    Bill_Type = models.CharField(max_length=50)
    Bill_Checked = models.BooleanField()
    Investor_ID = models.ForeignKey(Investors, on_delete=models.CASCADE)

class Invoices(models.Model):
    STATUS = [('validated','validated'), ('sent','sent'), ('paid','paid'), ('overdue','overdue')]

    Invoice_ID = models.AutoField(primary_key=True)
    List_of_Bills = models.ManyToManyField(Bills) 
    Invoice_Date = models.DateField()
    Invoice_Status = models.CharField(max_length=50, choices=STATUS, default='validated')
    Investor_ID  = models.ForeignKey(Investors, on_delete=models.CASCADE)
