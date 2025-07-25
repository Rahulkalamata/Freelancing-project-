from django.db import models

class ClientRequest(models.Model):
    name = models.CharField(max_length=100)
    project_complexity = models.FloatField(default=5.0)  # Complexity rating (1 to 10)
    project_duration = models.IntegerField(default=4)  # Duration in weeks
    predicted_budget = models.FloatField()  # Predicted budget value

    def __str__(self):
        return self.name
