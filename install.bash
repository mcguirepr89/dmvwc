set -ex
mkdir ~/WatchCollectionProject && git clone https://github.com/mcguirepr89/dmvwc.git ~/WatchCollectionProject/dmvwc

cd ~/WatchCollectionProject && python3 -m venv venv

cd ~/WatchCollectionProject/dmvwc && source ../venv/bin/activate

pip install -U pip

pip install -r requirements.txt

wget https://github.com/tailwindlabs/tailwindcss/releases/download/v3.0.23/tailwindcss-linux-x64 && mv tailwindcss-linux-x64 ../venv/bin/tailwindcss

chmod +x ~/WatchCollectionProject/venv/bin/tailwindcss

cat > ~/WatchCollectionProject/dmvwc/.env <<EOF
# .env
SECRET_KEY=django-insecure-mySuperLongSecretKeyThatNeedsToBeChangedForProduction
DEBUG=True
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=http://127.0.0.1
EOF


mkdir -p ~/WatchCollectionProject/dmvwc/{static/css,media}

cat > ~/WatchCollectionProject/dmvwc/static/css/input.css <<EOF
@tailwind base;
@tailwind components;
@tailwind utilities;
EOF


tailwindcss -i ~/WatchCollectionProject/dmvwc/static/css/input.css -o ~/WatchCollectionProject/dmvwc/static/css/output.css

python manage.py migrate --fake-initial
python manage.py migrate

python manage.py runserver
