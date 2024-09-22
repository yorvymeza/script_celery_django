from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.http import JsonResponse
from django.utils.timezone import now
import json


def schedule_dynamic_task(request, task_name:str, param1:int,param2:int):
    # Crear o usar un intervalo (aquí cada 10 segundos, pero puedes ajustar el tiempo como desees)
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute='*',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )

    # Crear una tarea periódica
    PeriodicTask.objects.create(
        crontab=schedule,                # Usar el intervalo creado
        name=f"Dynamic Task - {task_name}", # Nombre único de la tarea
        task='example.tasks.my_dynamic_scheduled_task', # Nombre completo de la tarea
        args=json.dumps([param1,param2]),        # Pasar los argumentos como JSON
        start_time=now()                  # Opcional: Puedes agregar start_time, expires, etc.
    )
    
    return JsonResponse({"status": "Tarea programada dinámicamente"})