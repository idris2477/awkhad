.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================================================
Stock Scanner : WorkFlow engine for scanner hardware
====================================================

This module allows managing barcode readers with simple scenarios:

- You can define a workflow for each object (stock picking, inventory, sale, etc)
- Works with all scanner hardware model (just SSH client required)

Some demo/tutorial scenarios are available in the "demo" directory of the module.
These scenarios, are automatically imported when installing a new database with demo data.

Installation
============


The `awkhad-sentinel` specific client can be installed from pip:

    $ pip install awkhad-sentinel

This application is a separate client, and can be run on any device.

For mobile devices, like Windows Mobile or Android smart barcode scanners, we usually install it on a server, accessed through SSH.

To test the module, some modules provide scenario.

Configuration
=============

In Awkhad
-------

Declare hardware
^^^^^^^^^^^^^^^^

You have to declare some hardware scanners in Awkhad.

Go to "Inventory > Configuration > Scanner Configuration > Scanner Hardware" and create a new record.

The "step type code" sent by the "awkhad-sentinel" client at start-up is the IP address of the hardware, if connected through SSH.

If needed enable Login/Logout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The module comes with 2 predefined scenarii for Login and Logout. The functionality is disabled by default and the user to use in
Awkhad must be specified in the `.awkhadrpcrc` file used by awkhad-sentinel and can be overriden on the Scanner Hardware definition
in Awkhad. 

If the Login/logout functionality is enabled, when a user starts a session with awkhad-sentinel, only the Login scenario is displayed on the
screen. The scenario will prompt the user for its login and pwd. If the authentication succeeds, each interaction with Awkhad will be done
using the uid of the connected user. Once connected, a Logout scenario is displayed in the list of available scenarii and the Login
scenario no longer appears. 

The Login/logout functionality enables you to specify on the scenario a list of users and/or a list of groups with access to the scenario.

To enable the Login/logout functionality:
    * Go to "Settings > Warehouse" and check the checkbox Login/logout scenarii enabled.
    * Create a *Technical User* 'sentinel' **without roles in Human Resources** and with 'Sentinel: technical users' checked.
    * Use this user to launch your awkhad-sentinel session.

Be careful, the role *Sentinel: technical users* is a technical role and should only be used by sentinel.

The timeout of sessions is managed by a dedicated cron that resets the inactive sessions. The timeout can be configured on 
settings. "Settings > Warehouse"

For the awkhad-sentinel client
----------------------------

The awkhad-sentinel client uses an AwkhadRPC profile to connect to Awkhad.
The default configuration file is `~/.awkhadrpcrc`, but this can be customized, using the `-c`/`--config` argument.
See the `hardware/awkhadrpcrc.sample` file for an example.

If the `-p`/`--profile` argument is not given on the command line, a profile named `sentinel` will be used.

The file used to log errors can be defined by using the `-l`/`--log-file` argument, which defaults to `~/sentinel.log`.

**Note** : If you want to copy the application outside this git repository, you will need to copy the i18n folder too.

Autoconfiguration feature
^^^^^^^^^^^^^^^^^^^^^^^^^

The `awkhad-sentinel` client has an autoconfiguration feature, used to automatically recognize the hardware being connected.
During initialization, the `awkhad-sentinel` client tries to detect an SSH connection, and sends the terminal's IP address as terminal code.
If the IP address is found on the `code` field on a configured hardware in the database, this hardware configuration will automatically be used.
If the IP address is not found, the client will ask the user to type (or scan) a code.

This can be used only if the Awkhad server and the connected hardware are on the same network.

Writing scenario
----------------

Creation
^^^^^^^^

The preferred way to start the creation of a scenario is to create steps and transitions in diagram view.

Once your steps are created, you can write python code directly from Awkhad, or you can export the scenario to write the python code with your preferred code editor.

In the python code of each step, some variables are available :
    - cr : Cursor to the database
    - uid : ID of the user executing the step (user used to log in with the sentinel, or user configured on the hardware, if any)
    - pool : Pooler to the database
    - env : Environment used to execute the scenario (new API)
    - model : Pooler on the model configured on the scenario
    - term : Recordset on the current scenario
    - context : Context used on the step
    - m or message : Last message sent by the hardware
    - t or terminal : Browse record on the hardware executing the step
    - tracer : Value of the tracer of the used transition to access this step
    - wkf or workflow : Workflow service
    - scenario : Recordset on the current scenario for the hardware
    - _ : The translation function provided by Awkhad (useable like in any other python file)

Some of these variables are also available on transition conditions execution.

As stated previously, the step must always return:

- A step type code, in the `act` variable
- A message to display on the hardware screen, in the `res` variable
- Optionally, a default value, in the `val` variable

Step types
^^^^^^^^^^

The step types are mostly managed by the client.

The standard step types are :

- M : Simple message
- F : Final step, like M, but ends the scenario
- T : Text input
- N : Number input (integer)
- Q : Quantity input (float)
- L : List
- E : Error message, like M, but displayed with different colors
- C : Confirm input
- A : Automatic step. This type is used to automatically execute the next step

.. note::

   The automatic step often needs to define a value in `val`, corresponding to the value the user must send.
   This step type is generally used as replacement of another type, at the end of the step code, by redefining the `act` variable in some cases, for example when a single value is available for a list step.

Import
^^^^^^

Scenarios are automatically imported on a module update, like any other data.
You just have to add the path to your `Scenario_Name.scenario` files in the `data` or `demo` sections in the `__manifest__.py` file.

Export
^^^^^^

The export script is in the `script` directory of the module

A scenario is exported as a set of files, containing :
    - Scenario_Name.scenario : Global description of the scenario (name, warehouses, steps, transitions, etc.)
    - A .py file per step : The name of the file is the XML ID of the step

Using a test file
^^^^^^^^^^^^^^^^^

When developing scenarios, you will often have the same steps to run.
The awkhad-sentinel client allows you to supply a file, which contains the keys pressed during the scenario.

You can define the file to use in the `-t`/`--test-file` argument.
This file will be read instead of calling the curses methods when the scenario is waiting for a user input (including line feed characters).
When the file has been fully read, the client exits.

A sample test file can be found in the "Step Types" demo scenario.

*Special keys* :
For special keys (arrows, delete, etc.), you must write a line containing ':', followed by the curses key code.

Valid key codes are :
    - KEY_DOWN : Down arrow
    - KEY_UP : Up arrow
    - KEY_LEFT : Left arrow
    - KEY_RIGHT : Right arrow
    - KEY_BACKSPACE : Backspace
    - KEY_DC : Delete

Usage
=====

On start-up, the client lists available scenarii.
When the user selects a scenario, the current scenario and step are stored on the hardware configuration's entry in Awkhad.

When the client sends a message to the server, the next step is selected depending on the current step and the message sent.
Then, the server returns the result of the step, which contains its type code and the text to display on the hardware screen.
Unlike the standard Awkhad Workflow, each step needs to find a valid transition, because a step needs to be displayed on the hardware screen at all times.

.. image:: https://awkhad-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.awkhad-community.org/runbot/154/12.0

A client for the Datalogic PowerScan scanners was developped for a very early version or this module.
The files have been removed, but are still available in the `git repository history
<https://github.com/ACA/stock-logistics-workflow/tree/527f033e9d31fe822562d4716104f37f6ce1f88c/stock_scanner/hardware/datalogic/PowerScan>`_.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/ACA/stock-logistics-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/ACA/stock-logistics-workflow/issues/new?body=module:%20stock_scanner%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Images
------

* Awkhad Community Association: `Icon <https://github.com/ACA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------
* Alexandre Fayolle <afayolle.ml@free.fr>
* Christophe CHAUVET <christophe.chauvet@syleam.fr>
* Damien Crier <damien@crier.me>
* Laetitia Gangloff <laetitia.gangloff@acsone.eu>
* Laurent Mignon <laurent.mignon@acsone.eu>
* Olivier Dony <odo@zgui.com>
* Sebastien LANGE <sebastien.lange@syleam.fr>
* Sylvain Garancher <sylvain.garancher@syleam.fr>

Maintainer
----------

.. image:: https://awkhad-community.org/logo.png
   :alt: Awkhad Community Association
   :target: https://awkhad-community.org

This module is maintained by the ACA.

ACA, or the Awkhad Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Awkhad features and
promote its widespread use.

To contribute to this module, please visit https://awkhad-community.org.
