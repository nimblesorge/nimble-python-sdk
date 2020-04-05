#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class HcClusterConfig(Resource):
    """
    Configuration information for virtual appliance that provides highly available storage and compute.

    Parameters:
    - id            : Identifier for the hc cluster config.
    - unique_id     : Unique identifier for the HC component.
    - name          : Name for the HC component.
    - description   : Text description of HC component.
    - username      : HC component username.
    - password      : HC component password.
    - type          : HCI config type ({invalid|node|block|cluster}).
    - metadata      : Key-value pairs that augment a HC cluster config's attributes.
    - creation_time : Time when this HC cluster configuration was created.
    - last_modified : Time when this HC cluster configuration was last modified.
    """

class HcClusterConfigList(Collection):
    resource = HcClusterConfig
    resource_type = "hc_cluster_configs"
