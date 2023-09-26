from django . urls import path
from . import views
app_name = 'searchapp'

urlpatterns = [

    path('search/',views.SearchResult,name='search'),

    ]