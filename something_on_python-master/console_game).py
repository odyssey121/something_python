#coding:utf8
def exp():
    import random
    exp=16*'*'
    dic={'сила':'','ловкость':'','выносливость':'','мудрость':''}
    new_exp=''
    while exp:
        
        print('''
Сила    \t-1-''',dic['сила'],'''
Ловкость\t-2-''',dic['ловкость'],'''
Выносливость\t-3-''',dic['выносливость'],'''
Мудрость\t-4-''',dic['мудрость'])
        print(exp[:-1])
        print('\n','<',name,'>')
        try:
            index=int(input('Введите цифру которая соотвецтвует хар-ке:'))
            if index==1:
                rand_poss=random.randrange(len(exp))
                dic['сила']+=exp[rand_poss]
                exp=exp[:rand_poss]+exp[(rand_poss+1):]
            elif index==2:
                rand_poss=random.randrange(len(exp))
                dic['ловкость']+=exp[rand_poss]
                exp=exp[:rand_poss]+exp[(rand_poss+1):]
            elif index==3:
                rand_poss=random.randrange(len(exp))
                dic['выносливость']+=exp[rand_poss]
                exp=exp[:rand_poss]+exp[(rand_poss+1):]
            elif index==4:
                rand_poss=random.randrange(len(exp))
                dic['мудрость']+=exp[rand_poss]
                exp=exp[:rand_poss]+exp[(rand_poss+1):]
        except:
            print('Ошибка ВВода!!!')
            
        
    
























import games
name=None
while not name:
    print('''N_A_M_E''')
    print('П_р_и_в_е_т_с_т_в_у_ю    в_а_с    в_о_и_н   с_в_е_т_а!!!!\n')
    name=input('\n\n\n\t\t\tВведите ваше имя : ')
    response=None
print('\n','<',name,'>')
response=games.ask_yes_no('предстоит распределить ваши характеристики ГОТОВЫ?(y/n)')
if response=='y':
    exp()
else:
    [print('\t\t',number,'\n') for number in range (3,0,-1)]
    print('\n\t\tG_A_M_E  O_V_E_R')
    input('Нажмите enter, чтобы выйти....')

    
                            
    
    
BONUS=('<клок шерсти>','<собачий клык>','<шерсть>')
class Player():
    ЧАСТИ=('рука','грудь','живот','нога','голова')
    
    def __init__(self,name,heal=100,curse=False,place=0,bleeding=False,gold=6):
        self.inventory=[]
        self.name=name
        self.heal=heal
        self.__curse=curse
        self.__place=place
        self.__is_bleed=bleeding
        self.gold=gold
        self.answer=None
        
    def shoot(self):
        import random
        c=random.choice(Player.ЧАСТИ)
        if c=='голова':
            self.heal-=100
            print(self.name,': получил выстрел ==>>',c)
            print('\t\tHead Shoot')
        elif c=='живот' or c=='грудь':
            self.heal-=50
            print(self.name,': получил выстрел ==>>',c)
            
        else:
            self.heal-=30
            print(self.name,':  получил выстрел ==>>',c)
    @property
    def bleeding(self):
        return self.__is_bleed
    @bleeding.setter
    def bleeding(self,new_set):
        if not self.__is_bleed and new_set==True:
            print('\t\t\n<У вас кровоточит рана>')
            self.__is_bleed=new_set
            print('\t\t\n<У вас кровотечение...>')
        elif self.__is_bleed and new_set==False:
            self.__is_bleed=new_set
            print('\t\t\n<Кровотечение прекращено, бинт сделал своё дело...>')
            
        elif self.__is_bleed and new_set==True:
            print('\t\t\n<Вы и так истекаете кровью...>')
            
    @property
    def place(self):
        return self.__place
    @place.setter
    def place(self,new_place):
        if new_place=='':
            print('Внутреняя ошибка <place>')
        else:
            if self.__is_bleed and self.__curse:
                self.__place=new_place
                print('\t\t<Ваша локация изменилась>')
                import random
                a=random.randrange(8)
                self.heal-=a
                b=random.randrange(8)
                self.heal-=b
                print('\t\t\nВы теряете кровь...')
                print('\t\t\n - ',a)
                print('Урон от проклятия\t-',b)
                
            
            elif self.__is_bleed:
                self.__place=new_place
                print('\t\t<Ваша локация изменилась>')
                import random
                a=random.randrange(8)
                self.heal-=a
                print('\t\t\nВы теряете кровь...')
                print('\t\t\n - ',a)
            elif self.__curse:
                self.__place=new_place
                import random
                b=random.randrange(8)
                self.heal-=b
                print('Урон от проклятия')
                print('-',b)
            
                
            else:
                self.__place=new_place
                print('\t\t<Ваша локация изменилась>')
    
        
        
    def win(self):
        [print('\n\t\t',i) for i in range(0,10,-1)]
        print('''
WIN''')
        print('П_О_Б_Е_Д_А!!!')
    def add(self,item):
        self.inventory.append(item)
        print('Вы нашли предмет: ',item)
    @property
    def status(self):
        if self.heal>100:
            self.heal=100
        return self.heal
    @property
    def curse(self):
        return self.__curse
    @curse.setter
    def curse(self,new_curse):
        self.__curse=new_curse
        if self.__curse==True:
            print('\n\t\tНа вас наложено <проклятие темных сил>\n')
        elif self.__curse==False:
            print('\n\t\tВы сняли <проклятие темных сил>\n')
        
        
    def is_hitting(self):
        response=games.ask_yes_no(self.name+':  будете ли вы сражаться или побежите в город?(y/n)')
        return response=='y'
    
    def add_gold(self):
        import random
        gold1=random.randint(4,12)
        self.gold+=gold1
        print('\t\t\nВы нашли:',gold1,'$')
            
    def hit(self):
        import random
        if not self.curse:
            print('Вы получили ранение')
            a=random.randrange(16)
            self.heal-=a
            print('-',a)
        else:
            print('Вы получили ранение')
            a=random.randrange(18)
            self.heal-=a
            print(a)
            a=random.randrange(6)
            self.heal-=a
            print('Урон от проклятия')
            print('-',a)
    def hill(self):
        if not self.curse:
            if self.heal<100:
                self.heal+=20
                print('\n+20 к здоровью')
            else:
                print('Вы уже максимально возможно поправились...')
        else:
            if self.heal<100:
                self.heal+=15
                print('\n+15 к здоровью')
            else:
                print('Вы уже максимально возможно поправились...')
                

    def loot(self):
        
        print('Вас вырубило, что-то повлияло на пространство и время \n вы упали в обморок...')
        self.inventory=[]
        print('Очнулись без единой вещи в инвентаре...')
        
    def die(self):
        return self.heal<=0
    def is_die(self):
        print('Вы метрвы...')
    def attack(self,bot):
        if '<револьвер>' in self.inventory:
            bot.shoot()
        elif '<зажигалка>' in self.inventory:
            bot.hit()
            bot.fire()
        else:
            bot.hit()
        
    def cancel(self):
        print('Вы получили ранение и скрылись')
        self.hit()
        self.heal-=10
        self.place=2
    def __str__(self):
        if not self.curse:
            rep=self.name+':\t'+'<'+str(self.status)+' из 100'+'>\tЗолота на руках: '+str(self.gold)+'$\n'
            if self.inventory:
                rep+='У вас в инвентаре:'
                for item in self.inventory:
                    rep+=str(item)+'  '
            else:
                rep+='У вас в инвентаре:'
                rep+='<пусто>'
        else:
            rep=self.name+':\t'+'<'+str(self.status)+' из 100'+'>\tЗолота на руках: '+str(self.gold)+'$\n'
            
            rep+='<Наложено проклятье>\n'
            if self.inventory:
                rep+='У вас в инвентаре:'
                for item in self.inventory:
                    rep+=str(item)+'  '
            else:
                rep+='У вас в инвентаре:'
                rep+='<пусто>'
        return rep
def heal(player):
    return player.heal

def map(player):
    PLACES=('<Лес>','<Переулок на окрайне города>','<Городской парк>','<Главная улица города>',
            '<улица Истринская>','<улица Ельнинская>','<улица Горбунова>','<Боллерная в парке>',
            '<Личная квартира>','<Полицейский участок>','<Больница>','<Подвал дядюшки сема>',
            '<Набережная>','Странный дом','Городской музей','Школа 732',
            '<бензо заправка>','<Заброшенный завод>')
            
    
    for plac in range(len(PLACES)):
        if player.place==plac:
            return PLACES[plac]

лес=('''\n Что-то живое замоячило перед глазами.... мухи летают....\n
Вы очнулись в тёмном лесу, а в переди видны многочисленые тени опасных существ...\n
болит голова и на правой руке оторван свежий кусок мяса и видна плесень\n
поскорей бы убраться из этого места... по правую сторону виден город!\n''')

городскойпарк=('''\nВ Гродском парке достаточно спокойно и тихо...\n
* для перемещения ==> боллерная в парке\n
# для перемещения ==> улица горбунова\n
# для перемещения ==> главная улица города\n''')
переулокнаокрайнегорода=('''\nМне кажется тут не очень безопасно...\n
# для перемещения ==> городской парк\n
* для перемещения ==> подвал дядюшки сэма\n
* для перемещения ==> странный дом\n
''')
улицаИстринская=('''\n Тут раньше было безопастное место, пока зомби не съели работников полицейского участка...\n
# для перемещения ==> главная улица города\n 
* для перемещения ==> магазин пива\n
* для перемещения ==> полицейский участок\n
# для перемещения ==> улица ельнинская\n
''')
главнаяулицагорода=('''
\n\t\tТут очень много всяких не разговорчивых беженцев...\n
* для перемещения ==> городской музей\n
* для перемещения ==> больница\n
# для перемещения ==> улица истринская\n
* для перемещения ==> странный дом\n
# для перемещения ==> улица ельнинская\n
''')
улицаЕльнинская=('''\n Знаменитая улица, самая приличная из всего города\n
# для перемещения ==> главная улица города\n
* для перемещения ==> квартира друга\n
* для перемещения ==> школа 732\n
# для перемещения ==> улица горбунова\n''')
улицаГорбунова=('''\n Тут иногда в дали мелькают странные тени существ...\n
* для перемещения ==> бензо заправка\n
* для перемещения ==> заброшенный завод\n
# для перемещения ==> переулок на окрайне города\n
* для перемещения ==> церковь\n''')
def answers(player):
    ANSWERS=('\tУ вас нету денег на это...','\tПотраченно 10$\n\tВы купили <бинты>',
         '\tПотрачено 15$\n\tВы купили <зелье здоровья>','\tПотрачено 50$\n\tВы купили <револьвер>',
         '\tПотрачено 25$\n\tВы полностью здоровы!Чувствуете энергию и силу!',
         '\tЗомбия: Я обожаю это делать!\n\tКровопускание прошло успешно...',)
    for num in range(len(ANSWERS)):
             if num==player.answer:
                 return ANSWERS[num]
         
def tite(player):
    TITLES=(лес,переулокнаокрайнегорода,городскойпарк,главнаяулицагорода,улицаИстринская,улицаЕльнинская,
            улицаГорбунова)
    for title in range(len(TITLES)):
        if title==player.place:
            return TITLES[title]

        
def main(name):
    
    print('''NAME''')
    item=Items()
    item.populate()
    
    
    
    print(лес)
    
    
    player=Player(name)
    while player.is_hitting():
        print('\n Схватка началась...')
        bot1=Bot('собака')
        while not bot1.die():
            player.attack(bot1)
            print(bot1)
            bot1.attack(player)
            
            if player.heal<=0:
                player.is_die()
                break
        if player.die():
            for i in range(10,0,-1):
                print('\t\t',i,'\n')
            print('\n\t\t G_A_M_E  O_V_E_R')
            rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
            if rebound=='y':
                main(name)
            else:
                input('Нажмите enter, чтобы выйти...')
                break
        else:
            import random
            bons=random.choice(BONUS)
            player.add(bons)
            player.add_gold()
            print(player)
            
            
    for i in range(10,0,-1):
        print('\t\t',i,'\n')
    player.cancel()
    bot2=Bot('Zombie')#боллерка
    bot3=Bot('Zombie')#музей
    bot33=Bot('Old Zombie')#музей
    bot4=Bot('Zombie')#бензо заправка
    bot5=Bot('Zombie')#зерковь
    bot6=Bot('Zombie')#церковь
    bot7=Bot('Mummya')#переулок
    bot10=Bot('Zombie')#завод
    bot11=Bot('Mummya')#завод
    bot12=Bot('Old Zombie')#завод
    bots=Bot('Бродячая собака')
    prod=Bot('Продавец Пива')
    bot7321=Bot('Mummy')
    bot7322=Bot('Old Mummy')
    bot7323=Bot('Acient Mummy')
    bot55=Bot('Cop Zombie')
    bot555=Bot('Cop Zombie')
    brodbot=Bot('Бродячий зомби')
    
    
    
            
            
            
    player.place=1
    target=None
        
    while not player.die():
        print ('Вы находитесь ==>',(map(player)),tite(player),'\n')
        print ('\n\t\t\tВаше здоровье в процентовке==>',heal(player),'%')
        
        target=input('Введите место: ')
        target=target.lower()
        if player.place==1 and target=='городской парк':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            player.place=2
            print(player)
        elif player.place==1 and target=='подвал дядюшки сэма':
            if '<ключ от подвала>' not in player.inventory:
                print('\nВы не можете открыть подвал дядюшки сэма без ключа...')
            else:
                player.win()
                print('\nВы удачно открыли дверь....\nИ попали в подвал а там....')
        elif player.place==1 and target=='странный дом':
            if not player.curse:
                
                print('\n\t\t<Вы в доме>')
                print('\n\t\tВы зашли в этот <странный дом>, нашли не много золота, и получили==> <Проклятия темных сил>')
                
                
                player.curse=True
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\n\t\t<Вы вышли в переулок>\n')
                print('\n\tВас осквернили темные силы, наложенно==> <Проклятия темных сил>\n')
                import random
                bons=random.choice(BONUS)
                player.add(bons)
                player.add_gold()
            else:
                [print('\n\t\t',i) for i in range(0,4,1)]
                print('\n\t\t<Вы в доме>')
                print('\n\t\tВы зашли в этот <странный дом>, но ничего не обнаружили <пусто>\n')
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\n\t\t<Вы вышли в переулок>\n')
                
                
                    
                    
        elif player.place==2 and target=='главная улица города':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            player.place=3
            print(player)
        elif player.place==3 and target=='улица истринская':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            player.place=4
            bot3=Bot('Zombie')#музей
            bot33=Bot('Old Zombie')#музей
            print(player)
        elif player.place==4 and target=='главная улица города':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            bot55=Bot('Cop Zombie')
            bot555=Bot('Cop Zombie')
            player.place=3
            print(player)
        elif player.place==4 and target=='улица ельнинская':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            bot55=Bot('Cop Zombie')
            bot555=Bot('Cop Zombie')
            player.place=5
            print(player)
        elif player.place==5 and target=='главная улица города':
            bot7321=Bot('Mummy')
            bot7322=Bot('Old Mummy')
            bot7323=Bot('Acient Mummy')
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            player.place=3
            bot3=Bot('Zombie')#музей
            bot33=Bot('Old Zombie')#музей
            print(player)
        elif player.place==5 and target=='улица горбунова':
            bot7321=Bot('Mummy')
            bot7322=Bot('Old Mummy')
            bot7323=Bot('Acient Mummy')
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\n\t\t<Вы на месте>')
            if not brodbot.die():
                print('\n\t\t На вас не спеша идёт зловонный зомби...')
                response=games.ask_yes_no('Зомбак почти рядом с вами, будете сражаться(y/n)')
                if response=='y':
                    while not brodbot.die():
                        player.attack(brodbot)
                        print(brodbot)
                        brodbot.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                        if player.die():
                            [print('\t\t',number,'\n') for number in range (3,0,-1)]
                            print('\n\t\tG_A_M_E  O_V_E_R')
                            rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                            if rebound=='y':
                                main(name)
                            else:
                                input('Нажмите enter, чтобы выйти....')
                                break
                    print('\n\t\tВы раскурочили на мясо этого зомби...')
                    player.add_gold()
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    
                    player.place=6
                    continue
                
                else:
                    player.cancel()
                    [print('\n\t\t',t) for t in range(5,0,-1)]
                    player.place=2
            bot3=Bot('Zombie')#музей
            bot33=Bot('Old Zombie')#музей
            print(player)        
            
            player.place=2
            
        elif player.place==6 and target=='переулок на окрайне города':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            if not bot7.die():
                print('\t\t<Вы на месте>\nЗа помойным ведром виден огромный силуэт какойто мумии...')
                response=games.ask_yes_no('Мумия почти рядом с вами, будете сражаться(y/n)')
                if response=='y':
                    while not bot7.die():
                        player.attack(bot7)
                        print(bot7)
                        bot7.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                        if player.die():
                            [print('\t\t',number,'\n') for number in range (3,0,-1)]
                            print('\n\t\tG_A_M_E  O_V_E_R')
                            rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                            if rebound=='y':
                                main(name)
                            else:
                                input('Нажмите enter, чтобы выйти....')
                                break
                    print('\n\t\tВы раскурочили на мясо этого зомби...')
                    player.bleeding=True
                    player.add_gold()
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    bot7=Bot('Old Mummya')
                    player.place=1
                
                else:
                    player.cancel()
                    [print('\n\t\t',t) for t in range(5,0,-1)]
                    player.place=2
            bot3=Bot('Zombie')#музей
            bot33=Bot('Old Zombie')#музей
            print(player)        
            player.place=1
            
        elif player.place==3 and target=='улица ельнинская':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            player.place=5
            print(player)
        elif player.place==2 and target=='улица горбунова':
            for number in range(10,0,-1):
                print('\t\t',number,'\n')
            print('\t\t<Вы на месте>')
            player.place=6
            print(player)
        elif target=='статус':
            print(player)
        elif player.place==2 and target=='боллерная в парке':
            if bot2.die():
                print('\n\t<Вы ТУТ УЖЕ БЫЛИ БОЛЛЕРКА ПУСТА>\n')
                [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                print('\t\t\nВы вышли <Городской парк>')
                bot2=Bot('Old Zombie')
                continue
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            
            num1=games.ask_yes_no('\n\t\t<Вы В БОЛЛЕРНОЙ>\n\t за трубами стоит Зомбак!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot2.die():
                    player.attack(bot2)
                    print(bot2)
                    bot2.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на мясо этого зомби...')
                print('\n\t\t<Вы вышли в парк>\n')
                player.add_gold()
                import random
                bons=random.choice(BONUS)
                player.add(bons)
            else:
                player.place=2
        elif player.place==3 and target=='городской музей':
            
            if bot3.die():
                print('\n\t<ВЫ ТУТ УЖЕ БЫЛИ - ни чего ценного кроме осколков...>\n')
                [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                continue
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            num1=games.ask_yes_no('\n\t\t<ВЫ В МУЗЕЕ>\n\t все экспанаты разбиты, а за ними стоит Зомбак!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot3.die():
                    player.attack(bot3)
                    print(bot3)
                    bot3.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на мясо этого зомби...')
                print('\n\t\tНа вас бежит еще 1....\n')
                num=games.ask_yes_no('\t\tБудете сражать или убежите?(y/n): ')
                if num=='y':
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    while not bot33.die():
                        player.attack(bot33)
                        print(bot33)
                        bot33.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                    if player.die():
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        print('\n\t\tG_A_M_E  O_V_E_R')
                        rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                        if rebound=='y':
                            main(name)
                        else:
                            input('Нажмите enter, чтобы выйти...')
                            break
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    
                    player.add_gold()
                    player.bleeding=True        
            else:
                [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                print('\n\t\t<Вы вышли на главную улицу>')
                player.cancel()
                player.place=3
                
        elif player.place==6 and target=='бензо заправка':
            if bot4.die():
                print('\n\t<Вы ТУТ УЖЕ БЫЛИ НИ ЧЕГО ЦЕННОГО>\n')
                [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                print('\t\t\nВы вышли <улица Горбунова>')
                bot4=Bot('Old Zombie')
                continue
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            num1=games.ask_yes_no('\n\t\t<Вы ВНУТРИ>\n\t за прилавком Зомбак кушает продовца!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot4.die():
                    player.attack(bot4)
                    print(bot4)
                    bot4.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на мясо этого зомби...')
                print('\t\t\nВы вышли <улица Горбунова>')
                player.place=6
                import random
                bons=random.choice(BONUS)
                player.add(bons)
            else:
                player.cancel()
                player.place=6
        elif player.place==3 and target=='странный дом':
            if not player.curse:
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\nВы зашли в этот <странный дом>, нашли не много <золота> и получили <Проклятие темных сил>')
                print('\t\t\nВы вышли <главная улица города>')
                player.curse=True
                player.add_gold()
                import random
                bons=random.choice(BONUS)
                player.add(bons)
            else:
                print('\nВы обыскали каждый уголок этого гниющего ни кому ни нужного дома\n <пусто>\n')
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\t\t\nВы вышли <главная улица города>')
                
        elif player.place==6 and target=='церковь':
            
            if bot5.die():
                print('\n\t<Вы находитесь в церкви, тут есть алтарь...>\n')
                wreck=games.ask_yes_no('\n\t\tБудете пользоваться алтарём?(y/n)\n')
                if wreck=='y':
                    print('\n\t\tЧто-то щёлкнуло и засветилось над головой...\n\t Вас наполняет энергия антиматерии света!!!')
                    player.curse=False
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('<Вы вышли на улицу Горбунова>')
                    
                    continue
                else:
                    
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('<Вы вышли на улицу Горбунова>')
                    continue
                    
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            num1=games.ask_yes_no('\n\t<Вы ВНУТРИ>\nО боже!Даже это место посмели осквернить Зомбаки!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot5.die():
                    player.attack(bot5)
                    print(bot5)
                    bot5.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на мясо этого зомби...')
                print('\n\t\tНа вас бежит еще 1....\n')
                num=games.ask_yes_no('\t\tБудете сражать или убежите?(y/n): ')
                if num=='y':
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    while not bot6.die():
                        player.attack(bot6)
                        print(bot6)
                        bot6.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                    if player.die():
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        print('\n\t\tG_A_M_E  O_V_E_R')
                        rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                        if rebound=='y':
                            main(name)
                        else:
                            input('Нажмите enter, чтобы выйти...')
                            break
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    player.add_gold()
                    item.deal(player)
                    player.bleeding=True
                    print('\n\t\tВы подошли к алтарю: <Сняли с себя все проклятия>\n')
                    player.curse=False
                    player.place=6
                else:
                    bot5=Bot('Old Zombie')
                    player.cancel()
                    player.place=6
            else:
                [print('\t\t\n',i) for i in range(5,0,-1)]
                print('<Вы вышли на улицу Горбунова>')
        elif player.place==3 and target=='больница':
            number=None
            while number!='выход':
                print('''
\n\t\tДобро пожаловать в городскую больницу!\n
больница в довольно хорошем состоянии, только пуста...\n
есть только в кабинете регистратуры злобная медсестра\n
которая может вам помочь, но не всё так просто...\n
\t\t Здравствуйте меня зовут Зомбирия, смотрите ниже прайс лист...
\t\t\t 1==> купить бинты(10$)
\t\t\t 2==> купить зелье здоровья(15$)
\t\t\t 3==> купить револьвер (50$)
\t\t\t 4==> полное восстановление(25$)
\t\t\t 5==> сделать кровотечение(бесплатно)\n
\t\t\t Введите выход для <выхода>
''')
                print(answers(player))
                print('\n\t\t\t\tВаше золото==>','<',player.gold,'>')
                number=input('Ваши действия: ')
                if number=='1':
                    if player.gold>=10:
                        player.add('<бинты>')
                        player.gold-=10
                        player.answer=1
                    else:
                        player.answer=0
                        
                elif number=='2':
                    if player.gold>=15:
                        player.add('<зелье здоровья>')
                        player.gold-=15
                        player.answer=2
                    else:
                        player.answer=0
                elif number=='3':
                    if player.gold>=50:
                        player.add('<револьвер>')
                        player.gold-=50
                        player.answer=3
                    else:
                        player.answer=0
                elif number=='4':
                    if player.gold>=25:
                        player.gold-=25
                        player.heal=100
                        
                        player.answer=4
                    else:
                        player.answer=0
                elif number=='5':
                    player.bleeding=True
                    player.answer=5
                    
                
            [print('\n\t\t',i) for i in range(5,0,-1)] 
            print('<Вы вышли на главную улицу>\n')
            player.answer=None 
         
        elif target=='бинты':
            if '<бинты>' not in player.inventory:
                print('\t\t\t\nВ инвентаре нету <бинтов>')
            else:
                player.inventory.remove('<бинты>')
                player.bleeding=False
        elif target=='зелье здоровья':
            if '<зелье здоровья>' in player.inventory:
                player.inventory.remove('<зелье здоровья>')
                print('\n')
                player.hill()
            else:
                print('\n\t\tВ инвентаре не имеется <зелье здоровья>')
                
        elif player.place==6 and target=='заброшенный завод':
            
            if bot12.die():
                print('\n\t<Вы находитесь на Заброшенном заводе>\n')
                wreck=games.ask_yes_no('\n\t\tБудете обыскивать каждый уголок?(y/n)\n')
                if wreck=='y':
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('\n\t\tНи чего ценного на заводе...')
                    print('<Вы вышли на улицу Горбунова>')
                    continue
                else:
                    
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('<Вы вышли на улицу Горбунова>')
                    continue
                    
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            num1=games.ask_yes_no('\n\t<Вы ВНУТРИ>\nО боже!Тут около 3 упырей!!!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot10.die():
                    player.attack(bot10)
                    print(bot10)
                    bot10.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на мясо этого зомби...')
                print('\n\t\tНа вас бежит еще 1....\n')
                num=games.ask_yes_no('\t\tБудете сражать или убежите?(y/n): ')
                if num=='y':
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    while not bot11.die():
                        player.attack(bot11)
                        print(bot11)
                        bot11.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                    if player.die():
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        print('\n\t\tG_A_M_E  O_V_E_R')
                        rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                        if rebound=='y':
                            main(name)
                        else:
                            input('Нажмите enter, чтобы выйти...')
                            break
                    player.add_gold()
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    
                    player.bleeding=True
                    print('\n\t\tВы раскурочили этого упыря на мясо...\n')
                    print('\n\t\tНа вас бежит еще 1....\n')
                    num=games.ask_yes_no('\t\tБудете сражать или убежите?(y/n): ')
                    if num=='y':
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        while not bot12.die():
                            player.attack(bot12)
                            print(bot12)
                            bot12.attack(player)
                            if player.heal<=0:
                                player.is_die()
                                break
                            if player.die():
                                [print('\t\t',number,'\n') for number in range (3,0,-1)]
                                print('\n\t\tG_A_M_E  O_V_E_R')
                                rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                                if rebound=='y':
                                    main(name)
                                else:
                                    input('Нажмите enter, чтобы выйти...')
                                    break
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)            
                    player.add_gold()
                    item.deal(player)
                    
                    player.place=6
                else:
                    bot10=Bot('Old Zombie')
                    player.cancel()
                    player.place=6
            else:
                [print('\n\t\t',i) for i in range(5,0,-1)]
                print('<Вы вышли на улицу Горбунова>')
        elif player.place==4 and target=='магазин пива':
            [print('\n\t\t',i) for i in range(3,0,-1)]
            print('<Вы в пивной лавке>\n')
            print('Перед вами продовец <у него револьвер!!!> упырь не хочет продавайть пиво за деньги!!!\n')
            print('Ему нужны ==> <клок шерсти> <собачий клык> <шерсть>')
            num=games.ask_yes_no('\t\tМеняетесь на Кружечку холодного пива?(y/n): ')
            if num=='y':
                if '<клок шерсти>' in player.inventory and '<собачий клык>' in player.inventory and '<шерсть>' in player.inventory:
                    player.inventory.remove('<клок шерсти>')
                    player.inventory.remove('<собачий клык>')
                    player.inventory.remove('<шерсть>')
                    [print('\n\t\t',i) for i in range(3,0,-1)]
                    print('\n\t\tВы вышли на <Улицу Истринская>\n')
                    print('\n\t\tВы получили <пинта пенного>')
                    player.add('<пинта пенного>')
                    continue
                    
                else:
                    print('\n\t\tНедостаточно трофеев вы собрали!!!')
                    num1=games.ask_yes_no('\t\tВыйдете или замочите продавца?!!!<у него револьвер!!!>\n(y/n): ')
                    if num1=='y':
                        while not prod.die():
                            player.attack(prod)
                            print(prod)
                            player.shoot()
                            print('Ваше здоровье==>','<',player.heal,'>')
                            if player.heal<=0:
                                player.is_die()
                                
                            if player.die():
                                [print('\t\t',number,'\n') for number in range (3,0,-1)]
                                print('\n\t\tG_A_M_E  O_V_E_R')
                                rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                                if rebound=='y':
                                    main(name)
                                else:
                                    input('Нажмите enter, чтобы выйти...')
                                    break
                        player.curse=True
                        print('\n\t\tВы раскурочили <пивного продавца>...')
                        print('\n\t\tВы вышли на <Улицу Истринская>\n')
                        player.add_gold()
                        import random
                        bons=random.choice(BONUS)
                        player.add(bons)
                        player.add('<револьвер>')
                        
                        item.deal(player)
                        continue
                    else:
                        [print('\n\t\t',i) for i in range(3,0,-1)]
                        print('\n\t\tВы вышли на <Улицу Истринская>\n')
            else:
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\n\t\tВы вышли на <Улицу Истринская>\n')
        elif target=='выпить пива':
            if '<пинта пенного>' in player.inventory:
                player.inventory.remove('<пинта пенного>')
                player.heal=100
                print('\n\t\tОтличное пиво вам подкрепило здоровье...\n')
                print('\n\t\tХорошее пиво восстановило здоровье на полную!!!\n')
            else:
                print('\t\t\nВ инвентаре нету Пива... :-(\n')
        elif player.place==5 and target=='школа 732':
            if bot7321.die():
                print('\n\t<Вы находитесь в школе 732>\n')
                wreck=games.ask_yes_no('\n\t\tБудете обыскивать каждый уголок?(y/n)\n')
                if wreck=='y':
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('\n\t\tНи чего ценного не обнаруженно...')
                    print('<Вы вышли на улицу Ельнинскую>')
                    continue
                else:
                    
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('<Вы вышли на улицу Ельнинскую>')
                    continue
                    
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            num1=games.ask_yes_no('\n\t<Вы ВНУТРИ>\nО боже!Тут около 3 МУМИЙ!!!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot7321.die():
                    player.attack(bot7321)
                    print(bot7321)
                    bot7321.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на куски эту мумию...')
                print('\n\t\tНа вас бежит еще 1....\n')
                num=games.ask_yes_no('\t\tБудете сражать или убежите?(y/n): ')
                if num=='y':
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    while not bot7322.die():
                        player.attack(bot7322)
                        print(bot7322)
                        bot11.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                    if player.die():
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        print('\n\t\tG_A_M_E  O_V_E_R')
                        rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                        if rebound=='y':
                            main(name)
                        else:
                            input('Нажмите enter, чтобы выйти...')
                            break
                    player.add_gold()
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    
                    player.bleeding=True
                    print('\n\t\tВы раскурочили этого упыря на мясо...\n')
                    print('\n\t\tНа вас бежит еще 1....\n')
                    num=games.ask_yes_no('\t\tБудете сражать или убежите?(y/n): ')
                    if num=='y':
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        while not bot7323.die():
                            player.attack(bot7323)
                            print(bot7323)
                            bot12.attack(player)
                            if player.heal<=0:
                                player.is_die()
                                break
                            if player.die():
                                [print('\t\t',number,'\n') for number in range (3,0,-1)]
                                print('\n\t\tG_A_M_E  O_V_E_R')
                                rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                                if rebound=='y':
                                    main(name)
                                else:
                                    input('Нажмите enter, чтобы выйти...')
                                    break
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)            
                    player.add_gold()
                    item.deal(player)
                    
                    player.place=5
                else:
                    bot7321=Bot('Old Mummy')
                    bot7322=Bot('Old Mummy')
                    
                    player.cancel()
                    player.place=5
            else:
                bot7321=Bot('Mummy')
                bot7322=Bot('Old Mummy')
                bot7323=Bot('Acient Mummy')
                [print('\n\t\t',i) for i in range(5,0,-1)]
                print('<Вы вышли на улицу Ельнинскую>')
    
        elif player.place==4 and target=='полицейский участок':
            if bot555.die():
                print('\n\t<ВЫ ТУТ УЖЕ БЫЛИ - ни чего ценного кроме осколков...>\n')
                [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                continue
                
            
            [print('\t\t',number,'\n') for number in range(5,0,-1)]
            
            num1=games.ask_yes_no('\n\t\t<ВЫ В МУСАРКЕ>\n\t кругом трупы копов..., пару зомбаков едят копов!\n(будете сражаться(y/n))??:\n')
            if num1=='y':
                while not bot55.die():
                    player.attack(bot55)
                    print(bot55)
                    bot55.attack(player)
                    if player.heal<=0:
                        player.is_die()
                        break
                if player.die():
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    print('\n\t\tG_A_M_E  O_V_E_R')
                    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                    if rebound=='y':
                        main(name)
                        
                    else:
                        input('Нажмите enter, чтобы выйти....')
                        break
                print('\n\t\tВы раскурочили на мясо этого зомби...')
                
                print('\n\t\tНа вас бежит еще 1....\n')
                num=games.ask_yes_no('\t\tБудете сражаться или убежите?(y/n): ')
                if num=='y':
                    [print('\t\t',number,'\n') for number in range (3,0,-1)]
                    while not bot555.die():
                        player.attack(bot555)
                        print(bot555)
                        bot555.attack(player)
                        if player.heal<=0:
                            player.is_die()
                            break
                    if player.die():
                        [print('\t\t',number,'\n') for number in range (3,0,-1)]
                        print('\n\t\tG_A_M_E  O_V_E_R')
                        rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
                        if rebound=='y':
                            main(name)
                        else:
                            input('Нажмите enter, чтобы выйти...')
                            break
                    import random
                    bons=random.choice(BONUS)
                    player.add(bons)
                    item.deal(player)
                    player.add_gold()
                    player.bleeding=True
                else:
                    [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                    print('\n\t\t<Вы вышли на улицу Истринская>')
                    bot55=Bot('Cop Zombie')
                    player.cancel()
                    player.place=4
                    
            else:
                [print('\n\t\t',number,'\n') for number in range(3,0,-1)]
                print('\n\t\t<Вы вышли на улицу Истринская>')
                bot55=Bot('Cop Zombie')
                player.cancel()
                player.place=4
            
        elif player.place==5 and target=='квартира друга':
            if '<ключи от квартиры>' not in player.inventory:
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\n\t\t<Вы на пороге квартиры>')
                print('\n\t\t<Но у вас нету ключей....>')
                [print('\n\t\t',i) for i in range(0,3)]
                print('\n\t\t<Вы вышли на улицу Ельнинская>')
            else:
                
                [print('\n\t\t',i) for i in range(3,0,-1)]
                print('\n\t\t<Вы на пороге квартиры>')
                print('\n\t\tВы в квартире ни чего ценного кроме <пинта пенного>')
                player.add('<пинта пенного>')
                [print('\n\t\t',i) for i in range(0,3)]
                print('\n\t\t<Вы вышли на улицу Ельнинская>')
        
        else:
            print('\n\t\t\tН_Е_В_Е_Р_Н_Ы_Й    В_В_О_Д !!!')
                
            
    [print('\t\t',number,'\n') for number in range (3,0,-1)]
    print('\n\t\tG_A_M_E  O_V_E_R')
    rebound=games.ask_yes_no('Желаете начать заново?(y/n)')
    if rebound=='y':
        main(name)
                        
    else:
        input('Нажмите enter, чтобы выйти....')                        
                            
                    

                   
                
            
            

    
                        

                        



      


      
                
            
            
    
    
    
    
    

        
    

            




class Bot():
    ЧАСТИ=('рука','грудь','живот','нога','голова')
    
    def __init__(self,name,heal=100):
        self.name=name
        self.heal=heal
    def attack(self,player):
        player.hit()
    def hit(self):
        import random
        a=random.randrange(15,30)
        self.heal-=a
        print(self.name,':  получил урон ==>>',a)
    def fire(self):
        import random
        b=random.randrange(2,8)
        self.heal-=b
        print('Урон от огня: ','<',b,'>')
    def shoot(self):
        import random
        c=random.choice(Bot.ЧАСТИ)
        if c=='голова':
            self.heal-=100
            print(self.name,': получил выстрел ==>>',c)
            print('\t\tHead Shoot')
        elif c=='живот' or c=='грудь':
            self.heal-=50
            print(self.name,': получил выстрел ==>>',c)
            
        else:
            self.heal-=30
            print(self.name,':  получил выстрел ==>>',c)
            
    @property
    def status(self):
        if 70>self.heal>=30:
            p='ранен'
        elif 30>self.heal>=1:
            p='сильно ранен'
        elif self.heal<=0:
            p='мёртв'
        else:
            p='здоров'
        return p
                
    def die(self):
        return self.heal<=0
    def is_die(self):
        print(self.name,': мертв...')
    def __str__(self):
        rep=self.name+':\t'+self.status
        return rep

class Items():
    ITEM=('<обычная дубина>','<бейсбольная бита>','<зажигалка>','<револьвер>','<ключи от квартиры>','<ключ от подвала>')
    def __init__(self):
        self.items=[]
    def populate(self):
        for item in Items.ITEM:
            self.items.append(item)
    def deal(self,player):
        if self.items:
            top_item=self.items[0]
            player.add(top_item)
            self.items.remove(top_item)
    def __str__(self):
        if self.items:
            rep='Итемы:'
            for item in self.items:
                rep+=str(item)
                
            rep=str(self.items)
        else:
            rep='<пусто>'
        return rep




        
          
    

print('\n','<',name,'>')
print('''Ваше задание в городе==> <Попасть в подвал дядюшки сэма> <==там спрятан могущественный Артефакт!!!''')
response=games.ask_yes_no('\n\t\tВы готовы погрузиться во тьму?(y/n)')
if response=='y':
    main(name)
else:
    [print('\t\t',number,'\n') for number in range (3,0,-1)]
    print('\n\t\tG_A_M_E  O_V_E_R')
    input('Нажмите enter, чтобы выйти....')


    

    
    
        

            
    
            
        
    
    
    
    
    
    
    
   
    
        
