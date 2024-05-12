from .models import TasksModel
import requests
from config.celery import app


TOKEN = ''
CHAT_ID = ''


@app.task
def repeatUndoneTasks():
    task = TasksModel.objects.filter(status=2).values()
  
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={'chat_id':f'{CHAT_ID}', 'text': f'{task}'}, )
    
    # print(response.status_code)