set -ex

install_dir=$HOME/WatchCollectionProject

mkdir $install_dir && git clone https://github.com/mcguirepr89/dmvwc.git $install_dir/dmvwc

cd $install_dir && python3 -m venv venv

cd $install_dir/dmvwc && source ../venv/bin/activate

pip install -U pip

pip install -r requirements.txt

archy=$(uname -m)
if [ $archy = "x86_64" ];then
    architecture=x64;
elif [ $archy = "aarch64" ];then
    architecture=arm64
else
    echo "Couldn't determine your hardware.
    Defaulting to x86_64"
    architecture=x64
fi
wget https://github.com/tailwindlabs/tailwindcss/releases/download/v3.0.23/tailwindcss-linux-$architecture && mv tailwindcss-linux-$architecture ../venv/bin/tailwindcss

chmod +x $install_dir/venv/bin/tailwindcss

cat > $install_dir/dmvwc/.env <<EOF
# .env
SECRET_KEY=django-insecure-mySuperLongSecretKeyThatNeedsToBeChangedForProduction
DEBUG=True
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=http://127.0.0.1
EOF


mkdir -p $install_dir/dmvwc/static/css
mkdir -p $install_dir/dmvwc/static/media
mkdir -p $install_dir/dmvwc/static/js

ln -sf $install_dir/dmvwc/jquery.min.js $install_dir/dmvwc/static/js/jquery.min.js

cat > $install_dir/dmvwc/static/css/input.css <<EOF
@tailwind base;
@tailwind components;
@tailwind utilities;
EOF


tailwindcss -i $install_dir/dmvwc/static/css/input.css -o $install_dir/dmvwc/static/css/output.css

python manage.py migrate --fake-initial
python manage.py migrate

DJANGO_SUPERUSER_EMAIL=blank@noemail.com DJANGO_SUPERUSER_USERNAME=superuser DJANGO_SUPERUSER_PASSWORD=dmvwatchclub1234 python manage.py createsuperuser --noinput

python manage.py runserver
