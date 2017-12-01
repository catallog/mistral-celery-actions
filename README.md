# Mistral Celery Actions


### Installation

First of all, clone the repo and go to the repo directory:

  ```.bash
    git clone https://github.com/collabo-br/mistral-celery-actions.git
    cd mistral-celery-actions
  ```

Local installation:


  ```.bash
    pip install -e .
  ```

Then we need to tell Mistral about them
and restart Mistral::

  ```.bash
    mistral-db-manage populate;
    systemctrl restart openstack-mistral*;
  ```


### Provide celery settings properties on your `mistral.conf` file:


```
[celery]
broker_url = amqp://<user>:<password>@<host>:<port>/mistral
result_backend = amqp://
task_serializer = json
result_serializer = json
```


### Usage

Call celery sync task:

    action: celery.sync-task
    input:
      task_name: 'task.my_custom_task'
      params: 
        task_param1: "Hi, I'm sync"
        task_param2: ...

Call celery async task:

    action: celery.async-task
    input:
      task_name: 'task.my_custom_async_task'
      params:
        task_param1: "Weeeeeeeeeeeee"
        task_param2: ...
        ....


Useful Links
============

* `Mistral`_ <https://github.com/openstack/mistral>
