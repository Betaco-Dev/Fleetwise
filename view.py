from django.contrib.auth.views import LoginView
from ratelimit.decorators import ratelimit

class RateLimitedLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
