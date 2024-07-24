import tkinter as tk
def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm Good"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."


def send_message():
    user_input = entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)
    
    response = get_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)

# Set up the main window
root = tk.Tk()
root.title("Personal Chatbot")

chat_log = tk.Text(root, state=tk.DISABLED, width=80, height=20, bg="aqua")
chat_log.grid(row=0, column=0, padx=10, pady=10)

scrollbar = tk.Scrollbar(root, command=chat_log.yview)
chat_log['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=0, column=1, sticky='ns')

entry = tk.Entry(root, width=80)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
