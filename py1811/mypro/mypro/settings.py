"""
Django settings for mypro project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 封装好的基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ohf-9evjb_iy1nqmh6qkwiviun2zslcw4mgjt-%=4ux^$_5#yw'

# SECURITY WARNING: don't run with debug turned on in production!
# 上线之后改为false
DEBUG = True

# 主机IP地址设置，设置多个用逗号隔开
# ALLOWED_HOSTS = ["192.168.15.40",]
# 匹配所有，通用（不建议使用）
ALLOWED_HOSTS = ["*"]

# Application definition
# 子模块应用加入
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
    'tinymce',
]
# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # csrf_token中间件
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路径位置
ROOT_URLCONF = 'mypro.urls'
# MVT中的T，公用的模板路径设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 目录
        'DIRS': ["temp"],
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
# 服务器直接起作用
WSGI_APPLICATION = 'mypro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE                         _DIR, 'db.sqlite3'),
        'NAME': 'qiku',
        'USER': 'lzj',
        'PASSWORD': '123456',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# 后台管理
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 后台管理平台语言显示
LANGUAGE_CODE = 'zh-Hans'
# 时间设置
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态文件的路径js, css
# 子模板静态资源
STATIC_URL = '/static/'

# 全局共用的静态资源的设置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# 让后台显示富文本编辑器的设置
TINYMCE_JS_URL = "/static/tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = "/static/tiny_mce/"
TINYMCE_DEFAULT_CONFIG = {
	'theme': "advanced",
	 'width': 600,
	 'height': 400,
}
