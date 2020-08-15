from django.shortcuts import render
from django.views.generic import TemplateView
from get_bank_csv.models import transaction
from datetime import datetime
import datetime as dt
from .function import graph_data

# Create your views here.

class chartViews(TemplateView):
	template_name="HomePage/show_chart.html"


	
	def get_context_data(self, **kwargs):
		messages=[]
		_month=datetime.now().month-1
		_year=datetime.now().year
		
		try:
			month=self.request.GET['month']
			if month=='month':
				_month=_month
			else:
				_month=int(month)

			year=self.request.GET['year']
			if year=='-987':
				_year=_year
			elif int(year)>_year:
				messages.append("Invalid year is enter")
			else:
				_year=int(year)		

		except Exception as e:
			# print("month")
			pass
			
		

		try:
			charData=graph_data(type='month',month=_month,year=_year)
			#outChartData={}
			if len(charData.dataSet)==0:
				# print('true')
				raise 
			
			else:

				outChartData = {
					'expense':charData.get_expenses_graph_data(),
					'income':charData.get_incom_graph_data(),
					'dalyTransaction':charData.get_dalyTransaction_graph_data(),
					'month':[dt.date(_year, _month, 1).strftime('%B'),dt.date(_year, _month-1, 1).strftime('%B')],
					'transiaction':charData.dataSet,
					'messages':messages,
				}
		
		
		except Exception as e:
			print(e)
			messages.append("can't get data for "+dt.date(_year, _month, 1).strftime("%b, %Y"),)
			outChartData={
				'errorMessages':messages,
			}

		context = super().get_context_data(**kwargs,)
		charData=graph_data(type='month',month=_month,year=_year)
		# print(outChartData)
		context['chartData'] = outChartData
		return context

