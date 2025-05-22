import pygame
import random
import mind

def choise_next_step():
    all_loc=[(0,0), (0,x2) , (0,x3), (x2,0), (x2,x2), (x2,x3), (x3,0), (x3,x2), (x3,x3)]
    por_loc= list_game_dire + list_game_zarb
    empty_loc= list(filter(lambda x:x not in por_loc,all_loc))

    if list_loc_mouse == []:
        next_step=(x2,x2)

    else:
        defend=mind.attack_or_defend(list_game_dire,empty_loc)
        attack=mind.attack_or_defend(list_game_zarb,empty_loc)
        first_step=mind.first_step(empty_loc)      
        if attack == None:
            if defend== None:
                next_step= first_step
                # print(first_step,'first_step')
                # print('empty',empty_loc)
            else:
                next_step=defend
                # print(defend,'defend')
        else:
            next_step=attack
            # print(attack,'attack')

    return next_step
        
def next_zarb():
    all_loc=[(0,0), (0,x2) , (0,x3), (x2,0), (x2,x2), (x2,x3), (x3,0), (x3,x2), (x3,x3)]
    por_loc= list_game_dire + list_game_zarb
    empty_loc= list(filter(lambda x:x not in por_loc,all_loc))
    
    if empty_loc != []:
        next_rand= random.choice(empty_loc)
        return next_rand

def chek_win(list_game):
    if (0,0) in list_game:
        if  (x2,x2) in list_game and (x3,x3) in list_game:
            return True
        elif (0,x2) in list_game  and (0,x3) in list_game:
            return True
        elif (x2,0) in list_game  and (x3,0) in list_game:
            return True
        
    if (x2,x3) in list_game:
        if (x2,x2) in list_game  and (x2,0) in list_game:
            return True 
        elif (0,x3) in list_game  and (x3,x3) in list_game:
            return True

    if (x3,x2) in list_game:
        if (x2,x2) in list_game  and (0,x2) in list_game:
            return True
        elif (x3,0) in list_game  and (x3,x3) in list_game:
            return True
        
    if (0,x3) in list_game  and (x2,x2) in list_game  and (x3,0) in list_game:
        return True
    
def game():
    global result_text
    global tol
    all_loc=[(0,0), (0,x2) , (0,x3), (x2,0), (x2,x2), (x2,x3), (x3,0), (x3,x2), (x3,x3)]
    por_loc= list_game_dire + list_game_zarb
    empty_loc= list(filter(lambda x:x not in por_loc,all_loc))
    dire_win=chek_win(list_game_dire)
    result=None
    if dire_win:
        # print('you win !')
        result=('you win !')
        tol = 75
    elif chek_win(list_game_zarb):
        # print('you lose !')
        result=('you lose!')
        sound_lose.play()
        tol = 75
        
    elif empty_loc== []:
        # print( 'equar')
        result=( 'equar')
        tol = 130

    if result!= None:
        result_text= result
        # print(result_text)
        sound_lose.play()

        # font=pygame.font.SysFont(None,50)
        # text=font.render(result, True, (0,0,0))
        # window.blit(text, (150,150))
        # print(1)
        # pygame.quit()
  
def trans_loc(location):
    if location < x2:
        location= 0            
    elif x2<location< x3:
        location = x2               
    elif location> x3:
        location= x3

    return location


# تعریف بازی و ساختن محیط اصلی
pygame.init()
pygame.mixer.init()
window= pygame.display.set_mode((400, 400))
pygame.display.set_caption('my game')
# font=pygame.font.SysFont(None,50)
# text=font.render('hello', True, (0,0,0)



#متغیر های تعریف شده عمومی برای خلاصه
x2= 400/3                                            
x3= (400/3)*2 +8
image_zarb=pygame.image.load('images/new.jpg')
image_dire= pygame.image.load('images/dire.webp')
background= pygame.image.load('images/dooz-game.png')
sound_lose= pygame.mixer.Sound('images/lose.mp3')
time_game=0
active_dealy=False
can_clik=True
result_text=None
end_game=None

# لیست های زخیره کننده
list_game_zarb=[]        #location هایی که ضربدر است
list_game_dire=[]        #location هایی که دایره است
list_loc_mouse = []      #برای قرار دادن دایره در جایگاه موس




#ترجمه رندوم و تبدیل به مختصات
dict_mokhtast= {
    '1' :(0,0),
    '2' : (x2,0),
    '3' :(x3,0),
    '4' :(0,x2),
    '5' :(x2,x2),
    '6' :(x3,x2),
    '7' :(0,x3),
    '8' :(x2,x3),
    '9' :(x3,x3),
}

running= True
while running == True:

    window.blit(background, (0,0))
    
    

    for ivent in pygame.event.get():
        if ivent.type == pygame.QUIT:
            running = False

        if ivent.type == pygame.MOUSEBUTTONDOWN and end_game != True:

            get_pos_mouse=list(pygame.mouse.get_pos())
            get_pos_mouse2=tuple(map(trans_loc, get_pos_mouse))

            if can_clik and get_pos_mouse2 not in list_game_dire :
                list_game_dire.append(get_pos_mouse2)
                list_loc_mouse.append(get_pos_mouse2)
                can_clik=False
                can_game=True
            else:
                #برسی میکنه که ایا جای قبلی کلیک کردی رو دایره یا نه
                can_game= False

            if get_pos_mouse2 not in list_game_zarb :
                save_next_zarb=choise_next_step()
                active_dealy=True
                time_game2=pygame.time.get_ticks()
       
    for loc_mouse in list_loc_mouse:
            window.blit(image_dire, loc_mouse)

    if list_game_zarb is not None:
            for loc_zarb in list_game_zarb:
                if loc_zarb != None:
                    window.blit(image_zarb, loc_zarb)

    if active_dealy:
        time_game_now=pygame.time.get_ticks()
        if time_game_now - time_game2 > 1000  :
            if save_next_zarb !=None:
                list_game_zarb.append(save_next_zarb)
            can_clik=True                                                           #چک میکنه که ضرب گذاشته شده یا نه
            active_dealy= False
            save_next_zarb= None
            
            #اگه رو دایره نزده باشی برسی میکنه که برنده شدی یا نه
            if can_game:
                game() 
                # if end :
                #     
                #     print(1)
                #     # pygame.quit()
                #     # pygame.display.update()

    if result_text:
        # tol=None
        font=pygame.font.SysFont(None,80)
        text=font.render(result_text, True, (255,0,0))
        window.blit(text, (tol,170))
        # print(1)
        end_game=True



                                                              
    pygame.display.update()

pygame.quit()
    



