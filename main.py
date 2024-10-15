import urwid

# Проверка пароля
def has_digit(password):
    return any(letter.isdigit() for letter in password)

def has_letters(password):
    return any(letter.isalpha() for letter in password)

def has_upper_letters(password):
    return any(letter.isupper() for letter in password)

def has_lower_letters(password):
    return any(letter.islower() for letter in password)

def is_very_long(password):
    return len(password) >= 12

def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)
# Подсчёт рейтинга
def calculate_score(password):
    score = 0

    checks = [
        (has_digit, 2),
        (has_letters, 2),
        (is_very_long, 2),
        (has_upper_letters, 2),
        (has_lower_letters, 2),
        (has_symbols, 2)
    ]
    for check, points in checks:
        if check(password):
            score += points
    
    return score
# Вывод на экран с счётчиком рейтинга
def on_password_change(edit, new_password):
    score = calculate_score(new_password)
    rating_text.set_text(f'Рейтинг пароля: {score}')

edit_password = urwid.Edit('Введите пароль: ')
rating_text = urwid.Text("Рейтинг пароля: 0")

pile = urwid.Pile([edit_password, rating_text])
fill = urwid.Filler(pile)

urwid.connect_signal(edit_password, 'change', on_password_change)

def main():
    loop = urwid.MainLoop(fill)
    loop.run()

if __name__ == "__main__":
    main()