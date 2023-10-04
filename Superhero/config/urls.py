from django.urls import path
from hero.views import  HulkView

urlpatterns = [
    path('hulk',        HulkView.as_view()),

]
