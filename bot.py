🇺🇿🇺🇿🇺🇿 🫀🐍, [01.03.2026 10:08]
import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# ===== SOZLAMALAR =====
TOKEN = "8734373114:AAF92DvxIMaMySqqeUdW5qhGgIzvmaAatO0"
ADMIN_ID = 7256724675  # Sizning ID

logging.basicConfig(level=logging.INFO)

# ===== ASOSIY MENYU =====
def main_menu():
    keyboard = [
        [KeyboardButton("📚 Sun'iy intellekt asoslari")],
        [KeyboardButton("📊 Narxlar")],
        [KeyboardButton("💳 Buyurtma berish")],
        [KeyboardButton("📞 Admin bilan bog'lanish")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ===== START =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}! 👋\n\n"
        "🎯 *Prezentatsiya Do'koniga* xush kelibsiz!\n\n"
        "Professional prezentatsiyalar tayyorlaymiz:\n"
        "✅ Sun'iy intellekt haqida\n"
        "✅ Biznes va marketing\n"
        "✅ Ta'lim mavzulari\n\n"
        "Quyidagi menyudan tanlang 👇",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

# ===== SUN'IY INTELLEKT ASOSLARI =====
async def ai_basics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💳 Sotib olish - 30 000 so'm", callback_data="buy_ai_basics")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="back")],
    ])
    await update.message.reply_text(
        "📚 *Sun'iy intellekt asoslari*\n\n"
        "📄 15 ta professional slayd\n"
        "🎨 Zamonaviy dizayn\n"
        "📝 To'liq mazmun\n\n"
        "✅ Nima mavzular kiritilgan:\n"
        "• AI nima?\n"
        "• Machine Learning asoslari\n"
        "• ChatGPT va boshqalar\n"
        "• AI kelajagi\n\n"
        "💰 Narxi: *30 000 so'm*\n"
        "📦 Format: PDF + PPTX",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

# ===== NARXLAR =====
async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 *Narxlar ro'yxati*\n\n"
        "🔹 *Tayyor prezentatsiyalar:*\n"
        "• Sun'iy intellekt asoslari - 30 000 so'm\n"
        "• Biznes rejasi - 35 000 so'm\n"
        "• Marketing strategiyasi - 35 000 so'm\n\n"
        "🔸 *Individual buyurtma:*\n"
        "• 10 slayd gacha - 50 000 so'm\n"
        "• 11-20 slayd - 80 000 so'm\n"
        "• 20+ slayd - 120 000 so'm\n\n"
        "⏰ Tayyorlanish vaqti: 1-2 kun\n"
        "📦 Format: PDF + PPTX",
        parse_mode="Markdown"
    )

# ===== BUYURTMA BERISH =====
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 *Buyurtma berish*\n\n"
        "Quyidagilarni yozing:\n\n"
        "1️⃣ Mavzu nomi\n"
        "2️⃣ Slayd soni\n"
        "3️⃣ Qo'shimcha izoh (ixtiyoriy)\n\n"
        "📝 *Misol:*\n"
        "Mavzu: Sun'iy intellekt\n"
        "Slayd: 15 ta\n"
        "Izoh: Ko'p rasmli bo'lsin\n\n"
        "Yuborgan xabaringiz adminга автоматик yetkaziladi! ✅",
        parse_mode="Markdown"
    )
    context.user_data['waiting_order'] = True

# ===== ADMIN BILAN BOG'LANISH =====
async def contact_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Admin bilan bog'lanish*\n\n"
        "👤 Telegram: @admin_username\n"
        "📱 Telefon: +998 90 4713066\n\n"
        "⏰ Ish vaqti: 9:00 - 22:00\n\n"
        "Yoki to'g'ridan-to'g'ri xabar yuboring 👇",
        parse_mode="Markdown"
    )

# ===== XABARLARNI QABUL QILISH =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

🇺🇿🇺🇿🇺🇿 🫀🐍, [01.03.2026 10:08]
if text == "📚 Sun'iy intellekt asoslari":
        await ai_basics(update, context)
    elif text == "📊 Narxlar":
        await prices(update, context)
    elif text == "💳 Buyurtma berish":
        await order(update, context)
    elif text == "📞 Admin bilan bog'lanish":
        await contact_admin(update, context)
    else:
        # Buyurtma yoki xabar adminga yuborish
        if context.user_data.get('waiting_order'):
            # Adminga xabar yuborish
            admin_message = (
                f"🛒 *Yangi buyurtma!*\n\n"
                f"👤 Mijoz: {user.first_name} {user.last_name or ''}\n"
                f"🆔 ID: {user.id}\n"
                f"📱 Username: @{user.username or 'yo\'q'}\n\n"
                f"📝 Buyurtma:\n{text}"
            )
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=admin_message,
                parse_mode="Markdown"
            )
            await update.message.reply_text(
                "✅ Buyurtmangiz qabul qilindi!\n\n"
                "Admin tez orada siz bilan bog'lanadi. 😊",
                reply_markup=main_menu()
            )
            context.user_data['waiting_order'] = False
        else:
            await update.message.reply_text(
                "Menyudan birini tanlang 👇",
                reply_markup=main_menu()
            )

# ===== INLINE TUGMALAR =====
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy_ai_basics":
        await query.message.reply_text(
            "💳 *To'lov ma'lumotlari*\n\n"
            "💰 Summa: *30 000 so'm*\n\n"
            "🏦 Karta raqami:\n"
            "9860356631092661\n\n"
            "📋 To'lov qilgach:\n"
            "1. Screenshot oling\n"
            "2. Shu yerga yuboring\n"
            "3. Admin tekshirib, fayl yuboradi ✅",
            parse_mode="Markdown"
        )
        context.user_data['waiting_payment'] = 'ai_basics'

# ===== SCREENSHOT QABUL QILISH =====
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if context.user_data.get('waiting_payment'):
        product = context.user_data['waiting_payment']

        # Adminga bildirish
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"💰 *Yangi to'lov!*\n\n"
                 f"👤 {user.first_name} (@{user.username or 'yo\'q'})\n"
                 f"🆔 ID: {user.id}\n"
                 f"📦 Mahsulot: {product}",
            parse_mode="Markdown"
        )
        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )

        await update.message.reply_text(
            "✅ To'lov screenshoti qabul qilindi!\n\n"
            "Admin tekshirgach, fayl yuboriladi.\n"
            "⏰ Odatda 5-15 daqiqa ichida.",
            reply_markup=main_menu()
        )
        context.user_data['waiting_payment'] = None
    else:
        await update.message.reply_text("Rasm qabul qilindi! ✅")

# ===== BOTNI ISHGA TUSHIRISH =====
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Bot ishga tushdi!")
    app.run_polling()

if name == "main":
    main()                                                              