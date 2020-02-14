import os
import sys
import signal
import time
import argparse
import shutil
import pathlib
import errno
from checksumdir import dirhash

import structlog
logger = structlog.get_logger()

# Global variables
parser = None
args = None

SERVER_PATH = os.path.join(pathlib.Path().absolute(), "submodules", "ServUO")
REPOSITORY_PATH = os.path.join(pathlib.Path().absolute(), "resources", "tv")
RESOURCES_DEFAULT_PATH = os.path.join("resources", "2D")
FOLDER_SERVER_LIST = ["Config"]
HASH_MD5_RESOURCES = "93945c306b645459c63adddc299e3760"

################################################################################
# Functions ####################################################################
################################################################################
def signal_handler(sig, frame):
    logger.info("Signal", sig=sig)

def copy_folder(src, dest):
    """
    Copy a folder tree overriding destiny
    """
    for folder in FOLDER_SERVER_LIST:
        file_src = os.path.join(src, folder)
        file_dest = os.path.join(dest, folder)
        logger.info("copying", file_src=file_src, file_dest=file_dest)
        if os.path.exists(file_dest):
            shutil.rmtree(file_dest)
        shutil.copytree(file_src, file_dest)
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
    copy_folder(src, dest)
    return
    
def update_repository_files():
    """
    Update server files. Copy from repository to server folders.
    """
    src = SERVER_PATH
    dest = REPOSITORY_PATH
    logger.info("update_repository_files", src=src, dest=dest)
    copy_folder(src, dest)
    return
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description="Helper to save server data",
                                    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-c','--check', help='Check than required resources are properly installed in Default path. You can provide other path if you want.',
                        default="", action='store_true')

    parser.add_argument('-u','--update', help='Update server files. Copy from repository to server folders.',
                        default="", action='store_true')

    parser.add_argument('-s','--save', help='Update repository files. Copy current server folders to repository.',
                        default="", action='store_true')

    args = parser.parse_args()

    if args.update:
        update_server_files()
    elif args.save:
        update_repository_files()
    elif args.check:
        check_resources()
    else:
        logger.info("Select any option. Did nothing")
    
    sys.exit(0)