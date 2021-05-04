import pygame
from os import path
import json
import random

pygame.font.init()

# GLOBAL VARIABLES
WIDTH, HEIGHT = 900, 700
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW_ICON = pygame.image.load(path.join("pictures/general", "download.png"))
pygame.display.set_icon(WINDOW_ICON)
pygame.display.set_caption("Clicker Legends")

GREEN = (0, 153, 0)
RED = (255, 0, 0)
YELLOW = (255, 212, 0)
PURPLE = (255, 0, 255)
MAIN_COLOR = (255, 255, 255)
WHITE = (255, 255, 255)
MAIN_COLOR2 = (0, 0, 0)

# FONTS
CUSTOM_FONT = path.join("pictures", "MyFont.ttf")
CUSTOM_FONT2 = path.join("pictures", "ClickFont.otf")
HEADER_FONT = pygame.font.Font(CUSTOM_FONT, 80)
PARAGRAPH_FONT = pygame.font.Font(CUSTOM_FONT, 30)
DESCRIPTION_FONT = pygame.font.Font(CUSTOM_FONT, 20)
CLICK_FONT = pygame.font.Font(CUSTOM_FONT2, 15)


# BUTTON CLASS
class Button:
    clicked = False

    def __init__(self, x, y, width, height, picture0, picture1, picture2):
        self.x = x - width // 2
        self.y = y
        self.width = width
        self.height = height
        self.picture0 = pygame.transform.scale(picture0, (self.width, self.height))  # normal version
        self.picture1 = pygame.transform.scale(picture1, (self.width, self.height))  # hover version
        self.picture2 = pygame.transform.scale(picture2, (self.width, self.height))  # clicked version

    def draw_button(self):

        WIN.blit(self.picture0, (self.x, self.y))

        action = False

        pos = pygame.mouse.get_pos()

        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            # if clicked on the button
            if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
                self.clicked = True
                WIN.blit(self.picture2, (self.x, self.y))
            # if mouse click is released while still on button
            elif pygame.mouse.get_pressed(num_buttons=3)[0] == 0 and self.clicked and button_rect.collidepoint(pos):
                self.clicked = False
                action = True
            else:
                WIN.blit(self.picture1, (self.x, self.y))
        else:
            self.clicked = False
            WIN.blit(self.picture0, (self.x, self.y))

        # needed to return if button had been pressed
        return action


# INTRO SCREEN VARIABLES
TITLE_PLACEHOLDER = HEADER_FONT.render("Clicker Legends", True, MAIN_COLOR2)

PLAY_BUTTON0 = pygame.image.load(path.join("pictures/intro", "play0.png"))
PLAY_BUTTON1 = pygame.image.load(path.join("pictures/intro", "play1.png"))
PLAY_BUTTON2 = pygame.image.load(path.join("pictures/intro", "play2.png"))

PLAY_PRESS = pygame.USEREVENT + 101
CREDITS_PRESS = pygame.USEREVENT + 102
ACHIEVEMENT_PRESS = pygame.USEREVENT + 103

play_button = Button(WIDTH // 2, 350, 420, 150, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
credits_button = Button(330, 530, 180, 90, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
achievements_button = Button(570, 530, 180, 90, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

# CREDITS VARIABLES
CREDITS1 = HEADER_FONT.render("Credits", True, YELLOW)
CREDITS2 = PARAGRAPH_FONT.render("Programmed by:", True, YELLOW)
CREDITS3 = PARAGRAPH_FONT.render("Michael Zhao and Owen Sullivan", True, WHITE)
CREDITS4 = PARAGRAPH_FONT.render("Assets by:", True, YELLOW)
CREDITS5 = PARAGRAPH_FONT.render("Griffin Oates and Chaia Espinas", True, WHITE)
CREDITS6 = PARAGRAPH_FONT.render("Playtesting by:", True, YELLOW)
CREDITS7 = PARAGRAPH_FONT.render("Owen Schofield", True, WHITE)

CREDITS_BACK_PRESS = pygame.USEREVENT + 701

credits_back_button = Button(WIDTH // 2, 600, 150, 80, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

# ACHIEVEMENT SCREEN VARIABLES

TROPHY0 = pygame.image.load(path.join("pictures/intro", "achievement0.png"))
TROPHY0 = pygame.transform.scale(TROPHY0, (80, 80))
TROPHY1 = pygame.image.load(path.join("pictures/intro", "achievement1.png"))
TROPHY1 = pygame.transform.scale(TROPHY1, (80, 80))

current_page = 0

ACHIEVEMENT_BACK_PRESS = pygame.USEREVENT + 801

ACHIEVEMENT_NAME1 = PARAGRAPH_FONT.render("First 10", True, YELLOW)
ACHIEVEMENT_DESCRIPTION1 = DESCRIPTION_FONT.render("Click 10 times", True, WHITE)
ACHIEVEMENT_NAME2 = PARAGRAPH_FONT.render("First 100", True, YELLOW)
ACHIEVEMENT_DESCRIPTION2 = DESCRIPTION_FONT.render("Click 100 times", True, WHITE)
ACHIEVEMENT_NAME3 = PARAGRAPH_FONT.render("First 500", True, YELLOW)
ACHIEVEMENT_DESCRIPTION3 = DESCRIPTION_FONT.render("Click 500 times", True, WHITE)
ACHIEVEMENT_NAME4 = PARAGRAPH_FONT.render("First 1 000", True, YELLOW)
ACHIEVEMENT_DESCRIPTION4 = DESCRIPTION_FONT.render("Click 1 000 times", True, WHITE)
ACHIEVEMENT_NAME5 = PARAGRAPH_FONT.render("First 5 000", True, YELLOW)
ACHIEVEMENT_DESCRIPTION5 = DESCRIPTION_FONT.render("Click 5 000 times", True, WHITE)

ACHIEVEMENT_NAME6 = PARAGRAPH_FONT.render("First 10 000", True, YELLOW)
ACHIEVEMENT_DESCRIPTION6 = DESCRIPTION_FONT.render("Click 10 000 times", True, WHITE)
ACHIEVEMENT_NAME7 = PARAGRAPH_FONT.render("First 100 000", True, YELLOW)
ACHIEVEMENT_DESCRIPTION7 = DESCRIPTION_FONT.render("Click 100 000 times", True, WHITE)
ACHIEVEMENT_NAME8 = PARAGRAPH_FONT.render("First 1 000 000", True, YELLOW)
ACHIEVEMENT_DESCRIPTION8 = DESCRIPTION_FONT.render("Click 1 000 000 times", True, WHITE)
ACHIEVEMENT_NAME9 = PARAGRAPH_FONT.render("1 000 L's taken", True, YELLOW)
ACHIEVEMENT_DESCRIPTION9 = DESCRIPTION_FONT.render("Lose 1 000 LP", True, WHITE)
ACHIEVEMENT_NAME10 = PARAGRAPH_FONT.render("The 0.1%", True, YELLOW)
ACHIEVEMENT_DESCRIPTION10 = DESCRIPTION_FONT.render("Hit Challenger for the first time", True, WHITE)

ACHIEVEMENT_NAME11 = PARAGRAPH_FONT.render("From Europe, with Love", True, YELLOW)
ACHIEVEMENT_DESCRIPTION11 = DESCRIPTION_FONT.render("Reach the Euorpean server for the first time", True, WHITE)
ACHIEVEMENT_NAME12 = PARAGRAPH_FONT.render("Dug a hole to China", True, YELLOW)
ACHIEVEMENT_DESCRIPTION12 = DESCRIPTION_FONT.render("Reach the Chinese server for the first time", True, WHITE)
ACHIEVEMENT_NAME13 = PARAGRAPH_FONT.render("Home of the best", True, YELLOW)
ACHIEVEMENT_DESCRIPTION13 = DESCRIPTION_FONT.render("Reach the Korean server for the first time", True, WHITE)
ACHIEVEMENT_NAME14 = PARAGRAPH_FONT.render("Super!", True, YELLOW)
ACHIEVEMENT_DESCRIPTION14 = DESCRIPTION_FONT.render("Reach the Super Server for the first time", True, WHITE)
ACHIEVEMENT_NAME15 = PARAGRAPH_FONT.render("THE BEST", True, YELLOW)
ACHIEVEMENT_DESCRIPTION15 = DESCRIPTION_FONT.render("Beat the Game", True, WHITE)

next_page_button = Button(570, 530, 50, 50, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
previous_page_button = Button(330, 530, 50, 50, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

clear_achievements_button = Button(850, 25, 50, 50, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
achievements_back_button = Button(WIDTH // 2, 600, 150, 80, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

# SAVE SCREEN VARIABLES

SAVE_SCREEN_BACKGROUND = pygame.image.load((path.join("pictures/save", "loadgamescreen.png")))
SAVE_SCREEN_BACKGROUND = pygame.transform.scale(SAVE_SCREEN_BACKGROUND, (WIDTH, HEIGHT))

NEW_GAME_BUTTON0 = pygame.image.load(path.join("pictures/save", "newgame0.png"))
NEW_GAME_BUTTON1 = pygame.image.load(path.join("pictures/save", "newgame1.png"))
NEW_GAME_BUTTON2 = pygame.image.load(path.join("pictures/save", "newgame2.png"))

LOAD_GAME_BUTTON0 = pygame.image.load(path.join("pictures/save", "load0.png"))
LOAD_GAME_BUTTON1 = pygame.image.load(path.join("pictures/save", "load1.png"))
LOAD_GAME_BUTTON2 = pygame.image.load(path.join("pictures/save", "load2.png"))

CLEAR_GAME_BUTTON0 = pygame.image.load(path.join("pictures/save", "clear0.png"))
CLEAR_GAME_BUTTON1 = pygame.image.load(path.join("pictures/save", "clear1.png"))
CLEAR_GAME_BUTTON2 = pygame.image.load(path.join("pictures/save", "clear2.png"))

START_GAME = pygame.USEREVENT + 201
SAVE_BACK_PRESS = pygame.USEREVENT + 202

saves_list = [
    "saves/save1.json",
    "saves/save2.json",
    "saves/save3.json"
]

stat_list = []
# opens and adds all of the saves in saves_list to the list stat_list
for a in range(len(saves_list)):
    with open(saves_list[a], "r") as get_save:
        stat_list.append(json.load(get_save))
selected_stats = {}
selected_save = ""

save_back_button = Button(WIDTH//2, 650, 80, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)


# ratio for save menu buttons are 51:19

new_game_button1 = Button(WIDTH // 6 + 20, 100, 153, 57, NEW_GAME_BUTTON0, NEW_GAME_BUTTON1, NEW_GAME_BUTTON2)
new_game_button2 = Button(3 * WIDTH // 6, 100, 153, 57, NEW_GAME_BUTTON0, NEW_GAME_BUTTON1, NEW_GAME_BUTTON2)
new_game_button3 = Button(5 * WIDTH // 6 - 20, 100, 153, 57, NEW_GAME_BUTTON0, NEW_GAME_BUTTON1, NEW_GAME_BUTTON2)

new_game_button_list = [
    new_game_button1,
    new_game_button2,
    new_game_button3
]

load_game_button1 = Button(WIDTH // 6 + 20, 100, 153, 57, LOAD_GAME_BUTTON0, LOAD_GAME_BUTTON1, LOAD_GAME_BUTTON2)
load_game_button2 = Button(3 * WIDTH // 6, 100, 153, 57, LOAD_GAME_BUTTON0, LOAD_GAME_BUTTON1, LOAD_GAME_BUTTON2)
load_game_button3 = Button(5 * WIDTH // 6 - 20, 100, 153, 57, LOAD_GAME_BUTTON0, LOAD_GAME_BUTTON1, LOAD_GAME_BUTTON2)

load_game_button_list = [
    load_game_button1,
    load_game_button2,
    load_game_button3
]

clear_game_button1 = Button(WIDTH // 6 + 20, 200, 153, 57, CLEAR_GAME_BUTTON0, CLEAR_GAME_BUTTON1, CLEAR_GAME_BUTTON2)
clear_game_button2 = Button(3 * WIDTH // 6, 200, 153, 57, CLEAR_GAME_BUTTON0, CLEAR_GAME_BUTTON1, CLEAR_GAME_BUTTON2)
clear_game_button3 = Button(5 * WIDTH // 6 - 20, 200, 153, 57, CLEAR_GAME_BUTTON0, CLEAR_GAME_BUTTON1,
                            CLEAR_GAME_BUTTON2)

clear_game_button_list = [
    clear_game_button1,
    clear_game_button2,
    clear_game_button3
]

# LOADING SCREEN VARIABLES

LOAD_BAR_WIDTH = 500
LOAD_BAR = pygame.Rect(WIDTH // 2 - LOAD_BAR_WIDTH // 2, 500, LOAD_BAR_WIDTH, 50)
progress = 0

DONE_LOADING = pygame.USEREVENT + 301

LOADING_SCREEN_TIPS = [
    "Try getting good!",
    "Go outside!",
    "Take a shower, you smell!",
    "Upgrade your tilt-proof stat or you will be stuck as a tilter",
    "Each click gives you LP",
    "Money income is proportional to your LP",
    "If you get to challenger on the super server, you win the game!",
    "It's dangerous to go alone. Take this tip with you!"
]

SELECTED_TIP = random.choice(LOADING_SCREEN_TIPS)
TIP_DISPLAY = PARAGRAPH_FONT.render(SELECTED_TIP, True, MAIN_COLOR2)
LOADING_TEXT = HEADER_FONT.render("Loading...", True, MAIN_COLOR2)

# MAIN SCREEN VARIABLES

MAIN_BACKGROUND = pygame.image.load((path.join("pictures/main", "mainbackground.png")))
MAIN_BACKGROUND = pygame.transform.scale(MAIN_BACKGROUND, (WIDTH, HEIGHT))

USER_BUTTON0 = pygame.image.load((path.join("pictures/main", "user0.png")))
USER_BUTTON1 = pygame.image.load((path.join("pictures/main", "user1.png")))
USER_BUTTON2 = pygame.image.load((path.join("pictures/main", "user2.png")))

PC_BUTTON0 = pygame.image.load((path.join("pictures/main", "pc0.png")))
PC_BUTTON1 = pygame.image.load((path.join("pictures/main", "pc1.png")))
PC_BUTTON2 = pygame.image.load((path.join("pictures/main", "pc2.png")))

REGION_BUTTON0 = pygame.image.load((path.join("pictures/main", "region0.png")))
REGION_BUTTON1 = pygame.image.load((path.join("pictures/main", "region1.png")))
REGION_BUTTON2 = pygame.image.load((path.join("pictures/main", "region2.png")))

SAVE_PAPER2 = pygame.image.load((path.join("pictures/save", "savepaper2.png")))
SAVE_PAPER2 = pygame.transform.scale(SAVE_PAPER2, (WIDTH // 2, HEIGHT - 100))

SAVE_BUTTON0 = pygame.image.load((path.join("pictures/main", "save0.png")))
SAVE_BUTTON1 = pygame.image.load((path.join("pictures/main", "save1.png")))
SAVE_BUTTON2 = pygame.image.load((path.join("pictures/main", "save2.png")))

# NOTIF_BAR = pygame.transform.scale(SAVE_PAPER, (WIDTH, 100))

INCOME_BAR_WIDTH = 200
LP_BAR = pygame.Rect(3 * WIDTH // 4 - INCOME_BAR_WIDTH // 2, 70, INCOME_BAR_WIDTH, 25)
MONEY_BAR = pygame.Rect(3 * WIDTH // 4 - INCOME_BAR_WIDTH // 2, 100, INCOME_BAR_WIDTH, 25)

current_tab = 0

lp_progress = 0
money_progress = 0
lp_loss_clicks = 0

click_button = Button(3 * WIDTH // 4, 300, 165, 165, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
save_button = Button(850, 25, 50, 50, SAVE_BUTTON0, SAVE_BUTTON1, SAVE_BUTTON2)

user_tab_button = Button(450 // 3 - 75, -1, 150, 80, USER_BUTTON0, USER_BUTTON1, USER_BUTTON2)
pc_tab_button = Button(450 // 2 + 1, -1, 150, 80, PC_BUTTON0, PC_BUTTON1, PC_BUTTON2)
region_tab_button = Button(2 * 450 // 3 + 77, -1, 150, 80, REGION_BUTTON0, REGION_BUTTON1, REGION_BUTTON2)

NO_BUY_BUTTON = pygame.image.load((path.join("pictures/main", "no_buy.png")))
NO_BUY_BUTTON = pygame.transform.scale(NO_BUY_BUTTON, (100, 40))

user_upgrade_button1 = Button(75, 200, 100, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
user_upgrade_button2 = Button(75, 373, 100, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
user_upgrade_button3 = Button(75, 546, 100, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

user_upgrade_buttons = [
    user_upgrade_button1,
    user_upgrade_button2,
    user_upgrade_button3
]

user_upgrade_icons1 = [
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade1.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade2.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade3.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade4.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade5.png"))),
]

user_upgrade_icons2 = [
    pygame.image.load((path.join("pictures/main/user_upgrade2", "upgrade1.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade2", "upgrade2.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade2", "upgrade3.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade2", "upgrade4.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade2", "upgrade5.png"))),
]

user_upgrade_icons3 = [
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade1.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade2.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade3.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade4.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade5.png"))),
]

user_upgrade_icons = [
    user_upgrade_icons1,
    user_upgrade_icons2,
    user_upgrade_icons3
]

user_upgrades1 = [
    ["", 1, 0, "", ""],
    ["Amateur", "5%", 100, "Reduces rank up requirement by 5%", "\"The beginning of your journey\""],
    ["Intermediate", "10%", 1000, "Reduces rank up requirement by 10%", "\"Your hard work is starting to pay off\""],
    ["Advanced", "15%", 5000, "Reduces rank up requirement by 15%", "\"You are officially 'cracked'\""],
    ["Pro", "20%", 25000, "Reduces rank up requirement by 20%", "\"Just don't join an NA team\""],
    ["Faker", "25%", 100000, "Reduces rank up requirement by 25%", "\"'You just have to not feed' -Faker\""],
]

user_upgrades2 = [
    ["", 1, 0, "", ""],
    ["Coffee", 2, 10, "Increases LP per click to 2", "\"A great starter drink\""],
    ["Monster", 25, 500, "Increases LP per click to 25", "\"For long hours of gaming\""],
    ["Red Bull", 100, 2500, "Increases LP per click to 100", "\"The real deal\""],
    ["G-Fuel", 250, 10000, "Increases LP per click to 250", "\"The G stands for gaming\""],
    ["Mountain Dew", 500, 100000, "Increases LP per click to 500", "\"The elixir of gaming\""],
]

user_upgrades3 = [
    ["", "30%", 0, "", ""],
    ["Tilter", "25%", 50, "Every 20 clicks, 25% chance of LP loss", "\"Jungle diff\""],
    ["Irritable", "20%", 500, "Every 20 clicks, 20% chance of LP loss", "\":/\""],
    ["Chill", "15%", 2500, "Every 20 clicks, 15% chance of LP loss", "\"You get used to losing after a while\""],
    ["Optimistic", "10%", 10000, "Every 20 clicks, 10% chance of LP loss", "\"GLHF! :)\""],
    ["Mental Monk", "5%", 50000, "Every 20 clicks, 5% chance of LP loss", "\"Your mind is a fortress\""],
]

user_upgrades = [
    [user_upgrades1, "Skill"],
    [user_upgrades2, "Energy Drink"],
    [user_upgrades3, "Tilt-proof"]
]

pc_upgrade_button1 = Button(75, 200, 100, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
pc_upgrade_button2 = Button(75, 373, 100, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
pc_upgrade_button3 = Button(75, 546, 100, 40, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

pc_upgrade_buttons = [
    pc_upgrade_button1,
    pc_upgrade_button2,
    pc_upgrade_button3
]

pc_upgrade_icons1 = [
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade1.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade2.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade3.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade4.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade5.png"))),
]

pc_upgrade_icons2 = [
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade1.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade2.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade3.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade4.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade5.png"))),
]

pc_upgrade_icons3 = [
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade1.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade2.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade3.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade4.png"))),
    pygame.image.load((path.join("pictures/main/user_upgrade1", "upgrade5.png"))),
]

pc_upgrade_icons = [
    pc_upgrade_icons1,
    pc_upgrade_icons2,
    pc_upgrade_icons3
]

pc_upgrades1 = [
    ["", 1, 0, "", ""],
    ["Basic Core", 5, 200, "Increases passive LP income to 5", "\"Basic core for a basic person\""],
    ["Octo Core", 20, 1000, "Increases passive LP income to 20", "\"Eight times the L’s\""],
    ["Elite Core", 100, 10000, "Increases passive LP income to 100", "\"Join the elite PC club\""],
    ["Hyper Core", 250, 50000, "Increases passive LP income to 250", "\"Maybe a little overkill...\""],
    ["Nova Core", 1000, 100000, "Increases passive LP income to 1000", "\"I don’t even know if this one is legal\""],
]

pc_upgrades2 = [
    ["", "0", 0, "", ""],
    ["McDonalds", "20%", 100, "Passive LP income is 20% faster", "\"The workers are sick of your raging\""],
    ["Cheap", "40%", 500, "Passive LP income is 40% faster", "\"Kinda sketchy\""],
    ["Modern", "60%", 5000, "Passive LP income is 60% faster", "\"Can’t blame your ping anymore\""],
    ["Fibre Optic", "80%", 10000, "Passive LP income is 80% faster", "\"Speed you can feel\""],
    ["Starlink", "100%", 25000, "Passive LP income is 100% faster", "\"Military grade\""],
]

pc_upgrades3 = [
    ["", "1%", 0, "", ""],
    ["Outdated", "20%", 250, "Passive money income is 20% faster", "\"Get with the times, old man!\""],
    ["Used", "40%", 1000, "Passive money income is 40% faster", "\"Apparently it is 'gently used'\""],
    ["New", "60%", 10000, "Passive money income is 60% faster", "\"Ooooh shiny\""],
    ["Cutting Edge", "80%", 50000, "Passive money income is 80% faster", "\"The lights add more performance\""],
    ["Futuristic", "100%", 100000, "Passive money income is 100% faster", "\"Now you can have multiple chrome tabs\""],
]

pc_upgrades = [
    [pc_upgrades1, "CPU"],
    [pc_upgrades2, "Internet"],
    [pc_upgrades3, "Ram"]
]

region_upgrade_button = Button(WIDTH//4, 270, 150, 80, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)
NO_REGION_BUTTON = pygame.transform.scale(NO_BUY_BUTTON, (150, 80))

REGION_TEXT0 = PARAGRAPH_FONT.render("WARNING: Resets ALL stats", True, RED)
REGION_TEXT1 = DESCRIPTION_FONT.render("Once you reach challenger, you can change regions", True, MAIN_COLOR2)
REGION_TEXT2 = DESCRIPTION_FONT.render("Each time increases all income permanently by 25%", True, MAIN_COLOR2)

region_list = [
    "North America",
    "Europe",
    "China",
    "Korea",
    "Super Server",
    "Freeplay Mode"
]

WIN_THE_GAME = pygame.USEREVENT + 401
RANK_UP = pygame.USEREVENT + 402
LP_LOSE = pygame.USEREVENT + 403

division_list = [
    "",
    "Iron",
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Diamond",
    "Masters",
    "Grandmasters",
    "Challenger"
]
rank_up_requirements = [
    10,
    100,
    1000,
    5000,
    10000,
    50000,
    100000,
    500000,
    1000000,
    ""
]

rank_income = [
    1,
    2,
    5,
    20,
    50,
    100,
    500,
    1000,
    2000,
    5000
]

lp_lose_messages = [
    "The enemy Nasus scaled too much!",
    "Griffin inted your game!",
    "Your Yuumi built Goredrinker!",
    "Your team accidently all typed /ff!",
    "The enemy team picked Gwen!",
    "You played ADC!",
    "Your teammate went AFK!",
    "Your Yasuo never hit his 0/10 powerspike!",
]

# END SCREEN VARIABLES

END_SCREEN_BACKGROUND = pygame.image.load((path.join("pictures/end", "end.png")))
END_SCREEN_BACKGROUND = pygame.transform.scale(END_SCREEN_BACKGROUND, (WIDTH, HEIGHT))

end_screen_button = Button((WIDTH // 2), (4 * HEIGHT // 6), (WIDTH // 2), 125, PLAY_BUTTON0, PLAY_BUTTON1, PLAY_BUTTON2)

END_SCREEN_CONTINUE_PRESSED = pygame.USEREVENT + 501

# ACHIEVEMENTS VARIABLES

FIRST_10_ACHV = pygame.USEREVENT + 601
FIRST_100_ACHV = pygame.USEREVENT + 602
FIRST_500_ACHV = pygame.USEREVENT + 603
FIRST_1000_ACHV = pygame.USEREVENT + 604
FIRST_5000_ACHV = pygame.USEREVENT + 605
FIRST_10000_ACHV = pygame.USEREVENT + 606
FIRST_100000_ACHV = pygame.USEREVENT + 607
FIRST_1000000_ACHV = pygame.USEREVENT + 608
FIRST_TIME_IN_CHALLENGER = pygame.USEREVENT + 609
EU_FIRST = pygame.USEREVENT + 610
CHINA_FIRST = pygame.USEREVENT + 611
KOREA_FIRST = pygame.USEREVENT + 612
SUPER_SERVER_FIRST = pygame.USEREVENT + 613
BEAT_THE_GAME = pygame.USEREVENT + 614
FIRST_1000_LOST = pygame.USEREVENT + 615

with open("saves/achievements.json", "r") as loaded_achievements:
    selected_achievements = json.load(loaded_achievements)

# NOTIFICATIONS VARIABLES

notification_duration = 10 * FPS
# we can change notification queue to just a variable instead of array
# but this allows support for multiple notifications
notification_queue = []
click_visual_queue = []
notification_dict = {
    "FIRST_10_ACHV": "New Achievement! You have reached 10 clicks!",
    "FIRST_100_ACHV": "New Achievement! You have reached 100 clicks!",
    "FIRST_500_ACHV": "New Achievement! You have reached 500 clicks!",
    "FIRST_1000_ACHV": "New Achievement! You have reached 1000 clicks!",
    "FIRST_5000_ACHV": "New Achievement! You have reached 5000 clicks!",
    "FIRST_10000_ACHV": "New Achievement! You have reached 10000 clicks!",
    "FIRST_100000_ACHV": "New Achievement! You have reached 100000 clicks!",
    "FIRST_1000000_ACHV": "New Achievement! You have reached 1000000 clicks!",
    "FIRST_TIME_IN_CHALLENGER": "New Achievement! You have made it to challenger for the first time!",
    "EU_FIRST": "New Achievement! You made it to Europe for the first time!",
    "CHINA_FIRST": "New Achievement! You made it to China for the first time!",
    "KOREA_FIRST": "New Achievement! You made it to Korea for the first time!",
    "SUPER_SERVER_FIRST": "New Achievement! You made it to the Super Server for the first time!",
    "BEAT_THE_GAME": "New Achievement! You have beat the game for the first time!",
    "FIRST_1000_LOST": "New Achievement! You have lost a total of 1000 LP!",
    "LP_LOSE": "",  # change this later on in the code
    "RANK_UP": "",
    "SAVE_GAME": "Game saved!"
}


def draw_intro():
    WIN.fill(MAIN_COLOR)
    WIN.blit(TITLE_PLACEHOLDER, (WIDTH // 2 - TITLE_PLACEHOLDER.get_width() // 2, 150))
    if play_button.draw_button():
        pygame.event.post(pygame.event.Event(PLAY_PRESS))
    if credits_button.draw_button():
        pygame.event.post(pygame.event.Event(CREDITS_PRESS))
    if achievements_button.draw_button():
        pygame.event.post(pygame.event.Event(ACHIEVEMENT_PRESS))

    pygame.display.update()


def draw_credits():
    WIN.fill(MAIN_COLOR2)
    if credits_back_button.draw_button():
        pygame.event.post(pygame.event.Event(CREDITS_BACK_PRESS))
    WIN.blit(CREDITS1, (WIDTH//2 - CREDITS1.get_width()//2, 50))
    WIN.blit(CREDITS2, (WIDTH // 2 - CREDITS2.get_width() // 2, 150))
    WIN.blit(CREDITS3, (WIDTH // 2 - CREDITS3.get_width() // 2, 180))
    WIN.blit(CREDITS4, (WIDTH // 2 - CREDITS4.get_width() // 2, 270))
    WIN.blit(CREDITS5, (WIDTH // 2 - CREDITS5.get_width() // 2, 300))
    WIN.blit(CREDITS6, (WIDTH // 2 - CREDITS6.get_width() // 2, 390))
    WIN.blit(CREDITS7, (WIDTH // 2 - CREDITS7.get_width() // 2, 420))
    pygame.display.update()


def draw_achievements(achievements):
    global current_page
    WIN.fill(MAIN_COLOR2)

    if achievements_back_button.draw_button():
        pygame.event.post(pygame.event.Event(ACHIEVEMENT_BACK_PRESS))
    if clear_achievements_button.draw_button():
        for achievement in selected_achievements:
            selected_achievements[achievement] = 0
        with open("saves/achievements.json", "w") as clear_achievement:
            json.dump(selected_achievements, clear_achievement, indent=4)
        print("reset all achievements")

    if next_page_button.draw_button() and current_page <= 1:
        current_page += 1
        print(current_page)
    if previous_page_button.draw_button() and current_page >= 1:
        current_page -= 1
        print(current_page)

    if current_page == 0:
        WIN.blit(ACHIEVEMENT_NAME1, (300, 50))
        WIN.blit(ACHIEVEMENT_DESCRIPTION1, (300, 80))
        if achievements["FIRST_10_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 30))
        else:
            WIN.blit(TROPHY0, (200, 30))

        WIN.blit(ACHIEVEMENT_NAME2, (300, 150))
        WIN.blit(ACHIEVEMENT_DESCRIPTION2, (300, 180))
        if achievements["FIRST_100_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 130))
        else:
            WIN.blit(TROPHY0, (200, 130))

        WIN.blit(ACHIEVEMENT_NAME3, (300, 250))
        WIN.blit(ACHIEVEMENT_DESCRIPTION3, (300, 280))
        if achievements["FIRST_500_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 230))
        else:
            WIN.blit(TROPHY0, (200, 230))

        WIN.blit(ACHIEVEMENT_NAME4, (300, 350))
        WIN.blit(ACHIEVEMENT_DESCRIPTION4, (300, 380))
        if achievements["FIRST_1000_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 330))
        else:
            WIN.blit(TROPHY0, (200, 330))

        WIN.blit(ACHIEVEMENT_NAME5, (300, 450))
        WIN.blit(ACHIEVEMENT_DESCRIPTION5, (300, 480))
        if achievements["FIRST_5000_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 430))
        else:
            WIN.blit(TROPHY0, (200, 430))

    elif current_page == 1:
        WIN.blit(ACHIEVEMENT_NAME6, (300, 50))
        WIN.blit(ACHIEVEMENT_DESCRIPTION6, (300, 80))
        if achievements["FIRST_10000_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 30))
        else:
            WIN.blit(TROPHY0, (200, 30))

        WIN.blit(ACHIEVEMENT_NAME7, (300, 150))
        WIN.blit(ACHIEVEMENT_DESCRIPTION7, (300, 180))
        if achievements["FIRST_100000_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 130))
        else:
            WIN.blit(TROPHY0, (200, 130))

        WIN.blit(ACHIEVEMENT_NAME8, (300, 250))
        WIN.blit(ACHIEVEMENT_DESCRIPTION8, (300, 280))
        if achievements["FIRST_1000000_ACHV_GOT"] == 1:
            WIN.blit(TROPHY1, (200, 230))
        else:
            WIN.blit(TROPHY0, (200, 230))

        WIN.blit(ACHIEVEMENT_NAME9, (300, 350))
        WIN.blit(ACHIEVEMENT_DESCRIPTION9, (300, 380))
        if achievements["FIRST_1000_LOST"] == 1:
            WIN.blit(TROPHY1, (200, 330))
        else:
            WIN.blit(TROPHY0, (200, 330))

        WIN.blit(ACHIEVEMENT_NAME10, (300, 450))
        WIN.blit(ACHIEVEMENT_DESCRIPTION10, (300, 480))
        if achievements["FIRST_TIME_IN_CHALLENGER"] == 1:
            WIN.blit(TROPHY1, (200, 430))
        else:
            WIN.blit(TROPHY0, (200, 430))

    elif current_page == 2:
        WIN.blit(ACHIEVEMENT_NAME11, (300, 50))
        WIN.blit(ACHIEVEMENT_DESCRIPTION11, (300, 80))
        if achievements["EU_FIRST"] == 1:
            WIN.blit(TROPHY1, (200, 30))
        else:
            WIN.blit(TROPHY0, (200, 30))

        WIN.blit(ACHIEVEMENT_NAME12, (300, 150))
        WIN.blit(ACHIEVEMENT_DESCRIPTION12, (300, 180))
        if achievements["CHINA_FIRST"] == 1:
            WIN.blit(TROPHY1, (200, 130))
        else:
            WIN.blit(TROPHY0, (200, 130))

        WIN.blit(ACHIEVEMENT_NAME13, (300, 250))
        WIN.blit(ACHIEVEMENT_DESCRIPTION13, (300, 280))
        if achievements["KOREA_FIRST"] == 1:
            WIN.blit(TROPHY1, (200, 230))
        else:
            WIN.blit(TROPHY0, (200, 230))

        WIN.blit(ACHIEVEMENT_NAME14, (300, 350))
        WIN.blit(ACHIEVEMENT_DESCRIPTION14, (300, 380))
        if achievements["SUPER_SERVER_FIRST"] == 1:
            WIN.blit(TROPHY1, (200, 330))
        else:
            WIN.blit(TROPHY0, (200, 330))

        WIN.blit(ACHIEVEMENT_NAME15, (300, 450))
        WIN.blit(ACHIEVEMENT_DESCRIPTION15, (300, 480))
        if achievements["BEAT_THE_GAME"] == 1:
            WIN.blit(TROPHY1, (200, 430))
        else:
            WIN.blit(TROPHY0, (200, 430))

    pygame.display.update()


def draw_save():
    global selected_stats
    global selected_save
    WIN.fill(MAIN_COLOR)
    WIN.blit(SAVE_SCREEN_BACKGROUND, (0, 0))
    if save_back_button.draw_button():
        pygame.event.post(pygame.event.Event(SAVE_BACK_PRESS))
    # loops through each list of buttons and loads each of the buttons depending on situatiom
    for b in range(len(stat_list)):
        if stat_list[b]["started"] == 0:
            if new_game_button_list[b].draw_button():
                print("new game for save", b + 1)
                # sets the started stat to 1
                stat_list[b]["started"] = 1
                selected_stats = stat_list[b]
                selected_save = saves_list[b]
                pygame.event.post(pygame.event.Event(START_GAME))
                # saves changes to save file (not final)
                # with open(saves_list[b], "w") as change_save:
                #     json.dump(stat_list[b], change_save, indent=4)
        else:
            if load_game_button_list[b].draw_button():
                print("load game for save", b + 1)
                selected_stats = stat_list[b]
                selected_save = saves_list[b]
                pygame.event.post(pygame.event.Event(START_GAME))
            if clear_game_button_list[b].draw_button():
                print("clear game for save", b + 1)
                # loops through each stat and sets it to 0
                for stat in stat_list[b]:
                    stat_list[b][stat] = 0
                with open(saves_list[b], "w") as change_save:
                    json.dump(stat_list[b], change_save, indent=4)

    pygame.display.update()


def draw_load():
    global progress
    WIN.fill(MAIN_COLOR)
    pygame.draw.rect(WIN, MAIN_COLOR2, LOAD_BAR)
    load_speed = random.randint(50, 500) / 10
    if progress < LOAD_BAR_WIDTH:
        progress += LOAD_BAR_WIDTH * 0.01 * load_speed / FPS
    else:
        progress = LOAD_BAR_WIDTH
        pygame.event.post(pygame.event.Event(DONE_LOADING))

    progress_bar = pygame.Rect(LOAD_BAR.x, LOAD_BAR.y, progress, 50)
    pygame.draw.rect(WIN, (0, 0, 255), progress_bar)

    # loading screen tips
    WIN.blit(TIP_DISPLAY, (WIDTH // 2 - TIP_DISPLAY.get_width() // 2, 300))
    WIN.blit(LOADING_TEXT, (WIDTH // 2 - LOADING_TEXT.get_width() // 2, 150))

    pygame.display.update()


def draw_main(stats, achievements):
    global current_tab
    global lp_progress
    global money_progress
    global lp_loss_clicks
    WIN.fill(MAIN_COLOR2)
    WIN.blit(MAIN_BACKGROUND, (0, 0))

    if stats["rank"] != 9:
        rank_up_requirements_text = rank_up_requirements[stats["rank"]] * (1 - stats["user_upgrade1"] * 0.05)
        lp_message = f'{stats["lp"]:.0f} LP / {rank_up_requirements_text:.0f} LP'
    else:
        lp_message = f'{stats["lp"]:.0f} LP'
    lp_text = PARAGRAPH_FONT.render(lp_message, True, MAIN_COLOR)
    WIN.blit(lp_text, (3 * WIDTH // 4 - lp_text.get_width() // 2, 10))

    money_text = PARAGRAPH_FONT.render(f'${stats["money"]:.0f}   (${rank_income[stats["rank"]]})', True, GREEN)
    WIN.blit(money_text, (3 * WIDTH // 4 - money_text.get_width() // 2, 40))

    # WIN.blit(NOTIF_BAR, (0, HEIGHT - NOTIF_BAR.get_height()))

    # draw the stuff in user tab
    if current_tab == 0:
        # WIN.blit(SAVE_PAPER, (0, 0))
        for i in range(3):
            upgrade = f"user_upgrade{i + 1}"

            if stats[upgrade] != 5:
                name = "Next: " + user_upgrades[i][0][stats[upgrade] + 1][0]
                price = user_upgrades[i][0][stats[upgrade] + 1][2]
                description = user_upgrades[i][0][stats[upgrade] + 1][3]
                flavour = user_upgrades[i][0][stats[upgrade] + 1][4]
                bonus = user_upgrades[i][0][stats[upgrade]][1]
                upgrade_icon = user_upgrade_icons[i][stats[upgrade]]

                if stats["money"] >= price:
                    if user_upgrade_buttons[i].draw_button():
                        stats["money"] -= price
                        stats[upgrade] += 1
                else:
                    WIN.blit(NO_BUY_BUTTON, (75 - NO_BUY_BUTTON.get_width() // 2, 200 + 173 * i))
                price_text = DESCRIPTION_FONT.render(f"${price}", True, MAIN_COLOR)

            else:
                name = user_upgrades[i][0][stats[upgrade]][0]
                price = "MAX"
                description = user_upgrades[i][0][stats[upgrade]][3]
                flavour = user_upgrades[i][0][stats[upgrade]][4]
                bonus = user_upgrades[i][0][stats[upgrade]][1]
                upgrade_icon = user_upgrade_icons[i][stats[upgrade] - 1]

                WIN.blit(NO_BUY_BUTTON, (75 - NO_BUY_BUTTON.get_width() // 2, 200 + 173 * i))

                price_text = DESCRIPTION_FONT.render(price, True, MAIN_COLOR)

            upgrade_text = PARAGRAPH_FONT.render(user_upgrades[i][1], True, YELLOW)
            name_text = DESCRIPTION_FONT.render(name, True, MAIN_COLOR)

            description_text = DESCRIPTION_FONT.render(description, True, MAIN_COLOR)
            flavour_text = DESCRIPTION_FONT.render(flavour, True, MAIN_COLOR)
            bonus_text = DESCRIPTION_FONT.render(f"Current Bonus: {bonus}", True, MAIN_COLOR)

            WIN.blit(upgrade_text, (140, 90 + 173 * i))
            WIN.blit(name_text, (140, 120 + 173 * i))
            WIN.blit(price_text, (350, 120 + 173 * i))
            WIN.blit(description_text, (140, 160 + 173 * i))
            WIN.blit(flavour_text, (140, 190 + 173 * i))
            WIN.blit(bonus_text, (140, 220 + 173 * i))
            WIN.blit(upgrade_icon, (75 - upgrade_icon.get_width()//2, 140 + 173 * i - upgrade_icon.get_height()//2))

    # draw the stuff in PC tab
    elif current_tab == 1:
        # WIN.blit(SAVE_PAPER1, (0, 0))
        for i in range(3):
            upgrade = f"pc_upgrade{i + 1}"

            if stats[upgrade] != 5:
                name = "Next: " + pc_upgrades[i][0][stats[upgrade] + 1][0]
                price = pc_upgrades[i][0][stats[upgrade] + 1][2]
                description = pc_upgrades[i][0][stats[upgrade] + 1][3]
                flavour = pc_upgrades[i][0][stats[upgrade] + 1][4]
                bonus = pc_upgrades[i][0][stats[upgrade]][1]
                upgrade_icon = pc_upgrade_icons[i][stats[upgrade]]

                if stats["money"] >= price:
                    if pc_upgrade_buttons[i].draw_button():
                        stats["money"] -= price
                        stats[upgrade] += 1
                else:
                    WIN.blit(NO_BUY_BUTTON, (75 - NO_BUY_BUTTON.get_width() // 2, 200 + 173 * i))
                price_text = DESCRIPTION_FONT.render(f"${price}", True, MAIN_COLOR)

            else:
                name = pc_upgrades[i][0][stats[upgrade]][0]
                price = "MAX"
                description = pc_upgrades[i][0][stats[upgrade]][3]
                flavour = pc_upgrades[i][0][stats[upgrade]][4]
                bonus = pc_upgrades[i][0][stats[upgrade]][1]
                upgrade_icon = pc_upgrade_icons[i][stats[upgrade] - 1]

                WIN.blit(NO_BUY_BUTTON, (75 - NO_BUY_BUTTON.get_width() // 2, 200 + 173 * i))

                price_text = DESCRIPTION_FONT.render(price, True, MAIN_COLOR)

            upgrade_text = PARAGRAPH_FONT.render(pc_upgrades[i][1], True, PURPLE)
            name_text = DESCRIPTION_FONT.render(name, True, MAIN_COLOR)
            description_text = DESCRIPTION_FONT.render(description, True, MAIN_COLOR)
            flavour_text = DESCRIPTION_FONT.render(flavour, True, MAIN_COLOR)
            bonus_text = DESCRIPTION_FONT.render(f"Current Bonus:{bonus}", True, MAIN_COLOR)
            WIN.blit(upgrade_icon, (75 - upgrade_icon.get_width()//2, 140 + 173 * i - upgrade_icon.get_height()//2))

            WIN.blit(upgrade_text, (140, 90 + 173 * i))
            WIN.blit(name_text, (140, 120 + 173 * i))
            WIN.blit(price_text, (350, 120 + 173 * i))
            WIN.blit(description_text, (140, 160 + 173 * i))
            WIN.blit(flavour_text, (140, 190 + 173 * i))
            WIN.blit(bonus_text, (140, 220 + 173 * i))

    # draw the stuff in region tab
    elif current_tab == 2:
        WIN.blit(SAVE_PAPER2, (0, 0))
        if stats["region"] != 5 and stats["rank"] == 9:
            if region_upgrade_button.draw_button():
                current_region = stats["region"]
                for stat in stats:
                    stats[stat] = 0
                stats["started"] = 1
                stats["region"] = current_region + 1
                if stats["region"] == 5:
                    pygame.event.post(pygame.event.Event(WIN_THE_GAME))
        else:
            WIN.blit(NO_REGION_BUTTON, (WIDTH//4 - NO_REGION_BUTTON.get_width()//2, 270))
        region_text3 = PARAGRAPH_FONT.render(f'Current Bonus: {stats["region"]*25}%', True, MAIN_COLOR2)
        region_text4 = PARAGRAPH_FONT.render(f'Current Region: {region_list[stats["region"]]}', True, MAIN_COLOR2)
        WIN.blit(REGION_TEXT0, (WIDTH//4 - REGION_TEXT0.get_width()//2, 150))
        WIN.blit(REGION_TEXT1, (WIDTH//4 - REGION_TEXT1.get_width()//2, 200))
        WIN.blit(REGION_TEXT2, (WIDTH // 4 - REGION_TEXT2.get_width() // 2, 230))
        WIN.blit(region_text3, (WIDTH // 4 - region_text3.get_width() // 2, 380))
        WIN.blit(region_text4, (WIDTH // 4 - region_text4.get_width() // 2, 420))

    if user_tab_button.draw_button():
        current_tab = 0
    if pc_tab_button.draw_button():
        current_tab = 1
    if region_tab_button.draw_button():
        current_tab = 2

    # calculate lp income
    lp_speed = 1.3 * (1 + 0.2 * stats["pc_upgrade2"])
    if lp_progress < INCOME_BAR_WIDTH:
        lp_progress += INCOME_BAR_WIDTH * 0.5 * lp_speed / FPS
    else:
        lp_progress = 0
        lp_income = round(pc_upgrades1[stats["pc_upgrade1"]][1] * (1 + 0.25 * stats["region"]), 2)
        if lp_income == 0:
            lp_income = 1
        stats["lp"] += lp_income

    pygame.draw.rect(WIN, MAIN_COLOR, LP_BAR)
    lp_progress_bar = pygame.Rect(LP_BAR.x, LP_BAR.y, lp_progress, 25)
    pygame.draw.rect(WIN, (0, 0, 255), lp_progress_bar)

    # calculate money income
    money_speed = 0.5 * (1 + 0.2 * stats["pc_upgrade3"])
    if money_progress < INCOME_BAR_WIDTH:
        money_progress += INCOME_BAR_WIDTH * money_speed / FPS
    else:
        money_progress = 0
        income = rank_income[stats["rank"]]
        stats["money"] += income

    pygame.draw.rect(WIN, MAIN_COLOR, MONEY_BAR)
    money_progress_bar = pygame.Rect(MONEY_BAR.x, MONEY_BAR.y, money_progress, 25)
    pygame.draw.rect(WIN, GREEN, money_progress_bar)

    # click button add 1 lp and random lp loss
    if click_button.draw_button():
        lp_on_click = round(user_upgrades2[stats["user_upgrade2"]][1] * (1 + 0.25 * stats["region"]), 2)
        if lp_on_click.is_integer():
            lp_on_click = round(lp_on_click)
        stats["lp"] += lp_on_click
        achievements["clicks"] += 1
        lp_loss_clicks += 1
        # adds click visuals using dict method over array method
        click_visual_queue.append(
            {"text": f"+{lp_on_click} LP",
             "time": 0,
             "x": pygame.mouse.get_pos()[0],
             "y": pygame.mouse.get_pos()[1]})
        if lp_loss_clicks >= 20:
            choice = random.randint(1, 100)
            lose_threshold = 30 - 5 * stats["user_upgrade3"]
            if choice <= lose_threshold and stats["lp"] > 20:
                lost_amount = (random.randint(4, 8) + round(stats["lp"] * 0.05))
                stats["lp"] -= lost_amount
                achievements["lp_lost"] += lost_amount
                lp_lose_message = random.choice(lp_lose_messages)
                notification_dict["LP_LOSE"] = f"{lp_lose_message} You lost {lost_amount} LP!"
                add_notification("LP_LOSE")
                click_visual_queue.append(
                    {"text": f"-{lost_amount} LP",
                     "time": 0,
                     "x": pygame.mouse.get_pos()[0],
                     "y": pygame.mouse.get_pos()[1]})
            lp_loss_clicks = 0

    # calculate rank ups
    if stats["lp"] >= 10 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 0:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 100 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 1:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 1000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 2:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 5000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 3:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 10000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 4:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 50000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 5:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 100000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 6:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 500000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 7:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))
    if stats["lp"] >= 1000000 * (1 - 0.05 * stats["user_upgrade1"]) and stats["rank"] == 8:
        stats["rank"] += 1
        pygame.event.post(pygame.event.Event(RANK_UP))

    for notification in notification_queue:
        if "You lost" in notification[0]:
            notification_text = PARAGRAPH_FONT.render(notification[0], True, RED)
        else:
            notification_text = PARAGRAPH_FONT.render(notification[0], True, MAIN_COLOR)
        if notification[1] <= notification_duration // 3:
            notification_text.set_alpha(255 * (notification[1] / (notification_duration // 3)))
        WIN.blit(notification_text,
                 (WIDTH // 2 - notification_text.get_width() // 2, 625 + notification[2]))
        if notification[2] > 0 and notification_queue.index(notification) == 0:
            notification[2] -= 2
        if notification[2] > 40 and notification_queue.index(notification) == 1:
            notification[2] -= 2
        notification[1] -= 1
        if notification[1] <= 0:
            notification_queue.remove(notification)

    # handling click visuals
    for visual in click_visual_queue:
        if "-" in visual["text"]:
            visual_text = CLICK_FONT.render(visual["text"], True, RED)
            visual["time"] += 1
        else:
            visual_text = CLICK_FONT.render(visual["text"], True, MAIN_COLOR)
            visual["time"] += 15
        visual_text.set_alpha(255 - visual["time"])
        WIN.blit(visual_text, (visual["x"], visual["y"] - visual["time"]/10))
        if visual["time"] >= 255:
            click_visual_queue.remove(visual)

    # save game button
    if save_button.draw_button():
        with open(selected_save, "w") as change_save:
            json.dump(selected_stats, change_save, indent=4)
        print("saving stats for save", selected_save)

        with open("saves/achievements.json", "w") as update_achievements:
            json.dump(achievements, update_achievements, indent=4)

        add_notification("SAVE_GAME")
    pygame.display.update()


# we can change notification queue to just a variable instead of array
# but this allows support for multiple notifications
def add_notification(notification):
    notification_queue.append([notification_dict[notification], notification_duration, len(notification_queue) * 50])
    if len(notification_queue) > 2:
        notification_queue.pop(0)
    with open("saves/achievements.json", "w") as update_achievements:
        json.dump(selected_achievements, update_achievements, indent=4)


def handle_achievements(stats, achievements):
    if achievements["clicks"] >= 10 and achievements["FIRST_10_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_10_ACHV))
        achievements["FIRST_10_ACHV_GOT"] = 1

    if achievements["clicks"] >= 100 and achievements["FIRST_100_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_100_ACHV))
        achievements["FIRST_100_ACHV_GOT"] = 1

    if achievements["clicks"] >= 500 and achievements["FIRST_500_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_500_ACHV))
        achievements["FIRST_500_ACHV_GOT"] = 1

    if achievements["clicks"] >= 1000 and achievements["FIRST_1000_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_1000_ACHV))
        achievements["FIRST_1000_ACHV_GOT"] = 1

    if achievements["clicks"] >= 5000 and achievements["FIRST_5000_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_5000_ACHV))
        achievements["FIRST_5000_ACHV_GOT"] = 1

    if achievements["clicks"] >= 10000 and achievements["FIRST_10000_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_10000_ACHV))
        achievements["FIRST_10000_ACHV_GOT"] = 1

    if achievements["clicks"] >= 100000 and achievements["FIRST_100000_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_100000_ACHV))
        achievements["FIRST_100000_ACHV_GOT"] = 1

    if achievements["clicks"] >= 1000000 and achievements["FIRST_1000000_ACHV_GOT"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_1000000_ACHV))
        achievements["FIRST_1000000_ACHV_GOT"] = 1

    if stats["rank"] == 9 and achievements["FIRST_TIME_IN_CHALLENGER"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_TIME_IN_CHALLENGER))
        achievements["FIRST_TIME_IN_CHALLENGER"] = 1

    if stats["region"] >= 1 and achievements["EU_FIRST"] == 0:
        pygame.event.post(pygame.event.Event(EU_FIRST))
        achievements["EU_FIRST"] = 1

    if stats["region"] >= 2 and achievements["CHINA_FIRST"] == 0:
        pygame.event.post(pygame.event.Event(CHINA_FIRST))
        achievements["CHINA_FIRST"] = 1

    if stats["region"] >= 3 and achievements["KOREA_FIRST"] == 0:
        pygame.event.post(pygame.event.Event(KOREA_FIRST))
        achievements["KOREA_FIRST"] = 1

    if stats["region"] >= 4 and achievements["SUPER_SERVER_FIRST"] == 0:
        pygame.event.post(pygame.event.Event(SUPER_SERVER_FIRST))
        achievements["SUPER_SERVER_FIRST"] = 1

    if stats["region"] >= 5 and achievements["BEAT_THE_GAME"] == 0:
        pygame.event.post(pygame.event.Event(BEAT_THE_GAME))
        achievements["BEAT_THE_GAME"] = 1

    if achievements["lp_lost"] >= 1000 and achievements["FIRST_1000_LOST"] == 0:
        pygame.event.post(pygame.event.Event(FIRST_1000_LOST))
        achievements["FIRST_1000_LOST"] = 1


def draw_end():
    WIN.fill(MAIN_COLOR)
    WIN.blit(END_SCREEN_BACKGROUND, (0, 0))
    if end_screen_button.draw_button():
        pygame.event.post(pygame.event.Event(END_SCREEN_CONTINUE_PRESSED))

    pygame.display.update()


def main():
    run_intro = True
    run_achievements = False
    run_credits = False
    run_save = False
    run_load = False
    run_main = False
    run_end = False

    while run_intro:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_intro = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_save = True
            if event.type == PLAY_PRESS:
                run_save = True

            if event.type == CREDITS_PRESS:
                run_credits = True

            if event.type == ACHIEVEMENT_PRESS:
                run_achievements = True

        draw_intro()

        while run_credits:
            pygame.time.Clock().tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run_credits = False
                    run_intro = False

                if event.type == CREDITS_BACK_PRESS:
                    run_credits = False

            draw_credits()

        while run_achievements:
            pygame.time.Clock().tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run_achievements = False
                    run_intro = False

                if event.type == ACHIEVEMENT_BACK_PRESS:
                    run_achievements = False

            draw_achievements(selected_achievements)

        while run_save:
            pygame.time.Clock().tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run_save = False
                    run_intro = False

                if event.type == START_GAME:
                    run_save = False
                    run_intro = False
                    run_load = True

                if event.type == SAVE_BACK_PRESS:
                    run_save = False

            draw_save()

    while run_load:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_load = False

            if event.type == DONE_LOADING:
                run_load = False
                run_main = True
                print("Starting game with", selected_save)

        draw_load()

    while run_main:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_main = False

            if event.type == WIN_THE_GAME:
                run_end = True

            if event.type == FIRST_10_ACHV:
                add_notification("FIRST_10_ACHV")

            if event.type == FIRST_100_ACHV:
                add_notification("FIRST_100_ACHV")

            if event.type == FIRST_500_ACHV:
                add_notification("FIRST_500_ACHV")

            if event.type == FIRST_1000_ACHV:
                add_notification("FIRST_1000_ACHV")

            if event.type == FIRST_5000_ACHV:
                add_notification("FIRST_5000_ACHV")

            if event.type == FIRST_10000_ACHV:
                add_notification("FIRST_10000_ACHV")

            if event.type == FIRST_100000_ACHV:
                add_notification("FIRST_100000_ACHV")

            if event.type == FIRST_1000000_ACHV:
                add_notification("FIRST_1000000_ACHV")

            if event.type == FIRST_TIME_IN_CHALLENGER:
                add_notification("FIRST_TIME_IN_CHALLENGER")

            if event.type == EU_FIRST:
                add_notification("EU_FIRST")

            if event.type == CHINA_FIRST:
                add_notification("CHINA_FIRST")

            if event.type == KOREA_FIRST:
                add_notification("KOREA_FIRST")

            if event.type == SUPER_SERVER_FIRST:
                add_notification("SUPER_SERVER_FIRST")

            if event.type == BEAT_THE_GAME:
                add_notification("BEAT_THE_GAME")

            if event.type == FIRST_1000_LOST:
                add_notification("FIRST_1000_LOST")

            if event.type == RANK_UP:
                notification_dict["RANK_UP"] = f'You ranked up to {division_list[selected_stats["rank"]]}!'
                add_notification("RANK_UP")

        draw_main(selected_stats, selected_achievements)
        handle_achievements(selected_stats, selected_achievements)
        while run_end:
            pygame.time.Clock().tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run_end = False
                    run_main = False

                if event.type == END_SCREEN_CONTINUE_PRESSED:
                    run_end = False

            draw_end()

    pygame.quit()


if __name__ == "__main__":
    main()
