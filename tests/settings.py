MIDDLEWARE_CLASSES = []

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

ROOT_URLCONF = 'wagtail.tests.urls'

SECRET_KEY = 'Gx8sMKAtnA69TR9lyAlLuSnozUv3kxdscHkpwEjatZRVQQ0laMY69KL4XPxvr3KY'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wagtail_factories',
    },
}

INSTALLED_APPS = [
    'wagtail.contrib.wagtailstyleguide',
    'wagtail.contrib.wagtailsitemaps',
    'wagtail.contrib.wagtailroutablepage',
    'wagtail.contrib.wagtailfrontendcache',
    'wagtail.contrib.wagtailapi',
    'wagtail.contrib.wagtailsearchpromotions',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
    'wagtail.wagtailforms',
    'wagtail.wagtailsearch',
    'wagtail.wagtailembeds',
    'wagtail.wagtailimages',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailadmin',
    'wagtail.api.v2',
    'wagtail.wagtailcore',

    'taggit',
    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'tests.testapp',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
