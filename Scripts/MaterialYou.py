import subprocess
import shutil
from pathlib import Path
from .Error import error

#---------------------------------------------------------------------------------------------------------------------------------

def Material_You(monitor, wallpaper):
    # Creating a color palette | Создаем цветовую палитру
    wal_result = subprocess.run(
        ["wal", "-n", "-s", "-q", "-i", f"{wallpaper}"]
        )
    if wal_result.returncode != 0:
        error("ERROR-001")

#---------------------------------------------------------------------------------------------------------------------------------

    # Сhecking for folder existence | Проверка существования папки
    creating_a_folder = Path(monitor)
    if creating_a_folder.exists():
        shutil.rmtree(creating_a_folder)
    creating_a_folder.mkdir(parents=True, exist_ok=True)
    cache_wal_dir = Path.home() / ".cache" / "wal"
    if not cache_wal_dir.exists():
        error("ERROR-002")
    shutil.copytree(cache_wal_dir, creating_a_folder, dirs_exist_ok=True)