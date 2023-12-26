import logging
import os
from urllib.parse import urlencode

from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

logging.basicConfig(level=logging.DEBUG)

oauth = OAuth()

auth0 = oauth.register(
    "auth0",
    **settings.AUTHLIB_OAUTH_CLIENTS["auth0"],
)


def login(request):
    logging.debug("Initiating login process")
    redirect_uri = "http://localhost:8863/callback"  # Change the port as needed
    logging.debug(f"Redirect URI: {redirect_uri}")
    return auth0.authorize_redirect(request=request, redirect_uri=redirect_uri)


def callback_handling(request):
    try:
        logging.debug(f"Request object: {request}")

        token = auth0.authorize_access_token(request=request)

        userinfo = token["userinfo"]

        # Manually authenticate the user based on Auth0 information
        User = get_user_model()
        user, created = User.objects.get_or_create(username=userinfo["email"])
        logging.debug(f"User: {user}, created: {created}")

        if created:
            # You can populate additional user fields here if needed
            pass

        # Log the user in using Django's authentication system
        r = django_login(request, user)
        logging.debug(f"django_login: {r}")

        request.session["profile"] = {
            "user_id": userinfo["sub"],
            "name": userinfo["name"],
            "picture": userinfo["picture"],
            "email": userinfo["email"],
            "email_verified": userinfo["email_verified"],
        }
        return redirect("dashboard")
    except Exception as e:
        # Debug: Print the error message and traceback
        logging.error("Error in callback handling", exc_info=True)
        return HttpResponse(str(e))


@login_required
def dashboard(request):
    return HttpResponse(
        f'Your email: {request.session["profile"].get("name")} '
        f'<br><img src="{request.session["profile"].get("picture")}">'
        '<br><a href="/logout">Logout</a>'
    )


def logout(request):
    request.session.clear()
    params = {
        "returnTo": "http://localhost:8863",  # Change the port as needed
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
    }
    return redirect(os.getenv("AUTH0_BASE_URL") + "/v2/logout?" + urlencode(params))


def home(request):
    if "profile" in request.session:
        logging.debug(os.environ)
        return redirect("dashboard")
    else:
        return redirect("login")
