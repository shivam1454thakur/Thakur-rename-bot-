# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22012861")

API_HASH = os.environ.get("API_HASH", "ffb42173665d08b61fb2e8d9c9ada442")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6254434109:AAEo9JG1m4c7TrPtUsRXZtllhV6GvMujddU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Thakur_rename_bot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Thakur_rename_bot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://shivamthakur1454:YQIDnNKRIV6еJNMV@cluster0.l1gtchg.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5664403564').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
