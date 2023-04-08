import bard

class BardPlugin(bard.Plugin):

    def __init__(self, bard):
        super().__init__(bard)

    def on_message(self, message):
        # This method is called whenever a message is received.
        # The message object has the following properties:
        #   * text: The text of the message.
        #   * sender: The name of the sender.
        #   * channel: The name of the channel where the message was sent.

        # Do something with the message.
        print(message.text)

    def on_ready(self):
        # This method is called when the plugin is ready to be used.
        # You can use this method to initialize any resources that the plugin needs.

        # For example, you could initialize a database connection or load some data.

        print("Bard plugin is ready!")


if __name__ == "__main__":
    bard = bard.Bard()
    plugin = BardPlugin(bard)
    plugin.run()
