import flet as ft
import random

def main(page: ft.Page):
    page.title = "Typing Test 🕗"
    
    words = ["private", "drawing", "dismissal", "civilization", "advice", "clarify", "perfume", "embark",
             "culture", "resist", "secular", "undertake", "fashionable", "sandwich", "suitcase", "electroencefalografista"]
    
    words_used = []
    random_word = random.choice(words)
    correct_words = 0
    
    def change_word():
        nonlocal random_word
        words_used.append(random_word)
        words_guessed.value = f"{len(words_used)}/{len(words)}"
        if len(words) == len(words_used):
            result.value = f"You've completed the test!\nYou had {round((correct_words/len(words)) * 100, 2)}% accuracy!"
            writing_word.disabled = True
            page.update()
            return
        else:
            while random_word in words_used:
                random_word = random.choice(words)
            word_display.value = random_word
            page.update()

    def check_word(e):
        nonlocal random_word
        nonlocal correct_words
        if writing_word.value == random_word:
            result.value = "Correct!"
            result.color = "green"
            correct_words += 1
        else:
            result.value = "Incorrect!"
            result.color = "red"
        writing_word.value = ""
        change_word()

    word_display = ft.Text(random_word)
    writing_word = ft.TextField(label="Type here", on_submit=check_word)
    words_guessed = ft.Text(f"0/{len(words)}")
    result = ft.Text()

    page.add(word_display, words_guessed, ft.Row([writing_word]), ft.Row([result]))

ft.app(main)