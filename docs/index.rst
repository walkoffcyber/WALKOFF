.. WALKOFF documentation master file, created by
   sphinx-quickstart on Thu May 30 16:51:18 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to WALKOFF's documentation!
===================================
Welcome to Walkoff’s Python documentation. If you are looking for documentation and tutorials on getting started with Walkoff, please first look at our Github Pages site. Here you’ll find tutorials and documentation on both UI usage and app and interface development. This documentation is intended to help app and interface developers as well as provide a reference for project contributors.


Deploying WALKOFF
------------------------
**Ensure that Python 3.7+, Docker, pip, and git are installed** 

1. Open a terminal on Linux or a command prompt on Windows, and run the command

.. code-block:: bash

		git clone https://github.com/nsacyber/WALKOFF.git

2. Change directories to the WALKOFF directory

.. code-block:: bash

		cd WALKOFF

3. To launch WALKOFF, perform the following commands

.. code-block:: bash

		docker swarm init
		docker-compose build
		docker stack deploy --compose-file docker-compose.yml walkoff

4. Navigate to the default IP and port.

.. code-block:: bash
		
		localhost:8080

the default IP and the port can be changed in the server. Configuration settings will be saved in the data/walkoff.config file.

5. Once navigated to the login page, the default username is "admin" and password is "admin." These can and should be changed upon initial login.

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents:

		Interface Overview <interface.rst>
		Workflow Development <workflow.rst>
		Prepackaged Applications <prepackaged_apps.rst>
		Application Development <apps.rst>
		Api Gateway <api.rst>



Change Log
--------------

