#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class ProtocolEndpoint(Resource):
    """
    Protocol endpoints are administrative logical units (LUs) in an LU conglomerate to be used with VMware Virtual Volumes.

    Parameters:
    - id                     : Identifier for the protocol endpoint.
    - name                   : Name of the protocol endpoint.
    - description            : Text description of the protocol endpoint.
    - pool_name              : Name of the pool where the protocol endpoint resides. If pool option is not specified, protocol endpoint is assigned to the default pool.
    - pool_id                : Identifier associated with the pool in the storage pool table.
    - state                  : Operational state of protocol endpoint.
    - serial_number          : Identifier associated with the protocol endpoint for the SCSI protocol.
    - target_name            : The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target protocol endpoint.
    - group_specific_ids     : External UID is used to compute the serial number and IQN which never change even if the running group changes (e.g. after group merge). Group-specific IDs determine whether external UID is used for computing serial number and IQN.
    - creation_time          : Time when this protocol endpoint was created.
    - last_modified          : Time when this protocol endpoint was last modified.
    - num_connections        : Number of connections via this protocol endpoint.
    - num_iscsi_connections  : Number of iSCSI connections via this protocol endpoint.
    - num_fc_connections     : Number of FC connections via this protocol endpoint.
    - access_control_records : List of access control records that apply to this protocol endpoint.
    - iscsi_sessions         : List of iSCSI sessions connected to this protocol endpoint.
    - fc_sessions            : List of FC sessions connected to this protocol endpoint.
    - access_protocol        : Access protocol of the protocol endpoint. Only initiator groups with the same access protocol can access the protocol endpoint. If not specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre Channel.
    """

class ProtocolEndpointList(Collection):
    resource = ProtocolEndpoint
    resource_type = "protocol_endpoints"
