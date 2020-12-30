from django.apps import AppConfig


class CmsConfig(AppConfig):
    name = 'cms'
    verbose_name = 'CMS'

    def ready(self):
        super(CmsConfig, self).ready()
        from . import checks