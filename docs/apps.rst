.. _apps:

Application Development
========================

I am WALKOFF d

Development Instructions
-------------------------

Write Python Functions in a Standalone Script
''''''''''''''''''''''''''''''''''''''''''''''
Start by developing your app in a standalone script outside of WALKOFF – this way you can get basic functionality down before dealing with WALKOFF.
All functions that you expect to turn into actions must be written with async (i.e. " async def function_name() ")

Port your script into WALKOFF
''''''''''''''''''''''''''''''
* Place your script into the WALKOFF app directory structure, using existing apps (such as the hello_world app directory) as examples.
* Note: Only files under **src** will be copied into the application's Docker container.
* Write an **api.yaml** which describes your app and its functions to WALKOFF.
* Write a requirements.txt which lists any python dependencies your app has. The Dockerfile will use this to pip install dependencies.
* Write a docker-compose.yml which controls how your app’s Docker container will run (at a minimum, it just needs the service name to match)
* If you want directories on your host to be available in the container, you can add volume mounts here.
* Write a Dockerfile which controls how your app will be built. Things to add (see hello_world’s Dockerfile for examples):
* If your app’s Python dependencies require any OS libraries to build
* If your app requires any OS packages to run, install those here
* You can test building your app before running it in WALKOFF: docker build -f apps/app_name/1.0.0/Dockerfile apps/app_name/1.0.0

Naming and String Requirements:
'''''''''''''''''''''''''''''''''
* App name must be snake_case and match in all the following locations:
* App directory, app_name in app.py, name in api.yaml, service name in docker-compose.yml
* Your action names in api.yaml must match the function names they correspond to in app.py
* If your script is not named app.py, the new name must match the command at the end of your Dockerfile



Troubleshooting
----------------
There are several key places to look to debug an application:

1.  **Umpire**
    Following the umpire’s logs (docker service logs -f walkoff_umpire) can give you an indication of whether build issues are happening within the stack. Building an app for the very first time can take a long time.

2.  **Docker Services**
    Watching docker services (watch -n 0.5 docker service ls) can give you an indication of whether your app is running or crashing. At idle with no work, apps and workers will scale to 0/N replicas. If you see something repeatedly scaling up and going to 0, it may be crashing.

3.  **Worker Service Logs**
    Checking the worker service log after the service becomes available for the first time (docker service logs -f worker) will allow you to view the worker logs. Generally apps will not cause problems here, but there may be edge cases missing in scheduling apps.

4.  **App Service Logs**
    Checking the app service log after the service becomes available for the first time (docker service logs -f walkoff_app_app_name) will allow you to view the stdout of your app, as well as any exceptions it might be raising.
	
5.  **App Containers**
    * Obtain app_container_name from docker ps.
    * You can docker exec -it app_container_name /bin/sh into your app container while it is running to check things like network connectivity, the filesystem, or to run your app manually inside it. (If it is crashing on startup, you will need to fix that first or override its starting command with a sleep instead)
    * You can also run the app manually outside of docker entirely: .. include:: ../app_sdk/README.md

