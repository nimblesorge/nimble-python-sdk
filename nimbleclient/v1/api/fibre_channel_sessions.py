#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class FibreChannelSession(Resource):
    """
    Fibre Channel session is created when Fibre Channel initiator connects to this group.

    Parameters:
    - id             : Unique identifier of the Fibre Channel session.
    - initiator_info : Information about the Fibre Channel initiator.
    - target_info    : Information about the Fibre Channel target.
    """

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")

class FibreChannelSessionList(Collection):
    resource = FibreChannelSession
    resource_type = "fibre_channel_sessions"

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
