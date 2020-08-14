from django.urls import path
from .views import chartViews

app_name = "HomePage"
urlpatterns=[
	path("", chartViews.as_view(), name="home"),
	path("<int:month>,<int:year>", chartViews.as_view(), name="monthlyData"),
]