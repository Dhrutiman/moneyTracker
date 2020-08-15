from datetime import datetime
from get_bank_csv.models import transaction



##category=['BusinessIncome', 'Call&Internet', 'Clothing', 'Coupons', 'Donation', 'EarnedIncome', 'Education', 'Entertanment', 'Food', 'Grocery', 'Health&Medicine', 'Help', 'Investment', 'InvestmentIncome', 'Loan', 'MonthlyRent', 'None', 'Others', 'Salary', 'Shopping', 'SoldIteams', 'Transport', 'UtilityBills', 'Wage']
color_code={
			'BusinessIncome': '#FF7F50', 
			'Call&Internet': '#9ACD32', 
			'Clothing': '#14EEEF', 'Coupons': 
			'#FFA500', 'Donation': '#DB7093', 
			'EarnedIncome': '#218986', 
			'Education': '#8A2BE2', 
			'Entertanment': '#7FFF00', 
			'Food': '#FF8C00', 
			'Grocery': '#2BA911', 
			'Health&Medicine': '#FF0000', 
			'Help': '#191970', 
			'Investment': '#B78DCF', 
			'InvestmentIncome': '#B78DCF', 
			'Loan': '#EA0E05', 
			'MonthlyRent': '#FFC107', 
			'None': '#000000', 
			'Others': '#8B008B', 
			'Salary': '#30F429', 
			'Shopping': '#1E90FF', 
			'SoldIteams': '#32CD32', 
			'Transport': '#8B008B',
			'UtilityBills': '#B5F8C4', 
			'Wage': '#EA07FA'
		}

income_category=['BusinessIncome', 'Coupons', 'EarnedIncome', 'Investment', 'InvestmentIncome', 'Loan', 'Salary', 'SoldIteams','Wage']
expense_category=['Transport', 'Food', 'Donation', 'Grocery', 'MonthlyRent', 'Shopping', 'UtilityBills', 'Call&Internet', 'Entertanment', 'Clothing', 'Help', 'Investment', 'Education', 'Health&Medicine','Others']

base={
		'Transport': 'Transport', 
		'Food': 'food', 
		'Donation': 'donation', 
		'Grocery': 'Grocery', 
		'MonthlyRent': 'rent', 
		'Shopping': 'Shopping', 
		'UtilityBills': 'Bills', 
		'Call&Internet': 'Call', 
		'Entertanment': 'Fun', 
		'Clothing': 'Cloth', 
		'Help': 'Help', 
		'Investment': 'Invested', 
		'Education': 'Education', 
		'Health&Medicine': 'Health', 
		'CashWithdraw': 'CASH', 
		'RefundORCancle': 'Refund', 
		'Loan': 'Loan', 
		'EarnedIncome': 'E-Incom', 
		'BusinessIncome': 'B-Incom', 
		'InvestmentIncome': 'I-Incom', 
		'SoldIteams': 'SOld', 
		'Coupons': 'Coupons', 
		'Salary': 'Salary', 
		'Wage': 'Wage', 
		'Others': 'Others', 
		'None': 'NONE'
	}


class graph_data:

	def __init__(self,month,year,type):
		self.month=month
		self.year=year
		self.type=type
		self.dataSet=transaction.objects.filter(dateTime__year=self.year,dateTime__month=self.month)

	def get_expenses_graph_data(self):
		dh=self.dataSet
		
		expense_category=['Transport', 'Food', 'Donation', 'Grocery', 'MonthlyRent', 'Shopping', 'UtilityBills', 'Call&Internet', 'Entertanment', 'Clothing', 'Help', 'Investment', 'Education', 'Health&Medicine','Others']

		
		dic={}
		
		"""for i in expense_category:
			dic[i]=0

		for i in dh:
			if i.category in expense_category:
				dic[i.category]=dic[i.category]+i.amount
		"""	
				
		for i in dh.filter(type='DEBIT'):
			if i.category in expense_category:
				com=i.category
				amo=i.amount

				if com in dic:
						dic[com]=dic[com]+amo
				else:
					dic[com]=amo
		

		sz=sorted(dic.items(), key=lambda x: x[1], reverse=True)
		global base

		lable=[base[la[0]] for la in sz]
		data=[la[1] for la in sz]
		color=[color_code[la[0]] for la in sz]
		amount_total=sum(data)
		persent=[float("{:.1f}".format(x/amount_total*100)) for x in data]
		# print(lable,data)


		return({
				'labels':lable,
				'data':data,
				'color':color,
				'percent':persent,
		})

	def get_incom_graph_data(self):
		
		def get_done(mont):
			dh=transaction.objects.filter(dateTime__year=self.year,dateTime__month=mont)
			dic={}
			dic['Income']=0
			dic['Expenses']=0
			dic['saveing']=0
			
			if len(dh)==0:
				return({
					'labels':list(dic.keys()),
					'data':list(dic.values()),
				})

			
			bal_f=dh.last()
			bal_a=bal_f.amount if bal_f.type =="DEBIT" else -1*bal_f.amount
			bal=bal_f.balance+bal_a

			for i in dh:
				if i.type == "DEBIT":
					dic['Expenses']=dic['Expenses']+i.amount
				else:
					dic['Income']=dic['Income']+i.amount

			dic['saveing']=bal+(dic['Income']-dic['Expenses'])


			return({
					'labels':list(dic.keys()),
					'data':list(dic.values()),
			})
		return {
			'data1':get_done(self.month),
			'data2':get_done(self.month -1),
		}

	def get_dalyTransaction_graph_data(self):
		dh=self.dataSet
		dic={}

		"""
		x=[c for c in dh.filter(dateTime__day=1)]
		x=x[0]
		print(x.balance+(x.amount if x.type =="DEBIT" else -1*x.amount))
		"""
		bal_f=dh.last()
		bal_a=bal_f.amount if bal_f.type =="DEBIT" else -1*bal_f.amount
		bal=bal_f.balance+bal_a
		#print(bal)

		for transiaction in dh:
			com=str(transiaction.dateTime.date().day)
			amo=0
			if transiaction.type =='DEBIT':
				amo=-1*transiaction.amount
			else:
				amo=transiaction.amount
			if com in dic:
				dic[com]=dic[com]+amo
			else:
				dic[com]=amo

		sz=sorted(dic.items(), key=lambda x: x[0], reverse=False)
		# print(dic.keys())
		lable=[str(i) for i in range(1,32,1)]
		# print(lable)
		data=[dic[str(i)] if str(i) in dic else 0 for i in range(1,32,1)]
		# print(data)
		data1=[]
		for i in data:
			data1.append(bal+i)
			bal=bal+i
		# print(data1)

		return({
				'labels':lable,
				'data':data,
				'data1':data1
		})

