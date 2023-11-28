from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
       from requests import get

response = get('https://google.com')
print ('Google', response)
print(response.text)