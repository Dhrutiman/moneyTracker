from django.urls import path
from .views import *

app_name = "get_bank_csv"
urlpatterns = [

    path("", bank_statement_page.as_view(), name="home"),
    path("upload", uplode_csv, name='uplode_csv'),
    path("withoutCategoryList", bank_statement_without_category_page.as_view(
    ), name="withoutCategoryList"),
    path("<str:pk>/edit", bank_statement_update_page.as_view(),
         name="transiaction_edite"),
    path('allTransiaction', bank_allStatement_page.as_view(), name="allTransiaction"),

]
