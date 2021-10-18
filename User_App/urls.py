from django.urls import path
from .views import *

urlpatterns = [
      path('sighn_up',sign_up,name="sign_up"),
      path('wel/', ReactView.as_view(), name="something"),
      path('sign/', UserSignUpReactView.as_view(), name="sign"),
]
