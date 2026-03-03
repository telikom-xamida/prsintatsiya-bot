import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ===== SOZLAMALAR =====
TOKEN = "8734373114:AAF92DvxIMaMySqqeUdW5qhGgIzvmaAatO0"  # tokeningizni shu yerga qo'ying
ADMIN_ID = 7256724675

logging.basicConfig(level=logging.INFO)

# ===== MENYU =====
def main_menu():
    keyboard = [
        [KeyboardButton("Sun'iy intellekt asoslari")],
        [KeyboardButton("Narxlar")],
        [KeyboardButton("Buyurtma berish")],
        [KeyboardButton("Admin bilan bog'lanish")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ===== START =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! 👋 Menyudan tanlang:", reply_markup=main_menu())

# ===== XABARLAR =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Sun'iy intellekt asoslari":
        await update.message.reply_text("Tez orada qo'shiladi!")
    elif text == "Narxlar":
        await update.message.reply_text("30 000 so'mdan boshlab...")
    elif text == "Buyurtma berish":
        await update.message.reply_text("Mavzu va slayd sonini yozing.")
    elif text == "Admin bilan bog'lanish":
        await update.message.reply_text("@telikom_xamida")
    else:
        await update.message.reply_text("Menyudan tanlang 👇", reply_markup=main_menu())

# ===== BOTNI ISHGA TUSHIRISH =====
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
