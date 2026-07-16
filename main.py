#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------------------------------------------

import subprocess
from Scripts.MaterialYou import Material_You
from Scripts.Error import error
from Scripts.VS_code import vs_code

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

    # Offer to apply a theme for VS Code | Предложить применить тему для VS code
    while True:
        vscode_question = input("Apply the VS Code theme? [y|N]" "|" "Применить тему для VS Code? [y|N]").strip().lower()
        if vscode_question.startswith("y"):
            for monitor, wallpaper in monitor_wallpapers.items():
                vs_code(monitor)
            break
        elif vscode_question.startswith("n"):
            break
        elif vscode_question == "":
            break

#---------------------------------------------------------------------------------------------------------------------------------

    print("The color palettes have been created and are ready to use | Цветовые палитры созданы и готовы к использованию")
    print("Code сreator Denxak777 | Создатель кода Denxak777")