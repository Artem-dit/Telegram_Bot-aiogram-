from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

bt1 = KeyboardButton(text='План тренировок')
bt2 = KeyboardButton(text='Годовой отчет')

btnTrainning = ReplyKeyboardMarkup(resize_keyboard=True).add(bt1, bt2)

bt3 = KeyboardButton(text='Недельный календарь')
bt4 = KeyboardButton(text='Что тут нужно')
btnExit = KeyboardButton(text='Return')
btnCalendar = ReplyKeyboardMarkup(resize_keyboard=True).add(bt3, bt4, btnExit)

btWEEK1 = KeyboardButton(text='первая неделя')
btWEEK2 = KeyboardButton(text='вторая неделя')
btWEEK3 = KeyboardButton(text='третья неделя')
btWEEK4 = KeyboardButton(text='четвертая неделя')
btWEEKS = ReplyKeyboardMarkup(resize_keyboard=True).add(btWEEK1, btWEEK2, btWEEK3, btWEEK4, btnExit)

btn01 = InlineKeyboardButton(text='Январь',
                             url="https://drive.google.com/drive/u/2/folders/10kaSGS3scOzdcq1preTAHDymA6Mk_bq6")
btn02 = InlineKeyboardButton(text='Февраль',
                             url="https://drive.google.com/drive/u/2/folders/1wK22Q83pRkKIIsBJ9LiTyzul8KDr82y9")
btn03 = InlineKeyboardButton(text='Март',
                             url="https://drive.google.com/drive/u/2/folders/1TGdWtKERexIZsU79_atoP0ZEkLEmW9ma")
btn04 = InlineKeyboardButton(text='Апрель',
                             url="https://drive.google.com/drive/u/2/folders/1No8N0f35Fk594r752a5Iim1FzC1vIAqv")
btn05 = InlineKeyboardButton(text='Май',
                             url="https://drive.google.com/drive/u/2/folders/1KgHNENdgCSqRTuVzYYb1hC-_9zcjHjXm")
btn06 = InlineKeyboardButton(text='Июнь',
                             url="https://drive.google.com/drive/u/2/folders/1ZIagZsnsLpop6YTkW556DUmnlEljAO4t")
btn07 = InlineKeyboardButton(text='Июль',
                             url="https://drive.google.com/drive/u/2/folders/1Kv5J1EllGfhO9hFbxBeH3_S-60xdUMT_")
btn08 = InlineKeyboardButton(text='Август',
                             url="https://drive.google.com/drive/u/2/folders/1sS69hUBJCo_nCpp7lr3JYEX3LFBFEaBU")
btn09 = InlineKeyboardButton(text='Сентябрь',
                             url="https://drive.google.com/drive/u/2/folders/1aJDfNc4wA1DZ1EdgPv6AHS_vMhB4gzil")
btn10 = InlineKeyboardButton(text='Октябрь',
                             url="https://drive.google.com/drive/u/2/folders/10Hh8lFrEBaNTWQ-0rC8nHxgxw7h2wdPA")
btn11 = InlineKeyboardButton(text='Ноябрь',
                             url="https://drive.google.com/drive/u/2/folders/1t6MEhJHc-NZCIWhKrdSAhcjCAmFjWQxy")
btn12 = InlineKeyboardButton(text='Декабрь',
                             url="https://drive.google.com/drive/u/2/folders/1WnPS9KpBSQQHv0fJZlJcC5prfNDnlATh")
btnMNTH = InlineKeyboardMarkup(row_width=2)
btnMNTH.add(btn01, btn02, btn03, btn04, btn05,
            btn06, btn07, btn08, btn09, btn10, btn11, btn12)

# btnFirst = InlineKeyboardButton(text='Неделя 1',
#                               url="https://docs.google.com/document/d/1vgRBXi52gimJJdOztRy-B-G1tf7Hsz57O98_TmSGpyQ/edit")
# btnSecond = InlineKeyboardButton(text='Неделя 2',
#                                url="https://docs.google.com/document/d/1txRsWA4KeIDjYOslflr5WLZcWdfJomes__iscenhwIM/edit")
# btnThird = InlineKeyboardButton(text='Неделя 3',
#                              url="https://docs.google.com/document/d/11gaEtLLuO489Im0GAFmIAMIuaPhFa17ErWZyoSCBknM/edit")
# btnFour = InlineKeyboardButton(text='Неделя 4',
#                              url="https://docs.google.com/document/d/1dyWJxKxVbvsrBQxs2zPi9uDJyOxr4gkkUkNLDQ7jFxA/edit")
# btn_WEEKS = InlineKeyboardMarkup(row_width=2)
# btn_WEEKS.add(btnFirst, btnSecond, btnThird, btnFour)
