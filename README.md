SimpleBackupTool
================

Backup tool to make automated backups of filesystems or directories to disks 
or servers

This is currently very early work in progress and hardly not useable for 
anyone else yet.

The plan is to add funtionality to add the following functionality:
  - Backups can be spread on multiple locations
  - Backups are automatically purged according to a schedule when becoming too
    old.
  - Backup destinations can be network shares also.
  - Mail is sent on failure and optionally on success.
  - Keeps track of when disks should be rotated.
  - Supports linux (ubuntu) and Mac OSX.
  - Configure logging.
  - Completely configurable.

Done this far:
  - Unchanged files are hard linked to the already existing file so that each
    backup is always complete.
  - Support for encrypted disks.

