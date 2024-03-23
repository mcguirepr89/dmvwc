# calibers/migrations/0006_add_initial_caliber.py

from django.db import migrations

def create_initial_caliber(apps, schema_editor):
    Caliber = apps.get_model('calibers', 'Caliber')
    Caliber.objects.create(name='Add a new caliber')

class Migration(migrations.Migration):

    dependencies = [
        ('calibers', '0005_caliber_slug'),  # Ensure correct dependency
    ]

    operations = [
        migrations.RunPython(create_initial_caliber),
    ]
