#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class FolderSet(Resource):
    """
    Folder set represents a set of folder each on separate pools that represent a group-scope datastore spanning the entire group.

    Parameters:
    - id             : Identifier of the folder set.
    - name           : Name of folder set.
    - full_name      : Fully qualified name of folder set in the group.
    - search_name    : Name of folder set used for object search.
    - description    : Text description of folder set.
    - creation_time  : Time when this folder set was created.
    - last_modified  : Time when this folder set was last modified.
    - app_uuid       : Application identifier of the folder set. If this attribute is not provided at creation, the system will generate one.
    - folder_list    : List of folders contained by the folder set. The folders must be of agent type VVol and share the same application server with the folder set.
    - appserver_id   : Identifier of the application server associated with the folder set and member folders.
    - appserver_name : Name of the application server associated with the folder set and member folders.
    """

class FolderSetList(Collection):
    resource = FolderSet
    resource_type = "folder_sets"
