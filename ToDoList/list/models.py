from django.db import models

class TasksModel(models.Model):
    
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=False)
    status = models.TextField(choices=[(0, "Провалено"),(1, "Не принят"),(2, "В работе"),(3, "Выполнено")])
    date = models.DateTimeField(auto_now_add=True)