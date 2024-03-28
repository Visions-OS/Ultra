# Made By Brooks Bentley And William Patton
# Empowering Visions, Unleashing Potential
# "With great power comes great responsibility"

from imports import *
from functions import *
from Text_Printer import *



ChatBot_Name = Fore.MAGENTA + "Ultra: "

def main_system(question):
  value = question
  if "exit" not in value.lower() and "weather" not in value.lower() and "time" not in value.lower() and "name" not in value.lower() and "date" not in value.lower() and "wikipedia" not in value.lower() and "news" not in value.lower() and "google" not in value.lower() and "email" not in value.lower() and "joke" not in value.lower() and "advice" not in value.lower() and "food" not in value.lower() and "hi" not in value.lower() and "credits" not in value.lower():
          genai.configure(api_key = "AIzaSyAU424NMmD oZ7MSI4dkJyl02kcQEzHhpfI")

          model = genai.GenerativeModel('gemini-pro')

          safe = [
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]


          chat = model.start_chat()
          prompt = value
          response = chat.send_message("In a sentence," + prompt, safety_settings=safe)
          response_text = response.text
          printer(ChatBot_Name + response_text, 200)

            

  elif "exit" in value:
          response_text = " Okay, Have A Good Day!"
          printer(ChatBot_Name + response_text, 200)
          sys.exit()

  elif "time" in value:
            tz_US = pytz.timezone("America/Chicago")
            datetime_US = datetime.now(tz_US)
            response_text = datetime_US.strftime("%I:%M %p")
            printer(ChatBot_Name + response_text, 200)


  elif "name" in value:
            response_text = " My Name Is Ultra, How Can I Assist You?"
            printer(ChatBot_Name + response_text, 200)

  elif "hi" in value:
            response_text = f" Hello {name} How May I Assist You?"
            printer(ChatBot_Name + response_text, 200)



  elif "date" in value:
            today = date.today()
            d2 = today.strftime("%B %d: %Y")
            response_text = d2
            printer(ChatBot_Name + response_text, 200)


  elif "wikipedia" in value: 
          search_query = input(ChatBot_Name + " Enter your Wikipedia search query: ")
          try:
              m = wikipedia.search(search_query, 3)
              if m:
                response_text = wikipedia.summary(m[0], sentences=4)
                printer(ChatBot_Name + response_text, 200)
              else:
                response_text = " No valid Wikipedia page found for search query."
                printer(ChatBot_Name + response_text, 200)
          except wikipedia.exceptions.DisambiguationError as e:
              s = random.choice(e.options)
              p = wikipedia.summary(s, sentences=2)
              response_text = p
              printer(ChatBot_Name + response_text, 200)
          except wikipedia.exceptions.PageError:
              response_text = " No Wikipedia page found for the search query."
              printer(ChatBot_Name + response_text, 200)

          
  elif "news" in value:
          get_news_by_category()


  elif "google" in value.lower():
          Google_News()

  elif "email" in value.lower():
            Send_Email()
            response_text = "Email Sent Sir!"
            printer(ChatBot_Name + response_text, 200)

  elif "joke" in value:
          response_text = "Hope you like this one..."
          printer(ChatBot_Name + response_text, 200)
          joke = get_random_joke()
          response_text = joke 
          printer(ChatBot_Name + response_text, 200)

  elif "advice" in value:
          response_text = "Here's some advice for you..."
          printer(ChatBot_Name + response_text, 200)
          advice = get_random_advice()
          response_text = advice
          printer(ChatBot_Name + response_text, 200)

  elif "food" in value:
    food()

  elif "weather" in value.lower():
    asyncio.run(getweather())
    

  elif "credits" in value:
    credits()