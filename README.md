# E-SHOP


## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Usage](#usage)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running app](#running-app)
- [Database](#database)
- [Author](#author)


### Project Overview

This project is created for web scraping. It can analyze web page, get articles and count stats of using words
linked with article author.


### Technologies

The most important technologies used in the project:

- Python 3.11
- Django 4.2.6
- DjangoRestFramework 3.14.0
- PostgreSQL 16
- Docker 24.0.5
- Pre-commit 3.5.0
- BeautifulSoup 4.12.2


### Usage

Set in constants.py variables:
- URL_TO_GET_ARTICLES - page to scrap
- BASE_URL - main page
Next, when you get into main page, it returns stats about these articles (top 10 words, top 10 words by author 
and all authors)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SzymKam/web_scraping
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Configure your project by setting up environment variables. You can use pre-created env.dist file.

- SECRET_KEY - default is randomly generated
- DEBUG - set False in production

Create local server of PostgreSQL, and set variables to connect:

- DB_USER - database user
- DB_PASSWORD - database user password
- DB_HOST - database host
- DB_NAME - database name


### Running app
You have follow a few steps:

1. Run database migrations:
   ```bash
    cd src
    python manage.py migrate
   ```

2. Run server
   ```bash
    python manage.py runserver
   ```

You can also use pre-configured Docker, by docker-compose file:
   
   ```bash
    docker-compose up --build
   ```


### Database

Overview of the database structure and models:

- [Model 1]: WordCount - includes data about article url, word, count and author. 


### Author

SzymKam
https://github.com/SzymKam