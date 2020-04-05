#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class Snapshot(Resource):
    """
    Snapshots are point-in-time copies of a volume. Snapshots are managed the same way you manage volumes. In reality, snapshots are volumes: they can be accessed by initiators, are subject to the same controls, can be modified, and have the same restrictions as volumes. Snapshots can be cloned and replicated. The initial snapshot uses no space: it shares the original data with the source volume. Each successive snapshot captures the changes that have occurred on the volume. The changed blocks are compressed.

    Parameters:
    - id                          : Identifier for the snapshot.
    - name                        : Name of snapshot.
    - description                 : Text description of snapshot.
    - size                        : Size of volume at time of snapshot (in bytes).
    - vol_name                    : Name of the parent volume in which the snapshot belongs to.
    - pool_name                   : Name of the pool in which the parent volume belongs to.
    - vol_id                      : Parent volume ID.
    - snap_collection_name        : Name of snapshot collection.
    - snap_collection_id          : Identifier of snapshot collection.
    - online                      : Online state for a snapshot means it could be mounted for data restore.
    - writable                    : Allow snapshot to be writable. Mandatory and must be set to 'true' for VSS application synchronized snapshots.
    - offline_reason              : Snapshot offline reason - possible entries: one of 'user', 'recovery', 'replica', 'over_volume_limit', 'over_snapshot_limit', 'over_volume_reserve', 'nvram_loss_recovery', 'pool_free_space_exhausted' .
    - expiry_time                 : Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never expires.
    - expiry_after                : Number of seconds after which this snapshot is considered expired by snapshot TTL. A value of 0 indicates that snapshot never expires, 1 indicates that snapshot uses group-level configured TTL value and any other value indicates number of seconds.
    - origin_name                 : Origination group name.
    - is_replica                  : Snapshot is a replica from upstream replication partner.
    - is_unmanaged                : Indicates whether the snapshot is unmanaged. The snapshot will not be deleted automatically unless the unmanaged cleanup feature is enabled.
    - is_manually_managed         : Is snapshot manually managed, i.e., snapshot is manually or third party created or created by system at the time of volume restore or resize.
    - replication_status          : Replication status.
    - access_control_records      : List of access control records that apply to this snapshot.
    - serial_number               : Identifier for the SCSI protocol.
    - target_name                 : The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target snapshot.
    - creation_time               : Time when this snapshot was created.
    - last_modified               : Time when this snapshort was last modified.
    - schedule_name               : Name of protection schedule.
    - schedule_id                 : Identifier of protection schedule.
    - app_uuid                    : Application identifier of snapshots.
    - metadata                    : Key-value pairs that augment a snapshot's attributes.
    - new_data_valid              : Indicate the usage infomation is valid.
    - new_data_compressed_bytes   : The bytes of compressed new data.
    - new_data_uncompressed_bytes : The bytes of uncompressed new data.
    - agent_type                  : External management agent type.
    - vpd_t10                     : The snapshot's T10 Vendor ID-based identifier.
    - vpd_ieee0                   : The first 64 bits of the snapshots's EUI-64 identifier, encoded as a hexadecimal string.
    - vpd_ieee1                   : The last 64 bits of the snapshots's EUI-64 identifier, encoded as a hexadecimal string.
    - force                       : Forcibly delete the specified snapshot even if it is the last replicated collection. Doing so could lead to full re-seeding at the next replication.
    """

    def cksum(self):
        """
        Computes checksum of snapshot which can be used to verify data integrity. Checksum computation is a long running operation and can take several minutes.

        Parameters:
        - id : ID of the snapshot to take a checksum of.
        """

        return self.collection.cksum(self.id)

    def get_allocated_bitmap(self, chunk_size_bytes, segment_length_bytes, segment_start_offset_bytes, timeout_secs):
        """
        Scan a segment within a snapshot and return a bitmap of the non-zero chunks.

        Parameters:
        - id                         : ID of the snapshot to scan.
        - segment_start_offset_bytes : The starting byte offset of the segment to scan. Must be a multiple of the chunk size.
        - segment_length_bytes       : The length in bytes of the segment to scan. Must be a multiple of the chunk size.
        - chunk_size_bytes           : The number of bytes represented by a bit in the bitmap. Must be a multiple of the snapshot's block size.
        - timeout_secs               : A limit on the time (in seconds) to generate a result. If a full result cannot be computed in this time, a partial result will be returned instead. The bitmap for a partial result will be shorter than expected and will comprise whole bytes.
        """

        return self.collection.get_allocated_bitmap(self.id, chunk_size_bytes, segment_length_bytes, segment_start_offset_bytes, timeout_secs)

    def get_unshared_bitmap(self, base_id, chunk_size_bytes, segment_length_bytes, segment_start_offset_bytes, timeout_secs):
        """
        Compare a segment of two related snapshots and return a bitmap of the differing chunks.

        Parameters:
        - id                         : ID of the derived snapshot. This snapshot must be a descendent of the base snapshot, and they must be the same size.
        - base_id                    : ID of the base snapshot. This snapshot must be an ancestor of the derived snapshot, and they must be the same size.
        - segment_start_offset_bytes : The starting byte offset of the segment to compare. Must be a multiple of the chunk size.
        - segment_length_bytes       : The length in bytes of the segment to compare. Must be a multiple of the chunk size.
        - chunk_size_bytes           : The number of bytes represented by a bit in the bitmap. Must be a multiple of the snapshot's block size.
        - timeout_secs               : A limit on the time (in seconds) to generate a result. If a full result cannot be computed in this time, a partial result will be returned instead. The bitmap for a partial result will be shorter than expected and will comprise whole bytes.
        """

        return self.collection.get_unshared_bitmap(self.id, base_id, chunk_size_bytes, segment_length_bytes, segment_start_offset_bytes, timeout_secs)

    def bulk_create(self, replicate, snap_vol_list, vss_snap):
        """
        Create snapshots on the given set of volumes.

        Parameters:
        - snap_vol_list : List of volumes to snapshot and corresponding snapshot creation attributes. VSS application-synchronized snapshot must specify the 'writable' parameter and set it to true.
        - replicate     : Allow snapshot to be replicated.
        - vss_snap      : VSS app-synchronized snapshot; we don't support creation of non app-synchronized sanpshots through this interface; must be set to true.
        """

        return self.collection.bulk_create(self.id, replicate, snap_vol_list, vss_snap)

    def bulk_async_create(self, list):
        """
        Create a snapshot of a number of volumes. Each volume will have a crash consistent snapshot, but they are not consistent with each other.

        Parameters:
        - list : List of volumes to snapshot.
        """

        return self.collection.bulk_async_create(self.id, list)

    def bulk_async_delete(self, list):
        """
        Delete a number of snapshots asynchronously.

        Parameters:
        - list : List of snapshot to delete.
        """

        return self.collection.bulk_async_delete(self.id, list)

class SnapshotList(Collection):
    resource = Snapshot
    resource_type = "snapshots"

    def cksum(self, id):
        """
        Computes checksum of snapshot which can be used to verify data integrity. Checksum computation is a long running operation and can take several minutes.

        Parameters:
        - id : ID of the snapshot to take a checksum of.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'cksum', id=id)

    def get_allocated_bitmap(self, chunk_size_bytes, id, segment_length_bytes, segment_start_offset_bytes, timeout_secs):
        """
        Scan a segment within a snapshot and return a bitmap of the non-zero chunks.

        Parameters:
        - id                         : ID of the snapshot to scan.
        - segment_start_offset_bytes : The starting byte offset of the segment to scan. Must be a multiple of the chunk size.
        - segment_length_bytes       : The length in bytes of the segment to scan. Must be a multiple of the chunk size.
        - chunk_size_bytes           : The number of bytes represented by a bit in the bitmap. Must be a multiple of the snapshot's block size.
        - timeout_secs               : A limit on the time (in seconds) to generate a result. If a full result cannot be computed in this time, a partial result will be returned instead. The bitmap for a partial result will be shorter than expected and will comprise whole bytes.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'get_allocated_bitmap', chunk_size_bytes=chunk_size_bytes, id=id, segment_length_bytes=segment_length_bytes, segment_start_offset_bytes=segment_start_offset_bytes, timeout_secs=timeout_secs)

    def get_unshared_bitmap(self, base_id, chunk_size_bytes, id, segment_length_bytes, segment_start_offset_bytes, timeout_secs):
        """
        Compare a segment of two related snapshots and return a bitmap of the differing chunks.

        Parameters:
        - id                         : ID of the derived snapshot. This snapshot must be a descendent of the base snapshot, and they must be the same size.
        - base_id                    : ID of the base snapshot. This snapshot must be an ancestor of the derived snapshot, and they must be the same size.
        - segment_start_offset_bytes : The starting byte offset of the segment to compare. Must be a multiple of the chunk size.
        - segment_length_bytes       : The length in bytes of the segment to compare. Must be a multiple of the chunk size.
        - chunk_size_bytes           : The number of bytes represented by a bit in the bitmap. Must be a multiple of the snapshot's block size.
        - timeout_secs               : A limit on the time (in seconds) to generate a result. If a full result cannot be computed in this time, a partial result will be returned instead. The bitmap for a partial result will be shorter than expected and will comprise whole bytes.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'get_unshared_bitmap', base_id=base_id, chunk_size_bytes=chunk_size_bytes, id=id, segment_length_bytes=segment_length_bytes, segment_start_offset_bytes=segment_start_offset_bytes, timeout_secs=timeout_secs)

    def bulk_create(self, replicate, snap_vol_list, vss_snap):
        """
        Create snapshots on the given set of volumes.

        Parameters:
        - snap_vol_list : List of volumes to snapshot and corresponding snapshot creation attributes. VSS application-synchronized snapshot must specify the 'writable' parameter and set it to true.
        - replicate     : Allow snapshot to be replicated.
        - vss_snap      : VSS app-synchronized snapshot; we don't support creation of non app-synchronized sanpshots through this interface; must be set to true.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'bulk_create', replicate=replicate, snap_vol_list=snap_vol_list, vss_snap=vss_snap)

    def bulk_async_create(self, list):
        """
        Create a snapshot of a number of volumes. Each volume will have a crash consistent snapshot, but they are not consistent with each other.

        Parameters:
        - list : List of volumes to snapshot.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'bulk_async_create', list=list)

    def bulk_async_delete(self, list):
        """
        Delete a number of snapshots asynchronously.

        Parameters:
        - list : List of snapshot to delete.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'bulk_async_delete', list=list)
