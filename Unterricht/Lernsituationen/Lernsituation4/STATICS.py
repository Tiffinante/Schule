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
    f"Kennst du {r.choice(games)}?"
]

tags = {
    "gaming": "Ich liebe Vidiospiele!",
    "spielst": f"Ich spiele {r.choice(games)}.",
    "rank": "ich bin Gold 3.",
    "platform": "Ich spiele auf der XBox.",
    "spiele": "Das sollten wir mal zusammen Spielen.",
    "müll": "Deine Mutter ist Müll!",
    "besser": "Das glaube ich nicht...",
    "mobile": "Ich Hasse Mobail Gamer!",
}
