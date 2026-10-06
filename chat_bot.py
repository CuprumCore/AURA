# ============================================================
#  AURA — Artificial Universal Response Assistant
#  Автор: Миша (CuprumCore)
#  GitHub: https://github.com/CuprumCore
#  Версия: 1.0
#  Лицензия: MIT
# ============================================================

# ════════════════════════════════════════════════════════════
#  ОПРЕДЕЛЕНИЕ ЯЗЫКА СИСТЕМЫ
# ════════════════════════════════════════════════════════════
import locale


def detect_language():
    """Определяет язык системы. Возвращает 'ru' или 'en'."""
    # Windows API (самый надёжный)
    try:
        import ctypes
        windll = ctypes.windll.kernel32
        lang_id = windll.GetUserDefaultUILanguage()
        # 0x0419 = 1049 = Russian
        if lang_id in (0x0419, 1049):
            return "ru"
        if lang_id in (0x0422, 1058):  # Ukrainian
            return "ru"  # украинцам тоже русский понятен
        if lang_id in (0x0423, 1059):  # Belarusian
            return "ru"
    except Exception:
        pass

    # Fallback через locale
    try:
        sys_lang = locale.getdefaultlocale()[0]
        if sys_lang and sys_lang.lower().startswith(("ru", "uk", "be")):
            return "ru"
    except Exception:
        pass

    return "en"


LANG = detect_language()


# ════════════════════════════════════════════════════════════
#  ПЕРЕВОДЫ
# ════════════════════════════════════════════════════════════
TEXTS = {
    "ru": {
        # Окно
        "window_title": "AURA — AI Assistant  •  {author}",
        "header_title": "✨  AURA",
        "header_author": "от {author}",
        "btn_logs": "📋 Логи",
        "btn_memory": "📚 Память",
        "btn_about": "ℹ️ О проекте",
        "check_browser": "🌐 Браузер",
        "btn_send": "Отправить",

        # Подсказки
        "tip_logs": "Открыть журнал событий AURA",
        "tip_memory": "Что AURA запомнила — факты, определения",
        "tip_about": "Информация об AURA и авторе",
        "tip_browser": "Открывать браузер с поиском на каждый вопрос",
        "tip_clip": "Открыть папку Загрузки",
        "tip_photo": "Прикрепить фото (или перетащить в окно)",
        "tip_entry": "Введите вопрос или команду. Enter — отправить",
        "tip_send": "Отправить сообщение (Enter)",
        "tip_remove": "Убрать прикреплённое фото",
        "tip_search_mem": "Искать в памяти AURA",
        "tip_clear_log": "Очистить журнал",
        "tip_close": "Закрыть окно",

        # Статусы
        "status_ready": "● готов",
        "status_thinking": "● думаю...",
        "status_vision": "● смотрю фото...",
        "status_searching": "● ищу...",
        "status_error": "● ошибка",

        # Приветствие
        "greeting": (
            "Привет! Я — AURA ✨\n"
            "Твой персональный ИИ-ассистент.\n"
            "Создан: {author}\n\n"
            "• 📎 — папка Загрузки, 📷 — фото.\n"
            "• 📚 Память — что я выучил.\n"
            "• Поиск в интернете — по триггерам "
            "(«найди», «новости», «погода»...) или галочке 🌐."
        ),

        # Сообщения
        "user_label": "Вы",
        "search_title": "🔍 Поиск",
        "searching": "Ищу: «{query}»...",
        "search_found": "✅ Нашёл информацию ({n} символов). Источники — в логах.",
        "search_not_found": "❌ Поиск не дал результатов.",
        "from_memory": "📚 Из памяти",
        "error_label": "Ошибка",
        "photo_caption": "📷 {name}",
        "btn_remove": "✕ Убрать",

        # Окно "О проекте"
        "about_title": "О AURA",
        "about_subtitle": "Artificial Universal Response Assistant",
        "about_version": "Версия:",
        "about_author": "Автор:",
        "about_github": "GitHub:",
        "about_license": "Лицензия:",
        "about_model": "Модель:",
        "about_vision": "Vision:",
        "about_close": "Закрыть",

        # Логи
        "logs_title": "📋 Логи AURA",
        "logs_header": "Журнал событий AURA  •  от {author}",
        "logs_clear": "Очистить",

        # Память
        "memory_title": "📚 Память AURA",
        "memory_header": "🧠 AURA помнит: {n} фактов",
        "memory_search": "🔍 Поиск:",
        "memory_shown": "Показано: {n}",

        # Ошибки
        "err_format": "Формат не поддерживается: {ext}",
        "err_no_file": "Файл не найден: {path}",
        "err_ollama": "Ollama не отвечает. Запусти Ollama и попробуй снова.",
        "err_downloads": "Папка Загрузки не найдена: {path}",
        "err_open_folder": "Не удалось открыть папку: {e}",
        "err_load_image": "Не удалось загрузить изображение: {e}",
        "err_photo": "Ошибка при обработке фото: {e}",

        # Консольные сообщения
        "console_start": "✨ AURA v{version}\n👤 Автор: {author}\n🔗 GitHub: {github}\n📜 Лицензия: {license}",
        "console_lang": "🌐 Язык системы: русский",
        "console_need_ollama": (
            "\n  ❌ Ollama не запущена!\n\n"
            "  Как исправить:\n"
            "     1. Скачай: https://ollama.com/download\n"
            "     2. Установи и запусти (значок ламы в трее)\n"
            "     3. Запусти AURA заново\n"
        ),
        "console_ollama_ok": "  ✅ Ollama работает",
        "console_models_check": "  🔍 Проверяю модели...",
        "console_pulling": "  📥 Скачиваю модель {model}...",
        "console_models_ready": "  ✅ Все модели готовы",
        "console_env_ready": "  ✅ Окружение готово, запускаю AURA...",
        "console_press_enter": "  Нажми Enter для выхода...",
        "console_python_old": "❌ Нужен Python {a}.{b}+",
        "console_libs_missing": "❌ Не установлены библиотеки:",
        "console_libs_install": "Установи командой:\n   pip install {pkgs}",

        # Системный промпт для AI
        "system_prompt": (
            "Ты — AURA, персональный русскоязычный ассистент. "
            "ОТВЕЧАЙ ТОЛЬКО НА РУССКОМ ЯЗЫКЕ. "
            "НИКОГДА не отвечай на английском или других языках. "
            "\n\n"
            "ПРАВИЛА: "
            "• Если пользователь пишет «подробнее», «ещё», «продолжи», «расскажи» — "
            "продолжай ПРЕДЫДУЩУЮ тему, а не начинай новую. "
            "• Смотри на 2-3 последних сообщения, чтобы понять контекст. "
            "• НЕ выдумывай факты. Если не знаешь — скажи «Я не знаю». "
            "• НЕ копируй предыдущие ответы. "
            "• Отвечай кратко и по делу."
        ),
    },

    "en": {
        # Window
        "window_title": "AURA — AI Assistant  •  {author}",
        "header_title": "✨  AURA",
        "header_author": "by {author}",
        "btn_logs": "📋 Logs",
        "btn_memory": "📚 Memory",
        "btn_about": "ℹ️ About",
        "check_browser": "🌐 Browser",
        "btn_send": "Send",

        # Tooltips
        "tip_logs": "Open AURA event log",
        "tip_memory": "What AURA learned — facts, definitions",
        "tip_about": "Information about AURA and the author",
        "tip_browser": "Open browser with search on every question",
        "tip_clip": "Open Downloads folder",
        "tip_photo": "Attach photo (or drag into window)",
        "tip_entry": "Type a question or command. Enter — to send",
        "tip_send": "Send message (Enter)",
        "tip_remove": "Remove attached photo",
        "tip_search_mem": "Search AURA memory",
        "tip_clear_log": "Clear log",
        "tip_close": "Close window",

        # Statuses
        "status_ready": "● ready",
        "status_thinking": "● thinking...",
        "status_vision": "● looking at photo...",
        "status_searching": "● searching...",
        "status_error": "● error",

        # Greeting
        "greeting": (
            "Hi! I'm AURA ✨\n"
            "Your personal AI assistant.\n"
            "Created by: {author}\n\n"
            "• 📎 — Downloads folder, 📷 — photo.\n"
            "• 📚 Memory — what I've learned.\n"
            "• Internet search — by triggers "
            "(\"find\", \"news\", \"weather\"...) or 🌐 checkbox."
        ),

        # Messages
        "user_label": "You",
        "search_title": "🔍 Search",
        "searching": "Searching: \"{query}\"...",
        "search_found": "✅ Found info ({n} chars). Sources in logs.",
        "search_not_found": "❌ Search returned no results.",
        "from_memory": "📚 From memory",
        "error_label": "Error",
        "photo_caption": "📷 {name}",
        "btn_remove": "✕ Remove",

        # About window
        "about_title": "About AURA",
        "about_subtitle": "Artificial Universal Response Assistant",
        "about_version": "Version:",
        "about_author": "Author:",
        "about_github": "GitHub:",
        "about_license": "License:",
        "about_model": "Model:",
        "about_vision": "Vision:",
        "about_close": "Close",

        # Logs
        "logs_title": "📋 AURA Logs",
        "logs_header": "AURA event log  •  by {author}",
        "logs_clear": "Clear",

        # Memory
        "memory_title": "📚 AURA Memory",
        "memory_header": "🧠 AURA remembers: {n} facts",
        "memory_search": "🔍 Search:",
        "memory_shown": "Shown: {n}",

        # Errors
        "err_format": "Format not supported: {ext}",
        "err_no_file": "File not found: {path}",
        "err_ollama": "Ollama is not responding. Start Ollama and try again.",
        "err_downloads": "Downloads folder not found: {path}",
        "err_open_folder": "Could not open folder: {e}",
        "err_load_image": "Could not load image: {e}",
        "err_photo": "Photo processing error: {e}",

        # Console
        "console_start": "✨ AURA v{version}\n👤 Author: {author}\n🔗 GitHub: {github}\n📜 License: {license}",
        "console_lang": "🌐 System language: English",
        "console_need_ollama": (
            "\n  ❌ Ollama is not running!\n\n"
            "  How to fix:\n"
            "     1. Download: https://ollama.com/download\n"
            "     2. Install and run (llama icon in tray)\n"
            "     3. Start AURA again\n"
        ),
        "console_ollama_ok": "  ✅ Ollama is running",
        "console_models_check": "  🔍 Checking models...",
        "console_pulling": "  📥 Pulling model {model}...",
        "console_models_ready": "  ✅ All models ready",
        "console_env_ready": "  ✅ Environment ready, starting AURA...",
        "console_press_enter": "  Press Enter to exit...",
        "console_python_old": "❌ Python {a}.{b}+ required",
        "console_libs_missing": "❌ Missing libraries:",
        "console_libs_install": "Install with:\n   pip install {pkgs}",

        # AI system prompt
        "system_prompt": (
            "You are AURA, a personal AI assistant. "
            "ALWAYS REPLY IN ENGLISH. "
            "NEVER reply in other languages. "
            "\n\n"
            "RULES: "
            "• If user writes \"more\", \"continue\", \"tell me more\" — "
            "continue the PREVIOUS topic, don't start a new one. "
            "• Look at the last 2-3 messages to understand context. "
            "• DO NOT make up facts. If you don't know — say \"I don't know\". "
            "• DO NOT copy previous answers. "
            "• Be concise and to the point."
        ),
    },
}


def t(key, **kwargs):
    """Получить перевод по ключу."""
    text = TEXTS.get(LANG, TEXTS["en"]).get(key)
    if text is None:
        text = TEXTS["en"].get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


# ════════════════════════════════════════════════════════════
#  ПРОВЕРКА ОКРУЖЕНИЯ
# ════════════════════════════════════════════════════════════
import os
import sys
import subprocess
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MIN_PYTHON = (3, 9)

if sys.version_info < MIN_PYTHON:
    print(t("console_python_old", a=MIN_PYTHON[0], b=MIN_PYTHON[1]))
    print(f"   You have: {sys.version_info.major}.{sys.version_info.minor}")
    input(t("console_press_enter"))
    sys.exit(1)


def _run_installer():
    installer = os.path.join(SCRIPT_DIR, "install.bat")
    if not os.path.isfile(installer):
        return False
    print("\n⚠ Running install.bat...\n")
    time.sleep(2)
    try:
        subprocess.Popen(["cmd", "/c", "start", "", installer], cwd=SCRIPT_DIR)
    except Exception as e:
        print(f"Failed to run installer: {e}")
        return False
    return True


REQUIRED = {
    "requests": "requests",
    "bs4": "beautifulsoup4",
    "duckduckgo_search": "duckduckgo-search",
    "PIL": "pillow",
    "pystray": "pystray",
    "lxml": "lxml",
}

missing = []
for mod, pip_name in REQUIRED.items():
    try:
        __import__(mod)
    except ImportError:
        missing.append(pip_name)

if missing:
    print("=" * 60)
    print(t("console_libs_missing"))
    for pkg in missing:
        print(f"   • {pkg}")
    print("=" * 60)
    print()
    print(t("console_libs_install", pkgs=" ".join(missing)))
    print()
    input(t("console_press_enter"))
    sys.exit(1)

try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False


# ════════════════════════════════════════════════════════════
#  КОНФИГ
# ════════════════════════════════════════════════════════════
import json

CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")

DEFAULT_CONFIG = {
    "chat_model": "qwen2.5:3b",
    "vision_model": "qwen2.5vl:3b",
    "keep_alive": "30m",
    "num_predict": 256,
    "num_ctx": 2048,
    "auto_pull_models": True,
    "language": "auto",  # auto / ru / en
}

if os.path.isfile(CONFIG_PATH):
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            user_config = json.load(f)
        config = {**DEFAULT_CONFIG, **user_config}
    except Exception as e:
        print(f"⚠ config.json error ({e}), using defaults")
        config = DEFAULT_CONFIG.copy()
else:
    config = DEFAULT_CONFIG.copy()
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"✅ Created {CONFIG_PATH}")
    except Exception:
        pass

# Переопределяем язык, если задан вручную в конфиге
if config.get("language") in ("ru", "en"):
    LANG = config["language"]


# ════════════════════════════════════════════════════════════
#  ПРОВЕРКА OLLAMA
# ════════════════════════════════════════════════════════════
import requests

OLLAMA_HOST = "http://localhost:11434"


def is_ollama_running():
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def get_installed_models():
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
        r.raise_for_status()
        return [m["name"] for m in r.json().get("models", [])]
    except Exception:
        return []


def model_is_installed(model_name):
    installed = get_installed_models()
    base = model_name.split(":")[0]
    for m in installed:
        if m == model_name or m.startswith(base + ":"):
            return True
    return False


def pull_model(model_name):
    print(t("console_pulling", model=model_name))
    try:
        result = subprocess.run(["ollama", "pull", model_name], check=False)
        return result.returncode == 0
    except FileNotFoundError:
        print("❌ 'ollama' command not found. Install: https://ollama.com/download")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def check_environment():
    print("=" * 60)
    print("  ✨ AURA — checking environment")
    print("=" * 60)
    print(f"  📁 Project folder: {SCRIPT_DIR}")
    print(f"  🐍 Python {sys.version_info.major}.{sys.version_info.minor}")
    print(t("console_lang"))
    print()

    print("  🔍 Checking Ollama...")
    if not is_ollama_running():
        print(t("console_need_ollama"))
        input(t("console_press_enter"))
        return False
    print(t("console_ollama_ok"))
    print()

    chat_model = config["chat_model"]
    vision_model = config["vision_model"]

    print(t("console_models_check"))
    print(f"     Chat:   {chat_model}")
    print(f"     Vision: {vision_model}")
    print()

    to_pull = []
    if not model_is_installed(chat_model):
        to_pull.append(chat_model)
    if not model_is_installed(vision_model):
        to_pull.append(vision_model)

    if to_pull:
        if config.get("auto_pull_models", True):
            print(f"  📥 Missing {len(to_pull)} models. Downloading...")
            for m in to_pull:
                if not pull_model(m):
                    print(f"\n  ❌ Failed to pull {m}")
                    input(t("console_press_enter"))
                    return False
            print()
            print(t("console_models_ready"))
        else:
            print(f"  ❌ Missing: {', '.join(to_pull)}")
            print(f"  Run: ollama pull {' '.join(to_pull)}")
            input(t("console_press_enter"))
            return False
    else:
        print(t("console_models_ready"))

    print()
    print("=" * 60)
    print(t("console_env_ready"))
    print("=" * 60)
    print()
    time.sleep(1)
    return True


# ════════════════════════════════════════════════════════════
#  ОСНОВНЫЕ ИМПОРТЫ
# ════════════════════════════════════════════════════════════
import tkinter as tk
from tkinter import font as tkfont, filedialog
import threading
import webbrowser
import base64
import re
from datetime import datetime
from urllib.parse import quote_plus, urlparse, urlunparse, unquote, quote
from io import BytesIO

from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

import pystray
from PIL import Image, ImageDraw, ImageTk

from memory_manager import MemoryManager


# ════════════════════════════════════════════════════════════
#  ИНФОРМАЦИЯ О ПРОЕКТЕ
# ════════════════════════════════════════════════════════════
APP_NAME = "AURA"
APP_FULL_NAME = "AURA — AI Assistant"
APP_VERSION = "1.0"
APP_AUTHOR = "Миша (CuprumCore)"
APP_GITHUB = "https://github.com/CuprumCore"
APP_LICENSE = "MIT"

OLLAMA_URL = f"{OLLAMA_HOST}/api/chat"

OLLAMA_MODEL = config["chat_model"]
OLLAMA_VISION_MODEL = config["vision_model"]
KEEP_ALIVE = config.get("keep_alive", "30m")
NUM_PREDICT = config.get("num_predict", 256)
NUM_CTX = config.get("num_ctx", 2048)

SYSTEM_PROMPT = t("system_prompt")

RAG_ENABLED = True
RAG_MAX_PAGES = 3
RAG_MAX_CHARS = 3000
RAG_TIMEOUT = 8
RAG_TOTAL_TIMEOUT = 20

# Цвета (одинаковые для всех языков)
BG_MAIN   = "#1e1e2e"
BG_HEADER = "#11111b"
BG_USER   = "#89b4fa"
BG_BOT    = "#313244"
BG_INPUT  = "#313244"
BG_LOG    = "#181825"
BG_TIP    = "#45475a"
FG_USER   = "#1e1e2e"
FG_BOT    = "#cdd6f4"
FG_ACCENT = "#89b4fa"
FG_STATUS = "#a6e3a1"
FG_ERROR  = "#f38ba8"
FG_LOG    = "#9399b2"
FG_LOGT   = "#6c7086"
FG_LOGS   = "#f9e2af"
FG_LOGTK  = "#a6e3a1"
FG_TIP    = "#f9e2af"
SEL_USER  = "#585b70"
SEL_BOT   = "#45475a"
FG_RAG    = "#cba6f7"
FG_SRC    = "#fab387"
FG_MEM    = "#f9e2af"
FG_AUTHOR = "#cba6f7"

BTN_CLIP_BG    = "#f9e2af"
BTN_PHOTO_BG   = "#f5c2e7"
BTN_SEND_BG    = "#89b4fa"
BTN_LOG_BG     = "#9399b2"
BTN_MEM_BG     = "#f9e2af"
BTN_ABOUT_BG   = "#cba6f7"
BTN_HOVER_BG   = "#89b4fa"
BTN_HOVER_FG   = "#1e1e2e"
BTN_BASE_FG    = "#1e1e2e"

# Триггеры поиска — для обоих языков
SEARCH_TRIGGERS = [
    # Русские
    "найди", "поищи", "погугли", "загугли",
    "в интернете", "в сети", "поиск в",
    "новости", "погода", "курс", "актуальн",
    "сегодня", "сейчас", "свеж", "последн",
    "что нового", "кто выиграл", "котировк",
    # Английские
    "find", "search", "google", "look up",
    "on the internet", "online", "news",
    "weather", "rate", "current", "latest",
    "today", "now", "recent", "who won",
]


def create_tray_image():
    size = 64
    img = Image.new("RGBA", (size, size), (30, 30, 46, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((6, 6, size - 6, size - 6), fill=(137, 180, 250, 255))
    draw.text((16, 22), "AURA", fill=(30, 30, 46, 255))
    return img


def is_internet_available(timeout=3):
    try:
        requests.head("https://duckduckgo.com", timeout=timeout)
        return True
    except Exception:
        return False


def get_downloads_folder():
    return os.path.join(os.path.expanduser("~"), "Downloads")


def clean_url(url):
    try:
        if not url or len(url) > 600:
            return None
        url = url.strip().replace("\n", "").replace("\r", "")
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return None
        try:
            path = unquote(parsed.path)
        except Exception:
            path = parsed.path
        safe_path = quote(path, safe="/:@&=+$,-_.!~*'()")
        return urlunparse((parsed.scheme, parsed.netloc, safe_path,
                           parsed.params, parsed.query, parsed.fragment))
    except Exception:
        return None


class ToolTip:
    def __init__(self, widget, text, delay=400):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip_window = None
        self.after_id = None
        widget.bind("<Enter>", self._on_enter, add="+")
        widget.bind("<Leave>", self._on_leave, add="+")
        widget.bind("<ButtonPress>", self._on_leave, add="+")

    def _on_enter(self, event=None):
        self._cancel()
        self.after_id = self.widget.after(self.delay, self._show)

    def _on_leave(self, event=None):
        self._cancel()
        self._hide()

    def _cancel(self):
        if self.after_id:
            try:
                self.widget.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None

    def _show(self):
        if self.tip_window:
            return
        try:
            x = self.widget.winfo_rootx() + self.widget.winfo_width() // 2
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        except Exception:
            return
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        tw.attributes("-topmost", True)
        frame = tk.Frame(tw, bg=BG_TIP, bd=0)
        frame.pack()
        tk.Label(frame, text=self.text, bg=BG_TIP, fg=FG_TIP,
                 font=("Segoe UI", 9), padx=8, pady=4).pack()

    def _hide(self):
        if self.tip_window:
            try:
                self.tip_window.destroy()
            except Exception:
                pass
            self.tip_window = None


def make_hover_button(parent, text, command,
                      base_bg=BTN_SEND_BG, base_fg=BTN_BASE_FG,
                      hover_bg=BTN_HOVER_BG, hover_fg=BTN_HOVER_FG,
                      font=None, padx=10, pady=4, tooltip=None, **kwargs):
    btn = tk.Button(
        parent, text=text, command=command,
        bg=base_bg, fg=base_fg,
        activebackground=hover_bg, activeforeground=hover_fg,
        relief="flat", bd=0, cursor="hand2",
        font=font, padx=padx, pady=pady,
        **kwargs
    )

    def on_enter(e):
        try:
            btn.config(bg=hover_bg, fg=hover_fg)
        except Exception:
            pass

    def on_leave(e):
        try:
            btn.config(bg=base_bg, fg=base_fg)
        except Exception:
            pass

    btn.bind("<Enter>", on_enter, add="+")
    btn.bind("<Leave>", on_leave, add="+")

    if tooltip:
        ToolTip(btn, tooltip)

    return btn


class ChatBot:
    def __init__(self, root):
        self.root = root
        root.title(t("window_title", author=APP_AUTHOR))
        root.geometry("900x820")
        root.minsize(700, 500)
        root.configure(bg=BG_MAIN)

        self.f_title = tkfont.Font(family="Segoe UI", size=15, weight="bold")
        self.f_name  = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.f_body  = tkfont.Font(family="Segoe UI", size=13)
        self.f_input = tkfont.Font(family="Segoe UI", size=13)
        self.f_btn   = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.f_icon  = tkfont.Font(family="Segoe UI Emoji", size=16)
        self.f_credit = tkfont.Font(family="Segoe UI", size=9, slant="italic")
        self.f_log   = tkfont.Font(family="Consolas", size=10)

        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        self.is_waiting = False
        self.current_bot_text = None
        self.allow_search = tk.BooleanVar(value=False)
        self.last_search_topic = ""

        self.pending_image_path = None
        self.pending_image_b64 = None
        self.pending_image_preview = None
        self._photo_refs = []

        self.log_window = None
        self.log_text = None
        self.tray_icon = None

        self.memory = MemoryManager()
        self.memory_window = None

        # ШАПКА
        header = tk.Frame(root, bg=BG_HEADER, height=60)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)

        tk.Label(header, text=t("header_title"), font=self.f_title,
                 bg=BG_HEADER, fg=FG_ACCENT).pack(side=tk.LEFT, padx=(20, 5))

        tk.Label(header, text=t("header_author", author=APP_AUTHOR),
                 font=self.f_credit,
                 bg=BG_HEADER, fg=FG_AUTHOR).pack(side=tk.LEFT, padx=(0, 20))

        self.status = tk.Label(header, text=t("status_ready"), font=self.f_name,
                               bg=BG_HEADER, fg=FG_STATUS)
        self.status.pack(side=tk.RIGHT, padx=20)

        make_hover_button(
            header, t("btn_logs"), self.toggle_log_window,
            base_bg=BTN_LOG_BG, font=self.f_name, padx=10, pady=4,
            tooltip=t("tip_logs")
        ).pack(side=tk.RIGHT, padx=4, pady=12)

        make_hover_button(
            header, t("btn_memory"), self.show_memory_window,
            base_bg=BTN_MEM_BG, font=self.f_name, padx=10, pady=4,
            tooltip=t("tip_memory")
        ).pack(side=tk.RIGHT, padx=4, pady=12)

        make_hover_button(
            header, t("btn_about"), self.show_about,
            base_bg=BTN_ABOUT_BG, font=self.f_name, padx=10, pady=4,
            tooltip=t("tip_about")
        ).pack(side=tk.RIGHT, padx=4, pady=12)

        self.search_check = tk.Checkbutton(
            header, text=t("check_browser"),
            variable=self.allow_search,
            font=self.f_name, bg=BG_HEADER, fg=FG_LOG,
            selectcolor=BG_HEADER, activebackground=BG_HEADER,
            activeforeground=FG_ACCENT, bd=0,
            highlightthickness=0)
        self.search_check.pack(side=tk.RIGHT, padx=10)
        ToolTip(self.search_check, t("tip_browser"))

        self.preview_frame = tk.Frame(root, bg=BG_MAIN)

        inp_outer = tk.Frame(root, bg=BG_MAIN)
        inp_outer.pack(fill=tk.X, side=tk.BOTTOM, padx=15, pady=(5, 15))

        inp_frame = tk.Frame(inp_outer, bg=BG_INPUT)
        inp_frame.pack(fill=tk.X)

        make_hover_button(
            inp_frame, "📎", self.open_downloads_folder,
            base_bg=BTN_CLIP_BG, font=self.f_icon, padx=10, pady=4,
            tooltip=t("tip_clip")
        ).pack(side=tk.LEFT, padx=(8, 4), pady=6)

        make_hover_button(
            inp_frame, "📷", self.attach_image,
            base_bg=BTN_PHOTO_BG, font=self.f_icon, padx=10, pady=4,
            tooltip=t("tip_photo")
        ).pack(side=tk.LEFT, padx=4, pady=6)

        self.entry = tk.Text(
            inp_frame, font=self.f_input, bg=BG_INPUT, fg=FG_BOT,
            insertbackground=FG_ACCENT, relief="flat",
            height=1, wrap=tk.WORD, padx=14, pady=12,
            borderwidth=0, highlightthickness=0,
        )
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=6)
        self.entry.bind("<Return>", self._on_enter)
        self.entry.bind("<Button-3>", self._entry_context_menu)
        self.entry.focus_set()
        ToolTip(self.entry, t("tip_entry"))

        make_hover_button(
            inp_frame, t("btn_send"), self.send_message,
            base_bg=BTN_SEND_BG, base_fg=BTN_BASE_FG,
            hover_bg="#74c7ec", hover_fg=BTN_HOVER_FG,
            font=self.f_btn, padx=18, pady=10,
            tooltip=t("tip_send")
        ).pack(side=tk.RIGHT, padx=8, pady=6)

        chat_frame = tk.Frame(root, bg=BG_MAIN)
        chat_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(chat_frame, bg=BG_MAIN, highlightthickness=0)
        scrollbar = tk.Scrollbar(chat_frame, orient="vertical",
                                 command=self.canvas.yview,
                                 width=12, relief="flat", borderwidth=0)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.messages_frame = tk.Frame(self.canvas, bg=BG_MAIN)
        self.msgs_window = self.canvas.create_window(
            (0, 0), window=self.messages_frame, anchor="nw"
        )
        self.messages_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.msgs_window, width=e.width)
        )
        self.canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        )

        if DND_AVAILABLE:
            self._setup_drag_and_drop()

        self.add_message(APP_NAME,
                         t("greeting", author=APP_AUTHOR),
                         is_user=False)

        self.log("SYS", "=" * 55)
        self.log("SYS", f"✨ {APP_NAME} v{APP_VERSION}")
        self.log("SYS", f"👤 {APP_AUTHOR}")
        self.log("SYS", f"🔗 {APP_GITHUB}")
        self.log("SYS", f"📜 {APP_LICENSE}")
        self.log("SYS", f"🌐 Language: {LANG}")
        self.log("SYS", f"📁 {SCRIPT_DIR}")
        self.log("SYS", "=" * 55)
        self.log("SYS", f"Model: {OLLAMA_MODEL}")
        self.log("SYS", f"Vision: {OLLAMA_VISION_MODEL}")
        self.log("MEM", f"Facts in memory: {self.memory.stats()['total']}")
        self.log("SYS", "Ready.")

        root.protocol("WM_DELETE_WINDOW", self.quit_app)
        self.start_tray()

    def show_about(self):
        about = tk.Toplevel(self.root)
        about.title(t("about_title"))
        about.geometry("500x420")
        about.configure(bg=BG_MAIN)
        about.resizable(False, False)

        tk.Label(about, text="✨", font=("Segoe UI Emoji", 48),
                 bg=BG_MAIN, fg=FG_ACCENT).pack(pady=(30, 5))

        tk.Label(about, text=APP_NAME,
                 font=("Segoe UI", 24, "bold"),
                 bg=BG_MAIN, fg=FG_ACCENT).pack()

        tk.Label(about, text=t("about_subtitle"),
                 font=("Segoe UI", 11, "italic"),
                 bg=BG_MAIN, fg=FG_LOG).pack(pady=(0, 20))

        info_frame = tk.Frame(about, bg=BG_MAIN)
        info_frame.pack(pady=10)

        info = [
            (t("about_version"), APP_VERSION),
            (t("about_author"), APP_AUTHOR),
            (t("about_github"), APP_GITHUB),
            (t("about_license"), APP_LICENSE),
            (t("about_model"), OLLAMA_MODEL),
            (t("about_vision"), OLLAMA_VISION_MODEL),
        ]

        for label, value in info:
            row = tk.Frame(info_frame, bg=BG_MAIN)
            row.pack(fill=tk.X, pady=3)
            tk.Label(row, text=label, font=("Segoe UI", 10, "bold"),
                     bg=BG_MAIN, fg=FG_LOG, width=12, anchor="w"
                     ).pack(side=tk.LEFT, padx=(30, 5))
            tk.Label(row, text=value, font=("Segoe UI", 10),
                     bg=BG_MAIN, fg=FG_BOT, anchor="w"
                     ).pack(side=tk.LEFT)

        make_hover_button(
            about, t("about_close"), about.destroy,
            base_bg=FG_ACCENT, font=("Segoe UI", 11, "bold"),
            padx=20, pady=8, tooltip=t("tip_close")
        ).pack(pady=25)

    def _setup_drag_and_drop(self):
        for widget in (self.canvas, self.messages_frame, self.entry, self.root):
            try:
                widget.drop_target_register(DND_FILES)
                widget.dnd_bind("<<Drop>>", self._on_drop)
            except Exception:
                pass

    def _on_drop(self, event):
        try:
            paths = self.root.tk.splitlist(event.data)
        except Exception:
            paths = [event.data]
        if not paths:
            return
        path = paths[0].strip("{}").strip()
        ext = os.path.splitext(path)[1].lower()
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"):
            self.show_error(t("err_format", ext=ext))
            return
        self._load_image_from_path(path)

    def start_tray(self):
        image = create_tray_image()
        menu = pystray.Menu(
            pystray.MenuItem(t("show_window") if "show_window" in TEXTS[LANG] else
                             ("Показать" if LANG == "ru" else "Show"),
                             self.show_window, default=True),
            pystray.MenuItem("Скрыть" if LANG == "ru" else "Hide",
                             self.hide_window),
            pystray.MenuItem(t("about_title"),
                             lambda i, it: self.show_about()),
            pystray.MenuItem("Выход" if LANG == "ru" else "Exit",
                             self.quit_app),
        )
        self.tray_icon = pystray.Icon(
            APP_NAME, image,
            f"{APP_NAME} — {APP_AUTHOR}",
            menu
        )
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    def hide_window(self, icon=None, item=None):
        self.root.withdraw()

    def show_window(self, icon=None, item=None):
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def quit_app(self, icon=None, item=None):
        self.log("SYS", "Exit...")
        self._destroy_log_window(reason="exit")
        if self.tray_icon:
            try:
                self.tray_icon.stop()
            except Exception:
                pass
        self.root.after(0, self.root.destroy)

    def toggle_log_window(self):
        if self.log_window is not None and self.log_window.winfo_exists():
            self._destroy_log_window(reason="user closed")
        else:
            self.create_log_window()

    def create_log_window(self):
        self.log_window = tk.Toplevel(self.root)
        self.log_window.title(t("logs_title"))
        self.log_window.geometry("800x600")
        self.log_window.configure(bg=BG_LOG)
        self.log_window.protocol("WM_DELETE_WINDOW",
                                 lambda: self._destroy_log_window("closed"))

        top = tk.Frame(self.log_window, bg=BG_LOG, height=40)
        top.pack(fill=tk.X)
        top.pack_propagate(False)
        tk.Label(top, text=t("logs_header", author=APP_AUTHOR),
                 font=self.f_name, bg=BG_LOG, fg=FG_ACCENT).pack(side=tk.LEFT, padx=15)

        make_hover_button(
            top, t("logs_clear"), self.clear_log,
            base_bg="#f38ba8", font=self.f_name, padx=10, pady=2,
            tooltip=t("tip_clear_log")
        ).pack(side=tk.RIGHT, padx=10, pady=5)

        frame = tk.Frame(self.log_window, bg=BG_LOG)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.log_text = tk.Text(frame, font=self.f_log, bg=BG_LOG, fg=FG_LOG,
                                relief="flat", wrap=tk.WORD, padx=10, pady=10,
                                borderwidth=0, highlightthickness=0)
        sb = tk.Scrollbar(frame, command=self.log_text.yview,
                          width=10, relief="flat", borderwidth=0)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=sb.set)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.log_text.config(state=tk.DISABLED)

        for tag, color in [("time", FG_LOGT), ("USER", FG_ACCENT),
                           ("BOT", FG_LOGTK), ("SYS", FG_LOGS),
                           ("TOOL", FG_STATUS), ("ERR", FG_ERROR),
                           ("RAG", FG_RAG), ("SRC", FG_SRC),
                           ("MEM", FG_MEM)]:
            self.log_text.tag_config(tag, foreground=color)

        self.log("SYS", "Logs window opened.")

    def _destroy_log_window(self, reason=""):
        if self.log_window is not None and self.log_window.winfo_exists():
            try:
                self.log_window.destroy()
            except Exception:
                pass
        self.log_window = None
        self.log_text = None

    def clear_log(self):
        if self.log_text and self.log_window and self.log_window.winfo_exists():
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete("1.0", tk.END)
            self.log_text.config(state=tk.DISABLED)

    def log(self, category, message):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] [{category}] {message}")
        if self.log_text and self.log_window and self.log_window.winfo_exists():
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, f"[{ts}] ", "time")
            self.log_text.insert(tk.END, f"[{category}] ", category)
            self.log_text.insert(tk.END, f"{message}\n")
            self.log_text.config(state=tk.DISABLED)
            self.log_text.see(tk.END)

    def show_memory_window(self):
        if self.memory_window and self.memory_window.winfo_exists():
            self.memory_window.destroy()
            self.memory_window = None
            return

        self.memory_window = tk.Toplevel(self.root)
        self.memory_window.title(t("memory_title"))
        self.memory_window.geometry("800x600")
        self.memory_window.configure(bg=BG_LOG)

        stats = self.memory.stats()

        top = tk.Frame(self.memory_window, bg=BG_LOG, height=80)
        top.pack(fill=tk.X)
        top.pack_propagate(False)
        tk.Label(top, text=t("memory_header", n=stats['total']),
                 font=self.f_title, bg=BG_LOG, fg=FG_MEM).pack(anchor="w",
                                                               padx=15, pady=(10, 2))
        tk.Label(top, text="memory/facts.db  •  memory/learned/useful_facts.json",
                 font=self.f_name, bg=BG_LOG, fg=FG_LOG).pack(anchor="w", padx=15)

        search_frame = tk.Frame(self.memory_window, bg=BG_LOG)
        search_frame.pack(fill=tk.X, padx=15, pady=5)
        tk.Label(search_frame, text=t("memory_search"), font=self.f_name,
                 bg=BG_LOG, fg=FG_MEM).pack(side=tk.LEFT)
        search_entry = tk.Entry(search_frame, font=self.f_body,
                                bg="#313244", fg=FG_BOT,
                                insertbackground=FG_ACCENT,
                                relief="flat")
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True,
                          padx=(8, 8), ipady=4)
        ToolTip(search_entry, t("tip_search_mem"))

        frame = tk.Frame(self.memory_window, bg=BG_LOG)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(5, 15))

        txt = tk.Text(frame, font=self.f_log, bg=BG_LOG, fg=FG_BOT,
                      relief="flat", wrap=tk.WORD, padx=10, pady=10,
                      borderwidth=0, highlightthickness=0)
        sb = tk.Scrollbar(frame, command=txt.yview,
                          width=10, relief="flat", borderwidth=0)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        txt.config(yscrollcommand=sb.set)
        txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        def refresh(query=""):
            txt.config(state=tk.NORMAL)
            txt.delete("1.0", tk.END)
            import sqlite3
            db = os.path.join(SCRIPT_DIR, "memory", "facts.db")
            conn = sqlite3.connect(db)
            c = conn.cursor()
            if query:
                c.execute("SELECT question, answer, category, created_at "
                          "FROM facts WHERE useful=1 AND "
                          "(question LIKE ? OR answer LIKE ?) "
                          "ORDER BY id DESC LIMIT 50",
                          (f"%{query}%", f"%{query}%"))
            else:
                c.execute("SELECT question, answer, category, created_at "
                          "FROM facts WHERE useful=1 ORDER BY id DESC LIMIT 50")
            results = c.fetchall()
            conn.close()

            txt.insert(tk.END, t("memory_shown", n=len(results)) + "\n\n")
            for i, (q, a, cat, created) in enumerate(results, 1):
                txt.insert(tk.END, f"[{i}] {q}\n", "question")
                txt.insert(tk.END, f"    💬 {a}\n", "answer")
                txt.insert(tk.END, f"    📁 {cat}  •  {created}\n\n", "meta")
            txt.config(state=tk.DISABLED)

        txt.tag_config("question", foreground=FG_MEM,
                       font=("Segoe UI", 11, "bold"))
        txt.tag_config("answer", foreground=FG_BOT)
        txt.tag_config("meta", foreground=FG_LOGT, font=("Segoe UI", 9))

        search_entry.bind("<Return>",
                          lambda e: refresh(search_entry.get().strip()))
        search_entry.bind("<KeyRelease>",
                          lambda e: refresh(search_entry.get().strip())
                          if len(search_entry.get()) >= 3 else None)

        refresh()
        search_entry.focus_set()

    def show_copy_menu(self, event, text_widget):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Копировать" if LANG == "ru" else "Copy",
                         command=lambda: self.copy_selection(text_widget))
        menu.add_command(label="Копировать всё" if LANG == "ru" else "Copy all",
                         command=lambda: self.copy_all(text_widget))
        menu.tk_popup(event.x_root, event.y_root)

    def copy_selection(self, text_widget):
        try:
            selected = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)
        except tk.TclError:
            pass

    def copy_all(self, text_widget):
        all_text = text_widget.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(all_text)

    def _entry_context_menu(self, event):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Вставить" if LANG == "ru" else "Paste",
                         command=lambda: self.entry.event_generate("<<Paste>>"))
        menu.tk_popup(event.x_root, event.y_root)

    def open_downloads_folder(self):
        folder = get_downloads_folder()
        self.log("TOOL", f"Opening: {folder}")
        try:
            if os.path.isdir(folder):
                subprocess.Popen(f'explorer "{folder}"')
            else:
                self.show_error(t("err_downloads", path=folder))
        except Exception as e:
            self.show_error(t("err_open_folder", e=e))

    def attach_image(self):
        downloads = get_downloads_folder()
        initialdir = downloads if os.path.isdir(downloads) else os.path.expanduser("~")
        path = filedialog.askopenfilename(
            title="Выберите изображение" if LANG == "ru" else "Select image",
            initialdir=initialdir,
            filetypes=[("Images", "*.png *.jpg *.jpeg *.gif *.bmp *.webp"),
                       ("All files", "*.*")])
        if not path:
            return
        self._load_image_from_path(path)

    def _load_image_from_path(self, path):
        if not os.path.isfile(path):
            self.show_error(t("err_no_file", path=path))
            return
        try:
            with open(path, "rb") as f:
                raw = f.read()
            self.pending_image_b64 = base64.b64encode(raw).decode("utf-8")
            self.pending_image_path = path
            img = Image.open(path)
            img.thumbnail((200, 200))
            self.pending_image_preview = ImageTk.PhotoImage(img)
            self._photo_refs.append(self.pending_image_preview)
            self._show_preview_panel(os.path.basename(path))
            self.log("SYS", f"Attached: {path}")
        except Exception as e:
            self.show_error(t("err_load_image", e=e))

    def _show_preview_panel(self, filename):
        for widget in self.preview_frame.winfo_children():
            widget.destroy()
        self.preview_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=15, pady=(5, 0))
        inner = tk.Frame(self.preview_frame, bg=BG_INPUT)
        inner.pack(fill=tk.X)
        tk.Label(inner, text=t("photo_caption", name=filename), font=self.f_name,
                 bg=BG_INPUT, fg=FG_ACCENT).pack(side=tk.LEFT, padx=10, pady=6)
        tk.Label(inner, image=self.pending_image_preview,
                 bg=BG_INPUT).pack(side=tk.LEFT, padx=5, pady=6)
        make_hover_button(
            inner, t("btn_remove"), self.clear_pending_image,
            base_bg="#f38ba8", font=self.f_name, padx=10, pady=2,
            tooltip=t("tip_remove")
        ).pack(side=tk.RIGHT, padx=10)

    def clear_pending_image(self):
        self.pending_image_path = None
        self.pending_image_b64 = None
        self.pending_image_preview = None
        self.preview_frame.pack_forget()
        self.entry.focus_set()

    def _on_enter(self, event):
        if event.state & 0x0001:
            return None
        self.send_message()
        return "break"

    def add_message(self, sender, text, is_user, is_memory=False):
        container = tk.Frame(self.messages_frame, bg=BG_MAIN)
        container.pack(fill=tk.X, padx=15, pady=4)

        name_color = FG_ACCENT if is_user else (FG_MEM if is_memory else FG_STATUS)
        tk.Label(container, text=sender, font=self.f_name, bg=BG_MAIN,
                 fg=name_color).pack(anchor="e" if is_user else "w", padx=8)

        bubble_bg = BG_USER if is_user else (BG_MEM if is_memory else BG_BOT)
        bubble_fg = FG_USER if is_user else (FG_USER if is_memory else FG_BOT)
        sel_bg = SEL_USER if is_user else SEL_BOT

        bubble = tk.Frame(container, bg=bubble_bg)
        bubble.pack(anchor="e" if is_user else "w", padx=8, pady=(2, 0))

        txt = tk.Text(bubble, font=self.f_body, bg=bubble_bg, fg=bubble_fg,
                      relief="flat", borderwidth=0, highlightthickness=0,
                      wrap=tk.WORD, width=55, height=1, cursor="arrow",
                      padx=14, pady=10,
                      selectbackground=sel_bg, selectforeground=bubble_fg)
        txt.insert("1.0", text)
        txt.config(state=tk.DISABLED)
        txt.pack()
        txt.bind("<Button-3>", lambda e, t=txt: self.show_copy_menu(e, t))

        self.autosize_text(txt)
        self.scroll_to_bottom()
        return txt

    def add_image_message(self, sender, image_b64, caption):
        container = tk.Frame(self.messages_frame, bg=BG_MAIN)
        container.pack(fill=tk.X, padx=15, pady=4)
        tk.Label(container, text=sender, font=self.f_name,
                 bg=BG_MAIN, fg=FG_ACCENT).pack(anchor="e", padx=8)
        bubble = tk.Frame(container, bg=BG_USER)
        bubble.pack(anchor="e", padx=8, pady=(2, 0))
        try:
            raw = base64.b64decode(image_b64)
            img = Image.open(BytesIO(raw))
            img.thumbnail((280, 280))
            photo = ImageTk.PhotoImage(img)
            self._photo_refs.append(photo)
            tk.Label(bubble, image=photo, bg=BG_USER).pack(padx=10, pady=(10, 4))
        except Exception as e:
            self.log("ERR", f"Photo error: {e}")
        if caption:
            tk.Label(bubble, text=caption, font=self.f_body,
                     bg=BG_USER, fg=FG_USER, wraplength=400,
                     justify="left").pack(padx=10, pady=(4, 10), anchor="w")
        self.scroll_to_bottom()

    def autosize_text(self, txt_widget):
        try:
            txt_widget.update_idletasks()
            result = txt_widget.count("1.0", "end", "displaylines")
            lines = result[0] if result else 1
            txt_widget.config(height=max(1, lines))
        except Exception:
            pass

    def set_text_content(self, txt_widget, content):
        txt_widget.config(state=tk.NORMAL)
        txt_widget.delete("1.0", tk.END)
        txt_widget.insert("1.0", content)
        txt_widget.config(state=tk.DISABLED)
        self.autosize_text(txt_widget)

    def scroll_to_bottom(self):
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def send_message(self):
        if self.is_waiting:
            return
        text = self.entry.get("1.0", tk.END).strip()

        if self.pending_image_b64:
            self._send_with_image(text)
            return

        if not text:
            return

        self.entry.delete("1.0", tk.END)
        self.add_message(t("user_label"), text, is_user=True)
        self.messages.append({"role": "user", "content": text})
        self.log("USER", text)
        self.memory.log_message("USER", text)

        self.is_waiting = True
        self.status.config(text=t("status_thinking"), fg=FG_ACCENT)
        self.current_bot_text = self.add_message(APP_NAME, "…", is_user=False)

        threading.Thread(target=self.process_query,
                         args=(text,), daemon=True).start()

    def _send_with_image(self, text):
        if not text:
            text = "Что на этом изображении?" if LANG == "ru" else "What's in this image?"
        self.entry.delete("1.0", tk.END)
        self.add_image_message(t("user_label"), self.pending_image_b64, text)
        img_b64 = self.pending_image_b64
        self.messages.append({"role": "user", "content": text, "images": [img_b64]})
        self.log("USER", f"[PHOTO] {text}")
        self.clear_pending_image()
        self.is_waiting = True
        self.status.config(text=t("status_vision"), fg=FG_ACCENT)
        self.current_bot_text = self.add_message(APP_NAME, "…", is_user=False)
        threading.Thread(target=self.query_vision, daemon=True).start()

    def query_vision(self):
        payload = {
            "model": OLLAMA_VISION_MODEL,
            "messages": self.messages,
            "stream": False,
            "keep_alive": KEEP_ALIVE,
        }
        try:
            self.log("SYS", "Sending photo...")
            r = requests.post(OLLAMA_URL, json=payload, timeout=300)
            r.raise_for_status()
            reply = r.json().get("message", {}).get("content", "").strip() or "(empty)"
            self.messages.append({"role": "assistant", "content": reply})
            self.log("BOT", reply)
            self.root.after(0, self.set_text_content, self.current_bot_text, reply)
            self.root.after(0, self.finish_reply, reply)
        except Exception as e:
            self.log("ERR", f"Vision: {e}")
            self.root.after(0, self.show_error, str(e))

    def process_query(self, user_query):
        try:
            if self.allow_search.get():
                self.log("SYS", "Browser search...")
                keywords = self._simple_search_query(user_query)
                self.last_search_topic = keywords
                self.open_browser(keywords)
            self.log("SYS", "Query to Ollama...")
            self.query_ollama_stream()
        except Exception as e:
            self.log("ERR", f"Critical: {e}")
            self.root.after(0, self.show_error, str(e))

    def ddg_search(self, query, max_results=RAG_MAX_PAGES):
        try:
            self.log("RAG", f"Search: «{query}»")
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=max_results * 2))
            urls = []
            for r in results:
                raw = r.get("href", "")
                if not raw:
                    continue
                cleaned = clean_url(raw)
                if cleaned and cleaned not in urls:
                    urls.append(cleaned)
                if len(urls) >= max_results:
                    break
            self.log("RAG", f"Links: {len(urls)}")
            return urls
        except Exception as e:
            self.log("ERR", f"DDG: {e}")
            return []

    def fetch_page_text(self, url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers, timeout=RAG_TIMEOUT,
                             allow_redirects=True)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "lxml")
            for tag in soup(["script", "style", "nav", "footer",
                             "header", "aside", "form"]):
                tag.decompose()
            text = soup.get_text(separator=" ", strip=True)
            text = re.sub(r"\s+", " ", text)
            return text[:RAG_MAX_CHARS]
        except Exception as e:
            self.log("RAG", f"  ✗ {url[:50]} — {e}")
            return ""

    def rag_search_and_read(self, query):
        urls = self.ddg_search(query)
        if not urls:
            self.log("RAG", "No links found")
            return ""

        self.log("RAG", "=" * 50)
        self.log("RAG", f"📚 SOURCES: «{query}»")
        for i, u in enumerate(urls, 1):
            self.log("RAG", f"  [{i}] {u}")
        self.log("RAG", "=" * 50)

        start_time = time.time()
        contexts = []
        used = []
        for i, url in enumerate(urls, 1):
            if time.time() - start_time > RAG_TOTAL_TIMEOUT:
                self.log("RAG", f"Timeout ({RAG_TOTAL_TIMEOUT}s)")
                break
            txt = self.fetch_page_text(url)
            if txt:
                contexts.append(f"[Source {i}] ({url}): {txt}")
                used.append((i, url, len(txt)))
                self.log("RAG", f"  ✓ [{i}] {len(txt)} chars")
            if len(contexts) >= RAG_MAX_PAGES:
                break

        if not contexts:
            return ""

        combined = "\n\n".join(contexts)
        return combined

    def _simple_search_query(self, text):
        stop_ru = ["найди", "поищи", "погугли", "загугли", "пожалуйста",
                   "в интернете", "в сети", "мне", "нужно", "давай",
                   "расскажи", "покажи", "а", "и", "что", "как", "где",
                   "когда", "почему", "какой", "какая", "какие", "такое"]
        stop_en = ["find", "search", "google", "look", "up", "please",
                   "on", "the", "internet", "online", "me", "need",
                   "tell", "show", "and", "what", "how", "where",
                   "when", "why", "which", "such", "a", "an"]
        stop = stop_ru + stop_en
        words = text.split()
        result = []
        for w in words:
            wl = w.lower().strip("?!.,:;")
            if wl not in stop and len(wl) > 1:
                result.append(w)
        query = " ".join(result) if result else text
        return query[:100]

    def _needs_search(self, text):
        low = text.lower()
        for kw in SEARCH_TRIGGERS:
            if kw in low:
                return True, kw
        return False, None

    def _similar_to_previous(self, new_text, threshold=0.7):
        if not new_text:
            return False
        new_words = set(re.findall(r"\w+", new_text.lower()))
        if len(new_words) < 5:
            return False
        for m in reversed(self.messages[-10:]):
            if m.get("role") != "assistant":
                continue
            prev = m.get("content", "")
            if not isinstance(prev, str) or not prev:
                continue
            prev_words = set(re.findall(r"\w+", prev.lower()))
            if not prev_words:
                continue
            inter = len(new_words & prev_words)
            union = len(new_words | prev_words)
            if union and (inter / union) > threshold:
                return True
        return False

    def query_ollama_stream(self):
        last_user_msg = ""
        for m in reversed(self.messages):
            if m.get("role") == "user" and isinstance(m.get("content"), str):
                last_user_msg = m["content"]
                break

        # Контекст для коротких продолжений — RU + EN
        short_continuations = [
            "подробнее", "ещё", "продолжи", "дальше",
            "расскажи", "и что", "а что", "почему",
            "а почему", "как именно",
            "more", "continue", "tell me more", "and what",
            "why", "how exactly", "go on"
        ]
        low = last_user_msg.lower().strip().rstrip("?!.")
        if (any(low == w or low.startswith(w) for w in short_continuations)
                and len(low) < 40):
            topic = ""
            for m in reversed(self.messages[:-1]):
                if m.get("role") == "user" and isinstance(m.get("content"), str):
                    c_text = m["content"].strip()
                    if (c_text.lower().rstrip("?!.") not in short_continuations
                            and len(c_text) > 5):
                        topic = c_text
                        break
            if topic:
                if LANG == "ru":
                    hint = (f"ВАЖНО: пользователь просит подробнее про: «{topic}». "
                            f"Отвечай ТОЛЬКО НА РУССКОМ по этой теме.")
                else:
                    hint = (f"IMPORTANT: user wants more details about: \"{topic}\". "
                            f"Reply ONLY IN ENGLISH on this topic.")
                self.messages.append({"role": "system", "content": hint})
                self.log("SYS", f"Context hint: «{topic}»")

        cached = self.memory.find_answer(last_user_msg, threshold=0.75)
        if cached:
            self.log("MEM", "📚 From memory")
            self.messages.append({"role": "assistant", "content": cached})
            self.root.after(0, self.add_message, t("from_memory"), cached, False, True)
            self.root.after(0, self.finish_reply, cached)
            return

        rag_context = ""
        internet_ok = is_internet_available()
        need_search = False
        trigger = None

        if not internet_ok:
            self.log("RAG", "No internet")
        else:
            need_search, trigger = self._needs_search(last_user_msg)
            if self.allow_search.get() and not need_search:
                need_search = True
                trigger = "checkbox 🌐"

            if need_search:
                self.log("RAG", f"Trigger: «{trigger}»")
            else:
                self.log("RAG", "No triggers — answering myself")

        if need_search:
            self.status.config(text=t("status_searching"), fg=FG_RAG)
            search_query = self._simple_search_query(last_user_msg)
            self.log("RAG", f"Query: «{search_query}»")

            placeholder = self.add_message(
                t("search_title"), t("searching", query=search_query), False
            )

            rag_context = self.rag_search_and_read(search_query)

            if rag_context:
                self.root.after(0, self.set_text_content, placeholder,
                                t("search_found", n=len(rag_context)))
                self.messages.append({
                    "role": "system",
                    "content": "WEB INFO (use only this):\n\n" + rag_context
                })
            else:
                self.root.after(0, self.set_text_content, placeholder,
                                t("search_not_found"))
                self.messages.append({
                    "role": "system",
                    "content": "Search gave no results. If you don't know — say so honestly."
                })

        payload = {
            "model": OLLAMA_MODEL,
            "messages": self.messages,
            "stream": True,
            "keep_alive": KEEP_ALIVE,
            "options": {
                "temperature": 0.3,
                "num_predict": NUM_PREDICT,
                "num_ctx": NUM_CTX,
            },
        }
        try:
            with requests.post(OLLAMA_URL, json=payload,
                               stream=True, timeout=300) as r:
                r.raise_for_status()
                full = ""
                token_count = 0
                first = True
                for line in r.iter_lines():
                    if not line:
                        continue
                    try:
                        chunk = json.loads(line.decode("utf-8"))
                    except json.JSONDecodeError:
                        continue
                    token = chunk.get("message", {}).get("content", "")
                    if token:
                        full += token
                        token_count += 1
                        if first:
                            first = False
                            self.root.after(0, self.set_first_token, token)
                        else:
                            self.root.after(0, self.append_token, token)
                    if chunk.get("done"):
                        break

            if self._similar_to_previous(full) and not rag_context:
                self.log("RAG", "Answer similar to previous")

            self.log("SYS", f"Answer ({token_count} tokens).")
            self.messages.append({"role": "assistant", "content": full})

            source = "rag" if rag_context else "llm"
            saved = self.memory.save_fact(last_user_msg, full,
                                          source=source, unsure=False)
            if saved:
                self.log("MEM", "Fact saved")
            self.memory.log_message("BOT", full)

            self.root.after(0, self.finish_reply, full)

        except requests.exceptions.ConnectionError:
            self.log("ERR", "Ollama not responding")
            self.root.after(0, self.show_error, t("err_ollama"))
        except Exception as e:
            self.log("ERR", f"Error: {e}")
            self.root.after(0, self.show_error, str(e))

    def set_first_token(self, token):
        if self.current_bot_text:
            self.set_text_content(self.current_bot_text, token)
            self.scroll_to_bottom()

    def append_token(self, token):
        if self.current_bot_text:
            current = self.current_bot_text.get("1.0", tk.END).rstrip("\n")
            self.set_text_content(self.current_bot_text, current + token)
            self.scroll_to_bottom()

    def finish_reply(self, full_text):
        self.is_waiting = False
        self.status.config(text=t("status_ready"), fg=FG_STATUS)
        self.entry.focus_set()
        self.current_bot_text = None
        self.log("SYS", "Ready.")

    def show_error(self, text):
        self.add_message(t("error_label"), text, is_user=False)
        self.is_waiting = False
        self.status.config(text=t("status_error"), fg=FG_ERROR)
        self.entry.focus_set()


# ============================================================
if __name__ == "__main__":
    if not check_environment():
        sys.exit(0)

    print("=" * 60)
    print(f"  ✨ {APP_NAME} v{APP_VERSION}")
    print(f"  👤 {APP_AUTHOR}")
    print(f"  🔗 {APP_GITHUB}")
    print(f"  📜 {APP_LICENSE}")
    print(f"  🌐 Language: {LANG}")
    print("=" * 60)
    print()

    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    app = ChatBot(root)
    root.mainloop()