from oslo_config import cfg

GROUP = 'celery'

CONF = cfg.CONF
CONF.register_opt(cfg.StrOpt('broker_url'), group=GROUP)
CONF.register_opt(cfg.StrOpt('result_backend'), group=GROUP)
CONF.register_opt(cfg.StrOpt('task_serializer'), group=GROUP)
CONF.register_opt(cfg.StrOpt('result_serializer'), group=GROUP)
