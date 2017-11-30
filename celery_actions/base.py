from mistral_lib.actions import base
from celery import Celery, signature
from oslo_config import cfg

CONF = cfg.CONF

celery_settings = {
    'BROKER_URL': CONF.celery.broker_url,
    'CELERY_RESULT_BACKEND': CONF.celery.result_backend,
    'CELERY_TASK_SERIALIZER': CONF.celery.task_serializer,
    'CELERY_RESULT_SERIALIZER': CONF.celery.result_serializer
}


class CeleryConfig(object):
    def __init__(self):
        self.celery_app = Celery()
        self.celery_app.config_from_object(celery_settings)


class BaseAction(CeleryConfig, base.Action):
    def __init__(self, task_name, params):
        super(BaseAction, self).__init__()
        self.task_name = task_name
        self.params = params

    def run(self, context):
        result = signature(self.task_name, kwargs=self.params).delay()
        return result.get()
