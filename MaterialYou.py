import subprocess

#---------------------------------------------------------------------------------------------------------------------------------

def Material_You(monitor):
    # Find wallpaper path for later use | Узнаем расположение обоев для дальнейшего использования
    info_wallpaper = f"awww query | grep {monitor} | awk -F'image: ' '{{print $2}}'"
    result = subprocess.run(info_wallpaper, shell=True, capture_output=True, text=True)
    wallpaper = result.stdout.strip()
    # Creating a color palette | Создаем цветовую палитру
    config = f"wal -n -s -q -i {wallpaper}"
    subprocess.run(config, shell=True)
    # checking for folder existence | проверка существования папки
    check_folder = f"ls | grep {monitor}"
    check = subprocess.run(check_folder, shell=True, capture_output=True, text=True)
    result_check = check.stdout.split()
    if result_check:
        deleting_the_folder = f"rm -rf {monitor}"
        subprocess.run(deleting_the_folder, shell=True)
    creating_a_folder = f"mkdir {monitor}"
    subprocess.run(creating_a_folder, shell=True)
    configuration_migration = f"cp -r $HOME/.cache/wal/. {monitor}/"
    subprocess.run(configuration_migration, shell=True)

#---------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Get the number of monitors on the computer | Узнаем количество мониторов на компьютере
    info_monitor = "awww query | awk -F': ' '{print $2}'"
    result = subprocess.run(info_monitor, shell=True, capture_output=True, text=True)
    monitors = result.stdout.strip().splitlines()
    # Running the script to get the color palette | Запускаем скрипт на получение палитры цветов
    for monitor in monitors:
        Material_You(monitor)
    print("The color palettes have been created and are ready to use | Цветовые палитры созданы и готовы к использованию")
    print("Code сreator Denxak777 | Создатель кода Denxak777")
    
#---------------------------------------------------------------------------------------------------------------------------------