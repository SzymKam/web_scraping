import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    DB_USER=(str, "db_web_scraping"),
    DB_PASSWORD=(str, "db_web_scraping"),
    DB_NAME=(str, "db_web_scraping"),
    DB_HOST=(str, "db"),
)
