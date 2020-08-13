from datetime import datetime
from .models import transaction


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

class graph_data:

	def get_expenses_graph_data(type='month',art=datetime.now().month):
		dh=transaction.objects.all()
		
		expense_category=['Transport', 'Food', 'Donation', 'Grocery', 'MonthlyRent', 'Shopping', 'UtilityBills', 'Call&Internet', 'Entertanment', 'Clothing', 'Help', 'Investment', 'Education', 'Health&Medicine']

		
		dic={}
		
		for i in expense_category:
			dic[i]=0

		for i in dh:
			if i.category in expense_category:
				dic[i.category]=dic[i.category]+i.amount
		

		sz=sorted(dic.items(), key=lambda x: x[1], reverse=True)
		
		lable=[la[0] for la in sz]
		data=[la[1] for la in sz]
		color=[color_code[la[0]] for la in sz]
		# print(lable,data)


		return({
				'labels':lable,
				'data':data,
				'color':color,
		})

	def get_incom_graph_data(type='month',art=datetime.now().month):
		dh=transaction.objects.all()
		income_category=['BusinessIncome', 'Coupons', 'EarnedIncome', 'Help', 'Investment', 'InvestmentIncome', 'Loan', 'Others', 'Salary', 'SoldIteams','Wage']
		dic={}
		
		for i in income_category:
			dic[i]=0

		for i in dh:
			if i.category in income_category:
				dic[i.category]=dic[i.category]+i.amount
		

		sz=sorted(dic.items(), key=lambda x: x[1], reverse=True)
		
		lable=[la[0] for la in sz]
		data=[la[1] for la in sz]
		color=[color_code[la[0]] for la in sz]
		# print(lable,data)


		return({
				'labels':lable,
				'data':data,
				'color':color,
		})

	def get_dalyTransaction_graph_data(type='month',art=datetime.now().month):
		dh=transaction.objects.filter(dateTime__month=art-1)
		dic={}
		
		bal_f=dh.first()
		bal_a=bal_f.amount if bal_f.type =="DEBIT" else -1*bal_f.amount
		bal=bal_f.balance+bal_a

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

