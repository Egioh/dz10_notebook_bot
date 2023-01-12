


from aiogram import Bot,Dispatcher,executor,types


TOKEN= "5800074540:AAEsGbzeQT_fsDK1UhuqJNae_uHLVWPxPSA"

bot= Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['help','start'])
async def start_handler(message: types.Message):
    user_id=message.from_user.id
    user_name=message.from_user.first_name

    await message.reply(f"Привет {user_name}, этот бот выполняет функцию записной книжки команды: /add_contact (имя телефон) , /view_contacts , /send_contacts ")
    
@dp.message_handler(commands=['add_contact'])
async def add_contact(message: types.Message):
    contact_name = message.text.split()[1]
    contact_phone = message.text.split()[2]
    # save the contact details in a database or a file
    await message.reply(f"Contact {contact_name} with phone number {contact_phone} is added")
    with open("contacts.txt", "a") as f:
        f.write(f"{contact_name}, {contact_phone}\n")

@dp.message_handler(commands=['view_contacts'])
async def view_contacts(message: types.Message):
    with open("contacts.txt", "r") as f:
        contacts = f.readlines()
    contact_list = "\n".join(contacts)
    await message.reply(f"Existing contacts:\n{contact_list}")

@dp.message_handler(commands=['send_contacts'])
async def send_contacts(message: types.Message):
    user_id = message.from_user.id
    with open("contacts.txt", "rb") as f:
        await bot.send_document(user_id, f)



print("start")

executor.start_polling(dp)