# Flux Lora Telegram Bot Creation Process

Create an account at fal.ai [https://fal.ai/]
Gather all photos of you you’d like to make into a Lora
Suggested: pick at least 10, ideally at least 15, of very high quality photos of you.
Adding photos where you’re blurred will lead to blurry results.
Adding photos where you don’t look good will lead to less attractive results.
Submit the photos to the fal Lora creation pipeline.
[https://fal.ai/models/fal-ai/flux-lora-fast-training]
When it’s done, click:
Run Inference
Go to the “Python” API
Copy the path for your script.

Create a Telegram Bot
Got to Botfather on Telegram @BotFather
Type /newbot to create a new telegram bot.
Name it with a name that ends in ‘bot’. Ex., @charlenephotobot
Give the bot a nickname, Ex., charlenefire
You’ll get a telegram bot token from the bot father, along with its HTTP API token, ex. 7629059306:AAFRzkXNaQC47Sdjm0gAz56yyinBrkjO3Lg

Set up a Server to Host Your Script
I use Linode, but any server works. [https://www.linode.com/]
You can run the script locally but the telegram bot will stop working every time you close it.
Serve the Flux Lora Calling Script
Add your flux path and the telegram bot HTTP API token to the script and serve it using tmux (or some other maintainer) on your server.
Consider adding monitoring (so you can know what images have been generated with which prompts) and adding a restarter (for uptime reliability).
