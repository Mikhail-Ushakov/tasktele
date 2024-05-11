from django.db import models

class TasksModel(models.Model):
    
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=False)
    status = models.TextField(choices=[("Провалено", 0),("Не принят", 1),("В работе", 2),("Выполнено", 3)])
    date = models.DateTimeField(auto_now_add=True)