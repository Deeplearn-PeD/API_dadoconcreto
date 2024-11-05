"""
Django settings for dadoconcreto_api project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1ybsqf19u=^i7a@$wj$f)f(t1q(7rdku0n*s!nrnt6emujs)c4"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dadoconcreto_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dadoconcreto_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "gdelt": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gdelt',
        'USER': 'postgres',
        'PASSWORD': 'eueueu',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Events(models.Model):
    globaleventid = models.BigIntegerField(primary_key=True, db_column='GLOBALEVENTID')
    sqldate = models.DateField(db_column='SQLDATE', blank=True, null=True)
    monthyear = models.IntegerField(db_column='MonthYear', blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    fractiondate = models.FloatField(db_column='FractionDate', blank=True, null=True)
    actor1code = models.CharField(db_column='Actor1Code', max_length=50, blank=True, null=True)
    actor1name = models.CharField(db_column='Actor1Name', max_length=255, blank=True, null=True)
    actor1countrycode = models.CharField(db_column='Actor1CountryCode', max_length=3, blank=True, null=True)
    actor1knowngroupcode = models.CharField(db_column='Actor1KnownGroupCode', max_length=50, blank=True, null=True)
    actor1ethniccode = models.CharField(db_column='Actor1EthnicCode', max_length=50, blank=True, null=True)
    actor1religion1code = models.CharField(db_column='Actor1Religion1Code', max_length=50, blank=True, null=True)
    actor1religion2code = models.CharField(db_column='Actor1Religion2Code', max_length=50, blank=True, null=True)
    actor1type1code = models.CharField(db_column='Actor1Type1Code', max_length=50, blank=True, null=True)
    actor1type2code = models.CharField(db_column='Actor1Type2Code', max_length=50, blank=True, null=True)
    actor1type3code = models.CharField(db_column='Actor1Type3Code', max_length=50, blank=True, null=True)
    actor2code = models.CharField(db_column='Actor2Code', max_length=50, blank=True, null=True)
    actor2name = models.CharField(db_column='Actor2Name', max_length=255, blank=True, null=True)
    actor2countrycode = models.CharField(db_column='Actor2CountryCode', max_length=3, blank=True, null=True)
    actor2knowngroupcode = models.CharField(db_column='Actor2KnownGroupCode', max_length=50, blank=True, null=True)
    actor2ethniccode = models.CharField(db_column='Actor2EthnicCode', max_length=50, blank=True, null=True)
    actor2religion1code = models.CharField(db_column='Actor2Religion1Code', max_length=50, blank=True, null=True)
    actor2religion2code = models.CharField(db_column='Actor2Religion2Code', max_length=50, blank=True, null=True)
    actor2type1code = models.CharField(db_column='Actor2Type1Code', max_length=50, blank=True, null=True)
    actor2type2code = models.CharField(db_column='Actor2Type2Code', max_length=50, blank=True, null=True)
    actor2type3code = models.CharField(db_column='Actor2Type3Code', max_length=50, blank=True, null=True)
    isrootevent = models.IntegerField(db_column='IsRootEvent', blank=True, null=True)
    eventcode = models.CharField(db_column='EventCode', max_length=50, blank=True, null=True)
    eventbasecode = models.CharField(db_column='EventBaseCode', max_length=50, blank=True, null=True)
    eventrootcode = models.CharField(db_column='EventRootCode', max_length=50, blank=True, null=True)
    quadclass = models.IntegerField(db_column='QuadClass', blank=True, null=True)
    goldsteinscale = models.FloatField(db_column='GoldsteinScale', blank=True, null=True)
    nummentions = models.IntegerField(db_column='NumMentions', blank=True, null=True)
    numsources = models.IntegerField(db_column='NumSources', blank=True, null=True)
    numarticles = models.IntegerField(db_column='NumArticles', blank=True, null=True)
    avgtone = models.FloatField(db_column='AvgTone', blank=True, null=True)
    actor1geo_type = models.IntegerField(db_column='Actor1Geo_Type', blank=True, null=True)
    actor1geo_fullname = models.CharField(db_column='Actor1Geo_FullName', max_length=255, blank=True, null=True)
    actor1geo_countrycode = models.CharField(db_column='Actor1Geo_CountryCode', max_length=2, blank=True, null=True)
    actor1geo_adm1code = models.CharField(db_column='Actor1Geo_ADM1Code', max_length=4, blank=True, null=True)
    actor1geo_lat = models.FloatField(db_column='Actor1Geo_Lat', blank=True, null=True)
    actor1geo_long = models.FloatField(db_column='Actor1Geo_Long', blank=True, null=True)
    actor1geo_featureid = models.CharField(db_column='Actor1Geo_FeatureID', max_length=50, blank=True, null=True)
    actor2geo_type = models.IntegerField(db_column='Actor2Geo_Type', blank=True, null=True)
    actor2geo_fullname = models.CharField(db_column='Actor2Geo_FullName', max_length=255, blank=True, null=True)
    actor2geo_countrycode = models.CharField(db_column='Actor2Geo_CountryCode', max_length=2, blank=True, null=True)
    actor2geo_adm1code = models.CharField(db_column='Actor2Geo_ADM1Code', max_length=4, blank=True, null=True)
    actor2geo_lat = models.FloatField(db_column='Actor2Geo_Lat', blank=True, null=True)
    actor2geo_long = models.FloatField(db_column='Actor2Geo_Long', blank=True, null=True)
    actor2geo_featureid = models.CharField(db_column='Actor2Geo_FeatureID', max_length=50, blank=True, null=True)
    actiongeo_type = models.IntegerField(db_column='ActionGeo_Type', blank=True, null=True)
    actiongeo_fullname = models.CharField(db_column='ActionGeo_FullName', max_length=255, blank=True, null=True)
    actiongeo_countrycode = models.CharField(db_column='ActionGeo_CountryCode', max_length=2, blank=True, null=True)
    actiongeo_adm1code = models.CharField(db_column='ActionGeo_ADM1Code', max_length=4, blank=True, null=True)
    actiongeo_lat = models.FloatField(db_column='ActionGeo_Lat', blank=True, null=True)
    actiongeo_long = models.FloatField(db_column='ActionGeo_Long', blank=True, null=True)
    actiongeo_featureid = models.CharField(db_column='ActionGeo_FeatureID', max_length=50, blank=True, null=True)
    dateadded = models.DateField(db_column='DATEADDED', blank=True, null=True)
    sourceurl = models.TextField(db_column='SOURCEURL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'
