from django.db import models

class SurveyResponse(models.Model):
    answers = models.JSONField()

    def __str__(self):
        return str(self.answers)
