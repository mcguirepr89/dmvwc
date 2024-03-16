# import_calibers.py

import os
import sys
import django

sys.path.append("watch_database")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watch_database.settings")
django.setup()

from calibers.models import Caliber

def import_calibers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            caliber_name = line.strip()
            # Check if brand already exists to avoid duplicates
            if not Caliber.objects.filter(name=caliber_name).exists():
                Caliber.objects.create(name=caliber_name)
                print(f"Caliber '{caliber_name}' imported successfully.")

if __name__ == "__main__":
    file_path = "calibers.txt"
    import_calibers(file_path)
