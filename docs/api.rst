API Gateway
========================

apps
-----

.. openapi:: swagger_api.yaml
    :paths:
        /apps
        /apps/apis
        /apps/apis/{app}


auth
------
.. openapi:: swagger_api.yaml
    :paths:
        /auth
        /auth/refresh
        /auth/logout


configuration
--------------
.. openapi:: swagger_api.yaml
    :paths:
        /configuration


globals
--------
.. openapi:: swagger_api.yaml
    :paths:
        /globals
        /globals/{global_var}
        /globals/templates
        /globals/templates/{global_template}


roles
------
.. openapi:: swagger_api.yaml
    :paths:
        /roles


scheduler
-----------
.. openapi:: swagger_api.yaml
    :paths:
        /scheduler


users
------
.. openapi:: swagger_api.yaml
    :paths:
        /users


workflows
----------
.. openapi:: swagger_api.yaml
    :paths:
        /workflows


dashboards
-----------
.. openapi:: swagger_api.yaml
    :paths:
        /dashboards