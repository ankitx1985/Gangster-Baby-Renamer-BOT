import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26994377")

API_HASH = os.environ.get("API_HASH", "9c9eb74a4a0a1ecd4c96abebf3c637ee")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8470851409:AAEXIxxnbot6wRz-r9tbhYkoe_i9qgx7oK4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1003024428633") 

DB_NAME = os.environ.get("DB_NAME","hbrnbot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://fixmayart834:FMWwXBd4JJYMs2Iv@cluster0.ltpube9.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/tjX.jpg/HGBOTZ.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '8184789731').split()]

PORT = os.environ.get("PORT", "8080")
