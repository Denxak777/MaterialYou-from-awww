import platform
from .Error import error
from .VS_Code import vs_code
from .VS_Codium import vs_codium
import subprocess

#---------------------------------------------------------------------------------------------------------------------------------

def handle_arch(monitor_wallpapers):
    # Additional commands list | Список дополнительных команд
    additional_functions = {
        'visual-studio-code': lambda: vs_code(monitor_wallpapers),
        'vscodium': lambda: vs_codium(monitor_wallpapers)
    }
    options = list(additional_functions.keys())
    # Fetching the list of installed software on the PC | Получаем список установленного софта на ПК
    result = subprocess.run(
        ["pacman", "-Qq"] , capture_output=True, text=True
    )
    installed_packages = result.stdout.splitlines()
    # Comparing installed programs with the list | Сравниваем установленные программы со списком
    found_programs = []
    for program_key in additional_functions.keys():
        if any(program_key in pkg for pkg in installed_packages):
            found_programs.append(program_key)
    if not found_programs:
        print("No compatible programs were detected | Подходящие программы не были обнаружены")
        return
    # Displaying a list of programs to choose from | Выводим список программ на выбор
    while True:
        print("Generate app themes | Генерация тем для программ")
        for i, name in enumerate(found_programs, 1):
            print(f"{i}. {name}")
        print("0. Exit | Выход")
        choice = input("Enter a function number | Выберите номер функции:").strip().lower()
        if choice == '0':
            return
        # Executing the selected option | Выполняем выбранный вариантS
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(found_programs):
                selected_name = found_programs[idx]
                additional_functions[selected_name]()
            else:
                print("This number is not in the list | Такого номера нет в списке")
        except (ValueError, Exception) as e:
            error("ERROR-008")


#---------------------------------------------------------------------------------------------------------------------------------

def handle_linux(monitor_wallpapers):
    # Additional commands list | Список дополнительных команд
    additional_functions = {
        'visual-studio-code': lambda: vs_code(monitor_wallpapers),
        'vscodium': lambda: vs_codium(monitor_wallpapers)
    }
    options = list(additional_functions.keys())
    # Displaying a list of programs to choose from | Выводим список программ на выбор
    print("Warning: Your distribution is not supported. Universal mode activated | Внимание: ваш дистрибутив не поддерживается программой. Активирован универсальный режим")
    while True:
        print("Generate app themes | Генерация тем для программ")
        for i, name in enumerate(options, 1):
            print(f"{i}. {name}")
        print("0. Exit | Выход")
        choice = input("Enter a function number | Выберите номер функции:").strip().lower()
        if choice == '0':
            return
        # Executing the selected option | Выполняем выбранный вариантS
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                selected_name = options[idx]
                additional_functions[selected_name]()
            else:
                print("This number is not in the list | Такого номера нет в списке")
        except (ValueError, Exception) as e:
            error("ERROR-008")

#---------------------------------------------------------------------------------------------------------------------------------

def system_check(monitor_wallpapers):
    # Let's find out which distribution is being used | Узнаем какой дистрибутив используется
    try:
        info = platform.freedesktop_os_release()
    except AttributeError:
        error("ERROR-007")
    os_id = info.get('ID', '').lower()
    id_like = info.get('ID_LIKE', '').lower().split()
    all_identifiers = {os_id, *id_like}
    # List of distributions | Список дистрибутивов
    family_map = {
        'arch': lambda: handle_arch(monitor_wallpapers),
    }
    # Comparing user OS with the list of supported distributions | Сравниваем ос пользователя и список подерживаюших дистрибутивов
    command = None
    for identifier in all_identifiers:
        if identifier in family_map:
            command = family_map[identifier]
            break
    else:
        command = handle_linux(monitor_wallpapers)
    if command:
        command()