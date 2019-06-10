import time

from django.db import models


class MemCard(models.Model):
    REMIND_PHASE = [0, 1, 17, 52, 121, 241, 483]

    key = models.TextField(null=False, help_text="기억카드 key")
    value = models.TextField(null=False, help_text="기억카드 value")
    created_at = models.DateTimeField(auto_now_add=True, null=False, help_text="생성일자")

    passed_at = models.PositiveIntegerField(default=0, help_text="마지막 기억 일시 (Epoch Timestamp)")
    remind_after = models.PositiveIntegerField(default=0, help_text="n * 5000초 후 다시 기억")

    def __str__(self):
        return f"MemCard[{self.key}, Remind After {self.passed_at - int(time.time()) + self.remind_after * 5000}s]"

    @property
    def current_phase(self):
        return self.REMIND_PHASE.index(self.remind_after)
