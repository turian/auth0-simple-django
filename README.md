# auth0-simple-django

Simple demonstration of auth0 authentication with Django.

NOTE: We should use [signals for token refresh](https://docs.authlib.org/en/latest/client/django.html#auto-update-token-via-signal).

```
pip install -r requirements.txt
```

Then:
```
cd auth0_integration

python manage.py migrate
```

Copy `.env.tmpl` to `.env` and edit it.

Configure auth0. Allowed Callback URLs:
```
http://localhost:8863/callback
```
Allowed Logout URLs:
```
http://localhost:8863/
```

```
python manage.py runserver localhost:8863
```

Visit: `https://localhost:8863`
