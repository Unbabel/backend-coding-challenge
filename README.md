# Unbabel Backend Challenge

Hey :smile:

Welcome to our Fullstack Challenge repository. This README will guide you on how to participate in this challenge.

In case you are doing this to apply for our open positions for a Fullstack Developer make sure you first check the available jobs at [https://unbabel.com/jobs](https://unbabel.com/jobs)

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.

**FYI:** Please understand that this challenge is not decisive if you are applying to work at [Unbabel](https://unbabel.com/jobs). There are no right and wrong answers. This is just an opportunity for us both to work together and get to know each other in a more technical way.

## Challenge

1) Build a basic web app with a simple input field that takes an English (EN) input translates it to Spanish (ES).
2) When a new translation is requested it should add to a list below the input field (showing one of three status: requested, pending or translated) - (note: always request human translation)
3) The list should be dynamically ordered by the size of the translated messages

#### Requirements
* Use Flask web framework
* Use PostgreSQL
* Create a scalable application. 
* Only use Unbabel's Translation API on sandbox mode
* Have tests

#### Notes
* Page load time shouldnt exceed 1 second

#### Resources
* Unbabel's API: http://developers.unbabel.com/

---------------------------------------------------------

## Run locally:
 
1 - Create the Redis and Database instances: 
 
    sudo docker-compose -f docker-compose-dev.yml up -d
    
2 - Create virtual environment and install requirements

3 - Upgrade the database - from the project path:
 
    flask db upgrade
 
4 - Setup the callback URL:

There are several ways to setup the variable. 
Using CALLBACK_IP_ADDRESS that will map inside the callback link (http://CALLBACK_IP_ADDRESS/api/translation), this address must be reachable by Unbabel Sandbox:
 
    export CALLBACK_IP_ADDRESS=somehost.com
    
    or
    
    export CALLBACK_IP_ADDRESS=10.21.10.10:5000
    
Define your own CALLBACK_URL, for example using a testing proxy with webhook testing service (e.g. webhook.site) in:
 
    export CALLBACK_URL=https://webhook.site/00b3fd24-3a7d-42af-9d31-771e7293ddf4
    
Note: using the second method the testing proxy must know where to redirect the response.

Change the application.ini with the desired variable.

 
5 - Open one terminal with the application:
 
    uwsgi --ini config/application.ini
    
6 - Open another terminal with Celery (also need to define step 3):
 
    celery worker --app=app -l info
    
7 - To run the tests

    python -m unittest
    
### Extra
You can also build the image 
 
    sudo docker build . -t unbabel-app
    
Run everything together 

    Change the variables in the docker-compose.yml file and run:
 
    sudo docker-compose -f docker-compose.yml up -d
    
Update the Database using:

    flask db upgrade
    
### Env Settings

All the following settings can be changed using env variables.

|                    Value | Description  | Default  |
|--------------------------|--------------|----------|
| DEBUG | Enable/Disable Debug Mode | True|
| UNBABEL_TRANSLATION_URL  |  Unbabel API url |  https://sandbox.unbabel.com/tapi/v2/translation/ |
| UNBABEL_USERNAME  | Unbabel API username  | fullstack-challenge  |
| UNBABEL_PASSWORD  | Unbabel API password  | 9db71b322d43a6ac0f681784ebdcc6409bb83359 |
| CALLBACK_IP_ADDRESS  | Callback Hostname that will be user to create the callback url to send to the Unbabel services  | None  |
| CALLBACK_URL  | An pre-defined url to send the callback response  | None  |
| DATABASE_HOST | Database host | 127.0.0.1 |
| DATABASE_PORT | Database port | 5432 |
| DATABASE_USERNAME | Database username | test |
| DATABASE_PASSWORD | Database password | test |
| DATABASE_NAME | Database name | test_db |
| CELERY_BROKER_URL | Celery Broker URL - (Redis tested for now) | redis://0.0.0.0:6379 |
| CELERY_RESULT_BACKEND | Celery Result Backend - (Redis tested for now) | redis://0.0.0.0:6379 |
| SECRET_KEY | Secret key for the CSRF | Some String |
| WTF_CSRF_ENABLED | CSRF Enable/Disable configuration  | True |
| SOURCE_TRANSLATION_LANGUAGE | Source language for the translation | en |
| TARGET_TRANSLATION_LANGUAGE | Target language for the translation  | es |
 
