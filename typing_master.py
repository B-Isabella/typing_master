import flet as ft
import random

def main(page: ft.Page):
    page.title = "Typing Test 🕗"
    
    words = ["private", "drawing", "dismissal", "civilization", "advice", "clarify", "perfume", "embark",
             "culture", "resist", "secular", "undertake", "fashionable", "sandwich", "suitcase", "electroencefalografista"]
    
    words_used = []
    random_word = random.choice(words)
    correct_words = 0

    word_display = ft.Text(random_word)

    page.add(word_display)

ft.app(main)