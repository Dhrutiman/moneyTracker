from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
import csv,io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import data,transaction
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView

# Create your views here.
@permission_required('admin.can_add_log_entry',login_url="login")
def uplode_csv(request):
	template="get_bank_csv/csvUplode.html"

	messages=[]

	prompt={
		'order':"Uplode CSV file of bank statement"
	}

	if request.method == 'GET':
		return render(request, template, prompt)

	csv_file=request.FILES['file']	

	if not (csv_file.name.endswith('csv') or csv_file.name.endswith('CSV')):
		messages.error(request, 'THIS IS NOT A CSV FILE')
		return render(request, template)
	
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)

	next(io_string)

	statements=[]

	## date_time,check_no,description, b_Code, debit, credit, balance

	for row in csv.reader(io_string,delimiter=','):
		
		_data=data(
    	row[0], row[2], 
    	row[3], row[4], 
    	row[5], row[6],
    	row[7])

		try :

			created = transaction.objects.update_or_create(
			 		id=_data.id,
					dateTime=datetime.combine(_data.date,_data.time),
					amount=_data.amount,
					type=_data.tr_type,
					check_no=_data.check_no,
					description=_data.description,
					balance=_data.balance,
					category='None',
			 	)

		except Exception as e:
			print(_data.id)
			messages.append(_data.id +'| is not been saved|')

	context={
		'messages':messages
	}
	#return(redirect("http://127.0.0.1:8000/get_csv"))
	return redirect('/get_csv')
	#return render(request, template, context)


class bank_statement_without_category_page(ListView):
	#model = transaction
	no_month=datetime.now().month - 3 ## last one month only
	queryset = transaction.objects.filter(category='None',dateTime__month__gte=no_month)
	template_name='get_bank_csv/statement.html'
	context_object_name="statements"

class bank_statement_page(ListView):
	#model = transaction
	queryset = transaction.objects.all()
	template_name='get_bank_csv/home.html'
	context_object_name="statements"

class bank_statement_update_page(PermissionRequiredMixin,UpdateView):
	model= transaction
	context_object_name="transaction"
	template_name="get_bank_csv/statement_edit.html"
	fields = ['category','sbject']
	permission_required = ('admin.can_add_log_entry',)
	login_url = 'login'

