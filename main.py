import pygame
from pygame import mixer
import time
import pygame.font
import speech_recognition as sr
from pygame.locals import *

start_time = pygame.time.get_ticks()

#Initialization
pygame.init()

#Screen creation 
screen = pygame.display.set_mode((1200,700))

#landing page image
land_image = pygame.image.load("land_image.jpg")

'''Background sound'''
mixer.music.load("smilee.mp3")
mixer.music.play(-1)

#page_2
char_s_image = pygame.image.load("Premium-Vector-Happy-cute-little-kid-study-alphabet-character.png")
char_s_image_status = 0

#page_3
char_s_scene = pygame.image.load("first_image.jpg")
char_s_scene_status = 0
s_command = mixer.Sound("s_command.mp3")
a_command = mixer.Sound("a_command.mp3")

#page5
night_scene_image = pygame.image.load("night_scene.jpg")
night_scene_image_status = 0 #currently inactive

#page_7
forest_scene_image = pygame.image.load("forest_scene_image.jpg")
forest_scene_status = 0 #currently inactive

#page 9
branch_scene_image = pygame.image.load("branch_scene.jpg")

#page 11
stars_scene = pygame.image.load("stars_scene.jpg")

# -----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# char a image
char_a_image = pygame.image.load("char_a_image.png")
a1_scene = pygame.image.load("a1_scene.png")
a1_apples = pygame.image.load("a1_apples.png")
a1_axe = pygame.image.load("a1_axe.png")
a1_ant = pygame.image.load("a1_ant.png")

a2_scene = pygame.image.load("a2_scene.png")
a2_apples = pygame.image.load("a2_apples.png")
a2_axe = pygame.image.load("a2_axe.png")
a2_alligator = pygame.image.load("a2_alligator.png")
a2_ant = pygame.image.load("a2_ant.png")

a3_scene = pygame.image.load("a3_scene.png")
a3_arrow = pygame.image.load("a3_arrow.png")

a4_scene = pygame.image.load("a4_scene.png")
a4_ambulance = pygame.image.load("a4_ambulance.png")

#Setting the Title
pygame.display.set_caption("Sakshar Game By Anushk Gupta and Aatif Ahmad")

#Setting the icon
icon_image = pygame.image.load("languages.png")
pygame.display.set_icon(icon_image)

#Sun Image Load
sun_image = pygame.image.load("final_sun_image.jpg")

#Snake Image Load
snake_image = pygame.image.load("snake.jpg")
forest_snake_image = pygame.image.load("forest_snake.jpg")

#Swing Image Load
swing_image = pygame.image.load("swing.jpg")

#Stone Image Load
stone_image = pygame.image.load("stone_image.jpg")
forest_stone_image = pygame.image.load("forest_stone.jpg")

#spider image load
spider_image = pygame.image.load("spider.jpg")
forest_spider_image = pygame.image.load("forest_spider.jpg")

#stars image load
stars_image = pygame.image.load("stars.jpg")
six_image = pygame.image.load("six.png")
superstar_sound = mixer.Sound("superstar.mp3")
try_sound = mixer.Sound("try.mp3")

#empty screen image for branches number
white_band = pygame.image.load("empty_screen.png")

#font for the text of the buttons
font = pygame.font.Font("freesansbold.ttf",28)

font_num = pygame.font.Font("freesansbold.ttf",56)

font2 = pygame.font.Font("freesansbold.ttf",32)
font3 = pygame.font.Font("freesansbold.ttf",48)
font4 = pygame.font.Font("freesansbold.ttf",84)


#winner image load
winner_image = pygame.image.load("46141 (1).jpg")
winner_image_2 = pygame.image.load("win2.png")
winner_image_3 = pygame.image.load("win3.png")
winner_image_4 = pygame.image.load("win4.png")
winner_image_5 = pygame.image.load("win5.png")
winner_image_6 = pygame.image.load("win6.png")
winner_image_7 = pygame.image.load("win7.png")
winner_image_8 = pygame.image.load("win8.png")
winner_image_9 = pygame.image.load("win9.png")

#sakshar image
sakshar_image = pygame.image.load("SAKSHAR.jpg")

#text names of the images   
font_new = pygame.font.Font("freesansbold.ttf", 42)
sun_text = font_new.render("sun", True, (255,128, 0))
stone_text = font_new.render("stones", True, (102,0,204))
swing_text = font_new.render("swing", True, (210,0,0))
snake_text = font_new.render("snake", True, (0,160,0))
spider_text = font_new.render("spider",True,(0,0,200))
forest_spider_text = font_new.render("spider",True,(240,30,30))
stars_text = font_new.render("stars",True,(240,230,30))
six_text = font_new.render("six",True,(0,0,200))


#a1_scene
ant_sound = mixer.Sound("ant_sound.mp3")
apples_sound = mixer.Sound("apples_sound.mp3")
axe_sound = mixer.Sound("axe_sound.mp3")
apples_text = font_new.render("apples", True, (205,10,10))
axe_text = font_new.render("axe", True, (70,70,70))
ant_text = font_new.render("ant", True, (153,0,76))


#a2_scene
ant_sound = mixer.Sound("ant_sound.mp3")
apples_sound = mixer.Sound("apples_sound.mp3")
axe_sound = mixer.Sound("axe_sound.mp3")
alligator_sound = mixer.Sound("alligator_sound.mp3")
alligator_text = font_new.render("alligator", True, (0,155,0))
apples_text = font_new.render("apples", True, (205,10,10))
axe_text = font_new.render("axe", True, (70,70,70))
ant_text = font_new.render("ant", True, (153,0,76))

#a3scene
arrow_sound = mixer.Sound("arrow_sound.mp3")
arrow_text = font_new.render("arrow", True, (255,128,0))

#a4scene
ambulance_sound = mixer.Sound("ambulance_sound.mp3")
ambulance_text = font_new.render("ambulance", True, (0,100,210))

#tmodule
t_char_image = pygame.image.load("t_char.png")

#sun,stones,snake and swing sound
sun_sound = mixer.Sound("Sun.mp3")
stones_sound = mixer.Sound("Stones.mp3")
snake_sound = mixer.Sound("Snake.mp3")
swing_sound = mixer.Sound("Swing.mp3")

#for the night scene
night_stones_sound = mixer.Sound("Stones.mp3")
night_swing_sound = mixer.Sound("Swing.mp3")
spider_sound = mixer.Sound("spider.mp3")
stars_sound = mixer.Sound("stars.mp3")

#for the branches scene and stars scene
branches_sound = mixer.Sound("branches_sound.mp3")
stars_scene_sound = mixer.Sound("stars_sound_1.mp3")

def sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def night_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def a1_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def a2_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def a3_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def a4_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def forest_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def wrong_answer_sound_play():
    wrong_answer_sound = mixer.Sound("wrong_ans.wav")
    wrong_answer_sound.play()

def branch_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def post_audio_scene_sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()

def show_score(x,y,points):
    score = font_new.render("Score : "+str(points),True,(255,130,0))
    screen.blit(score,(x,y))

def get_speech_input():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source, timeout=3)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError as e:
            print("Sorry, I encountered an error while requesting the API; {0}".format(e))
            return None


# def get_speech_input():
#     recognizer = sr.Recognizer()

#     # List available audio devices (microphones)
#     print("Available audio devices:")
#     microphone_names = sr.Microphone.list_microphone_names()
#     for index, name in enumerate(microphone_names):
#         print(f"{index}: {name}")

#     # Try to find the Bluetooth speaker by name
#     # bluetooth_speaker_name = 'JBL GO 2'
#     # speaker_index = next((i for i, name in enumerate(microphone_names) if bluetooth_speaker_name in name), None)

#     # if speaker_index is not None:
#     #     try:
#     #         with sr.Microphone(device_index=speaker_index) as source:
#     #             print(f"Using {bluetooth_speaker_name} as the audio source")
#     #             print("Say something:")
#     #             audio = recognizer.listen(source, timeout=3)

#     #         text = recognizer.recognize_google(audio)
#     #         print("You said:", text)
#     #         return text

#     #     except sr.UnknownValueError:
#     #         print("Sorry, I could not understand what you said.")
#     #         return None
#     #     except sr.RequestError as e:
#     #         print(f"Sorry, I encountered an error while requesting the API: {e}")
#     #         return None
#     # else:
#     #     print(f"{bluetooth_speaker_name} not found in the list of available audio devices.")
#     #     return None




#the button class with init method having parameters as text, x-y coordinates, button enabling, height and width
class Button:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):
        
        button_text = font.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#f07e0c",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 5,self.y_pos + 10))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
class Button4:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):
        
        button_text = font3.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#f07e0c",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 5,self.y_pos + 10))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Button2:
    def __init__(self, text, x_pos, y_pos, enabled, height, width,hovered):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        self.hovered = hovered  # Track whether the mouse pointer is over the button

    def draw(self):
        if self.hovered:
            button_color = (49, 20, 50)  # Red when hovered
        else:
            button_color = (122, 73, 136)  # Default color

        button_text = font2.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        pygame.draw.rect(screen, button_color, button_rect, 0, 5)
        screen.blit(button_text, (self.x_pos + 5, self.y_pos + 5))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        self.hovered = button_rect.collidepoint(mouse_pos)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
class Button3:
    def __init__(self, text, x_pos, y_pos, enabled, height, width,hovered):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        self.hovered = hovered  # Track whether the mouse pointer is over the button

    def draw(self):
        if self.hovered:
            button_color = (49, 20, 50)  # Red when hovered
        else:
            button_color = (122, 73, 136)  # Default color

        button_text = font4.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        pygame.draw.rect(screen, button_color, button_rect, 0, 5)
        screen.blit(button_text, (self.x_pos + 10, self.y_pos + 10))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        self.hovered = button_rect.collidepoint(mouse_pos)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


class New_Button:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):
        button_text = font_num.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#12e3d9",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 20,self.y_pos + 17))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
    
        
#Beginning status of several elements which will be modified as per the transitions of the game
input_1 = True
input_2 = False
char_s_scene_status = 0
sun_image_status = 0
snake_image_status = 0
swing_image_status = 0
stone_image_status = 0
sound_play_status = 1
night_scene_sound_play_status = 1
music_play_status = 0
delay_status = 1
sun_sound_status = 1 # 1 means active now.....From now onwards, I will use this notation
snake_sound_status = 1
stones_sound_status = 1
swing_sound_status = 1
night_stones_sound_status = 1 #active
night_swing_sound_status = 1 #active
spider_image_status = 1 #currently inactive
stars_image_status = 1 #currently inactive
spider_sound_status = 1 #active
stars_sound_status = 1
night_delay_status = 1 #for delay
forest_spider_sound_status = 1 #active
forest_sun_sound_status = 1 #active
forest_stones_sound_status = 1 #active
forest_snake_sound_status = 1 #active
forest_delay_status = 1
forest_scene_sound_play_status = 1
branch_scene_status = 0 #inactive
branch_scene_sound_status = 1 #active
post_branch_scene_status = 0 #inactive
branch_sound_status = 1 #active
stars_scene_status = 0 #inactive
stars_scene_sound_status = 1 #active
speech_detection_status = 0 #inactive---------------------------
superstar_sound_status = 1 #active
six_image_status = 0 #inactive
post_stars_scene_status = 0 #inactive
post_audio_scene_sound_status = 1
char_a_image_status = 0
a1scene_status = 0
a1_apples_image_status = 0 #inactive
a1_axe_image_status = 0 #inactive
a1_ant_image_status = 0
a1_apples_sound_status = 1
a1_axe_sound_status = 1
a1_ant_sound_status = 1
a1_delay_status = 1
a1_scene_sound_play_status = 1

a2_scene_status = 0

a2_apples_status = 0
a2_alligator_status = 0
a2_axe_status = 0
a2_ant_status = 0
a2_delay_status = 1
a2_scene_sound_play_status = 1
a2_apples_sound_status = 1
a2_axe_sound_status = 1
a2_alligator_sound_status = 1
a2_ant_sound_status = 1

a3_scene_status = 0

a3_apples_status = 0
a3_axe_status = 0
a3_arrow_status = 0
a3_scene_sound_play_status = 1
a3_delay_status = 1
a3_apples_sound_status = 1
a3_axe_sound_status = 1
a3_arrow_sound_status = 1

a4_scene_status = 0
a4_apples_status = 0
a4_ambulance_status = 0
a4_alligator_status = 0
a4_ant_status = 0
a4_delay_status = 1
a4_scene_sound_play_status = 1
a4_apples_sound_status = 1
a4_alligator_sound_status = 1
a4_ambulance_sound_status = 1
a4_ant_sound_status = 1

t_char_status = 0
t1_scene_status = 0

s_command_status = 1
a_command_status = 1

#analytics
time_0_0_status = 1
time_1_1_status = 1
time_1_2_1_status = 1
time_1_2_status = 1
time_1_3_1_status = 1
time_1_3_status = 1
time_1_4_1_status = 1
time_1_4_status = 1
time_1_5_1_status = 1
time_1_5_status = 1
time_2_1_1_status = 1
time_2_1_status = 1
time_2_2_1_status = 1
time_2_2_status = 1
time_2_3_1_status = 1
time_2_3_status = 1
time_2_4_1_status = 1
time_2_4_status = 1
time_3_1_1_status = 1
time_3_1_status = 1


time_0_0 = 0
time_1_1 = 0
time_1_2_1 = 0
time_1_2 = 0
time_1_3_1 = 0
time_1_3 = 0
time_1_4_1 = 0
time_1_4 = 0
time_1_5_1 = 0
time_1_5 = 0
time_2_1_1 = 0
time_2_1 = 0
time_2_2_1 = 0
time_2_2 = 0
time_2_3_1 = 0
time_2_3 = 0
time_2_4_1 = 0
time_2_4 = 0
time_3_1_1 = 0
time_3_1 = 0


control = True #status of the main while loop
while control: #main running loop of the game screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control = False
         #ensuring that the screen ends only when the quit event is pressed
        
    
    my_button_3 = Button("SUN",240,15,True,150,130)
    my_button_3.draw()

    my_button_4 = Button("SNAKE",800,550,True,200,150)
    my_button_4.draw()

    my_button_5 = Button("SWING",500,200,True,240,150)
    my_button_5.draw()

    my_button_6 = Button("STONE",50,500,True,150,150)
    my_button_6.draw()

    my_button_7 = Button("SPIDER",780,250,True,100,90)
    my_button_7.draw()

    my_button_8 = Button("STARS",40,10,True,120,165)
    my_button_8.draw()

    my_button_11 = Button("SUN",770,10,True,180,180)
    my_button_11.draw()

    my_button_12 = Button("SPIDER",0,600,True,100,100)
    my_button_12.draw()

    my_button_13 = Button("STONE",320,590,True,85,85)
    my_button_13.draw()

    my_button_14 = Button("SNAKE",880,620,True,100,100)
    my_button_14.draw()

    my_button_25 = Button("APPLES",400,150,True,250,400)
    my_button_25.draw()

    my_button_26 = Button("AXE",400,510,True,55,50)
    my_button_26.draw() #--------------26 buttons so far

    my_button_27 = Button("ANT",858,550,True,35,60)
    my_button_27.draw()

    #for a2 scene
    my_button_29 = Button("APPLES",570,100,True,180,280)
    my_button_29.draw()
    my_button_30 = Button("ALLIGATOR",40,470,True,100,270)
    my_button_30.draw()
    my_button_31 = Button("AXE",440,430,True,80,90)
    my_button_31.draw()
    my_button_32 = Button("ANT",900,390,True,30,70)
    my_button_32.draw()

    #for a3 scene
    my_button_35 = Button("APPLES",400,150,True,250,400)
    my_button_35.draw()
    my_button_36 = Button("AXE",400,510,True,55,50)
    my_button_36.draw() #--------------26 buttons so far
    my_button_37 = Button("ARROW",840,460,True,80,120)
    my_button_37.draw()

    #for a4scene
    my_button_40 = Button("APPLES",570,100,True,180,280)
    my_button_40.draw()
    my_button_41 = Button("ALLIGATOR",40,470,True,100,270)
    my_button_41.draw()
    my_button_42 = Button("ANT",900,390,True,30,70)
    my_button_42.draw()
    my_button_43 = Button("AMBULANCE",500,550,True,120,320)
    my_button_43.draw()

    
    screen.blit(land_image,(0,0))
    screen.blit(sakshar_image,(270,5))

    
    my_button_1 = Button4("LET US PLAY",360,590,True,60,320)
    my_button_1.draw()
    input_1 = my_button_1.check_click()
    if input_1:
        char_s_image_status = 1
        

    # my_button_2 = Button("NEXT",470,90,True,50,90)
    
    if char_s_image_status == 1:
        if s_command_status == 1:
            s_command.play()
            s_command_status = 0
        screen.fill((255,255,255))
        screen.blit(char_s_image,(180,170))
        my_button_2 = Button("NEXT",470,90,True,50,90)
        my_button_2.draw()
        input_2 = my_button_2.check_click()
        if input_2:
            char_s_scene_status = 1
    
    if char_s_scene_status == 1:
        if time_0_0_status == 1:
            time_0_0 = pygame.time.get_ticks()
            time_0_0_status = 0
        char_s_image_status = 0
        screen.blit(char_s_scene,(0,0))
        input_3 = my_button_3.check_click()
        if input_3:
            sun_image_status = 1
        
        input_4 = my_button_4.check_click()
        if input_4:
            snake_image_status = 1

        input_5 = my_button_5.check_click()
        if input_5:
            swing_image_status = 1

        input_6 = my_button_6.check_click()
        if input_6:
            stone_image_status = 1
    
    #blitting the images of elements on the screen after their positions are clicked
    if sun_image_status == 1:
        
        char_s_image_status = 2
        screen.blit(sun_image,(220,1))
        screen.blit(sun_text, (130, 60))
        if sun_sound_status == 1:
            sun_sound.play()
            sun_sound_status = 0
      
    if snake_image_status == 1:
        screen.blit(snake_image,(787,557))
        screen.blit(snake_text,(790,480))
        if snake_sound_status == 1:
            snake_sound.play()
            snake_sound_status = 0

    if swing_image_status == 1:
        screen.blit(swing_image,(518,192))
        screen.blit(swing_text,(390,280))
        if swing_sound_status == 1:
            swing_sound.play()
            swing_sound_status = 0
        
    if stone_image_status == 1:
        screen.blit(stone_image,(28,517))
        screen.blit(stone_text,(280,600))
        if stones_sound_status == 1:
            stones_sound.play()
            stones_sound_status = 0
      
    if sun_image_status == 1 and snake_image_status == 1 and swing_image_status == 1 and stone_image_status == 1 and delay_status == 1:
        screen.blit(stone_image,(28,517))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image,(165,20))
        if time_1_1_status == 1:
            time_1_1 = pygame.time.get_ticks() - time_0_0
            time_1_1_status = 0
        if sound_play_status == 1:
            sound_play()
            sound_play_status = 0
        my_button_9 = Button("NEXT",480,500,True,50,90)
        my_button_9.draw()
        input_7 = my_button_9.check_click()
        if input_7:
            second_char_status = 1

    if sun_image_status == 1 and snake_image_status == 1 and swing_image_status == 1 and stone_image_status == 1 and delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image,(165,20))
        show_score(420,280,1)
        if sound_play_status == 1:
            sound_play()
            sound_play_status = 0
        my_button_9 = Button("NEXT",480,500,True,50,90)
        my_button_9.draw()
        input_7 = my_button_9.check_click()
        if input_7:
            night_scene_image_status = 1

    #-------------------------Day Scene ----->>>>  Night Scene----------------------------
        
    if night_scene_image_status == 1:
        if time_1_2_1_status == 1:
            time_1_2_1 = pygame.time.get_ticks()
            time_1_2_1_status = 0
        sun_image_status = 2
        screen.blit(night_scene_image,(0,0))
        input_8 = my_button_6.check_click()
        if input_8:
            stone_image_status = 2
        
        input_9 = my_button_5.check_click()
        if input_9:
            swing_image_status = 2

        input_10 = my_button_7.check_click()
        if input_10:
            spider_image_status = 2

        input_11 = my_button_8.check_click()
        if input_11:
            stars_image_status = 2
    
    if stone_image_status == 2:
        screen.blit(stone_image,(8,527))
        screen.blit(stone_text,(280,600))
        if night_stones_sound_status == 1:
            night_stones_sound.play()
            night_stones_sound_status = 0

    if swing_image_status == 2:
        screen.blit(swing_image,(522,187))
        screen.blit(swing_text,(390,280))
        if night_swing_sound_status == 1:
            night_swing_sound.play()
            night_swing_sound_status = 0

    if spider_image_status == 2:
        screen.blit(spider_image,(775,258))
        screen.blit(spider_text,(790,380))
        if spider_sound_status == 1:
            spider_sound.play()
            spider_sound_status = 0

    if stars_image_status == 2:
        screen.blit(stars_image,(40,13))
        screen.blit(stars_text,(12,145))
        if stars_sound_status == 1:
            stars_sound.play()
            stars_sound_status = 0

    if stone_image_status == 2 and swing_image_status == 2 and spider_image_status == 2 and stars_image_status == 2 and night_delay_status == 1:
        screen.blit(stone_image,(8,527))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        night_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_2,(165,20))
        if time_1_2_status == 1:
            time_1_2 = pygame.time.get_ticks() - time_1_2_1
            time_1_2_status = 0
        if night_scene_sound_play_status == 1:
            night_scene_sound_play()
            night_scene_sound_play_status = 0
        my_button_10 = Button("NEXT",480,500,True,50,90)
        my_button_10.draw()
        input_12 = my_button_10.check_click()
        if input_12:
            forest_scene_status = 1

    if stone_image_status == 2 and swing_image_status == 2 and spider_image_status == 2 and stars_image_status == 2 and night_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image_2,(165,20))
        show_score(420,280,2)
        if night_scene_sound_play_status == 1:
            night_scene_sound_play()
            night_scene_sound_play_status = 0
        my_button_10 = Button("NEXT",480,500,True,50,90)
        my_button_10.draw()
        input_12 = my_button_10.check_click()
        if input_12:
            forest_scene_status = 1

    #---------------------Night Scene ----->>>  Forest Scene------------------------------------
    
    if forest_scene_status == 1:
        if time_1_3_1_status == 1:
            time_1_3_1 = pygame.time.get_ticks()
            time_1_3_1_status = 0
        night_scene_image_status = 2
        screen.blit(forest_scene_image,(0,0))
        input_13 = my_button_11.check_click()
        if input_13:
            sun_image_status = 3

        input_14 = my_button_12.check_click()
        if input_14:
            spider_image_status = 3

        input_15 = my_button_13.check_click()
        if input_15:
            stone_image_status = 3

        input_16 = my_button_14.check_click()
        if input_16:
            snake_image_status = 3

    if spider_image_status == 3:
        screen.blit(forest_spider_image,(0,600))
        screen.blit(forest_spider_text,(100,580))
        if forest_spider_sound_status == 1:
            spider_sound.play()
            forest_spider_sound_status = 0

    if sun_image_status == 3:
        screen.blit(sun_image,(770,10))
        screen.blit(sun_text, (670, 50))
        if forest_sun_sound_status == 1:
            sun_sound.play()
            forest_sun_sound_status = 0

    
    if stone_image_status == 3:
        screen.blit(forest_stone_image,(310,590))
        screen.blit(stone_text,(420,550))
        if forest_stones_sound_status == 1:
            night_stones_sound.play()
            forest_stones_sound_status = 0

    if snake_image_status == 3:
        screen.blit(forest_snake_image,(850,580))
        screen.blit(snake_text,(685,580))
        if forest_snake_sound_status == 1:
            snake_sound.play()
            forest_snake_sound_status = 0
        

    if stone_image_status == 3 and spider_image_status == 3 and snake_image_status == 3 and sun_image_status == 3 and forest_delay_status == 1:
        screen.blit(forest_stone_image,(310,590))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        forest_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_3,(165,20))
        if time_1_3_status == 1:
            time_1_3 = pygame.time.get_ticks() - time_1_3_1
            time_1_3_status = 0
        if forest_scene_sound_play_status == 1:
            forest_scene_sound_play()
            forest_scene_sound_play_status = 0
        my_button_15 = Button("NEXT",488,500,True,50,90)
        my_button_15.draw()
        input_17 = my_button_15.check_click()
        if input_17:
            branch_scene_status = 1

    if stone_image_status == 3 and spider_image_status == 3 and snake_image_status == 3 and sun_image_status == 3 and forest_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image_3,(165,20))
        show_score(420,280,3)
        if forest_scene_sound_play_status == 1:
            forest_scene_sound_play()
            forest_scene_sound_play_status = 0
        my_button_15 = Button("NEXT",488,500,True,50,90)
        my_button_15.draw()
        input_17 = my_button_15.check_click()
        if input_17:
            branch_scene_status = 1

    if branch_scene_status == 1:
        if time_1_4_1_status == 1:
            time_1_4_1 = pygame.time.get_ticks()
            time_1_4_1_status = 0
        forest_scene_status = 2
        screen.blit(branch_scene_image,(0,0))
        screen.blit(white_band,(0,450))
        if branch_sound_status:
            branches_sound.play()
            branch_sound_status = 0
        my_button_16 = New_Button("4",100,570,True,75,75)
        my_button_16.draw()
        my_button_17 = New_Button("5",350,570,True,75,75)
        my_button_17.draw()
        my_button_18 = New_Button("6",600,570,True,75,75)
        my_button_18.draw()
        my_button_19 = New_Button("7",850,570,True,75,75)
        my_button_19.draw()
        input_18 = my_button_18.check_click()
        if input_18:
            post_branch_scene_status = 1
        input_19 = my_button_16.check_click()
        if input_19:
            wrong_answer_sound_play()
        input_20 = my_button_17.check_click()
        if input_20:
            wrong_answer_sound_play()
        input_21 = my_button_19.check_click()
        if input_21:
            wrong_answer_sound_play()
        
            
    if post_branch_scene_status == 1:
        branch_scene_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_4,(165,20))
        if time_1_4_status == 1:
            time_1_4 = pygame.time.get_ticks() - time_1_4_1
            time_1_4_status = 0
        mixer.music.pause() #music paused here -------------------------------
        show_score(420,280,4)
        if branch_scene_sound_status == 1:
                branch_scene_sound_play()
                branch_scene_sound_status = 0 #inactive
        my_button_20 = Button("NEXT",485,500,True,50,90)
        my_button_20.draw()
        input_22 = my_button_20.check_click()
        if input_22:
            stars_scene_status = 1

    #---------------------Branches scene >>>>>>> Stars scene----------------
    if stars_scene_status == 1:
        post_branch_scene_status = 2 # so that it does not pop up again
        screen.blit(stars_scene,(0,0))
        if time_1_5_1_status == 1:
            time_1_5_1 = pygame.time.get_ticks()
            time_1_5_1_status = 0
        my_button_21 = Button("SPEAK",475,630,True,50,110)
        my_button_21.draw()
        if stars_scene_sound_status == 1:
            stars_scene_sound.play()
            stars_scene_sound_status = 0
        input_23 = my_button_21.check_click()
        if input_23:
            speech_detection_status = 1
            

    if speech_detection_status == 1:
        output = get_speech_input()
        if output == "there are six stars" or output == "there are 6 stars":
            six_image_status = 1
            speech_detection_status = 2
        else:
            my_button_21.active = False
            try_sound.play()

    if six_image_status == 1:
        speech_detection_status = 2
        input_23 = 0
        stars_scene_status = 2 #so that it does not pop up again
        screen.fill((255,255,255))
        screen.blit(six_image,(250,150))
        if time_1_5_status == 1:
            time_1_5 = pygame.time.get_ticks() - time_1_5_1
            time_1_5_status = 0
        if superstar_sound_status == 1:
            superstar_sound.play()
            superstar_sound_status = 0
        screen.blit(six_text,(450,100))
        my_button_22 = Button("NEXT",450,600,True,50,90)
        my_button_22.draw()
        input_24 = my_button_22.check_click()
        if input_24:
            post_stars_scene_status = 1
        
    if post_stars_scene_status == 1:
        mixer.music.play() # music resumed here ----------------------------------
        six_image_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_5,(165,20))
        show_score(420,280,5)
        my_button_23 = Button("NEXT",480,500,True,50,90)
        my_button_23.draw()
        if post_audio_scene_sound_status:
            post_audio_scene_sound_play()
            post_audio_scene_sound_status = 0
        input_25 = my_button_23.check_click()
        if input_25:
            char_a_image_status = 1

    if char_a_image_status == 1:
        if a_command_status == 1:
            a_command.play()
            a_command_status = 0
        post_stars_scene_status = 2
        screen.fill((255,255,255))
        screen.blit(char_a_image,(120,130))
        my_button_24 = Button("NEXT",445,90,True,50,90)
        my_button_24.draw()
        input_26 = my_button_24.check_click()
        if input_26:
            a1scene_status = 1
    
    if a1scene_status == 1:
        screen.blit(a1_scene,(0,0))
        if time_2_1_1_status == 1:
            time_2_1_1 = pygame.time.get_ticks()
            time_2_1_1_status = 0
        input_27 = my_button_25.check_click()
        if input_27 :
            a1_apples_image_status = 1
        input_28 = my_button_26.check_click()
        if input_28:
            a1_axe_image_status = 1
        
        input_29 = my_button_27.check_click()
        if input_29:
            a1_ant_image_status = 1
        
    
    
            
    if a1_apples_image_status == 1:
        screen.blit(a1_apples,(0,0))
        screen.blit(apples_text,(250,150))
        if a1_apples_sound_status == 1:
            apples_sound.play()
            a1_apples_sound_status = 0

    if a1_axe_image_status == 1:
        screen.blit(a1_axe,(0,458))
        screen.blit(axe_text,(200,470))
        if a1_axe_sound_status == 1:
            axe_sound.play()
            a1_axe_sound_status = 0

    if a1_ant_image_status == 1:
        screen.blit(a1_ant,(800,521))
        screen.blit(ant_text,(820,480))
        if a1_ant_sound_status == 1:
            ant_sound.play()
            a1_ant_sound_status = 0

    
    if a1_apples_image_status == 1 and a1_axe_image_status == 1 and a1_ant_image_status == 1 and a1_delay_status == 1:
        screen.blit(a1_ant,(800,521))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        a1_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_6,(165,20))
        if time_2_1_status == 1:
            time_2_1 = pygame.time.get_ticks() - time_2_1_1
            time_2_1_status = 0
        if a1_scene_sound_play_status == 1:
            a1_scene_sound_play()
            a1_scene_sound_play_status = 0
        my_button_28 = Button("NEXT",480,550,True,50,90)
        my_button_28.draw()
        input_30 = my_button_28.check_click()
        if input_30:
            a2_scene_status = 1

    if a1_apples_image_status == 1 and a1_axe_image_status == 1 and a1_ant_image_status == 1 and a1_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image_6,(165,20))
        show_score(420,280,6)
        if a1_scene_sound_play_status == 1:
            a1_scene_sound_play()
            a1_scene_sound_play_status = 0
        my_button_28 = Button("NEXT",480,550,True,50,90)
        my_button_28.draw()
        input_30 = my_button_28.check_click()
        if input_30:
            a2_scene_status = 1

    #-----------------------------------------
            
    if a2_scene_status == 1:
        screen.blit(a2_scene,(0,0))
        if time_2_2_1_status == 1:
            time_2_2_1 = pygame.time.get_ticks()
            time_2_2_1_status = 0
        input_31 = my_button_29.check_click()
        if input_31:
            a2_apples_status = 1

        input_32 = my_button_30.check_click()
        if input_32:
            a2_alligator_status = 1

        input_33 = my_button_31.check_click()
        if input_33:
            a2_axe_status = 1

        input_34 = my_button_32.check_click()
        if input_34:
            a2_ant_status = 1
        
    
    if a2_apples_status == 1:
        screen.blit(a2_apples,(0,0))
        screen.blit(apples_text,(350,150))
        if a2_apples_sound_status == 1:
            apples_sound.play()
            a2_apples_sound_status = 0
    
    if a2_alligator_status == 1:
        screen.blit(a2_alligator,(0,464))
        screen.blit(alligator_text,(50,350))
        if a2_alligator_sound_status == 1:
            alligator_sound.play()
            a2_alligator_sound_status = 0

    if a2_axe_status == 1:
        screen.blit(a2_axe,(380,403))
        screen.blit(axe_text,(450,350))
        if a2_axe_sound_status == 1:
            axe_sound.play()
            a2_axe_sound_status = 0

    if a2_ant_status == 1:
        screen.blit(a2_ant,(897,381))
        screen.blit(ant_text,(850,345))
        if a2_ant_sound_status == 1:
            ant_sound.play()
            a2_ant_sound_status = 0

    
    if a2_apples_status == 1 and a2_axe_status == 1 and a2_ant_status == 1 and a2_alligator_status == 1 and a2_delay_status == 1:
        screen.blit(a2_ant,(897,381))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        a2_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_7,(165,20))
        if time_2_2_status == 1:
            time_2_2 = pygame.time.get_ticks() - time_2_2_1
            time_2_2_status = 0
        if a2_scene_sound_play_status == 1:
            a2_scene_sound_play()
            a2_scene_sound_play_status = 0
        my_button_33 = Button("NEXT",480,550,True,50,90)
        my_button_33.draw()
        input_35 = my_button_33.check_click()
        if input_35:
            a3_scene_status = 1

    if a2_apples_status == 1 and a2_axe_status == 1 and a2_ant_status == 1 and a2_alligator_status == 1 and  a2_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image_7,(165,20))
        show_score(420,280,7)
        if a2_scene_sound_play_status == 1:
            a2_scene_sound_play()
            a2_scene_sound_play_status = 0
        my_button_34 = Button("NEXT",480,550,True,50,90)
        my_button_34.draw()
        input_36 = my_button_34.check_click()
        if input_36:
            a3_scene_status = 1

    
    if a3_scene_status == 1:
        screen.blit(a3_scene,(0,0))
        if time_2_3_1_status == 1:
            time_2_3_1 = pygame.time.get_ticks()
            time_2_3_1_status = 0
        input_37 = my_button_35.check_click()
        if input_37:
            a3_apples_status = 1

        input_38 = my_button_36.check_click()
        if input_38:
            a3_axe_status = 1

        input_39 = my_button_37.check_click()
        if input_39:
            a3_arrow_status = 1
    
    

    if a3_apples_status == 1:
        screen.blit(a1_apples,(0,0))
        screen.blit(apples_text,(300,150))
        if a3_apples_sound_status == 1:
            apples_sound.play()
            a3_apples_sound_status = 0
    
    if a3_arrow_status == 1:
        screen.blit(a3_arrow,(820,462))
        screen.blit(arrow_text,(780,420))
        if a3_arrow_sound_status == 1:
            arrow_sound.play()
            a3_arrow_sound_status = 0

    if a3_axe_status == 1:
        screen.blit(a1_axe,(0,458))
        screen.blit(axe_text,(240,450))
        if a3_axe_sound_status == 1:
            axe_sound.play()
            a3_axe_sound_status = 0
    
    if a3_apples_status == 1 and a3_axe_status == 1 and a3_arrow_status == 1 and a3_delay_status == 1:
        screen.blit(a3_arrow,(820,462))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        a3_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_8,(165,20))
        if time_2_3_status == 1:
            time_2_3 = pygame.time.get_ticks() - time_2_3_1
            time_2_3_status = 0
        if a3_scene_sound_play_status == 1:
            a3_scene_sound_play()
            a3_scene_sound_play_status = 0
        my_button_38 = Button("NEXT",480,550,True,50,90)
        my_button_38.draw()
        input_40 = my_button_38.check_click()
        if input_40:
            a4_scene_status = 1

    if a3_apples_status == 1 and a3_axe_status == 1 and a3_arrow_status == 1 and a3_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image_8,(165,20))
        show_score(420,280,8)
        if a3_scene_sound_play_status == 1:
            a3_scene_sound_play()
            a3_scene_sound_play_status = 0
        my_button_39 = Button("NEXT",480,550,True,50,90)
        my_button_39.draw()
        input_41 = my_button_39.check_click()
        if input_41:
            a4_scene_status = 1

    if a4_scene_status == 1:
        screen.blit(a4_scene,(0,0))
        if time_2_4_1_status == 1:
            time_2_4_1 = pygame.time.get_ticks()
            time_2_4_1_status = 0
        input_42 = my_button_40.check_click()
        if input_42:
            a4_apples_status = 1

        input_43 = my_button_41.check_click()
        if input_43:
            a4_alligator_status = 1

        input_44 = my_button_42.check_click()
        if input_44:
            a4_ant_status = 1

        input_45 = my_button_43.check_click()
        if input_45:
            a4_ambulance_status = 1


    if a4_apples_status == 1:
        screen.blit(a2_apples,(0,0))
        screen.blit(apples_text,(330,150))
        if a4_apples_sound_status == 1:
            apples_sound.play()
            a4_apples_sound_status = 0

    if a4_alligator_status == 1:
        screen.blit(a2_alligator,(0,464))
        screen.blit(alligator_text,(50,350))
        if a4_alligator_sound_status == 1:
            alligator_sound.play()
            a4_alligator_sound_status = 0
    
    if a4_ant_status == 1:
        screen.blit(a2_ant,(897,381))
        screen.blit(ant_text,(850,350))
        if a4_ant_sound_status == 1:
            ant_sound.play()
            a4_ant_sound_status = 0

    if a4_ambulance_status == 1:
        screen.blit(a4_ambulance,(480,537))
        screen.blit(ambulance_text,(480,500))
        if a4_ambulance_sound_status == 1:
            ambulance_sound.play()
            a4_ambulance_sound_status = 0

    if a4_apples_status == 1 and a4_ambulance_status == 1 and a4_ant_status == 1 and a4_alligator_status == 1 and a4_delay_status == 1:
        screen.blit(a4_ambulance,(480,537))
        pygame.display.update()  # Update the screen to show the fourth image
        time.sleep(1.0)
        a4_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image_9,(165,20))
        if time_2_4_status == 1:
            time_2_4 = pygame.time.get_ticks() - time_2_4_1
            time_2_4_status = 0
        if a4_scene_sound_play_status == 1:
            a4_scene_sound_play()
            a4_scene_sound_play_status = 0
        my_button_44 = Button("NEXT",480,550,True,50,90)
        my_button_44.draw()
        input_46 = my_button_44.check_click()
        if input_46:
            t_char_status = 1

    if a4_apples_status == 1 and a4_ambulance_status == 1 and a4_ant_status == 1 and a4_alligator_status == 1 and  a4_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image_9,(165,20))
        show_score(420,280,9)
        if a4_scene_sound_play_status == 1:
            a4_scene_sound_play()
            a4_scene_sound_play_status = 0
        my_button_44 = Button("NEXT",480,550,True,50,90)
        my_button_44.draw()
        input_46 = my_button_44.check_click()
        if input_46:
            t_char_status = 1

    if t_char_status == 1:
        a1scene_status = 2
        a2_scene_status = 2
        a3_scene_status = 2
        a4_scene_status = 2
        screen.fill((255,255,255))
        screen.blit(t_char_image,(120,130))

        if time_3_1_1_status == 1:
            time_3_1_1 = pygame.time.get_ticks()
            time_3_1_1_status = 0

        my_button_45 = Button("NEXT",475,90,True,50,90)
        my_button_45.draw()

        input_47 = my_button_45.check_click()
        if input_47:
            t1_scene_status = 1
    
    if t1_scene_status == 1:
        pass
    
    pygame.draw.rect(screen,(224, 176, 255),(1000,0,200,700))
    my_button_46 = Button2("END GAME",1007,20,True,47,183,False)
    my_button_46.check_hover()
    my_button_46.draw()

    my_button_47 = Button3("S",1057,170,True,93,77,False)
    my_button_47.check_hover()
    my_button_47.draw()

    my_button_48 = Button3("A",1057,370,True,92,77,False)
    my_button_48.check_hover()
    my_button_48.draw()

    my_button_49 = Button3("T",1057,570,True,92,77,False)
    my_button_49.check_hover()
    my_button_49.draw()

    input_60 = my_button_46.check_click()
    if input_60 :
        control = False

    input_61 = my_button_47.check_click()
    if input_61 :
        char_s_image_status = 1

    input_62 = my_button_48.check_click()
    if input_62 :
        char_a_image_status = 1

    input_63 = my_button_49.check_click()
    if input_63 :
        t_char_status = 1

    pygame.display.update()


end_time = pygame.time.get_ticks()
total_game_time = end_time - start_time

with open('analytics.txt','w') as file:
    file.write(str(time_1_1) + " " + str(time_1_2) + " " +str(time_1_3) + " " +str(time_1_4) + 
               " " +str(time_1_5) + " " +str(time_2_1) + " " + str(time_2_2) + " " +str(time_2_3)
               + " " +str(time_2_4) + " " + str(total_game_time))