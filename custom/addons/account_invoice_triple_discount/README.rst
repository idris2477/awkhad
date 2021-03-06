.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================
Account Invoice Triple Discount
===============================

This module allows to have three successive discounts on each invoice line.

Usage
=====

Create a new invoice and add discounts in any of the three discount fields
given. They go in order of precedence so discount 2 will be calculated over
discount 1 and discount 3 over the result of discount 2. For example, let's
divide by two on every discount:

Unit price: 600.00 ->

  - Disc. 1 = 50% -> Amount = 300.00
  - Disc. 2 = 50% -> Amount = 150.00
  - Disc. 3 = 50% -> Amount = 75.00

You can also use negative values to charge instead of discount:

Unit price: 600.00 ->

  - Disc. 1 = 50% -> Amount = 300.00
  - Disc. 2 = -5% -> Amount = 315.00

.. image:: https://awkhad-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.awkhad-community.org/runbot/95/11.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/ACA/account-invoicing/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Awkhad Community Association: `Icon <https://github.com/ACA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* David Vidal <david.vidal@tecnativa.com>
* Pedro M. Baeza <pedro.baeza@tecnativa.com>
* Nikul Chaudhary <nikulchaudhary2112@gmail.com>

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
