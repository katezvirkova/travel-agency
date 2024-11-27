from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    ConversationHandler,
)
from destinations import views


# Conversation stages
PRICE, DESTINATION, PAYMENT = range(3)

# Bot start message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Welcome to our Travel Agency Payment Bot! ✈️\n\n"
        "Please provide the price of your booking:"
    )
    return PRICE

# Ask for the destination
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["price"] = update.message.text  # Save price in user_data
    await update.message.reply_text(
        "Thank you! Now, please provide the destination for your booking:"
    )
    return DESTINATION

# Provide card details and request payment receipt
async def destination(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["destination"] = update.message.text  # Save destination
    card_number = "1234 5678 9876 5432"  # Example card number

    await update.message.reply_text(
        f"Got it! 🛩️ Your trip to *{context.user_data['destination']}* "
        f"costs *${context.user_data['price']}*.\n\n"
        f"Please make the payment to the following card:\n\n"
        f"**{card_number}**\n\n"
        "Once the payment is made, upload the payment receipt here for verification. 📄",
        parse_mode="Markdown",
    )
    return PAYMENT

# Handle payment receipt
async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.document:  # Check if the user sent a document
        await update.message.reply_text(
            "Thank you for your payment receipt! Our team will verify it shortly. 😊"
        )
    else:
        await update.message.reply_text(
            "Please upload a valid payment receipt document. 📄"
        )
        return PAYMENT

    # Reset conversation state
    return ConversationHandler.END

# Cancel handler
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Transaction canceled. If you need assistance, feel free to start over. 😊"
    )
    return ConversationHandler.END

# Main function
def main():
    application = ApplicationBuilder().token("7983181867:AAG4J3dd367gg-RE9Jm6tZn9accxfpUbsms").build()

    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PRICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, price)],
            DESTINATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, destination)],
            PAYMENT: [
                MessageHandler(filters.Document.ALL, payment),  # Handle document uploads
                MessageHandler(filters.TEXT & ~filters.COMMAND, payment),  # Handle wrong input
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Add handlers
    application.add_handler(conv_handler)

    # Start the bot
    application.run_polling()

