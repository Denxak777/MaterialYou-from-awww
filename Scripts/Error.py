import sys

#---------------------------------------------------------------------------------------------------------------------------------

def error(code):
    # If the application crashes at any stage, the root cause can be identified | Если приложение аварийно завершит работу на любом этапе, можно будет установить первопричину
    print(f"Critical error: {code} | Критическая ошибка: {code}")
    print("Read the information on GitHub or the ERRORS_EN.md file to troubleshoot the program | Ознакомьтесь с информацией на GitHub или в файле ERRORS_RU.md, чтобы устранить неполадки в программе")
    print("Code сreator Denxak777 | Создатель кода Denxak777")
    sys.exit(1)