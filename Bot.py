import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN = "8734373114:AAF92DvxIMaMySqqeUdW5qhGgIzvmaAatO0"
ADMIN_ID = 7256724675

logging.basicConfig(level=logging.INFO)

def main_menu():
    keyboard = [
        [KeyboardButton("Sun'iy intellekt asoslari")],
        [KeyboardButton("Narxlar")],
        [KeyboardButton("Buyurtma berish")],
        [KeyboardButton("Admin bilan bog'lanish")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}! 👋\n\n"
        "Prezentatsiya Do'koniga xush kelibsiz!\n\n"
        "Quyidagi menyudan tanlang 👇",
        reply_markup=main_menu()
    )

async def ai_basics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sotib olish - 30 000 so'm", callback_data="buy_ai_basics")],
        [InlineKeyboardButton("Orqaga", callback_data="back")],
    ])
    await update.message.reply_text(
        "*Sun'iy intellekt asoslari*\n\n"
        "15 ta slayd, zamonaviy dizayn, to'liq mazmun.\n\n"
        "💰 Narxi: 30 000 so'm",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("*Narxlar ro'yxati*\n\nTayyor: 30-35 ming so'm\nIndividual: 50-120 ming so'm", parse_mode="Markdown")

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("*Buyurtma berish*\nMavzu, slayd soni va izoh yozing.", parse_mode="Markdown")
    context.user_data['waiting_order'] = True

async def contact_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("*Admin bilan bog'lanish*\n@telikom_xamida yoki +998 90 4713066", parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Sun'iy intellekt asoslari":
        await ai_basics(update, context)
    elif text == "Narxlar":
        await prices(update, context)
    elif text == "Buyurtma berish":
        await order(update, context)
    elif text == "Admin bilan bog'lanish":
        await contact_admin(update, context)
    else:
        if context.user_data.get('waiting_order'):
            await context.bot.send_message(ADMIN_ID, f"Yangi buyurtma: {text}")
            await update.message.reply_text("Buyurtma qabul qilindi!")
            context.user_data['waiting_order'] = False
        else:
            await update.message.reply_text("Menyudan tanlang 👇", reply_markup=main_menu())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "buy_ai_basics":
        await query.message.reply_text("*To'lov:* 30 000 so'm\nKarta: 9860356631092661\nScreenshot yuboring.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('waiting_payment'):
        await context.bot.send_message(ADMIN_ID, "Yangi to'lov screenshot!")
        await context.bot.forward_message(ADMIN_ID, update.effective_chat.id, update.message.message_id)
        await update.message.reply_text("Screenshot qabul qilindi!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
