# Application Structure
Beeing *micro-framework* Flask doesn't force to any particular object structure, but there are some traits of a well structured app.

```
.
├── app/
│   ├── templates/
│   ├── static/
│   ├── main/
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── __init__.py
│   ├── email.py
│   └── models.py
├── migrations/
├── tests/
│   ├── __init__.py
│   └── test*.py
├── requirements.txt
├── config.py
└── manage.py
```

Basically there are three major parts: application, migrations, tests. They are supported by a configuration and manage script.

I found out that configuration file suits OO paradigm wery well. Configuration can be one class with different settings or many domain specific classes.

#### Application Factory

```
# Flask
from flask import Flask

# Extentions
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

# Configuration
from config import config

mail = Mail()
sqla = SQLAlchemy()

def app_factory(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    sqla.init_app(app)

    # etc

    return app
```

The factory function returns the configured and created application instance.
