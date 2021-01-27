'''
Created on 2021. 1. 27.

@author: Heun94
'''
from app import views
from django.urls.conf import path

urlpatterns = [
    path('survey', views.SurveyView),
    path('surveyprocess', views.SurveyProcess),
    

]