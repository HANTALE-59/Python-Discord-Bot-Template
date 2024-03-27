from inputimeout import inputimeout, TimeoutOccurred
import os
from dotenv import load_dotenv
import sys

TOKEN = None
load_dotenv()

# Lister les noms des bots et leurs tokens à partir du fichier .env
bots = {
    1: ("Nounours", os.getenv("TOKEN_Nounours")),
    2: ("Kahlan", os.getenv("TOKEN_Kahlan")),
    3: ("Beta bot", os.getenv("TOKEN_Beta_bot")),
    4: ('Chuuu',os.getenv("TOKEN_Chuuuuh")),
    5: ('Blockfront',os.getenv("TOKEN_Blockfront")),
    6: ('Community Updates',os.getenv("TOKEN_CU")),
    7: ('Clyde',os.getenv("TOKEN_Clyde")),
    8: ('AutoMod',os.getenv("TOKEN_Automod")),
    9: ('Discord',os.getenv("TOKEN_Discord"))
}

# Récupérer le numéro du bot à utiliser depuis les arguments de la ligne de commande
if len(sys.argv) > 1:
    print("Choisissez le numéro correspondant au bot que vous souhaitez utiliser :")
    for num, (name, _) in bots.items():
        print(f"Choisissez {num} pour utiliser le token de {name}")
    timeout = 10
    
    try:
        chosen_bot_index = inputimeout(prompt=f"You have {timeout} seconds to choose the correct answer...\n", timeout=timeout)
    except TimeoutOccurred:
        print("Sorry, timeout")
        chosen_bot_index = 1
            
    try:
        chosen_bot_index = int(chosen_bot_index)
        if chosen_bot_index not in bots:
            raise ValueError()
    except ValueError:
        print("Token invalide, token par défaut utilisé.")
        chosen_bot_index = 1
        
        # Sélectionner le token correspondant au choix de l'utilisateur
    #chosen_bot_name, chosen_token = bots[chosen_bot_index]
        

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

else:
    chosen_bot_index = 1  # Utiliser le premier bot par défaut si aucun numéro n'est spécifié
'''
# Vérifier si le numéro du bot est valide
if chosen_bot_index not in bots:
    print("Numéro de bot invalide.")
    exit()
'''
# Sélectionner le token correspondant au choix de l'utilisateur
chosen_bot_name, chosen_token = bots[chosen_bot_index]

# Vérifier si le token sélectionné est valide
if chosen_token is None:
    print("Token invalide, token par défaut utilisé")
    chosen_token = os.getenv("TOKEN_Nounours")

# Utiliser le token sélectionné
TOKEN = chosen_token
