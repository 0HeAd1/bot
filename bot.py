import telebot
from telebot import types
import math

bot = telebot.TeleBot('6244796995:AAHd9LHkSI9VtyAW7TnjigC8DqD--kQbJHE')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Салам, {message.from_user.first_name}! Що ви хочете вирішити?")
    bot.send_message(message.chat.id, f"Напишіть слово 'кіт' щоб продовжити")


@bot.message_handler(func=lambda message: message.text.lower() == 'кіт')
def st(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Квадратне рівняння')
    button2 = types.KeyboardButton('Кубічне рівняння')
    button3 = types.KeyboardButton('Біквадратне рівняння')
    button4 = types.KeyboardButton('Теорема Косинусів')
    button5 = types.KeyboardButton('Косинус кута між двома векторами')
    button6 = types.KeyboardButton('Підтримка')
    keyboard.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, "Виберіть опцію:", reply_markup=keyboard)
    bot.register_next_step_handler(message, choose)


def choose(message):
    if message.text == 'Квадратне рівняння':
        bot.register_next_step_handler(message, kvad_riv_command)
    elif message.text == 'Кубічне рівняння':
        bot.register_next_step_handler(message, kub_riv_command)
    elif message.text == 'Біквадратне рівняння':
        bot.register_next_step_handler(message, bikvad_riv_command)
    elif message.text == 'Теорема Косинусів':
        bot.register_next_step_handler(message, kosinus_ter_test)
    elif message.text == 'Косинус кута між двома векторами':
        bot.register_next_step_handler(message, cos_miz_vectorami)
    elif message.text == 'Підтримка':
        pidtrimka(message)


@bot.message_handler(func=lambda message: message.text.lower() == 'квадратне рівняння')
def kvad_riv_command(message):
    bot.send_message(message.chat.id, "Введіть три числа (a, b, c) через пробіл для вирішення квадратного рівняння")
    bot.register_next_step_handler(message, kvad_riv)


@bot.message_handler(func=lambda message: message.text.lower() == 'кубічне рівняння')
def kub_riv_command(message):
    bot.send_message(message.chat.id, "Введіть чотири числа (a, b, c, d) для вирішення кубічного рівняння через пробіл")
    bot.register_next_step_handler(message, kub_riv)


@bot.message_handler(func=lambda message: message.text.lower() == 'біквадратне рівняння')
def bikvad_riv_command(message):
    bot.send_message(message.chat.id, "Введіть три числа (a, b, c) через пробіл для вирішення біквадратного рівняння")
    bot.register_next_step_handler(message, bikvad_riv)


@bot.message_handler(func=lambda message: message.text.lower() == 'теорема косинусів')
def kosinus_ter_test(message):
    bot.send_message(message.chat.id, f"Введіть сторони a і b та градусну міру кута між ними")
    bot.register_next_step_handler(message, kosinus_ter)


@bot.message_handler(func=lambda message: message.text.lower() == 'косинус кута між двома векторами')
def cos_miz_vectorami(message):
    bot.send_message(message.chat.id, f"Введіть координати вектора а(а1;а2) та вектора b(b1;b2)")
    bot.register_next_step_handler(message, cos_miz_vect)


@bot.message_handler(func=lambda message: message.text.lower() == 'Підтримка')
def pidtrimka(message):
    bot.send_message(message.chat.id, f"Питання та пропозиції:\n @bulavd \n @Headnoshoot")


@bot.message_handler(func=lambda message: " " in message.text and message.chat.type == 'private')
def kvad_riv(message):
    if message.text == 'Повернутися':
        bot.register_next_step_handler(message, st)
    else:
        try:
            values = list(map(float, message.text.split()))
            a, b, c = values
            D = b ** 2 - 4 * a * c
            if D < 0:
                bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                  f'D = {b}² - (4 * {a} * {c}) < 0\n'
                                                  f'D < 0, отже коренів не існує.\n'
                                                  f'\n'
                                                  f'Відповідь: коренів немає.')

            elif D == 0:
                x = -b / (2 * a)
                bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                  f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                  f'D = 0, отже в нашому рівнянні 1 корінь\n'
                                                  f'\n'
                                                  f'         -b              -{b}\n'
                                                  f'x = ----------  =  ------------------- = {x}\n'
                                                  f'          2a            2 * {a}\n'
                                                  f'\n'
                                                  f'Відповідь: {x}')
            elif D > 0:
                x = (-b + (D ** 0.5)) / (2 * a)
                x1 = round(x, 5)

                x = (-b - (D ** 0.5)) / (2 * a)
                x2 = round(x, 5)

                bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                  f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                  f'D > 0, отже в нашому рівнянні 2 корні\n'
                                                  f'\n'
                                                  f'         -b + √D          -{b} + √{D}\n'
                                                  f'x1 =  -------------  =   ----------------------- = {x1}\n'
                                                  f'            2a                      2 * {a}\n'
                                                  f'\n'
                                                  f'         -b - √D            -{b} - √{D}\n'
                                                  f'x2 =  ----------  =     ---------------------- = {x2}\n'
                                                  f'           2a                     2 * {a}\n'
                                                  f'\n'
                                                  f'Відповідь: {x1} та {x2}'
                                                  f'\n'
                                                  f'\n'             
                                                  f'В випадку, якщо корінь не є цілим числом, просто запишіть дріб❗️')
        except ValueError:
            bot.send_message(message.chat.id,
                             f'Помилка! Введіть три числа (a, b, c) для вирішення квадратного рівняння через пробіл')
            bot.register_next_step_handler(message, kvad_riv)


@bot.message_handler(func=lambda message: " " in message.text and message.chat.type == 'private')
def kub_riv(message):
    try:
        values = list(map(float, message.text.split()))
        a, b, c, d = values
        p = -b / (3 * a)
        q = p ** 3 + (b * c - 3 * a * d) / (6 * a ** 2)
        r = c / (3 * a)
        D = q ** 2 + (r - p ** 2) ** 3
        if D > 0:
            S = (q + (D ** 0.5)) ** (1 / 3) + (q - (D ** 0.5)) ** (1 / 3)
            x1 = S - p
            x2 = complex(-(S / 2) - p, (S * 3 ** 0.5) / 2)
            x3 = complex(-(S / 2) - p, -(S * 3 ** 0.5) / 2)
            bot.send_message(message.chat.id, f'Корені кубічного рівняння: ({x1}), {x2} та {x3}')
        elif D == 0:
            x1 = (r - p ** 2) ** (1 / 3) - p
            x2 = complex(-(r - p ** 2) ** (1 / 3) - p, 0)
            x3 = complex(-(r - p ** 2) ** (1 / 3) - p, 0)
            bot.send_message(message.chat.id, f'Корені кубічного рівняння: {x1}, {x2} та {x3}')
        else:
            t = (3 * a * q - b) / (2 * a * (D ** 0.5))
            phi = complex(1 / 3, (3 ** 0.5) / 3)
            x1 = -2 * (r - p ** 2) ** (1 / 3) * t - p
            x2 = phi * (r - p ** 2) ** (1 / 3) * t - p
            x3 = phi.conjugate() * (r - p ** 2) ** (1 / 3) * t - p
            bot.send_message(message.chat.id, f'Корені кубічного рівняння: {x1}, {x2}, {x3}')
    except ValueError:
        bot.send_message(message.chat.id,
                         'Помилка! Введіть чотири числа (a, b, c, d) для вирішення кубічного рівняння через пробіл')
        bot.register_next_step_handler(message, kub_riv)


@bot.message_handler(func=lambda message: " " in message.text and message.chat.type == 'private')
def bikvad_riv(message):
    try:
        values = list(map(float, message.text.split()))
        a, b, c = values
        D = b ** 2 - 4 * a * c
        if D < 0:
            bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                              f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                              f'D < 0, отже коренів нема')
        elif D == 0:
            t = (-b / (2 * a))
            if t < 0:
                bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                  f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                  f'D = 0\n'
                                                  f'Оскільки дискримінант = 0, то робимо заміну t = x²\n'
                                                  f'Маємо рівняння:\n'
                                                  f'{a}t² + {b}t + c = 0\n'
                                                  f'Тоді маємо корінь:\n'
                                                  f'    {-b} \n'
                                                  f't = ----- \n'
                                                  f'    {2 * a}\n'
                                                  f't = {t}.\n'
                                                  f'Оскільки {t} < 0, то коренів нема')
            else:
                bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                  f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                  f'D = 0\n'
                                                  f'Оскільки дискримінант = 0, то робимо заміну t = x²\n'
                                                  f'Маємо рівняння:\n'
                                                  f'{a}t² + {b}t + c = 0\n'
                                                  f'Тоді маємо корінь:\n'
                                                  f'    {-b} \n'
                                                  f't = ----- \n'
                                                  f'    {2 * a}\n'
                                                  f't = {t}.\n'
                                                  f'Оскільки {t} > 0, то маємо корені:\n'
                                                  f'x = {t ** 0.5}, x1 = {-(t ** 0.5)}')
        elif D > 0:
            t = (-b + D ** 0.5) / (2 * a)
            t1 = (-b - D ** 0.5) / (2 * a)
            if t < 0 and t1 < 0:
                bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                  f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                  f'D = 0\n'
                                                  f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                  f'Маємо рівняння:\n'
                                                  f'{a}t² + {b}t + c = 0\n'
                                                  f'Тоді маємо корені:\n'
                                                  f'    {-b} + √{D}\n'
                                                  f't = ----------\n'
                                                  f'      {2 * a}\n'
                                                  f'    {-b} - √{D}\n'
                                                  f't1 = ----------\n'
                                                  f'      {2 * a}\n'
                                                  f't = {t}.\n'
                                                  f't1 = {t1}\n'
                                                  f'Оскільки {t} < 0, і {t1} < 0 то коренів нема\n')
            elif t > 0:
                if t1 < 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} > 0, і {t1} < 0 то маємо корені:\n'
                                                      f'x1 = √{t}, x2 = √{-t}')
                elif t1 > 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} > 0, і {t1} > 0 то маємо корені:\n'
                                                      f'x1 = √{t}, x2 = √{-t}, x3 = √{t1}, x4 = √{-t1}')
                elif t1 == 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} > 0, і {t1} = 0 то маємо корені:\n'
                                                      f'x1 = √{t}, x2 = √{-t}, x3 = 0')
            elif t < 0:
                if t1 < 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} < 0, і {t1} < 0 то коренів нема\n')
                elif t1 > 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} < 0, і {t1} > 0 то маємо корені:\n'
                                                      f'x1 = √{t1}, x2 = √{-t1}')
                elif t1 == 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} < 0, і {t1} = 0 то маємо корінь:\n'
                                                      f'x1 = 0')
            elif t == 0:
                if t1 < 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} = 0, і {t1} < 0 то маємо корінь:\n'
                                                      f'x1 = 0')
                elif t1 > 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}² - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} = 0, і {t1} > 0 то маємо корені:\n'
                                                      f'x1 = 0, x2 = √{t1}, x3 = √{-t1}')
                elif t1 == 0:
                    bot.send_message(message.chat.id, f'D = b² - 4ac\n'
                                                      f'D = {b}^2 - (4 * {a} * {c}) = 0\n'
                                                      f'D = 0\n'
                                                      f'Оскільки дискримінант = {D}, то робимо заміну t = x²\n'
                                                      f'Маємо рівняння:\n'
                                                      f'{a}t² + {b}t + c = 0\n'
                                                      f'Тоді маємо корені:\n'
                                                      f'    {-b} + √{D}\n'
                                                      f't = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f'    {-b} - √{D}\n'
                                                      f't1 = ----------\n'
                                                      f'      {2 * a}\n'
                                                      f't = {t}.\n'
                                                      f't1 = {t1}\n'
                                                      f'Оскільки {t} = 0, і {t1} = 0 то маємо корінь:\n'
                                                      f'x1 = 0')
            bot.send_message(message.chat.id, f'В випадку, якщо корінь не є цілим числом, просто запишіть дріб❗️')
    except ValueError:
        bot.send_message(message.chat.id,
                         f'Помилка! Введіть три числа (a, b, c) через пробіл для вирішення біквадратного рівняння')
        bot.register_next_step_handler(message, bikvad_riv)


@bot.message_handler(func=lambda message: " " in message.text and message.chat.type == 'private')
def kosinus_ter(message):
    try:
        values = list(map(float, message.text.split()))
        a, b, kyt = values
        k = kyt
        kyt = math.radians(kyt)
        c = ((a ** 2) + (b ** 2)) - (2 * a * b * round(math.cos(kyt), 5))
        bot.send_message(message.chat.id, f'c = a² * b² - 2ab * cos(кута)\n'
                                          f'\n'
                                          f'c = {a}² * {b}² - 2 * {a} * {b} * cos({k})'
                                          f'\n'
                                          f'\n'
                                          f'Третя сторона трикутника за теоремою косинусів буде: {c} см')
    except ValueError:
        bot.send_message(message.chat.id, f'Помилка! Введіть сторони a b та кут між ними через пробіл')
        bot.register_next_step_handler(message, kosinus_ter)


@bot.message_handler(func=lambda message: " " in message.text and message.chat.type == 'private')
def cos_miz_vect(message):
    try:
        values = list(map(float, message.text.split()))
        a1, a2, b1, b2 = values
        e = (a1 * b1 + a2 * b2) / (math.sqrt(a1 ** 2 + a2 ** 2) + math.sqrt(b1 ** 2 + b2 ** 2))
        e = round(e, 5)
        bot.send_message(message.chat.id,
                         f'             a1 * b1  +  a2 * b2\n'
                         f'------------------------------------------------  = cos\n'
                         f'√(a1^2 + a2^2) + √(b1^2 + b2^2)\n '
                         f'\n'
                         f'             {a1} * {b1}  +  {a2} * {b2}\n'
                         f'cos = ------------------------------------------------------\n'
                         f'           √({a1}² + {a2}²) + √({b1}² + {b2}²)\n '
                         f'\n'
                         f'Косинус між двома векторами = {e}')

    except ValueError:
        bot.send_message(message.chat.id, f'Помилка! Введіть сторони a b та кут між ними через пробіл')
        bot.register_next_step_handler(message, kosinus_ter)


bot.polling()
