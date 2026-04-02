import asyncio
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# আপনার বোটের তথ্য
TOKEN = "8253421279:AAGYB-P5XzSiA46l-tH4vrku86oEHY1bDc8"
TARGET_CHAT_ID = -1002250764940  # আপনার গ্রুপের আইডি

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def auto_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # শুধুমাত্র নির্দিষ্ট গ্রুপে মেসেজ এলে কাজ করবে
    if update.effective_chat.id == TARGET_CHAT_ID:
        try:
            message_id = update.effective_message.message_id
            
            # ৩টি ইমোজি রিঅ্যাকশন
            reactions = [
                {"type": "emoji", "emoji": "👍"},
                {"type": "emoji", "emoji": "🔥"},
                {"type": "emoji", "emoji": "❤️"}
            ]

            # রিঅ্যাকশন সেট করা
            await context.bot.set_message_reaction(
                chat_id=TARGET_CHAT_ID,
                message_id=message_id,
                reaction=reactions
            )
            print(f"Reaction sent to message {message_id}")
            
        except Exception as e:
            logging.error(f"Error sending reaction: {e}")

if __name__ == '__main__':
    # Render-এর জন্য পোর্ট সেটআপ (এটি প্রয়োজন হতে পারে)
    port = int(os.environ.get("PORT", 8080))
    
    # অ্যাপ্লিকেশন তৈরি
    app = ApplicationBuilder().token(TOKEN).build()

    # সব মেসেজের জন্য হ্যান্ডলার
    app.add_handler(MessageHandler(filters.ALL, auto_reaction))

    print("বটটি এখন সক্রিয়!")
    app.run_polling()
