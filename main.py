import requests
import replit

def get_joke():
  # Send a GET request to the icanhazdadjoke API to get a random joke
  response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
  data = response.json()
  joke = data["joke"]
  joke_id = data["id"]
  return joke, joke_id

def save_joke(joke_id):
  # Save the joke ID to the Replit database
  db = replit.db('jokes')
  db.insert({'joke_id': joke_id})

def view_saved_jokes():
  # Query the Replit database to get a list of saved joke IDs
  db = replit.db('jokes')
  saved_jokes = db.all()
  for joke in saved_jokes:
    joke_id = joke['joke_id']
    # Use the joke ID to fetch the joke from the icanhazdadjoke API
    response = requests.get(f"https://icanhazdadjoke.com/j/{joke_id}", headers={"Accept": "application/json"})
    joke_data = response.json()
    print(joke_data["joke"])

# Fetch a random joke and ask the user if they want to save it
joke, joke_id = get_joke()
print(joke)
save_response = input("Do you want to save this joke? (y/n) ")
if save_response.lower() == 'y':
  save_joke(joke_id)

# Ask the user if they want to view the saved jokes
view_response = input("Do you want to view the saved jokes? (y/n) ")
if view_response.lower() == 'y':
  view_saved_jokes()
