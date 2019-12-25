# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from awkhad.exceptions import UserError


class ConnectionFailedError(UserError):
    pass


class ConnectionSuccessError(UserError):
    pass
