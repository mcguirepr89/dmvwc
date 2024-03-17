import sys
import os
import csv
import django
from django.apps import apps

sys.path.append("watch_database")  # Update this with the path to your Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watch_database.settings")
django.setup()

def import_into_database(model_name, csv_filenames):
    # Setup Django environment
    django.setup()

    # Get the model class dynamically using the model name
    if model_name == 'Brand':
        app_label = 'brands'
    elif model_name == 'Caliber':
        app_label = 'calibers'
    elif model_name == 'Watch':
        app_label = 'watch_collection'
    elif model_name == 'Wishlist':
        app_label = 'wishlist'
    else:
        app_label = model_name

    try:
        model_class = apps.get_model(app_label, model_name=model_name)
    except LookupError:
        raise ValueError(f"Invalid model name: {model_name}")

    # Iterate over each CSV file provided
    for csv_filename in csv_filenames:
        # Open the CSV file and read its contents
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Iterate over each row in the CSV file
            for row in reader:
                # Check if an entry with the same data already exists
                existing_entry = model_class.objects.filter(name=row['name']).first()
                if existing_entry:
                    # Update existing entry with non-empty values from CSV
                    for field_name, value in row.items():
                        if value and hasattr(existing_entry, field_name):
                            setattr(existing_entry, field_name, value)
                    existing_entry.save()
                    print(f"Entry updated for data: {row}")
                else:
                    print("Data to be written:", row)
                    # Create a new instance of the model
                    instance = model_class()

                    # Iterate over the fields and populate the instance
                    for field_name, value in row.items():
                        setattr(instance, field_name, value)

                    # Save the instance to the database
                    instance.save()
                    print("Data written to database:", instance)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python import_into_database.py model_name csv_file1 [csv_file2 ...]")
        sys.exit(1)

    # Extract the model name and CSV filenames from command-line arguments
    model_name = sys.argv[1]
    csv_filenames = sys.argv[2:]

    # Call the import function with the provided arguments
    try:
        import_into_database(model_name, csv_filenames)
    except ValueError as e:
        print(e)
        sys.exit(1)

