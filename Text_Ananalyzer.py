# Пончик пОнчик, коТик альпак,а вовч!ок вовч*--ок АЛьпака *?№ вовчок. Пончик огурчик, котик пончик.

import argparse
import sys
import turtle
import random

parser = argparse.ArgumentParser(description='Input data')

parser.add_argument('--type', choices=[1, 2], default=1, type=int,
                    help="Diagram's type: 1 - Sector chart, 2 - Bar chart")
parser.add_argument('--text', nargs='*', default='', type=str, help='Input text')
args = parser.parse_args()

array_ = list()

print('')

if args.text == '':
    print('Отсутствует текст для анализа! Введите текст для корректной работы приложения.')
    sys.exit()

for word in args.text:
    temp_word = ''
    if word.isalpha():
        array_.append(word.lower().capitalize())
    elif not word.isalpha():
        for letter in word:
            if str(letter).isalpha():
                temp_word += str(letter).lower()
        if temp_word != '':
            array_.append(temp_word.capitalize())
        else:
            continue

word_dict = {}

for word in array_:
    word_dict[word] = {}
    word_dict[word]['quantity'] = array_.count(word)
    r_ = str(hex(random.randint(17, 254)).lstrip('0x'))
    g_ = str(hex(random.randint(17, 254)).lstrip('0x'))
    b_ = str(hex(random.randint(17, 254)).lstrip('0x'))
    word_dict[word]['color'] = '#' + r_ + g_ + b_

t = turtle.Turtle()
t.speed(10)
t.ht()


def sector_chart(word_dict):

    r = 250

    t.penup()
    t.setposition(-150, 0)
    t.pendown()

    n = 0
    for i in word_dict:
        n += int(word_dict[i]['quantity'])
    if len(word_dict) != 1:
        for j in word_dict:
            t.begin_fill()
#            t.pencolor(word_dict[j]['color'])
            t.fillcolor(word_dict[j]['color'])
            angle = int(word_dict[j]['quantity']) / n * 360
            t.forward(r)
            t.left(90)
            t.circle(r, angle)
            t.left(90)
            t.forward(r)
            t.left(180)
            t.end_fill()
    else:
        t.penup()
        t.setposition(-150, -r)
        t.pendown()
        t.begin_fill()
        for _ in word_dict:
            t.fillcolor(word_dict[_]['color'])
        t.circle(r)
        t.end_fill()


def bar_chart(word_dict):

    max_ = 0
    for i in word_dict:
        if int(word_dict[i]['quantity']) > max_:
            max_ = int(word_dict[i]['quantity'])

    step_x = 500 / (2 * len(word_dict) - 1)
    step_y = 500 / max_

    t = turtle.Turtle()
    t.speed(10)
    t.ht()

    if len(word_dict) != 1:
        n = 0
        for j in word_dict:
            t.penup()
            t.setposition(-400 + n * 2 * step_x, -250)
            t.pendown()
            t.begin_fill()
#            t.pencolor(word_dict[j]['color'])
            t.fillcolor(word_dict[j]['color'])
            for _ in range(2):
                t.forward(step_x)
                t.left(90)
                t.forward(word_dict[j]['quantity'] * step_y)
                t.left(90)
            t.end_fill()
            n += 1
    else:
        t.penup()
        t.setposition(-400, -250)
        t.pendown()
        t.begin_fill()
        for _ in word_dict:
            t.fillcolor(word_dict[_]['color'])
        for _ in range(2):
            t.forward(60)
            t.left(90)
            t.forward(500)
            t.left(90)
        t.end_fill()


if args.type == 1:
    sector_chart(word_dict)
elif args.type == 2:
    bar_chart(word_dict)
else:
    print('Такого типа диаграммы не существует!')

delta_y_text = 0
t.penup()

for k in word_dict.keys():
    t.setposition(200, 230 - delta_y_text)
    t.pendown()
    t.pencolor(word_dict[k]['color'])
    t.dot()
    t.write(k + ' - ' + str(word_dict[k]['quantity']) + ' item(s)', move=True, font=('arial', 16, 'bold'))
    delta_y_text += 40
    t.penup()

input()
