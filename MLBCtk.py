from requests import get
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='requests')
from pprint import PrettyPrinter
import customtkinter as ctk
import tkinter

def getinfo(event=None):
    if str(entrybox.get("1.0", "end-1c")).strip():
        try:
            username = str(entrybox.get("1.0", "end-1c")).strip()
            GAME_LOG = "https://mlb25.theshow.com/apis/game_history.json?username="+username+"&platform=mlbts&mode=all"
            PLAYER_DATA = "https://mlb25.theshow.com/apis/player_search.json?username="+username
            gamedata = get(GAME_LOG).json()
            playerdata = get(PLAYER_DATA).json()
            gamelists = gamedata['game_history']
            playerlists = playerdata['universal_profiles']
            home_team_name = gamelists[0]['home_full_name']
            away_team_name = gamelists[0]['away_full_name']
            home_runs = gamelists[0]['home_runs']
            away_runs = gamelists[0]['away_runs']
            display_date = gamelists[0]['display_date']
            game_id = gamelists[0]['id']
            pitcher_info = gamelists[0]['display_pitcher_info']
            gamesplayed = playerlists[0]['games_played']
            defensestats = str(playerlists[0]['lifetime_defensive_stats']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")
            offensestats = str(playerlists[0]['lifetime_hitting_stats']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")
            usernamelab.configure(text=username.capitalize())
            statstext.configure(text=f"Offensive Stats:\n{offensestats}\nDefensive Stats:\n{defensestats}")
            userinfotext.configure(text=f"User Info:\n\nGames Played: {gamesplayed}")
            lastgametext.configure(text=f"Latest Game:\n{display_date}\n\n{home_team_name} - {home_runs}\n{away_team_name} - {away_runs}\n\nNotable Pitchers:\n{pitcher_info}")
        except IndexError:
            username = "User Not Found"
            usernamelab.configure(text=username)
            statstext.configure(text="Stats:")
            lastgametext.configure(text="Latest Game:")
            userinfotext.configure(text="User Info:")
    return "break"

window = ctk.CTk()
window.geometry("850x600")
window.title("MLB The Show Profile")
window.iconbitmap("25logo.ico")
ctk.set_appearance_mode("dark")

app = ctk.CTkFrame(window,height=600, width=850, fg_color="#262626")
app.pack_propagate(False)
app.pack(expand=True)

entrybox = ctk.CTkTextbox(app, height=100, width=840, corner_radius=10, border_width=2, border_color="#000000", font=("Impact", 14))
entrybox.pack(pady=5, padx=5, side="bottom")
window.bind('<Return>', getinfo)

enterbut = ctk.CTkButton(app, text="🢁", width=840, height=30, corner_radius=15, border_width=2, border_color="#1E6DB3", command=getinfo)
enterbut.pack(pady=5,padx=5, side='bottom')

lastgameframe = ctk.CTkFrame(app, width=400, height=500, fg_color="#1F1F1F", border_width=2, border_color="#000000")
lastgameframe.pack(padx=5, pady=5, side='right')
lastgameframe.pack_propagate(False)

userinfo = ctk.CTkFrame(app, width=440, height=250, fg_color="#1F1F1F", border_width=2, border_color="#000000")
userinfo.pack(padx=5, pady=5, side='top')
userinfo.pack_propagate(False)

userstats = ctk.CTkFrame(app, width=440, height=200, fg_color="#1F1F1F", border_width=2, border_color="#000000")
userstats.pack(padx=5, pady=5, side='bottom')
userstats.pack_propagate(False)

usernamelab = ctk.CTkLabel(userinfo, text="User", font=("Impact", 40,), )
usernamelab.pack(pady=10, padx=10, anchor='nw')

statslab = ctk.CTkLabel(userstats, text="Stats", font=("Impact", 40,), )
statslab.pack(pady=10, padx=10, anchor='nw')

lastgamelab = ctk.CTkLabel(lastgameframe, text="Last Game", font=("Impact", 40,), )
lastgamelab.pack(pady=10, padx=10, anchor='nw')

statstext = ctk.CTkLabel(userstats, text="Stats:", font=("Lexend", 12,), justify='left')
statstext.pack(pady=2, padx=10, anchor='nw')

lastgametext= ctk.CTkLabel(lastgameframe, text="Latest Game:", font=("Lexend", 12,), justify='left', wraplength=385)
lastgametext.pack(pady=2, padx=10, anchor='nw')

userinfotext = ctk.CTkLabel(userinfo, text="User Info:", font=("Lexend", 12,), justify='left', wraplength=385)
userinfotext.pack(pady=2, padx=10, anchor='nw')

window.mainloop()