﻿

init:
<<<<<<< HEAD
    # Картинки
    image 47 = "images/47.jpg"
    image 41 = "images/41.jpg"
    image pris = "images/prison.jpg"
=======
    # Бэки
    image prison = "images/prison.jpg"
>>>>>>> origin/master
    image shur = "images/shur.jpg"
    image bobik = "images/bobik.png"
    image bg II home cabinet = "images/2fl_207_class.png"
    image bg II home enter = "images/2fl_207_enter.png"
    image bg II hall = "images/2fl_hall.png"
    image bg II corridor = "images/2fl_corridor.png"
    image bg III stairs = "images/3fl_stairs.png"
    image bg IV corridor = "images/4fl_corridor.png"
    image bg IV sofa = "images/4fl_sofa.png"
    image bg IV toilet = "images/4fl_toilet.png"

    # Персонажи
    image gark norm = "images/gark_norm.png"
    image gark sleep = "images/gark_sleep.png"

    image pash_norm = "images/pash_norm.png"
    image pash_angry = "images/pash_angry.png"
    image pash_mystery = "images/pash_mystery.png"
    image meln = "images/meln.png"
    image turi = "images/turi.png"

    
    #Указывай первые четыре буквы фамилий, чтобы потом легче было писать.
    $ g = Character(u'Артуриан') #Главный персонаж
    
    #Мужские персонажи
    $ gark = Character(u'Илюша')
    $ gatc = Character(u'Дениска')
    $ malk = Character(u'Сереженька')
    $ baku  = Character(u'Артём')
    $ otra = Character(u'Слава')
    $ simo  = Character(u'Никита')
    $ pash = Character(u'Лео')
    $ kaza = Character(u'Даниил')
    $ turi = Character(u'Женя')
    $ meln = Character(u'Дима')
    $ kash = Character(u'Кашин')
    $ tomi = Character(u'Томилов')
    #Пловцы и прочие личности
    $ melk  = Character(u'Никита')
    $ epif = Character(u'Эдик')
    $ alex = Character(u'Вася')
    $ scrt = Character(u'Таинственный голос')
    $ miha = Character(u'Миша')
    
    #Женские персонажи
    $ novo = Character(u'Настенька')
    $ osip = Character(u'Ася')
    $ hazi = Character(u'Оля')
    $ grom = Character(u'Юля')
    $ teli = Character(u'Алина')
    $ gorb = Character(u'Аня')
    $ afan = Character(u'Анна')
    $ kudr = Character(u'Алина')
    $ boyc = Character(u'Настя')
    $ miro = Character(u'Геля')
    $ turt = Character(u'Анна')
    $ dev = Character(u'Девушка') # Абстракная девушка


label start:
    #Пусть здесь будут переменные
    #Префикс "need" пусть значит необходимость предмета, например в данном случае: Герой стоит на крыльце и у него обветриваются губы - ему нужен крем - появляется еще один альтернативный вариант для знакомства
    $ need_cream = False #Нужен ли гг крем для кожи
    $ brutality = 0 # Супер-переменная, увеличивается при любом храбром поступке гг, открывает доступ к секретной концовке
    scene black
    # play music "sounds/AY-ToP.mp3"
    $ renpy.pause(1.5)
    # $ surname = renpy.input("Какая у тебя фамилия?")
    # $ surname = surname.strip()
    $ surname = u'Бог'

    "Он, я, они... Мы все прокляты. Только формула проклятия у каждого своя, моим является одиночество."
    "Ни в одном обществе мне нет места. В каждой компании я третий лишний."
    "Еще в детском саду другие дети показывали на меня пальцем, называли меня чуркой. \nРезала по ушам фраза \"Черножопый Арсен\"."
    "А ведь я даже не Арсен. Но они не понимали этого, ибо были твердолобыми аутистами, способными лишь обзываться и бить меня моими же игрушками."
    "И по сей день я одинокий воин. Только я стал настолько одинок, что у меня не было даже недоброжелателей..."
    "...,но был любимый человек!"
    "Моя скромная персона до самого конца верила в искреннюю любовь. Благодаря ей."
    #счастливые кадры с Серёгой
    "Но счастье не могло длиться вечно."
    "Она оставила меня, вероломно предала. Краски жизни потускнели в очах моих, а сердце моё вмиг почернело..."
    #показывается сцена с изменой в столовке
    "Всё рухнуло внутри меня, я отчаялся. Но мне резко вспомнились слова моего деда Мансурчика:"
    "\"Жи есть жи, пацаны, я б ее внуков прямо у нее на спине {b}вылюбил{/b}, но культурный молодой человек себе такого позволить не может, иншаллах.\""
    "Я резко понял, что она теперь лишь часть моего прошлого. Моё сердце освободилось, и я ушёл."
    "Так и начались мои великие скитания в поисках {i}КАЧЕСТВЕННОЙ{/i} женщины."
    
    #Нужен фон ночной комнаты
    "Что-то разбудило меня посреди ночи."
    "~Мне нужна женщина. Молодая и сочная. Школьница.~"

    show shur #Мелькают Шурыгина, ментовский бобик, тюремная камера
    $ renpy.pause(0.5)
    show bobik
<<<<<<< HEAD
    $ renpy.pause(1.0)
    show pris
    #Мелькают Шурыгина, ментовский бобик, тюремная камера
    "~Но ведь 8 лет. Хм.. Тогда нужно найти школьницу из Гимназии, в таких девочках наверняка минимум меркантильности.~"
    show 41 with vpunch
    play sound "sounds/error.mp3"
=======
    $ renpy.pause(0.5)
    show prison
    $ renpy.pause(0.5)
    hide bobik
    hide shur
    hide prison
    
    "~Но ведь 8 лет. Хм.. Тогда нужно найти школьницу из Гимназии, в них наверняка минимум меркантильности.~"
    #Появляется фотография 41 гимназии, звук ошибки, сотрясение экрана 
>>>>>>> origin/master
    "~А, ну да, я явно что-то перепутал.~"
    scene bg 47 with dissolve
    window show dissolve
    "~Да, самые приличные, секасные и душевные самочки обитают именно в этом вольере…~"
    "~Но в каком же классе самые нежные девушки Гимназии?~"
    #не забыть описать Мишу и таинственный голос как персонажей
    scrt "А вот тут тебе не помешает моя помощь, друг"
    g "Кто здесь?! Шайтан?! Мой голова, тебе сюда нельзя! Аллах - судья твоим деяниям."
    scrt "Я вижу, что твои помыслы чисты, и я думаю, что обязан помочь тебе. Всё просто: тебе подходит лишь одна параллель - 11 классы."
    scrt "В 11 'В' не лезь, это моя территория. В 'Б' классе нет никого, подходящего тебе. То, что ты ищешь, есть в 11 'А'. {w} Но, сперва тебе нужно убрать этот язвительный акцент, иначе ты всех девушек распугаешь."
    g "Как пожелаешь. Но как мне сойтись с этими девушками?"
    scrt "Тебе понадобится помощь трёх наставников из 11 'А' : Лёни, Илюши и Даниила."
    g "Где мне их найти?"
    scrt "Связь плохая, ничего не слышу, пока!"
    "~Пфф, сам разберусь.~"
    "~Завтра обязательно схожу в эту Гимназию~"
    "Веки резко потяжелели, я уснул."
    
    #scene enter
    
    "И вот я вхожу в заветную обитель прекрасных нимф. Но откуда здесь турникет?!"
    "Первой красавицей на моём пути оказалась вахтёрша, женщина в возрасте, но всё еще молодая и с искоркой."
    "~Что же мне делать?~"
    
    #надо фон с вахтершой
    
    menu:
        "Упасть на колени и начать умолять вахтершу, чтобы она впустила меня":
            $ brutality -= 1
            "Вахтерша настолько поглощена чтением Донцовой, что не замечает моей речи с южным акцентом"
            g "Что мне делать теперь?"
            menu:
                "Проползти под турникетом":
                    "Я незаметно пролез под турникетом и полетел по лестнице,ведущей на второй этаж, как-будто украл арбуз с рынка"
                    $ brutality += 1
                "Ждать на улице, пока кто-нибудь будет заходить":
                    "Я стоял на улице 15 минут и моя нежная  кожа уже начала шелушиться"
                    "Мне потребуется крем, чтобы я смог хоть кого-нибудь закадрить"
                    $ need_cream = True
                    "Но мне повезло: в школу заходит отряд первоклассников"
                    "Я сел на корты и пошел вместе с ними"
                    "Я незаметно пролез под турникетом и полетел по лестнице,ведущей на второй этаж, как-будто украл арбуз с рынка"
        "Проползти под турникетом":
                "Я незаметно пролез под турникетом и полетел по лестнице,ведущей на второй этаж, как-будто украл арбуз с рынка"
                $ brutality += 2
        "Ждать на улице, пока кто-нибудь будет заходить":
                "Я стоял на улице 15 минут и моя нежная  кожа уже начала шелушиться"
                "Мне потребуется крем, чтобы я смог хоть кого-нибудь закадрить"
                $ need_cream = True
                "Но мне повезло: в школу заходит отряд первоклассников"
                "Я сел на корты и пошел вместе с ними"
                "Я незаметно пролез под турникетом и полетел по лестнице,ведущей на второй этаж, как-будто украл арбуз с рынка"
    #Герой проник в школу
    #scene bg возле актового зала
    "Чтобы как следует подготовиться к 8 марта, мне нужна помощь мудрых наставников: сенсеев из 11 А."
    "Одного из них, кажется, зовут Леонид."
    "Легенды гласят, что он великий мастер шуток юмора, поможет мне правильно ворваться в женский коллектив."
    "Не зная как его найти, я пошел по коридору второго этажа."
<<<<<<< HEAD
    #scene bg корридор второго этажа
    "Вдруг, дверь какого-то кабинета распахнулась и из него стали с всхлипами выпадать люди."
    "~Они... смеются?~"
    "~Кажется, я нашел того, кого мне надо!~"
    "~Номер кабинета - 207.~"
    #scene bg 207 кабинет
=======
    menu:
        "Зайти в кабинет, из которого доносится ржач":
            pass
        "Сходить до мужского туалета":
            jump semaslava_branch
        "Зайти в актовый зал":
            $ brutality += 1
            # Снять видос какой-нибудь танца
            g "ААААА!!!"
            "Я с криками выбежал из этого блаженного места, из глаз текла кровь, заливая бровь"
            "Стоит вернуться к тому странному кабинету."
label pash:
    "Вдруг, дверь кабинета распахнулась передо мной, и из него стали с всхлипами выпадать люди."
    "~Они... смеются?~"
    "~Кажется, я нашел того, кого мне надо!~"
    scene bg II home enter
    show pash_norm at center with dissolve
>>>>>>> origin/master
    g "Ты и есть легендарный Леонид: бог юмора и задорных представлений?"
    pash "Да, это я."
    g "Меня зовут Артуриан, и я хотел бы поближе познакомиться с девчонками из твоего класса."
    g "Но для «познакомиться поближе» нужно хотя бы просто познакомиться."
    pash "А достоин ли ты их?"
    hide pash_norm
    show pash_angry at center
    pash "Тебе придется пройти испытания {b}ЮМОРОМ{/b}!"
    hide pash_angry
    show pash_norm at center
    pash "Я расскажу тебе анекдот..."
    pash "Продолжи его."
    pash "Мама собирает сына в поход:"
    pash "Мама говорит: вот положила тебе масло, хлеб и килограмм гвоздей."
    pash "Сын спрашивает: Но зачем?"
    pash "Мама отвечает: Понятно зачем! Масло на хлеб намажь и поешь!"
    pash "Сын вопрошает: А гвозди?"
    pash "Что ответила мама?"
    hide pash_norm
    show pash_mystery at center
    menu:
        "Съешь их на полдник..?":
            pash "..."
            pash "Чувство юмора у тебя хромает"
            pash "Так и быть, помогу тебе за твою раскосую бровь."
        "Ну вот же они, положила!":
            $ brutality += 1
            pash "АХАХАХАХАХА"
            pash "Ух, подлец!"
            pash "Такому шутнику и помочь не грех!"
        "*Ответить танцем*":
            $ brutality += 2
            #Песенка маленьких утят 
            pash "Глубокий танец, глубокий..."
            pash "Я к твоим услугам!"
    "*Входит девушка*"
    hide pash_mystery
    show pash_norm at right
    pash "*шепчет*: А вот и твоя первая жертва."
    pash "Попрактикуйся."

    g "Девушка, я недавно болтал с Аллахом, он поведал мне по секрету, что весь его гарем, глядя на вас, плачет от собственной неполноценности."
    g "Я просто обязан с вами познакомиться!"
    dev "Ну что ж , знакомься."
    # Видосик с девушкой
    dev "Очень приятно, а я Вероника. Твоё экстравагантное представление сбило меня с толку."
    u"Вероника" "Я забыла, зачем сюда пришла. Вернусь обратно, возможно, всё вспомню."
    "Не успел я нахмурить бровь, как она ушла. Ушла... Любви не понимая..."
    "Теперь я обязан найти следующего сенсея..."
    "У него много имён..."
    "Настоящий мужчина, летописец, спящий сыч..."
    "Но его настоящее имя - Илья."
    "Он покажет мне, как должен себя вести {b}НАСТОЯЩИЙ МУЖЧИНА{/b}."
    g "Леопольд-сенсей, подскажите мне, где же найти Илью Игоревича, признанного образцом маскулинности?"
    show pash_norm
    pash "Выйди из предбанника, найдешь тело на скамейке."
    hide pash_norm
label gark:
    "Зашел я в сам кабинет.."
    scene bg II home cabinet
    "Меня встретила спящая красавица. Вернее, спящее чудовище."
    show gark sleep at left
    with dissolve
    g "Привет, ты, кажется, Илья?"
    g "Я бы хотел подкатить к мамзелям из вашего класса, чтобы ровно и по-масти."
    g "Что посоветуешь?"
    g "Меня, кстати, Артуром зовут."
    gark "*Не отвечает*"
    menu:
        "Потыкать указкой":
            "*Илья нехотя просыпается*"
        "Пошутить про Илюшину мамку":
            $ brutality += 1
            "*Илья с яростью продирает свои глаза*"
        "Ласково погладить Илью по головушке, поцеловать в щечку":
            $ brutality += 2
            "*На щеках Ильи появляется румянец. Он постепенно просыпается*"
    hide gark sleep
    show gark norm at left
    g "Кхм-кхм, меня Артуром зовут..."
    gark "Здарова, приятно познакомиться, Ашот. Чё надо?"
    g "Да вот, хочу я познакомиться с девоньками из твоего класса.."
    gark "Ну знакомься, будить-то меня зачем? Мне как раз снилось, как я сплю.."
    g "Требуется твоя помощь, сонный ты мой комочек тестостерона. Как мне покорить их сердца?"
    gark "Ну смотри, тебе надо заниматься силовыми упражнениями."
    gark "Стать крепче, тогда настоящие женщины почувствуют твой дух мужчины."
    "Я уже минуты 3 чувствовал 'дух мужчины', испускаемый Илюшенькой."
    g "Сейчас же приступлю к работе над собой. Кстати, меня Артур зовут, а не Ашот!"
    gark "Ну, я так и сказал: Вазген. Не мешай спать."
    hide gark norm
    show gark sleep at left
    "Я поставил рядом с ним новенький 'Олд Спайс'."
    "Забрал обратно, ибо столько мужественности в одном теле не уместится, а двух Илюш школа не потянет."
    g "Ну, хрен с тобой, золотая рыбка, за работу!"
    hide gark sleep
    "~Стоя у выхода в школу, я слышал откуда-то справа свистки и нервные крики какой-то истерички, практикующей йогу.{w} Наверное, там спортзал.~"
    "Я направился прямиком туда."
    # Видосик с упражнениями 
    "~Фух, знатно потренировался. У меня аж волосы на ногах заболели. Надеюсь, самочки оценят рельеф на моей брови...~"
    "~Теперь мне осталось получить последний урок – покорение девичьих сердец интеллектом.~"
    "~Для этого мне необходим наставник Даниил.~"
    "Ходят слухи, что его IQ равен 192, и он участвовал в убийстве Кеннеди."
    "~Что ж, проверим...~"
    "В корридоре я поднял записку. Развернул. 'Приходи на лестницу спуска. Площадка 3 этажа.'"
label kaza:
    "~Рядовой Черножопенко на место сбора прибыл.~"
    g "Добрейший вечерочек. Ты и есть величайший ум человечества, Даня?"
    kaza "*С еврейским акцентом*: Точно так."
    g "Почему мы встретились здесь?"
    kaza "Это единственное место, не утыканное камерами."
    g "А ты прячешься от чужих глаз?"
    kaza "Я криминальная личность. Ворую препараты из кабинета химии.."
    "Прости, мама, что рано вырос бандитом!"
    #Далее нужна идея Даниила
    jump swimmers_branch

label final
    scene bg II home enter
    "~Ребята задерживаются.~"
    "~Надеюсь, они придут.~"
    "В последний раз я так волновался, когда врачи выдергивали меня из утробы матери.."
    "~Скорее бы открылась эта дверь.~"
    if brutality >= 4:
        "Как по велению судьбы, я услышал шаги за дверью"
        "~Это они. Точно они.~"
        "~Ну всё, Артурчик, настало время показать себя.~"
        scene white with dissolve #Так вообще можно? разберусь и доделаю.
    else:
        "Время шло, а парни так и не появлялись.{w} Из кабинета уже доносились возмущенные голоса девушек."
        "~Они уже не придут.. В одиночку я ничего не смогу.~"
        "Остается лишь уйти с позором."
        #Тут доделать плохую концовку
        
        
