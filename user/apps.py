from django.apps import AppConfig

# 这个文件里面存放的是每个所在子应用的配置信息;
# 例如这里放的就是user这个子应用的配置信息
class UserConfig(AppConfig):
    name = 'user'
