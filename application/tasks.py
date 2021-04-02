from celery import shared_task
from time import sleep

@shared_task
def sum(a, b):
	sleep(10)
	return a+b


@shared_task
def send_email(email):
	print(f'A sample email is sent to {email}')