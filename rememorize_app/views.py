import time
import random

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import F
from django.http.request import HttpRequest

from rememorize_app.models import MemCard


class CardView(View):
    def get(self, request, *args, **kwargs):
        card_box = []

        now = int(time.time())
        card_queryset = MemCard.objects.annotate(
            remind_time=F('passed_at') + (F('remind_after') * 5000)
        ).filter(remind_time__lte=now).order_by('-remind_time')
        for card_object in card_queryset.all()[:3]:
            card_box.append({
                'card_id': card_object.id,
                'card_key': card_object.key,
                'card_value': card_object.value
            })

        if len(card_box) > 1:
            picked_card = random.choice(card_box)
        else:
            picked_card = {'card_id': None}

        return render(request, 'card.html', picked_card)

    def post(self, request: HttpRequest, *args, **kwargs):
        card_id = request.POST['cardId']
        is_passed = request.POST.get('isPassed', 0)

        now = int(time.time())

        card = MemCard.objects.get(pk=int(card_id))

        card.passed_at = now
        card.remind_after = MemCard.REMIND_PHASE[card.current_phase + 1 if int(is_passed) > 0 else 0]
        card.save()

        return redirect('/app')
