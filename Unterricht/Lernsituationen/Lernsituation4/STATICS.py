import random as r


class ColorCodes:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    TURQUOISE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'  # WHITE
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


bot_name = ColorCodes.GREEN + "Emmi" + ColorCodes.RESET
cmd_signal = "!"

games = ["Valorant", "Minecraft", "Rainbow", "ARK", "GTA5", "GTA4", "Red Dead Redemption", "Red Dead Redemption 2"]

random_answers = [
    "Was spielst du so?",
    "Auf Was für einer Platform Spielst du?",
    f"Kennst du {r.choice(games)}?",
    "Schön.",
    "Sultan Kösen ist der Größte mensch der welt mit ganzen 2,51m",
]

tags = {
    # Komunikation
    "hallo": "Hi.",

    # Allgemainwissen
    "fortnite": "NEIN!",

    "Ninja": "Ein Ninja oder Shinobi ist ein besonders ausgebildeter Kämpfer. Der Ursprung findet sich im "
             "vorindustriellen Japan. Ninja wurden als Kundschafter, Spion, Saboteur oder Meuchelmörder eingesetzt. "
             "Weibliche Ninja werden Kunoichi genannt.",
    "pewdiepie": "PewDiePie ist ein schwedischer Webvideoproduzent und Betreiber des gleichnamigen YouTube-Kanals, "
                 "auf welchem er vor allem verschiedene Gamingformate veröffentlicht.",
    "youtuber": "Gronkh ist ein deutscher Webvideoproduzent, Computer- und Videospielejournalist, "
                "Computerspieleentwickler, Synchronsprecher, Musiker, Livestreamer und Unternehmer. Bekannt wurde "
                "Gronkh durch sogenannte Let’s-Play-Videos auf der Internetplattform YouTube. In diesen spielt und "
                "kommentiert er Computer- und Videospiele.",
    # Games
    "minecraft": "Minecraft ist ein Sandbox-Computerspiel, das ursprünglich vom schwedischen Programmierer Markus "
                 "„Notch“ Persson und seinem dazu gegründeten Unternehmen Mojang entwickelt wurde. Mojang samt Spiel "
                 "gehört seit September 2014 zu Microsoft. Minecraft erschien erstmals am 17. Mai 2009 als "
                 "Early-Access-Titel für PC.",
    "valorant": "Valorant ist ein Free-to-play-Multiplayer-Ego-Shooter, der von Riot Games entwickelt wurde. Es ist "
                "das erste Spiel, das Riot Games in diesem Genre entwickelt hat. Das Spiel wurde erstmals im Oktober "
                "2019 mit dem Codenamen Project A angekündigt. Es wurde am 2. Juni 2020 für Windows veröffentlicht.",
    "rainbow": "Tom Clancy’s Rainbow Six Siege ist ein taktischer Ego-Shooter, der zur Computerspielserie Rainbow Six "
               "gehört. Das Spiel wurde von Ubisoft Montreal entwickelt und von Ubisoft veröffentlicht.",
    # Gaming
    "gaming": "Ich liebe Vidiospiele!",
    "spiele ": f"Ich spiele {r.choice(games)}.",
    "rank": "ich bin Gold 3.",
    "platform": "Ich spiele auf der XBox.",
    "spiele": "Das sollten wir mal zusammen Spielen.",
    "müll": "Deine Mutter ist Müll!",
    "besser": "Das glaube ich nicht...",
    "mobile": "Ich Hasse Mobail Gamer!",
    "esport": "E-Sport ist der sportliche Wettkampf mit Computerspielen.",
    "e-sport": "E-Sport ist der sportliche Wettkampf mit Computerspielen.",
}
