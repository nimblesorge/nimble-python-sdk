#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class DebugLog(Resource):
    """
    Method to help log events from outside of storage array to provide context for troubleshooting host-side or array-side issues.

    Parameters:
    - level   : Log level.
    - tag     : Specifies the context of the message.
    - message : The message to log.
    """

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")

class DebugLogList(Collection):
    resource = DebugLog
    resource_type = "debug_log"

    def create(self, **kwargs):
        resp = self._client.create_resource(self.resource_type, **kwargs)
        return self.resource(resp['id'], resp, client=self._client, collection=self)

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
