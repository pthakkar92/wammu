# Django settings for wammu website project.
# -*- coding: UTF-8 -*-

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Michal Čihař', 'michal@cihar.com'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': './wammu.db',   # Or path to database file if using sqlite3.
        'USER': '',             # Not used with sqlite3.
        'PASSWORD': '',         # Not used with sqlite3.
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

WEB_ROOT = os.path.dirname(os.path.abspath(__file__))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('cs', u'Čeština'),
    ('de', u'Deutsch'),
    ('en', u'English'),
    ('es', u'Español'),
    ('fr', u'Français'),
    ('pt-br', u'Português brasileiro'),
    ('sk', u'Slovenčina'),
)

LOCALE_PATHS = ('%s/locale' % WEB_ROOT, )

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '%s/media/' % WEB_ROOT

HTML_ROOT= '%s/html/' % WEB_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c=kt_6vtz&(418w-0(uti(q5&e76q#lc=%vuwzm&+ulqrkgyp3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wammu.middleware.SiteLocaleMiddleware',
    'wammu.middleware.HTTPHeadersMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'wammu.context_processors.translations',
    'wammu.context_processors.message',
    'wammu.context_processors.dates',
    'wammu.context_processors.feeds',
    'wammu.context_processors.data',
    )

TEMPLATE_DIRS = (
    HTML_ROOT,
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'crispy_forms',
    'news',
    'wammu',
    'downloads',
    'screenshots',
    'links',
    'phonedb',
    'tools',
)

NEWS_PER_PAGE = 5
NEWS_ON_MAIN_PAGE = 5
NEWS_ON_PRODUCT_PAGE = 2
NEWS_IN_RSS = 10
SCREENSHOTS_PER_PAGE = 20
PHONES_PER_PAGE = 50
PHONES_ON_INDEX = 10
PHONES_ON_MAIN_PAGE = 5
PHONES_IN_RSS = 10

THUMBNAIL_SIZE = (180, 180)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SEND_BROKEN_LINK_EMAILS = True
SERVER_EMAIL = 'django@wammu.eu'

CACHE_BACKEND = 'db://cache'

DEFAULT_CONTENT_TYPE = 'application/xhtml+xml'
DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET = 'utf-8'

# Use etags based caching
USE_ETAGS = True

IGNORABLE_404_ENDS = ['logo.png', 'logo_001.png', 'piwik.js', 'piwik.js/', 'piwik.php', 'michal@cihar.com', 'piwik.php/']
IGNORABLE_404_STARTS = ['/plugins/editors/tinymce', '/cgi-bin/']

EMAIL_SUBJECT_PREFIX = '[wammu.eu] '

ALLOWED_HOSTS = [
    'wammu.eu',
    'cs.wammu.eu',
    'de.wammu.eu',
    'es.wammu.eu',
    'fr.wammu.eu',
    'pt-br.wammu.eu',
    'sk.wammu.eu'
]

# Force sane test runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
