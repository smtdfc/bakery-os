from repository import add_local_repo, add_cache_repo
from utils import run_command_and_stream, directory_has_files
from base import *
from extensions import *
from package import *
from pacman import config_pacman
import configparser
import os


def create_user_filesystem() -> None:
    user_dirs = [
        "Desktop",
        "Documents",
        "Downloads",
        "Templates",
        "Public",
        "Music",
        "Pictures",
        "Videos"
    ]

    for i in user_dirs:
        os.makedirs(user_skel / i, exist_ok=True)


def update_system() -> None:
    print("Updating .... ")
    run_command_and_stream(["sudo", "pacman", "-Syu"])
    run_command_and_stream(["sudo", "pacman", "-S", "--needed", "base-devel"])
    run_command_and_stream(["sudo", "pacman", "-S", "--needed", "squashfs-tools",
                           "dosfstools", "mtools", "arch-install-scripts", "xorriso"])


def ensure_files() -> None:
    print("Creating files and dirs .... ")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(snapshot_dir, exist_ok=True)
    os.makedirs(local_repo_dir, exist_ok=True)
    os.makedirs(gnome_extension_dir, exist_ok=True)
    os.makedirs(package_cache_dir, exist_ok=True)
    os.makedirs(build_log_dir, exist_ok=True)


def prepare() -> None:
    update_system()
    ensure_files()
    config_pacman()
    create_user_filesystem()
    # download_all_core_packages()
    setup_gnome_extensions()
    extract_all_snapshot()
    build_all_pkg()
    add_local_repo()
