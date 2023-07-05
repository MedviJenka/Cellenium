from botbuilder.core import BotFrameworkAdapter, TurnContext, BotFrameworkAdapterSettings



# Your bot's logic goes here
async def on_message_activity(turn_context: TurnContext):
    # Echo back the user's message
    await turn_context.send_activity(f"You said: {turn_context.activity.text}")


# Set up the adapter
SETTINGS = BotFrameworkAdapterSettings("YOUR_BOT_ID", "YOUR_BOT_PASSWORD")
ADAPTER = BotFrameworkAdapter(SETTINGS)


# Listen for incoming activities
async def messages_activity_handler(turn_context: TurnContext):
    if turn_context.activity.type == ActivityTypes.message:
        # Call the on_message_activity function to process the message
        await on_message_activity(turn_context)


# Set up the route for the bot
ADAPTER.on_turn(messages_activity_handler)

# Start the bot
if __name__ == "__main__":
    from aiohttp import web

    APP = web.Application()
    APP.router.add_route("POST", "/api/messages", messages_activity_handler)

    web.run_app(APP, host="localhost", port=3978)
