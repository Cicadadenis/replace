from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


domenu = InlineKeyboardMarkup()
domenu.add(
    InlineKeyboardButton("amzntop.ru", callback_data="cj1"),
    InlineKeyboardButton("amzntopl.ru", callback_data='cj2')
)


menu = InlineKeyboardMarkup()
menu.add(
    InlineKeyboardButton("ОПЕРАТОР", callback_data="oper"),
    InlineKeyboardButton("ТЕХПОДДЕРЖКА", callback_data='tex')
)
menu.add(
    InlineKeyboardButton("БОТ", callback_data="bott"),
    InlineKeyboardButton("ФОРУМ", callback_data='forum')
)
menu.add(
    InlineKeyboardButton("Сайт Biz", callback_data="biz"),
    InlineKeyboardButton("ОТЗЫВЫ", callback_data='otziv')
)
menu.add(
    InlineKeyboardButton("Bot2", callback_data='bot2')
)
menu.add(
    InlineKeyboardButton("Фон", callback_data="img1"),
    InlineKeyboardButton("Логотип", callback_data='img2')
)
menu.add(
    InlineKeyboardButton("🔙 Назад", callback_data='bbb1')
)    


menu2 = InlineKeyboardMarkup()
menu2.add(
    InlineKeyboardButton("ОПЕРАТОР", callback_data="oper2"),
    InlineKeyboardButton("ТЕХПОДДЕРЖКА", callback_data='tex2')
)
menu2.add(
    InlineKeyboardButton("БОТ", callback_data="bott2"),
    InlineKeyboardButton("ФОРУМ", callback_data='forum2')
)
menu2.add(
    InlineKeyboardButton("Сайт Biz", callback_data="biz2"),
    InlineKeyboardButton("ОТЗЫВЫ", callback_data='otziv2')
)
menu2.add(
    InlineKeyboardButton("Работа", callback_data='bot22')
)
menu2.add(
    InlineKeyboardButton("Фон", callback_data="img12"),
    InlineKeyboardButton("Логотип", callback_data='img22')
)
menu2.add(
    InlineKeyboardButton("🔙 Назад", callback_data='bbb1')
)    


izm = InlineKeyboardMarkup()
izm.add(
    InlineKeyboardButton("✅ ДА", callback_data="yes"),
    InlineKeyboardButton("❌ НЕТ", callback_data='no')
)
otm = InlineKeyboardMarkup()
otm.add(
    InlineKeyboardButton("🔙 Назад", callback_data='bbb')
)
otm2 = InlineKeyboardMarkup()
otm2.add(
    InlineKeyboardButton("🔙 Назад", callback_data='bbb2')
)