# Made By Brooks Bentley And William Patton
# Empowering Visions, Unleashing Potential
# "With great power comes great responsibility"

from imports import *
from Text_Printer import *

ChatBot_Name = Fore.MAGENTA + "Ultra: "

def food():
  food_type = input("Enter the type of food you want: ")

  params = {
  "engine": "google_maps",
  "q": f"{food_type} in {food_location}",  
  "type": "search",
  "api_key": "bb3d84962bfbbef5e23fedae893295807bd7868b438099d47b8d0f9438435b5c"
}
  try:
    search = GoogleSearch(params)
    results = search.get_dict()
    local_results = results["local_results"]
    first_result = local_results[0]
    name = first_result.get("title")
    rating = first_result.get("rating")
    address = first_result.get("address")
    response_text = f"Name: {name}, Rating: {rating}, Address: {address}"
    printer(ChatBot_Name + response_text, 200)



  except Exception as e:
    response_text = "No results found."
    printer(ChatBot_Name + response_text, 200)

def get_news_by_category():
  category = input("Enter the category of news you want.(business, entertainment, general, health, science, sports, technology): ")


  newsapi = NewsApiClient(api_key='3f07679b192b4a1b95b92b83410f1157')
  top_headlines = newsapi.get_top_headlines(category=category,
                      language='en',
                      country='us')
  articles = top_headlines['articles']

  if articles:
      article = articles[0]
      title = article['title']
      description = article['description']
      response_text = "Title:", title
      printer(response_text, 200)
      response_text = "Description:", description
      printer(response_text, 200)
  else:
    response_text = "No news found for the given category."
    printer(ChatBot_Name + response_text, 200)




def Send_Email():
  yag = yagmail.SMTP('brookstb@madisoncity.k12.al.us', 'bb053821')
  receiver = input(ChatBot_Name + "To who is this email being sent?")
  subject = input(ChatBot_Name + "What should the subject be?")
  contents = input(ChatBot_Name + "What would you like to say?")
  yag.send(receiver, subject, contents)



def get_random_advice():
  res =       requests.get("https://api.adviceslip.com/advice").json()
  return res['slip']['advice']



def get_random_joke():
  headers = {
  'Accept': 'application/json'
}
  res = requests.get("https://icanhazdadjoke.com/",      headers=headers).json()
  return res["joke"]


def Google_News():
  search_query = input("Enter what you want to look up on Google: ")
  params = {
    "engine": "google",
    "q": search_query,
    "api_key": "bb3d84962bfbbef5e23fedae893295807bd7868b438099d47b8d0f9438435b5c"
}

  search = GoogleSearch(params)
  results = search.get_dict()
  organic_result = results["organic_results"]

  for result in organic_result[:1]:
    response_text = ChatBot_Name + result["snippet"]
    printer(ChatBot_Name + response_text, 200)


async def getweather():
  async with   python_weather.Client(unit=python_weather.IMPERIAL) as client:
    weather = await client.get(weather_locations)
    response_text = f"Sir, The Current Temperature In {weather_location} Is {weather.current.temperature} Degrees"
    printer(ChatBot_Name + response_text, 200)

def credits():
  f = open('credits.txt', 'r')
  content = f.read()
  printer(ChatBot_Name + content, 200)
  