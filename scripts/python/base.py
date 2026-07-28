from pathlib import Path


script_dir = Path(__file__).resolve().parent
project_dir = script_dir.parent.parent
work_dir = project_dir / "work"
out_dir = project_dir / "out"
user_skel = project_dir / "airootfs" / "etc" / "skel"
build_profile = project_dir / "profiledef.sh"
packagex64_file = project_dir / "packages.x86_64"
pacman_config_file = project_dir / "pacman.conf"
bt_pacman_config_file = project_dir / "pacman.conf"
data_dir = project_dir / "build_time"
build_log_dir = data_dir / "logs"
bt_pacman_config_file = data_dir / "pacman.conf"
package_cache_dir = data_dir / "cache"
package_cache_db = data_dir / "bakeryos-cache.db.tar.gz"
snapshot_dir = project_dir / "pkg-snapshots"
snapshot_target_dir = data_dir / "pkgs"
local_repo_dir = data_dir / "local-repo"
local_repo_db_file = local_repo_dir/"custom.db.tar.gz"
gnome_version = 50
gnome_extension_dir = data_dir / "gnome-extensions"
gnome_extension_install_dir = project_dir / "airootfs" / \
    "usr" / "share" / "gnome-shell" / "extensions"
gnome_extensions: list[dict[str, str]] = [
    {
        "id": "dash-to-panel@jderose9.github.com",
        "version": "73",
    },
    {
        "id": "blur-my-shell@aunetx",
        "version": "71",
    },
    {
        "id": "tilingshell@ferrarodomenico.com",
        "version": "76",
    },
    {
        "id": "arcmenu@arcmenu.com",
        "version": "71"
    },
    {
        "id": "gtk4-ding@smedius.gitlab.com",
        "version": "139"
    }
]


pacman_config_file = project_dir / "pacman.conf"
package_snapshots = []

bakeryos_repository = "https://repo.bakeryos.smtdfc.net/$arch"
bakeryos_mkiso_tool = project_dir / "tools"/"bakeryos-mkiso"/"run.sh"
