from utils import run_command_and_stream
from base import *
from pacman import create_build_time_pacman_conf, ensure_db_cache


def build_iso() -> None:
    ensure_db_cache()
    create_build_time_pacman_conf()
    run_command_and_stream([
        "sudo",
        "bash",
        str(bakeryos_mkiso_tool),
        "-v",
        "-C",
        str(pacman_config_file),
        "-w",
        str(work_dir),
        "-o",
        str(out_dir),
        str(project_dir)
    ], None, build_log_dir / "iso.log")
