Coordinating Server
===================

Application running on publicly accessible server to coordinate interactions between clients and targets.

API
===

/upload_backup (method: POST)
  Send a file from client to be backed up on targets.
  Clients should send updated copies of files regularly.
  
  Required POST data:
  
  - client_name
  - list of target_name
  - file data

/collect_backup/<target_name> (method: GET)
  Retrieve all backup jobs for a target.
  Targets should regularly collect their backups.
  
  Returned as JSON:
  
  - list of { client_name, file data }

/upload_manifest (method: POST)
  Send a list of all client files that exist on a target to the server.
  This should be regularly updated by each target.
  
  Required POST data:
  
  - client_name
  - target_name
  - list of files

/collect_manifest/<target_name>/<client_name> (method: GET)
  Get most recent manifest of client files on a target.
  
  Returned as JSON:
  
  - list of client files on target
