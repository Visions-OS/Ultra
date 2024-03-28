import tkinter as tk
from main_system import main_system



def get_response():
  question = question_entry.get()
  response = main_system(question)  # Pass the question as an argument
  if response:  # Check if response is not None
      response_text.insert(tk.END, response + "\n")
  else:
      response_text.insert(tk.END, "No response received.\n") 

# Create the main window
root = tk.Tk()
root.title("AI Chatbot")

# Question input box
question_label = tk.Label(root, text="Enter your question:")
question_label.pack()

question_entry = tk.Entry(root)
question_entry.pack()

# Response output box
response_label = tk.Label(root, text="AI Response:")
response_label.pack()

response_text = tk.Text(root, height=10, width=50)
response_text.pack()

# Button to submit the question
submit_button = tk.Button(root, text="Ask", command=get_response)
submit_button.pack()

# Run the main event loop
root.mainloop()