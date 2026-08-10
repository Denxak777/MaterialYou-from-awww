#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------------------------------------------

import subprocess
from Scripts.MaterialYou import Material_You
from Scripts.Error import error
from Scripts.Additional_functions import system_check

#---------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Get all monitor info in one single call | Получаем всю информацию о мониторах за один вызов
    result = subprocess.run(
        ["awww", "query"] , capture_output=True, text=True
        )
    monitor_wallpapers = {}
    for line in result.stdout.splitlines():
        if not line.split():
            continue
        clean_line = line.strip().lstrip(":").strip()
        current_monitor = clean_line.split(":")[0].strip()
        if "image:" in clean_line:
            current_wallpapers = clean_line.split("image: ")[1].strip()
            monitor_wallpapers[current_monitor] = current_wallpapers
    if not monitor_wallpapers:
        error("ERROR-000")
    # Running the script to get the color palette | Запускаем скрипт на получение палитры цветов
    for monitor, wallpaper in monitor_wallpapers.items():
        Material_You(monitor, wallpaper)

#---------------------------------------------------------------------------------------------------------------------------------

    # Offer to additional functions | Предложить дополнительные фунуции
    while True:
        functions = input("Open additional functions? [y|N]" "|" "Открыть допольнительные функции? [y|N]").strip().lower()
        if functions.startswith("y"):
            system_check(monitor_wallpapers)
            break
        elif functions.startswith("n"):
            break
        elif functions == "":
            break

#---------------------------------------------------------------------------------------------------------------------------------

    print("The color palettes have been created and are ready to use | Цветовые палитры созданы и готовы к использованию")
    print("Code сreator Denxak777 | Создатель кода Denxak777")