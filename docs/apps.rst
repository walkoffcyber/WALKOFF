Application Development
========================

I am WALKOFF d

Development Instructions
-------------------------

Troubleshooting
----------------
There are several key places to look to debug an application.
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
    * You can also run the app manually outside of docker entirely:


