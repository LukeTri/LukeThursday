from django.urls import path, include
from django.conf import settings
from django.contrib import admin, auth

from fullstackexam.views import RatingList, AboutPage, RatingCreate, PicturePage

urlpatterns = [
    path('', RatingList.as_view(), name="rating_list"),
    path('ratings/', RatingList.as_view(), name="rating_list"),
    path('about/', AboutPage.as_view(), name="about_page"),
    path('rating/add/', RatingCreate.as_view(), name='rating_add'),
    path('logo/', PicturePage.as_view(), name='picture_page')
]