# Restful API

Enables a REST API for the Awkhad server. The API has routes to
authenticate and retrieve a token. Afterwards, a set of routes to
interact with the server are provided.

### Documentation

* [Clients]
* [Examples] 
* [Documentation] 
* [Framework]

### Installation

To install this module, you need to:

[Download] the module and add it to your Awkhad addons folder. Afterward,
log on to your Awkhad server and go to the Apps menu. Trigger the debug
mode and update the list by clicking on the "Update Apps List" link. Now
install the module by clicking on the install button.

Another way to install this module is via the package management for
Python ([PyPI]).

To install our modules using the package manager make sure
[awkhad-autodiscover] is installed correctly. Then open a console and
install the module by entering the following command:

`pip install --extra-index-url https://nexus.mukit.at/repository/awkhad/simple <module>`

The module name consists of the Awkhad version and the module name, where
underscores are replaced by a dash.

**Module:**

`awkhad<version>-addon-<module_name>`

**Example:**

`sudo -H pip3 install --extra-index-url https://nexus.mukit.at/repository/awkhad/simple awkhad11-addon-muk-utils`

Once the installation has been successfully completed, the app is
already in the correct folder. Log on to your Awkhad server and go to the
Apps menu. Trigger the debug mode and update the list by clicking on the
"Update Apps List" link. Now install the module by clicking on the
install button.

You can also view available Apps directly in our [repository] and find a
more detailed installation guide on our [website].

### Upgrade

To upgrade this module, you need to:

[Download] the module and add it to your Awkhad addons folder. Restart the
server and log on to your Awkhad server. Select the Apps menu and upgrade
the module by clicking on the upgrade button.

If you installed the module using the "pip" command, you can also update
the module in the same way. Just type the following command into the
console:

`pip install --upgrade --extra-index-url https://nexus.mukit.at/repository/awkhad/simple <module>`

When the process is finished, restart your server and update the
application in Awkhad, just like you would normally.

### Configuration

In case the module should be active in every database just change the
auto install flag to `True`. To activate the routes even if no database
is selected the module should be loaded right at the server start. This
can be done by editing the configuration file or passing a load
parameter to the start script.

Parameter: `--load=web,muk_rest`

To configure this module, you need to:

1.  Go to *Settings -\> Restful API -\> Dashboard*. Here you can see an
    overview of all your APIs.
2.  Click on *Create* or go to either *Restful API -\> OAuth1* or
    *Restful API -\> OAuth2* to create a new API.

### Usage

This module provides a set of routes to interact with the system via
HTTP requests. Take a look at the [clients] and [examples] or open the 
[documentation] to get a detailed description of every available route.

[Clients]: ./clients/clients.md
[Examples]: ./examples/examples.md
[Documentation]: https://app.swaggerhub.com/apis/keshrath/muk_rest/3.0.0
[Framework]: ./framework/framework.md
[Download]: https://apps.awkhad.com/apps/modules/12.0/muk_rest/
[clients]: https://github.com/muk-it/muk_docs/blob/12%2C0/muk_rest/clients/clients.md
[examples]: https://github.com/muk-it/muk_docs/blob/12%2C0/muk_rest/examples/examples.md
[documentation]: https://app.swaggerhub.com/apis/keshrath/muk_rest/docs/3.0.0/
[PyPI]: https://pypi.org/project/pip/
[awkhad-autodiscover]: https://pypi.org/project/awkhad-autodiscover/
[repository]: https://nexus.mukit.at/#browse/browse:awkhad
[website]: https://mukit.at/page/open-source
[MuK IT]: https://www.mukit.at/