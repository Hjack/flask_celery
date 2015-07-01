### Flask Celery app

Celery worker startup command:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program celery -A tasks worker --loglevel=info
```

Flask app starup command:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn app:app
```

RabbitMQ startup command:

```
/usr/local/sbin/rabbitmq-server
```
