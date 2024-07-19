# import logging
# import telepot
# import requests
# from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
# from admins import admins
# from user_data import users

# # Logger sozlamalari
# logging.basicConfig(filename='bot.log', level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # Bot tokeni
# TOKEN = '7289784476:AAGo3M-J2LYree0jVxGA3PkijgEWYcEk33w'

# # Telegram botni aktivlashtirish
# bot = telepot.Bot(TOKEN)

# # Valyuta kurslarini olish uchun ExchangeRate-API
# API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'

# user_state = {}

# # Foydalanuvchilar ro'yxatini yangilash
# def update_user_list(chat_id):
#     if chat_id not in users:
#         users.append(chat_id)
#         with open('user_data.py', 'w') as f:
#             f.write(f"users = {users}")

# # Botga kelgan so'rovlarni qabul qilish
# def handle(msg):
#     try:
#         content_type, chat_type, chat_id = telepot.glance(msg)
#         logging.info(f'Received message: {msg}')
        
#         if content_type == 'text':
#             command = msg['text'].strip().lower()
            
#             update_user_list(chat_id)  # Foydalanuvchilar ro'yxatini yangilash
            
#             if chat_id in admins:
#                 if command == '/start' or command == '/convert':
#                     keyboard = ReplyKeyboardMarkup(keyboard=[
#                         [KeyboardButton(text='USD to UZS')],
#                         [KeyboardButton(text='UZS to USD')],
#                         [KeyboardButton(text='Send message to users')],
#                         [KeyboardButton(text='View users')],
#                     ])
#                     bot.sendMessage(chat_id, 'Valyuta konvertatsiyasini tanlang yoki xabar yuboring:', reply_markup=keyboard)
                
#                 elif command == 'send message to users':
#                     bot.sendMessage(chat_id, 'Yuborish uchun xabarni kiriting:')
#                     user_state[chat_id] = 'sending_message'
                
#                 elif command == 'view users':
#                     bot.sendMessage(chat_id, f"Foydalanuvchilar soni: {len(users)}")
                
#                 elif chat_id in user_state and user_state[chat_id] == 'sending_message':
#                     # Barcha foydalanuvchilarga xabar yuborish
#                     for user_chat_id in users:
#                         if user_chat_id != chat_id:
#                             bot.sendMessage(user_chat_id, f" {msg['text']}")
#                     bot.sendMessage(chat_id, 'Xabar barcha foydalanuvchilarga yuborildi.')
#                     del user_state[chat_id]
#                 else:
#                     process_conversion(chat_id, command)
#             else:
#                 process_conversion(chat_id, command)
#     except Exception as e:
#         logging.error(f'Error handling message: {str(e)}')

# def process_conversion(chat_id, command):
#     try:
#         if command == '/start' or command == '/convert':
#             keyboard = ReplyKeyboardMarkup(keyboard=[
#                 [KeyboardButton(text='USD to UZS')],
#                 [KeyboardButton(text='UZS to USD')],
#             ])
#             bot.sendMessage(chat_id, 'Valyuta konvertatsiyasini tanlang:', reply_markup=keyboard)
        
#         elif command == 'usd to uzs' or command == 'uzs to usd':
#             user_state[chat_id] = command
#             bot.sendMessage(chat_id, 'Pul qiymatini kiriting:\nBarcha Dollar narxlari real vaqt asosila olingan!\nShunchaki kerakli summani yozing \nMasalan:1')
        
#         elif chat_id in user_state:
#             try:
#                 amount = float(command)
#                 conversion_type = user_state[chat_id]
                
#                 # Valyuta kurslarini olish
#                 response = requests.get(API_URL)
#                 data = response.json()
                
#                 if conversion_type == 'usd to uzs':
#                     from_currency = 'USD'
#                     to_currency = 'UZS'
#                     rate = data['rates']['UZS']
#                     converted_amount = amount * rate
                
#                 elif conversion_type == 'uzs to usd':
#                     from_currency = 'UZS'
#                     to_currency = 'USD'
#                     rate = data['rates']['UZS']
#                     converted_amount = amount / rate
                
#                 else:
#                     bot.sendMessage(chat_id, "Xatolik: Noto'g'ri holat.")
#                     return
                
#                 converted_amount = round(converted_amount, 2)
                
#                 # Natijani foydalanuvchiga yuborish
#                 bot.sendMessage(chat_id, f"{amount} {from_currency} = {converted_amount} {to_currency}")
#                 del user_state[chat_id]
                
#             except ValueError:
#                 bot.sendMessage(chat_id, "Xatolik: To'g'ri pul miqdorini kiriting.")
#     except Exception as e:
#         logging.error(f'Error processing conversion: {str(e)}')

# # Botga so'rovlarni qabul qilishni boshlash
# try:
#     bot.message_loop(handle)
#     logging.info('Bot started')
# except Exception as e:
#     logging.error(f'Error starting bot: {str(e)}')

# # Botni ishga tushirish
# print('Bot ishga tushirildi. Buyruqlarni kutamiz...')

# # Dasturni ishga tushirishni saqlash
# import time
# while True:
#     time.sleep(10)
