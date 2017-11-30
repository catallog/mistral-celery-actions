import base

from celery import signature


class AsyncAction(base.BaseAction):

    def run(self, context):
        signature(self.task_name, kwargs=self.params).delay()

    def is_sync(self):
        return False
