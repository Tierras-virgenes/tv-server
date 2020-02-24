import os
import sys
import subprocess
import signal
import time
import argparse
import shutil
import pathlib
import datetime
import tarfile
import errno

from distutils.dir_util import copy_tree
from checksumdir import dirhash

import structlog
logger = structlog.get_logger()

# Global variables
parser = None
args = None

ROOT_PATH = pathlib.Path().absolute()
SERVER_PATH = os.path.join(ROOT_PATH, "submodules", "ServUO")
REPOSITORY_PATH = os.path.join(ROOT_PATH, "resources", "tv")
BACKUP_PATH = os.path.join(ROOT_PATH, "backups")
RESOURCES_DEFAULT_PATH = os.path.join("resources", "2D")
FOLDER_SERVER_LIST = ["Config"]
BACKUP_FOLDER_LIST = ["Config", "Saves", "Spawns"]
HASH_MD5_RESOURCES = "93945c306b645459c63adddc299e3760"

################################################################################
# Functions ####################################################################
################################################################################
def signal_handler(sig, frame):
    logger.info("Signal", sig=sig)

def recursive_copy(src, dst):
    """
    Copy a folder tree overriding destination

    Notes
    -----
    working directory stay the same.
    """
    working_directory = os.getcwd()
    os.chdir(src)
    for item in os.listdir():
        if os.path.isfile(item):
            shutil.copy(item, dst)
            
        elif os.path.isdir(item):
            new_dst = os.path.join(dst, item)
            os.makedirs(new_dst, exist_ok=True)
            recursive_copy(os.path.abspath(item), new_dst)

    # Restore the original working directory
    os.chdir(working_directory)
    return

def copy_server_folders(src, dst):
    """
    Copy all folders in the SERVER_LIST
    """
    for folder in FOLDER_SERVER_LIST:
        file_src = os.path.join(src, folder)
        file_dst = os.path.join(dst, folder)
        logger.info("copying", file_src=file_src, file_dest=file_dst)
        recursive_copy(file_src, file_dst)
    return

def check_resources():
    """
    Check than required resources are properly installed in Default path. 

    * Check if exist default resources 2D path
    * Check if checksum is the same

    Notes
    -----
    You can provide other path if you want.
    """
    if not os.path.exists(RESOURCES_DEFAULT_PATH):
        logger.error("Resources default path no exists", path=RESOURCES_DEFAULT_PATH)
        return

    logger.info("Calculating resources MD5", path=RESOURCES_DEFAULT_PATH)
    md5hash = dirhash(RESOURCES_DEFAULT_PATH, 'md5')
    if not HASH_MD5_RESOURCES == md5hash:
        logger.error("Bad MD5 checksum for resources", hash=md5hash, expected=HASH_MD5_RESOURCES)
        return
        
    logger.info("Resources path looks OK", hash=md5hash)
    return

def update_server_files():
    """
    Update repository files. Copy current server folders to repository.
    """
    src = REPOSITORY_PATH
    dest = SERVER_PATH
    logger.info("update_server_files", src=src, dest=dest)
    copy_server_folders(src, dest)
    return
    
def update_repository_files():
    """
    Update server files. Copy from repository to server folders.
    """
    src = SERVER_PATH
    dest = REPOSITORY_PATH
    logger.info("update_repository_files", src=src, dest=dest)
    copy_server_folders(src, dest)
    return

def backup():
    """
    Generate backup file with timestamp name

    * The saved folders are stored at: BACKUP_FOLDER_LIST
    * A tar file will be generated.
    * The name contain the backup timestamp.
    """
    timestamp_name = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + ".tar"
    output_file = os.path.join(BACKUP_PATH, timestamp_name)
    
    logger.info("Generating backup tar file", file=output_file)

    with tarfile.open(output_file, 'w') as tar:
        for folder in BACKUP_FOLDER_LIST:
            current_folder = os.path.join(SERVER_PATH, folder)
            logger.info("Adding folder", folder=current_folder)
            tar.add(current_folder, arcname=folder)
    
    time.sleep(0.001)
    return

def restore(backup_file):
    """
    Restore give backup file in server path
    """
    logger.info("Restoring backup file", path=backup_file)

    if not os.path.isfile(backup_file):
        logger.error("Path no exist", path=backup_file)
        return False

    logger.info("Extracting at server path", path=SERVER_PATH)
    with tarfile.open(backup_file, 'r') as tar:
        tar.extractall(SERVER_PATH)
    return True

def start_server():
    """
    Start running the server
    """
    logger.info("Starting server")
    working_directory = os.getcwd()
    os.chdir(SERVER_PATH)

    if sys.platform.startswith('linux'):
        logger.info("Detected GNU/Linux platform")
        p = subprocess.Popen('make', stdout=subprocess.PIPE)
        while p.poll() is None:
            log = p.stdout.readline() # This blocks until it receives a newline.
            print(log.decode())
    elif sys.platform.startswith('win32'):
        logger.info("Detected windows platform")
    elif sys.platform.startswith('darwin'):
        logger.info("Detected MacOS platform")
    else:
        logger.info("Not valid platform")

    # Restore the original working directory
    os.chdir(working_directory)
    return

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description="Helper to manage server data. This helps to use a control version with configuration files, update the submodules (ServUO and crossuo) without lost the files. Also it can backup file saves and configurations to easy porting the server.",
                                    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-b','--backup', help='Generate a timestamped copy of the server data. This include save binaries, configuration, and spawns', default="", action='store_true')

    parser.add_argument('-r','--restore', help='Restore a timestamped copy of the server data. This include Save binaries, configuration, and spawns', default="", type=str, metavar='path')

    parser.add_argument('-c','--check', help='Check than required resources are properly installed in Default path. You can provide other path if you want.', default="", action='store_true')

    parser.add_argument('-l','--load', help='Update server files. Copy from repository to server folders. Warning, all changes in server files are override', default="", action='store_true')

    parser.add_argument('-s','--save', help='Update repository files. Copy current server folders to repository. Git will detect changes from last commits, you can discard or commit them.', default="", action='store_true')

    parser.add_argument('-o','--on', help='EXPERIMENTAL: This command DO NOT redirect stdin and stdout properly. Start running the server from default path', default="", action='store_true')

    args = parser.parse_args()

    if args.load:
        update_server_files()
    elif args.save:
        update_repository_files()
    elif args.check:
        check_resources()
    elif args.backup:
        backup()
    elif args.restore:
        restore(args.restore)
    elif args.on:
        start_server()
    else:
        logger.info("Select any option. Did nothing. Printing help.")
        parser.print_help()
    
    sys.exit(0)
