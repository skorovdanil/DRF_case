from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Название задачи (до 100 символов)"
    )

    is_completed = models.BooleanField(
        default=False,
        help_text="Статус выполнения задачи"
    )

    def __str__(self):
        return self.title
