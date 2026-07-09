import os
import time

# Настройки путей (относительно корня репозитория)
FILES_DIR = "mods/files"
OUTPUT_HTML = "mods/index.html"

# HTML-шапка (стилизована под серверный индекс Apache/Nginx)
html_content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Index of /mods/files/</title>
    <style>
        body { font-family: monospace; padding: 20px; background-color: #fff; color: #000; }
        h1 { font-size: 1.5em; font-weight: normal; }
        hr { border: 0; border-top: 1px solid #ccc; }
        a { text-decoration: none; color: #0000ee; }
        a:hover { text-decoration: underline; }
        table { border-collapse: collapse; min-width: 600px; }
        th { text-align: left; padding: 0 20px 10px 0; }
        td { padding: 2px 20px 2px 0; white-space: nowrap; }
    </style>
</head>
<body>
    <h1>Index of /mods/files/</h1>
    <hr>
    <table>
        <tr>
            <th>Name</th>
            <th>Last modified</th>
            <th>Size</th>
        </tr>
        <tr>
            <td><a href="../">../</a></td>
            <td>-</td>
            <td>-</td>
        </tr>
"""

# Читаем файлы, сортируем по алфавиту
try:
    files = sorted(os.listdir(FILES_DIR))
except FileNotFoundError:
    print(f"Ошибка: Папка {FILES_DIR} не найдена!")
    exit(1)

for filename in files:
    file_path = os.path.join(FILES_DIR, filename)
    
    # Пропускаем папки (если вдруг там появятся)
    if not os.path.isfile(file_path):
        continue
        
    # Берем инфу о файле
    stat = os.stat(file_path)
    
    # Форматируем дату, как на сервере Gentoo
    mtime = time.strftime('%d-%b-%Y %H:%M', time.localtime(stat.st_mtime))
    
    # Считаем размер (в KB или MB для красоты)
    size_bytes = stat.st_size
    if size_bytes < 1024 * 1024:
        size_str = f"{size_bytes / 1024:.1f} KB"
    else:
        size_str = f"{size_bytes / (1024 * 1024):.1f} MB"
        
    # Записываем строку таблицы. 
    # ВАЖНО: href ведет на "files/название.jar"
    html_content += f"""
        <tr>
            <td><a href="files/{filename}">{filename}</a></td>
            <td>{mtime}</td>
            <td>{size_str}</td>
        </tr>"""

# Закрываем теги
html_content += """
    </table>
    <hr>
</body>
</html>
"""

# Сохраняем в mods/index.html
with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Успех! Файл {OUTPUT_HTML} сгенерирован. Найдено модов: {len(files)}.")
