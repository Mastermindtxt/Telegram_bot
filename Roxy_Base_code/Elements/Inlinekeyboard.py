from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Data storage for user inputs
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler."""
    keyboard = [
        [InlineKeyboardButton("Start Input", callback_data="start_input")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Press the button below to provide input.", reply_markup=reply_markup)

async def handle_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user inputs step by step."""
    query = update.callback_query
    await query.answer()

    # Step 1: Dimension input
    if query.data == "start_input":
        keyboard = [
            [InlineKeyboardButton("720x1650", callback_data="dim_720x1650")],
            [InlineKeyboardButton("235x2657", callback_data="dim_235x2657")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Select the video dimensions:", reply_markup=reply_markup)

    # Step 2: FPS input
    elif query.data.startswith("dim_"):
        dimension = query.data.split("_")[1]
        user_data["dimension"] = dimension
        keyboard = [
            [InlineKeyboardButton("30 FPS", callback_data="fps_30")],
            [InlineKeyboardButton("60 FPS", callback_data="fps_60")],
            [InlineKeyboardButton("90 FPS", callback_data="fps_90")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Selected dimension: {dimension}\nNow, select FPS:", reply_markup=reply_markup)

    # Step 3: Quality input
    elif query.data.startswith("fps_"):
        fps = query.data.split("_")[1]
        user_data["fps"] = fps
        keyboard = [
            [InlineKeyboardButton("Low (4)", callback_data="quality_4")],
            [InlineKeyboardButton("Medium (2)", callback_data="quality_2")],
            [InlineKeyboardButton("High (1)", callback_data="quality_1")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Selected FPS: {fps}\nNow, select quality:", reply_markup=reply_markup)

    # Step 4: Audio extraction input
    elif query.data.startswith("quality_"):
        quality = query.data.split("_")[1]
        user_data["quality"] = quality
        keyboard = [
            [InlineKeyboardButton("Yes", callback_data="audio_yes")],
            [InlineKeyboardButton("No", callback_data="audio_no")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Selected quality: {quality}\nDo you want to extract audio?", reply_markup=reply_markup)

    # Final Step: Save audio preference and display summary
    elif query.data.startswith("audio_"):
        audio_pref = "Yes" if query.data == "audio_yes" else "No"
        user_data["audio"] = audio_pref
        await query.edit_message_text(
            f"Input summary:\n"
            f"- Dimensions: {user_data['dimension']}\n"
            f"- FPS: {user_data['fps']}\n"
            f"- Quality: {user_data['quality']}\n"
            f"- Audio extraction: {user_data['audio']}\n\n"
            "Thank you for providing the inputs!"
        )

def main():
    """Run the bot."""
    # Replace 'YOUR-BOT-TOKEN' with your bot token from BotFather
    application = Application.builder().token("YOUR-BOT-TOKEN").build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_input))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
