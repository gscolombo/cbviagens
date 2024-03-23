# Migration to feed database on initialization
from datetime import timedelta
from json import load

from django.db import migrations

def initialData(apps, _):
    Travel = apps.get_model("travels", "Travel")
    Travel.objects.all().delete()
    data = load(open('data/data.json', 'r'))
    for entry in data['transport']:
        entry = {
            **entry,
            "price_confort": float(entry["price_confort"].replace('R$ ', '')),
            "price_econ": float(entry["price_econ"].replace('R$ ', '')),
            "duration": timedelta(hours=int(entry["duration"].replace('h', '')))
        }
        del entry['id']
        Travel(**entry).save()

class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialData)
    ]
