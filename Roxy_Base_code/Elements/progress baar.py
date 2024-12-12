from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# A dictionary to track progress for each user
progress_data = {}

def get_progress_bar(progress: int) -> str:
    """Generate a progress bar string."""
    bar_length = 10  # Total length of the bar
    filled_length = int(bar_length * progress / 100)
    bar = f"[{'#' * filled_length}{'-' * (bar_length - filled_length)}] {progress}%"
    return bar

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler."""
    user_id = update.effective_user.id
    progress_data[user_id] = 0  # Initialize progress for the user
    await update.message.reply_text("Progress started! Use /progress to check the progress.")

async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the current progress."""
    user_id = update.effective_user.id
    progress = progress_data.get(user_id, 0)
    progress_bar = get_progress_bar(progress)
    await update.message.reply_text(progress_bar)

async def update_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Update the progress bar."""
    user_id = update.effective_user.id
    if user_id not in progress_data:
        await update.message.reply_text("No progress bar found! Start with /start.")
        return

    progress = progress_data[user_id]
    if progress >= 100:
        await update.message.reply_text("Progress is already complete!")
        return

    # Simulate progress update
    for i in range(progress, 101, 10):  # Increment in steps of 10%
        progress_data[user_id] = i
        progress_bar = get_progress_bar(i)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=progress_bar)
        await asyncio.sleep(1)  # Simulate a delay

async def complete_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manually complete the progress bar."""
    user_id = update.effective_user.id
    if user_id not in progress_data:
        await update.message.reply_text("No progress bar found! Start with /start.")
        return

    progress_data[user_id] = 100
    progress_bar = get_progress_bar(100)
    await update.message.reply_text(f"Progress completed!\n{progress_bar}")

def manual_progress_update(user_id: int, progress: int):
    """Manually update progress for a specific user."""
    progress_data[user_id] = progress
def manual_progress_update(user_id: int, progress: int):
    """Manually update progress for a specific user."""
    progress_data[user_id] = progress
def manual_progress_update(user_id: int, progress: int):
    """Manually update progress for a specific user."""
    progress_data[user_id] = progress
def manual_progress_update(user_id: int, progress: int):
    """Manually update progress for a specific user."""
    progress_data[user_id] = progress
def manual_progress_update(user_id: int, progress: int):
    """Manually update progress for a specific user."""
    progress_data[user_id] = progress

def main():
    """Run the bot."""
    application = Application.builder().token("7638290429:AAHvdpB-tp1ycbCyMGBXW0FLCH_4QwmYdOg").build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("progress", progress))
    application.add_handler(CommandHandler("update", update_progress))
    application.add_handler(CommandHandler("complete", complete_progress))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
