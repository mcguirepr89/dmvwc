# Inside your migration file (e.g., 000x_run_import_script.py)

import glob 
from django.db import migrations
import subprocess

def run_import_script(apps, schema_editor):

    csv_files = glob.glob("brands*.csv")
    
    subprocess.run(["python", "import_into_database.py", "Brand"] + csv_files)

class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_alter_brand_options'),
    ]

    operations = [
        # Run your custom function during the migration
        migrations.RunPython(run_import_script),
    ]
