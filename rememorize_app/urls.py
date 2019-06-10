from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from rememorize_app.views import CardView

urlpatterns = [
    path('', staff_member_required(CardView.as_view())),
]
