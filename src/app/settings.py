DEBUG = False
# This public stateless example accepts any deployment hostname. No sessions,
# cookies, signing, auth, admin, or database are enabled; no secret is required.
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "app.urls"
INSTALLED_APPS = []
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware"]
DATABASES = {}
USE_I18N = False
USE_TZ = True
SECURE_CONTENT_TYPE_NOSNIFF = True
