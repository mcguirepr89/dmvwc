# Inside your migration file (e.g., 000x_run_import_script.py)

import glob
from django.db import migrations
import subprocess

def run_import_script(apps, schema_editor):

    csv_files = glob.glob("calibers_*.csv")

    subprocess.run(["python", "import_into_database.py", "Caliber"] + csv_files)

class Migration(migrations.Migration):

    dependencies = [
        ('calibers', '0006_add_initial_caliber'),
    ]

    operations = [
        # Run your custom function during the migration
        migrations.RunPython(run_import_script),
    ]
