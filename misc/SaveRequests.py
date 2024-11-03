from burp import IBurpExtender, IContextMenuFactory
from javax.swing import JMenuItem
from java.io import FileWriter, PrintWriter
import os

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Save Selected Responses")
        callbacks.registerContextMenuFactory(self)
        print("Extension loaded: Save Selected Responses")

    def createMenuItems(self, invocation):
        self.context = invocation
        menu_item = JMenuItem("Save Selected Responses", actionPerformed=self.save_responses)
        return [menu_item]

    def save_responses(self, event):
        selected_items = self.context.getSelectedMessages()
        if not selected_items:
            print("No items selected.")
            return

        save_path = os.path.join(os.getcwd(), "saved_responses.txt")
        print("Saving selected responses to:", save_path)

        writer = None
        try:
            writer = PrintWriter(FileWriter(save_path, True))
            for item in selected_items:
                response = item.getResponse()
                if response:
                    writer.println("Response:\n" + self.helpers.bytesToString(response))
                    writer.println("\n---\n")
                else:
                    writer.println("No response.\n---\n")
            print("Responses saved successfully.")
        except Exception as e:
            print("An error occurred while saving:", str(e))
        finally:
            if writer:
                writer.close()
