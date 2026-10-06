@echo off
chcp 65001 >nul
title AURA — Установка / Installation
color 0B

echo.
echo ============================================================
echo   AURA - AI Assistant
echo   Автор / Author: Миша (CuprumCore)
echo   GitHub: https://github.com/CuprumCore
echo ============================================================
echo.
echo   Этот установщик / This installer:
echo     1. Проверит Python          / Check Python
echo     2. Установит библиотеки     / Install libraries
echo     3. Проверит/установит Ollama / Check/install Ollama
echo     4. Скачает модели           / Download models
echo     5. Создаст ярлык            / Create shortcut
echo.
echo ============================================================
echo.
pause

cd /d "%~dp0"

REM ════════════════════════════════════════════════
REM  1. ПРОВЕРКА PYTHON
REM ════════════════════════════════════════════════
echo.
echo [1/5] Проверяю Python...

python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if errorlevel 1 (
        echo.
        echo  ============================================
        echo   Python не найден! / Python not found!
        echo  ============================================
        echo.
        echo  Установи Python 3.14+ / Install Python 3.14+:
        echo     https://www.python.org/downloads/
        echo.
        echo  ВАЖНО / IMPORTANT:
        echo     Отметь галочку "Add Python to PATH"
        echo     Check "Add Python to PATH"
        echo.
        echo  Открыть сайт? / Open site? (y/n)
        set /p open="> "
        if /i "%open%"=="y" (
            start https://www.python.org/downloads/
        )
        pause
        exit /b 1
    ) else (
        set "PY_CMD=py"
    )
) else (
    set "PY_CMD=python"
)

%PY_CMD% --version
echo  ✅ Python найден / found
echo.

REM ════════════════════════════════════════════════
REM  2. УСТАНОВКА БИБЛИОТЕК
REM ════════════════════════════════════════════════
echo [2/5] Устанавливаю библиотеки / Installing libraries...
echo.

%PY_CMD% -m pip install --upgrade pip --quiet
%PY_CMD% -m pip install requests beautifulsoup4 duckduckgo-search pillow pystray lxml tkinterdnd2 colorama

if errorlevel 1 (
    echo.
    echo  ⚠ Некоторые библиотеки не установились
    echo  ⚠ Some libraries failed
    echo.
    echo  Попробуй вручную / Try manually:
    echo     pip install -r requirements.txt
    echo.
    pause
) else (
    echo  ✅ Библиотеки установлены / Libraries installed
)
echo.

REM ════════════════════════════════════════════════
REM  3. ПРОВЕРКА OLLAMA
REM ════════════════════════════════════════════════
echo [3/5] Проверяю Ollama / Checking Ollama...

where ollama >nul 2>&1
if errorlevel 1 (
    echo.
    echo  ⚠ Ollama не найдена в PATH / not found in PATH
    echo.
    echo  Варианты / Options:
    echo     [1] Скачать установщик автоматически
    echo         Download installer automatically
    echo     [2] Открыть сайт для ручной установки
    echo         Open site for manual install
    echo     [3] У меня уже установлена, но не в PATH
    echo         Already installed, but not in PATH
    echo     [4] Пропустить / Skip
    echo.
    set /p choice="Выбор / Choice [1-4]: "
    
    if "%choice%"=="1" goto download_ollama
    if "%choice%"=="2" goto open_ollama_site
    if "%choice%"=="3" goto find_ollama
    if "%choice%"=="4" goto skip_ollama
    goto download_ollama
)

:download_ollama
    echo.
    echo  📥 Скачиваю Ollama / Downloading Ollama...
    echo     Размер ~700 МБ / Size ~700 MB
    echo.
    
    powershell -Command "try { Invoke-WebRequest -Uri 'https://ollama.com/download/OllamaSetup.exe' -OutFile '%TEMP%\OllamaSetup.exe' -UseBasicParsing } catch { exit 1 }"
    
    if not exist "%TEMP%\OllamaSetup.exe" (
        echo.
        echo  ❌ Не удалось скачать / Download failed
        echo.
        echo  Скачай вручную / Download manually:
        echo     https://ollama.com/download
        echo.
        pause
        exit /b 1
    )
    
    echo  📥 Запускаю установку / Running installer...
    echo.
    echo  ⚠ ВАЖНО / IMPORTANT:
    echo     Откроется окно установщика Ollama.
    echo     Нажми кнопку "Install".
    echo     Дождись окончания установки.
    echo.
    echo     An Ollama installer window will open.
    echo     Click "Install" button.
    echo     Wait for installation to complete.
    echo.
    pause
    
    start /wait "" "%TEMP%\OllamaSetup.exe"
    
    echo.
    echo  ⏳ Жду 10 секунд / Waiting 10 seconds...
    timeout /t 10 /nobreak >nul
    
    where ollama >nul 2>&1
    if errorlevel 1 (
        echo.
        echo  ⚠ Ollama установлена, но не в PATH.
        echo  ⚠ Installed, but not in PATH.
        echo.
        echo  Что делать / What to do:
        echo     1. Перезагрузи компьютер / Reboot PC
        echo     2. Запусти AURA через run.bat
        echo.
        echo  Или найди ollama.exe и добавь в PATH вручную.
        echo  Or find ollama.exe and add to PATH manually.
        echo.
        pause
        goto skip_ollama
    ) else (
        echo  ✅ Ollama установлена / installed
    )
    goto after_ollama

:open_ollama_site
    start https://ollama.com/download
    echo.
    echo  Открыл сайт / Opened site. Установи Ollama вручную.
    echo  Install Ollama manually, then run install.bat again.
    pause
    exit /b 0

:find_ollama
    echo.
    echo  Ищу ollama.exe на диске / Searching for ollama.exe...
    echo.
    for /f "delims=" %%i in ('dir /s /b "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" 2^>nul') do (
        echo  Найдено / Found: %%i
        set "OLLAMA_PATH=%%i"
        goto found_ollama
    )
    for /f "delims=" %%i in ('dir /s /b "%PROGRAMFILES%\Ollama\ollama.exe" 2^>nul') do (
        echo  Найдено / Found: %%i
        set "OLLAMA_PATH=%%i"
        goto found_ollama
    )
    echo  ❌ Не нашёл / Not found. Установи через вариант 1.
    pause
    exit /b 1

:found_ollama
    echo.
    echo  ✅ Использую / Using: %OLLAMA_PATH%
    echo.
    echo  Запускаю Ollama в фоне / Starting Ollama...
    start "" "%OLLAMA_PATH%" serve
    timeout /t 5 /nobreak >nul
    goto after_ollama

:skip_ollama
    echo  ⏭ Пропускаю Ollama / Skipping Ollama
    goto after_models

:after_ollama
echo.

REM ════════════════════════════════════════════════
REM  4. СКАЧИВАНИЕ МОДЕЛЕЙ
REM ════════════════════════════════════════════════
echo [4/5] Скачиваю модели / Downloading models (~5 GB)...
echo   Это займёт 5-15 минут / This will take 5-15 min
echo.

REM Проверяем, запущена ли Ollama
timeout /t 3 /nobreak >nul

echo   📥 Модель 1/2: qwen2.5:3b (текст / text)
ollama pull qwen2.5:3b
if errorlevel 1 (
    echo.
    echo  ⚠ Не удалось скачать qwen2.5:3b
    echo  ⚠ Failed to pull qwen2.5:3b
    echo.
    echo  Проверь / Check:
    echo     1. Ollama запущена? / Ollama running?
    echo     2. Интернет работает? / Internet works?
    echo     3. Свободно 3 ГБ? / 3 GB free?
    echo.
)
echo.

echo   📥 Модель 2/2: qwen2.5vl:3b (фото / vision)
ollama pull qwen2.5vl:3b
if errorlevel 1 (
    echo.
    echo  ⚠ Не удалось скачать qwen2.5vl:3b
    echo  ⚠ Failed to pull qwen2.5vl:3b
    echo.
)
echo.

:after_models
echo  ✅ Проверка моделей завершена / Model check done
echo.

REM ════════════════════════════════════════════════
REM  5. СОЗДАНИЕ ЯРЛЫКА
REM ════════════════════════════════════════════════
echo [5/5] Создаю ярлык / Creating shortcut...
echo.

if not exist "run.bat" (
    (
        echo @echo off
        echo chcp 65001 ^>nul
        echo cd /d "%%~dp0"
        echo start "" pythonw chat_bot.py
    ) > run.bat
)

powershell -Command ^
    "$ws = New-Object -ComObject WScript.Shell; " ^
    "$sc = $ws.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\AURA.lnk'); " ^
    "$sc.TargetPath = '%CD%\run.bat'; " ^
    "$sc.WorkingDirectory = '%CD%'; " ^
    "$sc.Description = 'AURA - AI Assistant'; " ^
    "$sc.Save()"

echo  ✅ Ярлык "AURA" на рабочем столе / Shortcut on Desktop
echo.

echo ============================================================
echo   ✅ Установка завершена! / Installation complete!
echo ============================================================
echo.
echo   Что дальше / What's next:
echo     1. Запусти AURA через ярлык на рабочем столе
echo        Run AURA via Desktop shortcut
echo     2. Или через run.bat в этой папке
echo        Or via run.bat in this folder
echo.
echo   Запустить сейчас? / Run now? (y/n)
set /p launch="> "
if /i "%launch%"=="y" (
    if exist "run.bat" (
        start "" run.bat
    ) else (
        start "" pythonw chat_bot.py
    )
)
echo.
pause