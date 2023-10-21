import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    DB_USER=(str, ""),
    DB_PASSWORD=(str, ""),
    DB_NAME=(str, ""),
    DB_HOST=(str, ""),
)
