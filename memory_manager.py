# ============================================================
#  MEMORY MANAGER — память AURA
#  Автор: Миша (CuprumCore)
#  GitHub: https://github.com/CuprumCore
#  Лицензия: MIT
# ============================================================

import os
import re
import json
import sqlite3
from datetime import datetime


# Все пути — от расположения этого файла
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_DIR = os.path.join(SCRIPT_DIR, "memory")
SESSIONS_DIR = os.path.join(MEMORY_DIR, "sessions")
LEARNED_DIR = os.path.join(MEMORY_DIR, "learned")
DB_PATH = os.path.join(MEMORY_DIR, "facts.db")
FACTS_JSON = os.path.join(LEARNED_DIR, "useful_facts.json")

STOP_PHRASES = [
    "привет", "как дела", "как ты", "спасибо", "пока", "до свидания",
    "ок", "окей", "хорошо", "да", "нет", "угу", "ага",
    "что делаешь", "как жизнь", "как настроение",
    "hi", "hello", "hey", "thanks", "thank you", "bye", "goodbye",
    "ok", "okay", "yes", "no", "how are you", "what's up",
]

MIN_QUESTION_LEN = 10
MIN_ANSWER_LEN = 30


class MemoryManager:
    def __init__(self):
        self._init_dirs()
        self._init_db()
        self.session_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.session_file = os.path.join(
            SESSIONS_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.txt")

    def _init_dirs(self):
        os.makedirs(MEMORY_DIR, exist_ok=True)
        os.makedirs(SESSIONS_DIR, exist_ok=True)
        os.makedirs(LEARNED_DIR, exist_ok=True)

    def _init_db(self):
        conn = sqlite3.connect(DB_PATH)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                source TEXT DEFAULT 'llm',
                category TEXT DEFAULT 'general',
                confidence REAL DEFAULT 1.0,
                useful INTEGER DEFAULT 1,
                used_count INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_question ON facts(question)")
        conn.commit()
        conn.close()

    def is_worth_saving(self, question, answer, source="llm", unsure=False):
        """Решает, стоит ли сохранять факт в память."""
        if not question or not answer:
            return False, "пусто"
        q_low = question.lower().strip()
        a_low = answer.lower().strip()
        if len(question) < MIN_QUESTION_LEN:
            return False, "короткий вопрос"
        if len(answer) < MIN_ANSWER_LEN:
            return False, "короткий ответ"
        for phrase in STOP_PHRASES:
            if q_low.startswith(phrase):
                return False, f"болтовня («{phrase}»)"
        if any(x in a_low for x in [
            "я не знаю", "не знаю", "не могу ответить",
            "затрудняюсь", "нет информации",
            "i don't know", "i do not know", "cannot answer",
        ]):
            return False, "не знаю"
        if source == "rag":
            return False, "RAG"
        if unsure:
            return False, "неуверенно"
        if len(question.split()) < 3:
            return False, "мало слов"
        return True, "ok"

    def save_fact(self, question, answer, source="llm",
                  category="general", confidence=1.0, unsure=False):
        """Сохраняет факт, если он прошёл фильтр."""
        worth, reason = self.is_worth_saving(question, answer, source, unsure)
        if not worth:
            self._log_session("SKIP", f"{reason} | Q: {question[:50]}")
            return False
        if self._is_duplicate(question, answer):
            self._log_session("SKIP", f"дубликат | Q: {question[:50]}")
            return False
        conn = sqlite3.connect(DB_PATH)
        conn.execute(
            "INSERT INTO facts (question, answer, source, category, confidence) "
            "VALUES (?, ?, ?, ?, ?)",
            (question.strip(), answer.strip(), source, category, confidence))
        conn.commit()
        conn.close()
        self._append_to_json(question, answer, source, category)
        self._log_session("SAVE", f"Q: {question[:60]}")
        return True

    def _is_duplicate(self, question, answer):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT question FROM facts ORDER BY id DESC LIMIT 100")
        rows = c.fetchall()
        conn.close()
        new_words = set(re.findall(r"\w+", question.lower()))
        for (prev_q,) in rows:
            prev_words = set(re.findall(r"\w+", prev_q.lower()))
            if not new_words or not prev_words:
                continue
            inter = len(new_words & prev_words)
            union = len(new_words | prev_words)
            if union and (inter / union) > 0.8:
                return True
        return False

    def _append_to_json(self, question, answer, source, category):
        try:
            facts = []
            if os.path.isfile(FACTS_JSON):
                with open(FACTS_JSON, "r", encoding="utf-8") as f:
                    facts = json.load(f)
            facts.append({
                "timestamp": datetime.now().isoformat(),
                "question": question.strip(),
                "answer": answer.strip(),
                "source": source,
                "category": category,
            })
            with open(FACTS_JSON, "w", encoding="utf-8") as f:
                json.dump(facts, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[MEMORY] JSON: {e}")

    def find_answer(self, question, threshold=0.6):
        """Ищет похожий вопрос в памяти. Возвращает ответ или None."""
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT question, answer FROM facts WHERE useful=1 "
                  "ORDER BY used_count DESC, id DESC LIMIT 200")
        rows = c.fetchall()
        conn.close()
        new_words = set(re.findall(r"\w+", question.lower()))
        if not new_words:
            return None
        best_answer, best_score = None, 0
        for prev_q, prev_a in rows:
            prev_words = set(re.findall(r"\w+", prev_q.lower()))
            if not prev_words:
                continue
            inter = len(new_words & prev_words)
            union = len(new_words | prev_words)
            score = inter / union if union else 0
            if score > best_score and score >= threshold:
                best_score = score
                best_answer = prev_a
        if best_answer:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("UPDATE facts SET used_count = used_count + 1 "
                         "WHERE answer = ?", (best_answer,))
            conn.commit()
            conn.close()
        return best_answer

    def _log_session(self, tag, message):
        ts = datetime.now().strftime("%H:%M:%S")
        try:
            with open(self.session_file, "a", encoding="utf-8") as f:
                f.write(f"[{ts}] [{tag}] {message}\n")
        except Exception:
            pass

    def log_message(self, role, message):
        self._log_session(role.upper(), message[:200])

    def stats(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM facts WHERE useful=1")
        total = c.fetchone()[0]
        c.execute("SELECT category, COUNT(*) FROM facts WHERE useful=1 "
                  "GROUP BY category ORDER BY COUNT(*) DESC")
        by_cat = c.fetchall()
        conn.close()
        return {"total": total, "by_category": by_cat}

    def search(self, query, limit=10):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT question, answer, category, created_at "
                  "FROM facts WHERE question LIKE ? OR answer LIKE ? LIMIT ?",
                  (f"%{query}%", f"%{query}%", limit))
        results = c.fetchall()
        conn.close()
        return results


if __name__ == "__main__":
    mm = MemoryManager()
    print(f"📁 Папка памяти: {MEMORY_DIR}")
    print(f"🧠 Фактов: {mm.stats()['total']}")