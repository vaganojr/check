api_id = 123 # Ваш апи айди
api_hash='01234abcde' # Ваш апи ключ
# Инструкция по получению: https://telegra.ph/Sozdayom-paru-api-idhash-dlya-lovca-chekov-11-03

channel = -100 # Айди канала с логами об активированных чеках. Если вы хотите указать публичный канал, то введите 'тег без @', Например channel = 'lovec_checkov'

avto_vivod = True # Если данные параметр True, то скрипт раз в сутки будет переводить деньги с помощью чека на указанный аккаунт. Чтобы отключить укажите False, например avto_vivod = False
avto_vivod_tag = 'ваш_тег' # Тег аккаунта(без @), куда раз в сутки будет отправляться чек со всеми собранными средствами. Например avto_vivod_tag = 'absolutely_enough'

avto_otpiska = True # Если данные параметр True, то скрипт будет автоматически выходить из каналов, которе не публиковали чеки в течении суток. Чтобы отключить укажите False, например avto_otpiska = False

anti_captcha = True # Если параметр True, то скрипт будет автоматически разгадывать каптчу для CryptoBot. Чтобы отключить укажите False, например anti_captcha = False

ocr_api_key = 'ваш ocr_api_key' # Инструкция по получению: https://telegra.ph/Poluchenie-OCR-API-KEY-11-03

# https://t.me/+7xF6Jb3ka9A0ZDhi

"""
🛠 Инструкция по настройке и запуску: Мануал по установке ловца чеков https://telegra.ph/Manual-po-ustanovke-lovca-chekov-11-02

🔑 Инструкция по созданию api id/api hash: Создаём пару api id/hash для ловца чеков | https://telegra.ph/Sozdayom-paru-api-idhash-dlya-lovca-chekov-11-03

🖼️ Инструкция по настройке антикаптчи(создание ocr_api_key): Получение OCR API KEY | https://telegra.ph/Poluchenie-OCR-API-KEY-11-03
"""