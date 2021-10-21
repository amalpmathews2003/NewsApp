from django.urls import path
from .views import *

urlpatterns = [
      path('wel/', ReactView.as_view(), name="something"),
      path('sign/', UserSignUpReactView.as_view(), name="sign"),
]
