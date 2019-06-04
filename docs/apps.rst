.. _apps:

.. |br| raw:: html

   <br />

Application Development
========================

Development Instructions
-------------------------

**1. Write Python Functions in a Standalone Script**
    * Start by developing your app and its functions in a standalone script outside of WALKOFF – this way you can get basic functionality down before dealing with WALKOFF.
    * **Note:** all functions that you expect to turn into actions must be written asynchronously (i.e. ``async def function_name()``)

**2. Create a Package in the Apps directory of WALKOFF**
    *  **Note:** The package name must be in ``snake_case`` and should have the same name as the app you want to create
    * Within the new application package, store all files within a version folder (i.e. "1.0.0")
    * Place your developed app script into a ``src`` folder within the version folder.
    * Only files under ``src`` will be copied into the application's Docker container.

**3. Create an ``api.yaml`` YAML metadata file to convert methods to actions**
    * For WALKOFF to recognize a function as an action, it must have an entry in the apps's ``api.yaml`` file
    * Place this file at the same level as the ``src`` directory
    * Note:
        * The top-level name of the action in this file must match exactly the "run" field of the action in the source file
        * You must include ``name``, ``app_version``, and ``actions`` in this file.

**4. Include a ``requirements.txt``**
    * This file should include any python dependencies your app contains
    * Place this file at the same level as the ``src`` directory
    * The Dockerfile will use this to pip install dependencies

**5. Create a ``docker-compose`` YAML file**
    * This will control how your app’s Docker container will run.
    * Place this file at the same level as the ``src`` directory
    * At a minimum, utilize the ``hello_world`` application's ``docker-compose.yml`` and simply change the service name to match that of your new application.
        * **Note:** If you want directories on your host to be available in the container, you can add volume mounts here.

**6. Create a ``Dockerfile``**
    * This will control how your app will be built.
    * See ``hello_world’s Dockerfile`` for a detailed, step-by-step example on how to create your own ``Dockerfile``
    * If your application's python dependencies require any OS libraries to build or if your application required any OS packages to run, include them in this file.
    * You can test building your app with the Dockerfile before running it in WALKOFF:

.. code-block:: console

        docker build -f apps/app_name/1.0.0/Dockerfile apps/app_name/1.0.0


Developing Conditions and Triggers
''''''''''''''''''''''''''''''''''''
**Develop a Condition**
**Develop a Trigger**

Naming and String Requirements:
'''''''''''''''''''''''''''''''''
    * App name must be ``snake_case`` and match in all the following locations:
        #. app directory
        #. app_name in ``app.py``
        #. app_name in ``api.yaml``
        #. service name in ``docker-compose.yml``
    * Your action names in ``api.yaml`` must match the function names they correspond to in ``app.py``
    * If your script is not named ``app.py``, the new name must match the command at the end of your ``Dockerfile``

|br|
|br|
|br|

Troubleshooting
----------------
There are several key places to look to debug an application:

1.  **Umpire**
    |br| Following the umpire’s logs (docker service logs -f walkoff_umpire) can give you an indication of whether build issues are happening within the stack. Building an app for the very first time can take a long time.

2.  **Docker Services**
    |br| Watching docker services (watch -n 0.5 docker service ls) can give you an indication of whether your app is running or crashing. At idle with no work, apps and workers will scale to 0/N replicas. If you see something repeatedly scaling up and going to 0, it may be crashing.

3.  **Worker Service Logs**
    |br| Checking the worker service log after the service becomes available for the first time (docker service logs -f worker) will allow you to view the worker logs. Generally apps will not cause problems here, but there may be edge cases missing in scheduling apps.

4.  **App Service Logs**
    |br| Checking the app service log after the service becomes available for the first time (docker service logs -f walkoff_app_app_name) will allow you to view the stdout of your app, as well as any exceptions it might be raising.
	
5.  **App Containers**|br|
    * Obtain app_container_name from docker ps.
    * You can docker exec -it app_container_name /bin/sh into your app container while it is running to check things like network connectivity, the filesystem, or to run your app manually inside it. (If it is crashing on startup, you will need to fix that first or override its starting command with a sleep instead)
    * You can also run the app manually outside of docker entirely: `APP SDK <https://github.com/nsacyber/WALKOFF/tree/1.0.0-alpha.1/app_sdk>`_.

