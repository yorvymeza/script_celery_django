# script_celery_django
Crear un script para gestionar una tarea de 2 parametros
 
# correr migraciones 
```bash
python manage.py migrate
```

# Correr los workers de celery
```bash
celery -A core beat  --scheduler django_celery_beat.schedulers:DatabaseScheduler  --loglevel=debug

celery -A core worker --loglevel=debug

```