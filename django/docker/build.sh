set -e

if [ "$MODE" = "DEV" ]; then
    echo "Starting makemigrations"
    python manage.py makemigrations
fi

echo "Starting migrate"
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:8000