from django.db import models
from django.urls import reverse

# Create your models here.

class transaction(models.Model):
	
	choice=[
		('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT'),
	]
	category_choices=[
		('Transport','TRANSPORT'),
		('Food','FOOD'),
		('Donation','DONATION'),
		('Grocery','GROCERY'),
		('MonthlyRent','MONTHLY RENT'),
		('Shopping','SHOPPING'),
		('UtilityBills','UTILITY BITTS'),
		('Call&Internet','CALL AND INTERNET'),
		('Entertanment','ENTERTANMENT'),
		('Clothing','CLOTHING'),
		('Help','HELP'),
		('Investment','INVESTMENT'),
		('Education','EDUCATION'),
		('Health&Medicine','HEALTH AND MEDICINE'),
		('Loan','LOAN'),
		('EarnedIncome','EARNED INCOME'),
		('BusinessIncome','BUSINESS INCOME'),
		('InvestmentIncome','INVESTMENT INCOME'),
		('SoldIteams','SOLD ITEMS'),
		('Coupons','COUPONS'),
		('Salary','SALARY'),
		('Wage','WAGE'),
		('Others','OTHERS'),
		('None','NONE'),
	]
	## sort the category_choices
	def sortFunc(e):
		return(e[0])

	category_choices.sort(key=sortFunc)

	id=models.CharField(primary_key=True,max_length=30)
	dateTime=models.DateTimeField()
	amount=models.FloatField()
	type=models.CharField(choices=choice,max_length=10)
	category=models.CharField(choices=category_choices, max_length=30,null=True,blank=True)
	description=models.CharField(max_length=300)
	check_no=models.CharField(max_length=20,null=True,blank=True)
	balance=models.FloatField()
	sbject=models.CharField(max_length=100,null=True,blank=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.amount)+" | "+self.description[:15]+" | "+self.type+ " | "+ self.id

	def get_absolute_url(self):
		return(reverse('get_bank_csv:csvHome'))



# class to use for views

from datetime import datetime
import json


class data:

	imop_tr_amount = 5000

	def __init__(self,date_time,check_no,description, b_Code, debit, credit, balance):

		self.date,self.time=self.get_date_time(date_time)
		self.check_no=check_no if check_no!="" else 'N/A'
		self.description= description if description!="" else  'N/A'
		self.b_Code= b_Code if  b_Code!="" else  'N/A'
		self.debit= self.get_float(debit) if debit !="" else 0.0
		self.credit=self.get_float(credit) if credit !="" else 0.0
		self.balance=self.get_float(balance) if balance !="" else 0.0
		self.amount,self.tr_type,self.balance_BF= self.get_amount_and_type(self.debit,self.credit,self.balance)
		self.priority= self.get_priority()
		self.category = self.set_category()
		self.pay_mode = self.get_pay_mode()
		self.id=self.get_id()

	def get_id(self):
		stid=str(self.date.year)+str(self.date.month).zfill(2)+str(self.date.day).zfill(2)+str(self.time.hour).zfill(2)+str(self.time.minute).zfill(2)+str(self.time.second).zfill(2)+str(self.tr_type[:1])+str(int(self.amount))
		return(stid)

	def get_amount_and_type(self,debit,credit,balance):

		amount=debit - credit

		if amount>0:
			tr_type = "DEBIT"
		else:
			tr_type = "CREDIT"

		return((abs(amount),tr_type,(balance+amount)))

	def get_float(self,no):

		try:
			no=no.replace(',','')
			no=float(no)
		except :
			no=0
		return(no)

	def get_date_time(self,date_time):
		date=datetime.strptime(date_time, '%d-%b-%Y %H:%M:%S')
		return((date.date(),date.time()))

	def get_priority(self):

		if self.amount >= self.imop_tr_amount:
			return(10)
		elif self.amount >= self.imop_tr_amount/2:
			return(5)
		else:
			return(0)

	def set_category(self):
		return("")

	def get_pay_mode(self):

		#mode=['cash','upi','online']
		dec=self.description.lower()
		if dec.find('atm cash')>=0 and self.debit>0:
			return ("cash")
		elif dec.find('upi')>=0:
			return ("upi") 
		else:
			return ("online")


	def serialize(self):
		return({
			"id": self.get_id(),
			"date" : str(self.date), 	# json don't support datatime object
			"time" : str(self.time),	# json don't support datatime object
			"check_no":self.check_no,
			"description" : self.description,
			"debit" : self.debit,
			"credit" : self.credit,
			"amount" : self.amount,
			"type" : self.tr_type,
			"balance_B/F" : self.balance_BF,
			"balance" : self.balance,
			"priority" : self.priority,
			"payment_mode" : self.pay_mode,
			"category":"",
		})

			
	def print_it(self):
		#print(self.date.month)
		if self.pay_mode != 'cash':

			json_data=json.dumps(self.serialize(),indent=4)
			with open("sample.json", "a") as outfile:
				outfile.write(json_data+'\n')
				outfile.close()

