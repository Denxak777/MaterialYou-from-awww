import subprocess
import shutil
from pathlib import Path
import sys

#---------------------------------------------------------------------------------------------------------------------------------

def Material_You(monitor):
    # Find wallpaper path for later use | Узнаем расположение обоев для дальнейшего использования
    result = subprocess.run(
        "awww query", shell=True, capture_output=True, text=True
        )
    wallpaper = None
    for line in result.stdout.splitlines():
        clean_line = line.strip().lstrip(":").strip()
        if clean_line.startswith(monitor) and "image:" in clean_line:
            wallpaper = clean_line.split("image: ")[1].strip()
            break
    if wallpaper is None:
        error("ERROR-001")
    # Creating a color palette | Создаем цветовую палитру
    wal_result = subprocess.run(
        f"wal -n -s -q -i {wallpaper}", shell=True
        )
    if wal_result.returncode != 0:
        error("ERROR-002")
    # Сhecking for folder existence | Проверка существования папки
    creating_a_folder = Path(monitor)
    if creating_a_folder.exists():
        shutil.rmtree(creating_a_folder)
    creating_a_folder.mkdir(parents=True, exist_ok=True)
    cache_wal_dir = Path.home() / ".cache" / "wal"
    if not cache_wal_dir.exists():
        error("ERROR-003")
    shutil.copytree(cache_wal_dir, creating_a_folder, dirs_exist_ok=True)

#---------------------------------------------------------------------------------------------------------------------------------

def error(code):
    # If the application crashes at any stage, the root cause can be identified | Если приложение аварийно завершит работу на любом этапе, можно будет установить первопричину
    print(f"Critical error: {code} | Критическая ошибка: {code}")
    print("Read the information on GitHub or the ERRORS_EN.md file to troubleshoot the program | Ознакомьтесь с информацией на GitHub или в файле ERRORS_RU.md, чтобы устранить неполадки в программе")
    print("Code сreator Denxak777 | Создатель кода Denxak777")
    sys.exit(1)

#---------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Get the number of monitors on the computer | Узнаем количество мониторов на компьютере
    result = subprocess.run(
        "awww query", shell=True, capture_output=True, text=True
        )
    monitors = []
    for line in result.stdout.splitlines():
        if not line.split():
            continue
        clean_line = line.strip().lstrip(":").strip()
        monitor_name = clean_line.split(":")[0].strip()
        if monitor_name not in monitors:
            monitors.append(monitor_name)
    if not monitors:
        error("ERROR-000")
    # Running the script to get the color palette | Запускаем скрипт на получение палитры цветов
    for monitor in monitors:
        Material_You(monitor)
    print("The color palettes have been created and are ready to use | Цветовые палитры созданы и готовы к использованию")
    print("Code сreator Denxak777 | Создатель кода Denxak777")
    
#---------------------------------------------------------------------------------------------------------------------------------