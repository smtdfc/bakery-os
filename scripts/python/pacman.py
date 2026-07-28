from repository import add_local_repo, add_cache_repo
from utils import run_command_and_stream, directory_has_files
from base import *
from extensions import *
from package import *
import configparser
import os


class CaseConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr: str) -> str:
        return optionstr


def config_pacman() -> None:
    print("Config pacman .... ")
    config = CaseConfigParser()
    if pacman_config_file.exists():
        config.read(pacman_config_file)

        if len(package_snapshots) > 0:
            config["custom"] = {
                "Server": f"file://{local_repo_dir}"
            }
        else:
            if config.has_section("custom"):
                del config["custom"]

        config["bakeryos"]["Server"] = bakeryos_repository

        with open(pacman_config_file, 'w') as configfile:
            config.write(configfile)


def ensure_db_cache() -> None:
    print("Ensure cache db .... ")
    if directory_has_files(package_cache_dir) and not package_cache_db.exists():
        add_cache_repo()


def create_build_time_pacman_conf() -> None:
    print("Generating build time pacman config file .... ")
    config = CaseConfigParser()
    if pacman_config_file.exists():
        config.read(pacman_config_file)

        if len(package_snapshots) > 0:
            config["custom"] = {
                "Server": f"file://{local_repo_dir}"
            }
        else:
            if config.has_section("custom"):
                del config["custom"]

        # if package_cache_db.exists():
        #     config["bakeryos-cache"] = {
        #         "Server": f"file://{package_cache_db}"
        #     }

        config["bakeryos"]["Server"] = bakeryos_repository

        with open(bt_pacman_config_file, 'w') as configfile:
            config.write(configfile)
