#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class ReplicationPartner(Resource):
    """
    Manage replication partner. Replication partners let one storage array talk to another for replication purposes. The two arrays must be able to communicate over a network, and use ports 4213 and 4214. Replication partners have the same name as the remote group. Replication partners can be reciprocal, upstream (the source of replicas), or downstream (the receiver of replicas) partners.

    Parameters:
    - id                               : Identifier for a replication partner.
    - name                             : Name of replication partner.
    - full_name                        : Fully qualified name of replication partner.
    - search_name                      : Name of replication partner used for object search.
    - description                      : Description of replication partner.
    - partner_type                     : Replication partner type. Possible values are group or pool.
    - alias                            : Name this group uses to identify itself to this partner.
    - secret                           : Replication partner shared secret, used for mutual authentication of the partners.
    - creation_time                    : Time when this replication partner was created.
    - last_modified                    : Time when this replication partner was last modified.
    - control_port                     : Port number of partner control interface.
    - hostname                         : IP address or hostname of partner interface.  This must be the partner's Group Management IP address.
    - port_range_start                 : For tunnel_endpoint partner types, first port available on the ssh proxy available for reverse forwarding. It must be guaranteed that the proxy has the next N ports reserved for this partner, where N is the count of DSDs in this group. This attribute is only valid for tunnel_endpoint partner type.
    - proxy_hostname                   : IP address of tunnel endpoint. Only valid for tunnel_endpoint partner types.
    - proxy_user                       : User to authenticate with tunnel endpoint. Only valid for tunnel_endpoint partner types.
    - repl_hostname                    : IP address or hostname of partner data interface.
    - data_port                        : Port number of partner data interface.
    - is_alive                         : Whether the partner is available, and responding to pings.
    - partner_group_uid                : Replication partner group uid.
    - last_keepalive_error             : Most recent error while attempting to ping the partner.
    - cfg_sync_status                  : Indicates whether all volumes and volume collections have been synced to the partner.
    - last_sync_error                  : Most recent error seen while attempting to sync objects to the partner.
    - array_serial                     : Serial number of group leader array of the partner.
    - version                          : Replication version of the partner.
    - pool_id                          : The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume.
    - pool_name                        : The pool name where volumes replicated from this partner will be created.
    - folder_id                        : The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners.
    - folder_name                      : The Folder name within the pool where volumes replicated from this partner will be created.
    - match_folder                     : Indicates whether to match the upstream volume's folder on the downstream.
    - paused                           : Indicates whether replication traffic from/to this partner has been halted.
    - unique_name                      : Indicates whether this partner actively mangles object names to avoid name conflicts during replication.
    - subnet_label                     : Label of the subnet used to replicate to this partner.
    - subnet_type                      : Type of the subnet used to replicate to this partner.
    - throttles                        : Throttles used while replicating from/to this partner.
    - throttled_bandwidth              : Current bandwidth throttle for this partner, expressed either as megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no throttle. This attribute is superseded by throttled_bandwidth_current.
    - throttled_bandwidth_current      : Current bandwidth throttle for this partner, expressed either as megabits per second or as -1 to indicate that there is no throttle.
    - throttled_bandwidth_kbps         : Current bandwidth throttle for this partner, expressed either as kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no throttle. This attribute is superseded by throttled_bandwidth_current_kbps.
    - throttled_bandwidth_current_kbps : Current bandwidth throttle for this partner, expressed either as kilobits per second or as -1 to indicate that there is no throttle.
    - subnet_network                   : Subnet used to replicate to this partner.
    - subnet_netmask                   : Subnet mask used to replicate to this partner.
    - volume_collection_list           : List of volume collections that are replicating from/to this partner.
    - volume_collection_list_count     : Count of volume collections that are replicating from/to this partner.
    - volume_list                      : List of volumes that are replicating from/to this partner.
    - volume_list_count                : Count of volumes that are replicating from/to this partner.
    - replication_direction            : Direction of replication configured with this partner.
    """

    def pause(self):
        """
        Pause replication for the specified partner.

        Parameters:
        - id : ID of the partner to pause.
        """

        return self.collection.pause(self.id)

    def resume(self):
        """
        Resume replication for the specified partner.

        Parameters:
        - id : ID of the partner to resume.
        """

        return self.collection.resume(self.id)

    def test(self):
        """
        Test connectivity to the specified partner.

        Parameters:
        - id : ID of the partner to test.
        """

        return self.collection.test(self.id)

    def delete_replica_volume(self, vol_id):
        """
        Delete a replica volume and all associated replica snapshots stored on the given downstream partner. The replica must be owned by this group (the upstream partner) and must not be in a volume collection. The original volume, which may or may not still exist on the upstream partner, is not affected by this operation.

        Parameters:
        - id     : ID of the downstream partner storing the replica.
        - vol_id : ID of the replica volume to delete.
        """

        return self.collection.delete_replica_volume(self.id, vol_id)

    def delete_replica_snapshot(self, snap_id):
        """
        Delete a replica snapshot stored on the given downstream partner. The replica must be owned by this group (the upstream partner). The original snapshot, which may or may not still exist on the upstream partner, is not affected by this operation.

        Parameters:
        - id      : ID of the downstream partner storing the replica.
        - snap_id : ID of the replica snapshot to delete.
        """

        return self.collection.delete_replica_snapshot(self.id, snap_id)

class ReplicationPartnerList(Collection):
    resource = ReplicationPartner
    resource_type = "replication_partners"

    def pause(self, id):
        """
        Pause replication for the specified partner.

        Parameters:
        - id : ID of the partner to pause.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'pause', id=id)

    def resume(self, id):
        """
        Resume replication for the specified partner.

        Parameters:
        - id : ID of the partner to resume.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'resume', id=id)

    def test(self, id):
        """
        Test connectivity to the specified partner.

        Parameters:
        - id : ID of the partner to test.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'test', id=id)

    def delete_replica_volume(self, id, vol_id):
        """
        Delete a replica volume and all associated replica snapshots stored on the given downstream partner. The replica must be owned by this group (the upstream partner) and must not be in a volume collection. The original volume, which may or may not still exist on the upstream partner, is not affected by this operation.

        Parameters:
        - id     : ID of the downstream partner storing the replica.
        - vol_id : ID of the replica volume to delete.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'delete_replica_volume', id=id, vol_id=vol_id)

    def delete_replica_snapshot(self, id, snap_id):
        """
        Delete a replica snapshot stored on the given downstream partner. The replica must be owned by this group (the upstream partner). The original snapshot, which may or may not still exist on the upstream partner, is not affected by this operation.

        Parameters:
        - id      : ID of the downstream partner storing the replica.
        - snap_id : ID of the replica snapshot to delete.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'delete_replica_snapshot', id=id, snap_id=snap_id)
