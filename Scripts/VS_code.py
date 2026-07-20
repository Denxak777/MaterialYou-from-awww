from pathlib import Path
import json
from .Error import error
import shutil

#---------------------------------------------------------------------------------------------------------------------------------

def vs_code(monitor):
    # We take the config file | Берем файл с конфигом
    config = Path() / monitor / "colors-vscode.json"
    if not config.exists():
        error("ERROR-003")
    try:
        data = json.loads(config.read_text(encoding="utf-8"))
        tokens = data.get("editor.tokenColorCustomizations", {})
        workbench = data.get("workbench.colorCustomizations", {})
    except Exception:
        error("ERROR-004")
    # Generating unique names for the topic | Генерируем уникальные имена для темы
    monitor_fix = monitor.replace("-", "_").lower()
    theme_name = f"MaterialYou {monitor}"
    theme_id = f"materialyou_{monitor_fix}"
    # Setting the path to the extensions folder | Задаем путь к папке расширений
    extensions_dir = Path.home() / ".vscode" / "extensions" / theme_id
    theme_dir = extensions_dir / "themes"
    if extensions_dir.exists():
        try:
            shutil.rmtree(extensions_dir)
        except Exception:
            pass
    # Creating a theme config | Создаем конфиг для темы
    bg = workbench.get("editor.background")
    fg = tokens.get("variables")
    comments = tokens.get("comments")
    functions = tokens.get("functions")
    keywords = tokens.get("keywords")
    package_manifest = {
        "name": theme_id,
        "displayName": theme_name,
        "version": "1.0.0",
        "engines": {"vscode": "^1.50.0"},
        "categories": ["Themes"],
        "contributes": {
            "themes": [
                {
                    "label": theme_name,
                    "uiTheme": "vs-dark",
                    "path": "./themes/theme.json"
                }
            ]
        }
    }
    theme_data = {
        "name": theme_name,
        "type": "dark",
        "colors": {
            "editor.background": bg,
            "editor.foreground": fg,
            "sideBar.background": bg,
            "sideBar.border": f"{fg}11",
            "activityBar.background": bg,
            "activityBar.border": f"{fg}11",
            "activityBar.foreground": fg,
            "activityBar.inactiveForeground": f"{fg}55",
            "editorGroupHeader.tabsBackground": bg,
            "tab.activeBackground": bg,
            "tab.activeForeground": fg,
            "tab.inactiveBackground": bg,
            "tab.inactiveForeground": f"{fg}66",
            "tab.border": f"{fg}11",
            "titleBar.activeBackground": bg,
            "titleBar.activeForeground": fg,
            "titleBar.inactiveBackground": bg,
            "terminal.background": bg,
            "terminal.foreground": fg,
            "statusBar.background": functions if functions else bg,
            "statusBar.foreground": bg,
            "editorLineNumber.foreground": f"{comments}55" if comments else f"{fg}33",
            "editorLineNumber.activeForeground": keywords if keywords else fg,
            "editor.lineHighlightBackground": f"{fg}08",
            "menu.background": bg,
            "menu.foreground": fg,
            "menu.border": f"{fg}11",
            "menu.separatorBackground": f"{fg}22",
            "menu.selectionBackground": f"{fg}22",
            "menu.selectionForeground": fg,
            "editorWidget.background": bg,
            "editorWidget.border": f"{fg}11",
            "editorWidget.foreground": fg,
            "editorHoverWidget.background": bg,
            "editorHoverWidget.border": f"{fg}11",
            "editorHoverWidget.foreground": fg,
            "dropdown.background": bg,
            "dropdown.foreground": fg,
            "dropdown.border": f"{fg}11",
            "input.background": bg,
            "input.foreground": fg,
            "input.border": f"{fg}11",
            "list.activeSelectionBackground": f"{fg}22",
            "list.activeSelectionForeground": fg,
            "list.hoverBackground": f"{fg}11",
            "list.hoverForeground": fg,
            "list.inactiveSelectionBackground": f"{fg}15",
            "list.inactiveSelectionForeground": fg,
        },
        "tokenColors": [
            {"name": "Comments", "scope": ["comment"], "settings": {"foreground": tokens.get("comments")}},
            {"name": "Keywords", "scope": ["keyword", "storage"], "settings": {"foreground": tokens.get("keywords")}},
            {"name": "Numbers", "scope": ["constant.numeric"], "settings": {"foreground": tokens.get("numbers")}},
            {"name": "Strings", "scope": ["string"], "settings": {"foreground": tokens.get("strings")}},
            {"name": "Types", "scope": ["entity.name.type"], "settings": {"foreground": tokens.get("types")}},
            {"name": "Variables", "scope": ["variable"], "settings": {"foreground": tokens.get("variables")}},
            {"name": "Functions", "scope": ["entity.name.function"], "settings": {"foreground": tokens.get("functions")}}
        ]
    }
    try:
        theme_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        error("ERROR-005")
    try:
        package_file = extensions_dir / "package.json"
        package_file.write_text(
            json.dumps(package_manifest, indent=4, ensure_ascii=False), 
            encoding="utf-8"
        )
        theme_file = theme_dir / "theme.json"
        theme_file.write_text(
            json.dumps(theme_data, indent=4, ensure_ascii=False), 
            encoding="utf-8"
        )      
    except Exception:
        error("ERROR-006")