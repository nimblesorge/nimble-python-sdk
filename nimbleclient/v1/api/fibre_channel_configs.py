#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class FibreChannelConfig(Resource):
    """
    Manage group wide Fibre Channel configuration.

    Parameters:
    - id                 : Identifier for Fibre Channel configuration.
    - array_list         : List of array Fibre Channel configs.
    - group_leader_array : Name of the group leader array.
    """

    def regenerate(self, precheck, wwnn_base_str):
        """
        Regenerate Fibre Channel configuration.

        Parameters:
        - id            : ID of the Fibre Channel configuration.
        - wwnn_base_str : Base World Wide Node Name(WWNN).
        - precheck      : Check if the interfaces are offline before regenerating the WWNN (World Wide Node Name).
        """

        return self.collection.regenerate(self.id, precheck, wwnn_base_str)

    def hw_upgrade(self):
        """
        Update Fibre Channel configuration after hardware changes.

        Parameters:
        - id : ID of the Fibre Channel configuration.
        """

        return self.collection.hw_upgrade(self.id)

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")

class FibreChannelConfigList(Collection):
    resource = FibreChannelConfig
    resource_type = "fibre_channel_configs"

    def regenerate(self, id, precheck, wwnn_base_str):
        """
        Regenerate Fibre Channel configuration.

        Parameters:
        - id            : ID of the Fibre Channel configuration.
        - wwnn_base_str : Base World Wide Node Name(WWNN).
        - precheck      : Check if the interfaces are offline before regenerating the WWNN (World Wide Node Name).
        """

        return self._client.perform_resource_action(self.resource_type, id, 'regenerate', id=id, precheck=precheck, wwnn_base_str=wwnn_base_str)

    def hw_upgrade(self, id):
        """
        Update Fibre Channel configuration after hardware changes.

        Parameters:
        - id : ID of the Fibre Channel configuration.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'hw_upgrade', id=id)

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
