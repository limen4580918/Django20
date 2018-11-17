"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# 导入操作系统模块
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# os.path.abspath:表示绝对路径; abspath()函数可以获取到当前文件的绝对路径
# __file__:表示当前文件  ;  dirname()函数可以获取到上一级的路径
# 项目根目录<根路径>
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 所以这里取到当前文件的上一层的上一层文件路径
# print(BASE_DIR) # 这里可以看出BASE_DIR取到的是项目的根目录

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# django默认给我们准备好的密钥,将来作某些功能需要用来签名计算
SECRET_KEY = 'o513t3kokt%tjh&nz1utx4h1j_*kr*inkq_5s887#y9t35&=#o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 表示允许哪些host<主机>访问此程序; allowed允许的意思
ALLOWED_HOSTS = []

# Application definition
#  将自己创建的子应用的配置信息文件apps.py中的Config类 添加到INSTALLED_APPS列表中,表示注册安装子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 将子应用的配置信息文件apps.py中的Config类添加到INSTALLED_APPS列表中
    # '子应用名.apps.子应用名Config'
    # 注册安装子应用;
    'user.apps.UserConfig',  # 注意后面的逗号别落下

    'request_response.apps.RequestResponseConfig',  # 这是在安装第二个子应用
    'classview.apps.ClassviewConfig',  # 注册classview这个子应用
]

# 中间件<类似Flask的请求勾子>
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Django默认开启了CSRF防护,会对POST、PUT、PATCH、DELETE请求方式进行CSRF防护验证,测试时可以手动注释掉下面这行代码
    # 'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 添加到列表后,这个自定义中间件就可以监听到工程中任何请求和响应
    'middleware.my_middleware1',  # 自定义中间件
    'middleware.my_middleware2',
]

#  指定项目总路由(根路由)的地址为 demo.urls
ROOT_URLCONF = 'demo.urls'

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

# 部署上线后程序启动的入口
WSGI_APPLICATION = 'demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库配置项:默认是sqlite3 将来上线后换成MySQL
DATABASES = {
    'default': {
        # django默认使用的数据库是sqlite3,现在我们需要用到mysql
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'django_demo' # 使用的数据库的名字
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 验证密码规则
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

# 默认初始化的工程默认语言是英语
# LANGUAGE_CODE = 'en-us'
# 设置工程默认语言中文
LANGUAGE_CODE = 'zh-hans'

# 默认初始化的工程默认时区是格林威治时间
# TIME_ZONE = 'UTC'
# 设置工程默认时区为中国上海
TIME_ZONE = 'Asia/Shanghai'

# 18表示中间省略了18个字母
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# 下面这两行代码用来配置 存放静态文件的 文件夹路径;
# 默认设置的访问静态文件的路由前缀;
STATIC_URL = '/static/'
# 参数BASE_DIR表示根路径<见第20行>; 参数static_files表示项目根路径下的static_files文件夹
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files')
]

# 配置redis数据库<自己加的>  CACHES缓存的意思
CACHES = {
    "default": {
        # 后端 :     django_redis 的缓存 用redis来缓存
        "BACKEND": "django_redis.cache.RedisCache",
        # 缓存的地址   最后的数字表示启用哪个redis数据库<这里是用1号数据库>
        "LOCATION": "redis://127.0.0.1:6379/1",
        # 选项
        "OPTIONS": {
            # 客户端类,表示你要用哪个客户端<这里指定的django_redis>来操作redis来存
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# session的引擎    用django下的contrib下的sessions下的后端缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# 设置缓存的别名  也就是上面的default
SESSION_CACHE_ALIAS = "default"
