from django.shortcuts import render
from django.views.generic import TemplateView
from get_bank_csv.models import transaction
from datetime import datetime
from .function import graph_data

# Create your views here.

class chartViews(TemplateView):
	template_name="HomePage/show_chart.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs,)
		context['chartData'] = {
			'expense':graph_data.get_expenses_graph_data(),
			'income':graph_data.get_incom_graph_data(),
			'dalyTransaction':graph_data.get_dalyTransaction_graph_data(),
		}
		return context

