from datetime import datetime
from .models import transaction

class graph_data:

	def get_graph_data(type='month',art=datetime.now().month):
		dh=transaction.objects.all()
		category=['BusinessIncome', 'Call&Internet', 'Clothing', 'Coupons', 'Donation', 'EarnedIncome', 'Education', 'Entertanment', 'Food', 'Grocery', 'Health&Medicine', 'Help', 'Investment', 'InvestmentIncome', 'Loan', 'MonthlyRent', 'None', 'Others', 'Salary', 'Shopping', 'SoldIteams', 'Transport', 'UtilityBills', 'Wage']
		
		expense_category=['Transport', 'Food', 'Donation', 'Grocery', 'MonthlyRent', 'Shopping', 'UtilityBills', 'Call&Internet', 'Entertanment', 'Clothing', 'Help', 'Investment', 'Education', 'Health&Medicine']

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
		dic={}
		
		for i in expense_category:
			dic[i]=0

		for i in dh:
			if i.category in expense_category:
				dic[i.category]=dic[i.category]+i.amount

		sz=sorted(dic.items(), key=lambda x: x[1], reverse=False)
		
		lable=[la[0] for la in sz]
		data=[la[1] for la in sz]
		color=[color_code[la[0]] for la in sz]
		#print(lable,data)


		return({
				'labels':lable,
				'data':data,
				'color':color,
		})
"""
{
	'labels':list(dic.keys()),
	'data':list(dic.values()),
	'color':list(color_code.values()),
}
"""