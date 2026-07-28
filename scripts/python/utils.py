import subprocess
import sys
import os


def run_command_and_stream(command: str | list[str], cwd: str | None = None,  log_file: str | Path | None = None, ) -> int:
    print("--------------------------------------------------")

    log_handle = open(log_file, "a", encoding="utf-8") if log_file else None

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            shell=True if isinstance(command, str) else False,
            cwd=cwd
        )

        for chunk in iter(lambda: process.stdout.read(1), ''):
            sys.stdout.write(chunk)
            sys.stdout.flush()

            if log_handle:
                log_handle.write(chunk)

        return process.wait()

    except Exception as e:
        print(f"An error occurred while executing command: {e}")
        return -1
    finally:
        if log_handle:
            log_handle.close()


def directory_has_files(dir_path):
    try:
        with os.scandir(dir_path) as it:
            return any(it)
    except FileNotFoundError:
        return False
