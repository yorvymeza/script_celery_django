from celery import shared_task

@shared_task
def my_dynamic_scheduled_task(param1,param2):
	print("Se ejecuto")
	with open("prueba.txt","w") as f:
		f.write(str(param1+param2))
	return "tarea completada"