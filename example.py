from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import fal_client
import os
import concurrent.futures
from tqdm.notebook import tqdm

os.environ['FAL_KEY'] = "TODO: Insert Fal Key"

def fal(prompt, lora="flux"):
    if lora == "flux":
        model = "fal-ai/flux/dev"
    else:
        model = "fal-ai/flux-lora"

    if lora == "name":
        lora_path = "TODO: Insert Lora Path"
        prompt = "a picture of TOK. " + prompt

    
    
    handler = fal_client.submit(
        model,
        arguments={
            "prompt": prompt,
            "image_size" :"portrait_4_3",
            "enable_safety_checker": False,                                
            "loras": [{
                    "path": lora_path,
                    "scale": 1
                }],
            "embeddings": []               
            },
    )
    
    result = handler.get()

    return result['images'][0]['url']
    
def parallel_fal(prompt_list, lora="flux"):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(fal, prompt_list, [lora for _ in range(len(prompt_list))])))
    
    # Filter out any non-string results (assuming URLs are always strings)
    url_list = [result for result in results if isinstance(result, str)]
    
    return url_list

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}! I'm your new Telegram bot."
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text     
    await update.message.reply_photo(fal(prompt, lora="name"), caption=update.message.text[:200])
    await update.message.reply_photo(fal(prompt, lora="name"), caption=update.message.text[:200])
    await update.message.reply_photo(fal(prompt, lora="name"), caption=update.message.text[:200])
    await update.message.reply_photo(fal(prompt, lora="name"), caption=update.message.text[:200])

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("TODO: Insert Telegram HTTP API token").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()