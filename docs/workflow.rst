.. _workflow_dev:

.. |br| raw:: html

  <br />
  
Workflow Development
====================
Below you can find information about how to create a workflow as well as the tools that are available to you as a user.

Workflow Creation
-----------------
In this tutorial, we will create our first, basic workflow in order to demonstrate the general features of the workflow editor.


Create Global
'''''''''''''
	Before we create a workflow, we will create a global that our actions will use.
	
	In the top navigation bar, click on "Globals", then "Add Global". Fill out the required fields for this example and set the value to an integer between 1-10. Then click "Save" in the dialog box. If nothing is populated in the globals table then verify that you created your encryption key by going to 
	:ref:`encryption-label`.
	
.. image:: ../docs/images/create_global.png

Create Workflow
'''''''''''''''
	In the top navigation bar, click "Workflows" to return to the main Workflow page. Then, near the top of the page, click the "Create New" button. Here you can enter a name for a new workflow. Once you enter the name and have filled out the other fields (optional) click "Continue"
.. image:: ../docs/images/create_workflow.png
	
Add Actions to Workspace
''''''''''''''''''''''''
	Let's begin by adding a Hello World action and a Pause action from the HelloWorld app. Expand the HelloWorld app by clicking on the app name in the left pane. Then, double-click, or click and drag the desired actions into the workspace.
	
	Ensure that the Hello World action is set as the starting node by clicking "Set as Start Action" in the Action Parameters pane.
.. image:: ../docs/images/add_actions.png

Configure Options
'''''''''''''''''
	Some actions will have inputs; some required, some optional. In this case, the pause action requires a parameter, but the hello_world action does not. Set the pause parameter's type to "global" from the dop down and select the global that you created in the previous examples. The global that you set is the amount of time that the pause action will pause for.
	
	Finally, connect the actions together by clicking and dragging from the top of the hello_world action to the top of the pause action.
.. image:: ../docs/images/configuration.png

Save and Execute Workflow
'''''''''''''''''''''''''
	Use the Save button and the Execute button in the toolbar.
.. image:: ../docs/images/save_and_execute.png



Examine Results:
''''''''''''''''
	Now you can either check the results of your workflow under the 'Execution' tab below your workflow, or you can navigate to the 'Execution' tab at the top of the screen for a more organized view of your app. If everything was configured properly you can expect to see results identical to what is shown below.
.. image:: ../docs/images/results.PNG

|br|

Workflow Editor
---------------
In this tutorial, we will explore the different components of the Workflow Editor interface.

Toolbar:
''''''''
From left to right, the buttons in the toolbar are: 

+-----------------------+-----------------------------------------------+
|   Save Workflow       | Saves current workflow under specified name	|
+-----------------------+-----------------------------------------------+
|        Undo	       	| Reverts the most recent change in the editor	|
+-----------------------+-----------------------------------------------+
|        Redo	       	|   Reapplies the most recent undone action	|
+-----------------------+-----------------------------------------------+
| Delete Selected Nodes	|    Deletes the selected Action or Edge	|
+-----------------------+-----------------------------------------------+
|        Copy		|        Copies the selected Action		|
+-----------------------+-----------------------------------------------+
|        Paste		|  Pastes the previously copied or cut Action	|
+-----------------------+-----------------------------------------------+
|    Execute Workflow	|  Schedules the Workflow to run immediately	|
+-----------------------+-----------------------------------------------+
| Clear Execution 	|   Clears the green/ red highlighting of 	|
| Results		|   executed actions				|
+-----------------------+-----------------------------------------------+
|    Edit Description	|  Allows you to edit the description of the 	|
|			|  workflow you are currently working on	|
+-----------------------+-----------------------------------------------+
|    Create Variable	| Creates workflow variabe that is local to the	|
|			| workflow you are currently working on		|
+-----------------------+-----------------------------------------------+
