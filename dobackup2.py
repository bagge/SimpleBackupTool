import subprocess
import datetime
import os
import sys

DEBUG=False

BACKUPDEVICE="/dev/sdc1"
BACKUPMAPPER="encBackup"
BACKUPMOUNT="/mnt/backup"
#BACKUPMOUNT="/home/alex/backupdummy"

def getBackupName():
    now = datetime.datetime.today()
    return "%d%02d%02d_%02d%02d" % (now.year, now.month, now.day, 
        now.hour, now.minute)

def exec_cmd(cmd, DEBUGOVERRIDE=None):
    if DEBUGOVERRIDE is None and DEBUG or DEBUGOVERRIDE == True:
        print "DEBUG: ", cmd
    else:
        subprocess.check_call(cmd)

def doOpenDevice():
    #print "Opening encrypted device..."
    #exec_cmd(["cryptsetup", "luksOpen", BACKUPDEVICE, BACKUPMAPPER])

    print "Mounting device"
    exec_cmd(["mount", BACKUPMOUNT])

def doCloseDevice():
    print "Unmounting device"
    exec_cmd(["umount", BACKUPMOUNT])

    #print "Closing encrypted device"
    #exec_cmd(["cryptsetup", "luksClose", BACKUPMAPPER])

def doBackup(source, jobname): #, backupname):
    print "Doing backup of %s" % source
    backupstore = os.path.join(BACKUPMOUNT, jobname)
    print "Examining existing backups in %s" % backupstore

    #backups = getBackups(backupstore)
    #backups.sort()
    #if len(backups) > 0:
        #print "Found: "
        #for i in backups:
            #print "  %s" % i
        #linkdest = os.path.join(backupstore, backups[-1])
        #print "Using %s as basis for new backup" % linkdest
    #else:
        #print "No previous backup found. Will copy all files"
        #linkdest = None

    cmd = ["rsync", "-a", "-t", "-x", "--delete", "--stats"]
    #if linkdest is not None:
        #cmd.append("--link-dest=%s" % linkdest)
    if not source.endswith(os.path.sep):
        source += os.path.sep
    cmd.append(source)
    cmd.append(backupstore)
    exec_cmd(cmd)

def getBackups(path):
    return os.listdir(path)

if __name__=='__main__':

    if not os.geteuid()==0:
        sys.exit("\nOnly root can run this script\n")

    #backupname = getBackupName()
    #print "Determined backup name to: %s" % backupname

    doOpenDevice()
    doBackup("/home/alex/.xbmc", "xbmc") #, backupname)
    #doBackup("/home/alex/.lircrc", "lircrc") #, backupname)
    #doBackup("/", "root", backupname)
    doCloseDevice()
