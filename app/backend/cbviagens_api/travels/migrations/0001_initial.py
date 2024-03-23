from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_confort', models.FloatField()),
                ('price_econ', models.FloatField()),
                ('city', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('seat', models.CharField(max_length=3)),
                ('bed', models.CharField(max_length=3)),
            ],
        ),
    ]
