import pygame
from pygame import mixer
import time
import pygame.font
import speech_recognition as sr

#Initialization
pygame.init()

#Screen creation
screen = pygame.display.set_mode((1000,700))

'''Background sound'''
mixer.music.load("smile.mp3")
mixer.music.play(-1)

#landing page image
land_image = pygame.image.load("land_image.jpg")

#page_2
char_s_image = pygame.image.load("Premium-Vector-Happy-cute-little-kid-study-alphabet-character.png")
char_s_image_status = 0

#page_3
char_s_scene = pygame.image.load("first_image.jpg")
char_s_scene_status = 0

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

#winner image load
winner_image = pygame.image.load("46141 (1).jpg")

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

# branches = font_new.render("Count the number of branches in the tree",True,(240,0,100))

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

control = True #status of the main while loop
while control: #main running loop of the game screen
    
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
    
    screen.blit(land_image,(0,0))
    screen.blit(sakshar_image,(270,5))

    my_button_1 = Button("LET US PLAY",430,590,True,50,190)
    my_button_1.draw()
    input_1 = my_button_1.check_click()
    if input_1:
        char_s_image_status = 1

    my_button_2 = Button("---->>>",470,90,True,50,90)
    
    if char_s_image_status == 1:
        screen.fill((255,255,255))
        screen.blit(char_s_image,(180,170))
        my_button_2.draw()
        input_2 = my_button_2.check_click()
        if input_2:
            char_s_scene_status = 1
    
    if char_s_scene_status == 1:
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
        time.sleep(1.5)
        delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        if sound_play_status == 1:
            sound_play()
            sound_play_status = 0
        my_button_9 = Button("NEXT",475,590,True,50,90)
        my_button_9.draw()
        input_7 = my_button_9.check_click()
        if input_7:
            second_char_status = 1

    if sun_image_status == 1 and snake_image_status == 1 and swing_image_status == 1 and stone_image_status == 1 and delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        show_score(420,80,20)
        if sound_play_status == 1:
            sound_play()
            sound_play_status = 0
        my_button_9 = Button("NEXT",475,590,True,50,90)
        my_button_9.draw()
        input_7 = my_button_9.check_click()
        if input_7:
            night_scene_image_status = 1

    #-------------------------Day Scene ----->>>>  Night Scene----------------------------
        
    if night_scene_image_status == 1:
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
        time.sleep(1.5)
        night_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        if night_scene_sound_play_status == 1:
            night_scene_sound_play()
            night_scene_sound_play_status = 0
        my_button_10 = Button("NEXT",475,590,True,50,90)
        my_button_10.draw()
        input_12 = my_button_10.check_click()
        if input_12:
            forest_scene_status = 1

    if stone_image_status == 2 and swing_image_status == 2 and spider_image_status == 2 and stars_image_status == 2 and night_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        show_score(420,80,40)
        if night_scene_sound_play_status == 1:
            night_scene_sound_play()
            night_scene_sound_play_status = 0
        my_button_10 = Button("NEXT",475,590,True,50,90)
        my_button_10.draw()
        input_12 = my_button_10.check_click()
        if input_12:
            forest_scene_status = 1

    #---------------------Night Scene ----->>>  Forest Scene------------------------------------
    
    if forest_scene_status == 1:
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
        time.sleep(1.5)
        forest_delay_status = 2
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        if forest_scene_sound_play_status == 1:
            forest_scene_sound_play()
            forest_scene_sound_play_status = 0
        my_button_15 = Button("NEXT",475,590,True,50,90)
        my_button_15.draw()
        input_17 = my_button_15.check_click()
        if input_17:
            branch_scene_status = 1

    if stone_image_status == 3 and spider_image_status == 3 and snake_image_status == 3 and sun_image_status == 3 and forest_delay_status == 2:
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        show_score(420,80,60)
        if forest_scene_sound_play_status == 1:
            forest_scene_sound_play()
            forest_scene_sound_play_status = 0
        my_button_15 = Button("NEXT",475,590,True,50,90)
        my_button_15.draw()
        input_17 = my_button_15.check_click()
        if input_17:
            branch_scene_status = 1

    if branch_scene_status == 1:
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
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        show_score(420,80,80)
        if branch_scene_sound_status == 1:
                branch_scene_sound_play()
                branch_scene_sound_status = 0 #inactive
        my_button_20 = Button("NEXT",475,590,True,50,90)
        my_button_20.draw()
        input_22 = my_button_20.check_click()
        if input_22:
            stars_scene_status = 1

    #---------------------Branches scene >>>>>>> Stars scene----------------
    if stars_scene_status == 1:
        screen.blit(stars_scene,(0,0))
        my_button_21 = Button("SPEAK",475,490,True,50,110)
        my_button_21.draw()
        if stars_scene_sound_status == 1:
            stars_scene_sound.play()
            stars_scene_sound_status = 0
        input_23 = my_button_21.check_click()
        if input_23:
            speech_detection_status = 1
            six_image_status = 1

    
    # if speech_detection_status == 1:
    #     output = get_speech_input()
    #     if output == "there are six stars":
    #         six_image_status = 1
    #         speech_detection_status = 2
    #     else:
    #         try_sound.play()

    if six_image_status == 1:
        screen.fill((255,255,255))
        screen.blit(six_image,(250,150))
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
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        show_score(420,80,100)
        my_button_23 = Button("NEXT",455,590,True,50,90)
        my_button_23.draw()
        if post_audio_scene_sound_status:
            post_audio_scene_sound_play()
            post_audio_scene_sound_status = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control = False #ensuring that the screen ends only when the quit event is pressed

    pygame.display.update()

