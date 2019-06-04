.. _index:
.. |br| raw:: html

   <br />

Welcome to WALKOFF's documentation!
===================================
This documentation is intended to help app and interface developers as well as provide a reference for project contributors.
Here you’ll find tutorials and information on WALKOFF interface and workflow development as well as application development.
Look below for information on getting started with WALKOFF.


.. _deploying-walkoff-label:

Deploying WALKOFF
------------------------
**Ensure that Python 3.7+, Docker, pip, and git are installed** 

1. Open a terminal on Linux or a command prompt on Windows, and run the command

    .. code-block:: console

            git clone https://github.com/nsacyber/WALKOFF.git

2. Change directories to the WALKOFF directory

    .. code-block:: console

            cd WALKOFF

.. _encryption-label:

3. Create an encryption key

    .. code-block:: console

            python key_creation.py | docker secret create encryption_key -


3.  Perform the following commands to launch WALKOFF in stack mode

        .. code-block:: console

                docker swarm init

        **Note:** If you have multiple NICs you will need to use --advertise-addr to pick an address from which the swarm will be accessible.

        .. code-block:: console

                docker-compose build
                docker stack deploy --compose-file docker-compose.yml walkoff

4. Navigate to the default IP and port. The default IP and the port can be changed in the server. Configuration settings will be saved in the ``common/config.py`` file.


    .. code-block:: console

            localhost:8080

5. Once navigated to the login page, the default username is "admin" and password is "admin." These can and should be changed upon initial login.

6. To shutdown WALKOFF, run the following two commands

    .. code-block:: console

            docker stack rm walkoff
            docker-compose down


|br|

.. toctree::
   :maxdepth: 2
   :caption: Contents:

		Interface Overview <interface.rst>
		Workflow Development <workflow.rst>
		Prepackaged Applications <prepackaged_apps.rst>
		Application Development <apps.rst>
		API Gateway <api.rst>
        Changelog <changelog.rst>

