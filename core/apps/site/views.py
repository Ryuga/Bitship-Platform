from django.shortcuts import render
from django.views import View
from django.conf import settings
from utils.oauth import Oauth

oauth = Oauth(redirect_uri=settings.OAUTH_REDIRECT_URI, scope="identify%20email")

# OAUTH_URL = oauth.discord_login_url

class IndexView(View):
    template_name = "site/index.html"

    def get(self, request):
        OAUTH_URL = settings.BPD_ENDPOINT
        return render(request, self.template_name, {"oauth_uri": OAUTH_URL})


