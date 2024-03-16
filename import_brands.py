# import_brands.py

import os
import sys
import django

# Set up Django environment
sys.path.append("watch_database")  # Update this with the path to your Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watch_database.settings")
django.setup()

from brands.models import Brand

def import_brands(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            brand_name = line.strip()
            # Check if brand already exists to avoid duplicates
            if not Brand.objects.filter(name=brand_name).exists():
                Brand.objects.create(name=brand_name)
                print(f"Brand '{brand_name}' imported successfully.")

if __name__ == "__main__":
    file_path = "brands.txt"  # Update this with the path to your brands.txt file
    import_brands(file_path)
