# dmvwc
A Watch Collection Application for the DMV Watch Club

This uses TailwindCSS for styling -- find the standalone binary for
your architecture <a href="https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.0.23">HERE</a>

Run this to setup the development environment
```
curl -s https://raw.githubusercontent.com/mcguirepr89/dmvwc/main/install.bash | bash
```

OR

Follow the steps below.
## Development setup
1. Make a directory for the project, clone the repo there, and establish the virtual environment:

   ```
   mkdir ~/WatchCollectionProject && git clone https://github.com/mcguirepr89/dmvwc.git ~/WatchCollectionProject/dmvwc
   ```
1. Create a virtual environment:

   ```
   cd ~/WatchCollectionProject && python3 -m venv venv
   ```
1. Go to the project and `source` the environment

   ```
   cd ~/WatchCollectionProject/dmvwc && source ../venv/bin/activate
   ```
1. Update `pip`

   ```
   pip install -U pip
   ```
1. Install Python dependencies:

   ```
   pip install -r requirements.txt
   ```
1. Get your tailwindcss binary from <a href="https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.0.23">HERE</a>

   Linux x86 example:
   ```
   wget https://github.com/tailwindlabs/tailwindcss/releases/download/v3.0.23/tailwindcss-linux-x64 && mv tailwindcss-linux-x64 ../venv/bin/tailwindcss
   ```
1. Make the binary executable:

   ```
   chmod +x ~/WatchCollectionProject/venv/bin/tailwindcss
   ```

## Development getting started

1. Make your `.env` file

   ```
   cat > ~/WatchCollectionProject/dmvwc/.env <<EOF
   # .env
   SECRET_KEY=django-insecure-mySuperLongSecretKeyThatNeedsToBeChangedForProduction
   DEBUG=True
   ALLOWED_HOSTS=*
   CSRF_TRUSTED_ORIGINS=http://127.0.0.1
   EOF
   ```

1. Make your `./static/css` and `./media` directories:

   ```
   mkdir -p ~/WatchCollectionProject/dmvwc/{static/css,media}
   ```
1. Make your `./static/css/input.css` file:

   ```
   cat > ~/WatchCollectionProject/dmvwc/static/css/input.css <<EOF
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   EOF
   ```

1. Compile your CSS and run the watcher:

   ```
   tailwindcss -i ~/WatchCollectionProject/dmvwc/static/css/input.css -o ~/WatchCollectionProject/dmvwc/static/css/output.css --watch
   ```
1. Migrate database tables:

   ```
   python manage.py migrate --fake-initial
   python manage.py migrate
   ```
1. Populate the Brand model:

   ```
   python ./import_brands.py
   ```
1. Run the development server:

   ```
   python manage.py runserver
   ```
