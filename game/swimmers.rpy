﻿label swimmers_branch:
play music "sounds/sea.mp3" fadeout 1.0 fadein 1.0
"Мне резко захотелось посидеть на троне философа. А поскольку самый комфортабельный туалет расположен на 1 этаже, я направился туда."
"Уже подходя к заветной двери, я услышал булькающие звуки..."
epif "Ой, да в этом 11А все девочки скучные."
alex "И недалёкие."
melk "А еще у них титьки маленькие! И попы толстые!!"
"Это они про тех красавиц, которых я собираюсь охмурять?!"
stop music
play music "sounds/epic.mp3" fadein 1.0 fadeout 1.0
"У меня горело.. Во мне бурлило.. Я чувствовал гнев, поднимающийся из области таза и вздымающийся ввысь, до самых моих очей."
"Я подогнал к таинственным негодяям. Передо мной предстали 3 спортивных шкафчика.."
"Хм.. Глаза слегка красные.. От хлорки? Наверняка пловцы!"
g "Э, шакалы водоплавающие, вы вообще страх потеряли? Позволяете себе оскорблять мамзелей? Больше я такого не потерплю."
g "Даю вам последний шанс исправиться: покайтесь! Потом можете сматывать свой {b}Летучий Голландец{/b} и валить хоть к Посейдону."
u"Пловцы" "У нас есть идея получше. Ща мы тебе {b}намылим шею{/b}, будешь знать своё место, принц-монобровка!"
g "Не так быстро, у меня теперь есть союзники!"
stop music fadeout 1.0
#Появляется 1 кадр(!) из видосика.
play sound "sounds/whistle.mp3"
$ renpy.pause(1.0)
#начинается видос:
#    под музыку "буду погибать молодым" идем с пачанами, делаем характерные движения, которые я покажу
#    кто-то поигрывает ножом, кулаками, еще какие-нибудь брутальности
#    подгоняем к пловцам.
#    Обращаюсь к пловцу, стоящему посередине: -Ну что, Губка Боб, сейчас я и тебя, и твою команду на дно пущу! На абордаааааж!!!
#    Пловцы хором: "А.. А.. А МЫ СМЫВАЕМСЯ!", забегают в туалет и захлопывают дверь.
#    Все пачаны пожимают руками, я: -Ну, туалет - это своего рода храм. Там драться нельзя. Пойдемте, пачаны, мы отвоевали честь наших дам...
"~Эх, не удалась философия.~"
g "Друзья, прекрасным дамам нужно что-то подарить. У вас есть идеи?"
show meln at left
with dissolve
meln "Да, мы уже всё приготовили."
show turi at right
with dissolve
turi "Отправляйся в 207 кабинет и жди в предбаннике."
show pash norm at center 
with dissolve
pash "Девочки уже ждут за партами. Мы прибудем с подарком, ты к нам примажешься, поздравим все вместе."
hide meln
hide turi
hide pash norm
show gark norm
gark "Эх, жаль Славик этого не увидит.."
gark "После того, как его семья переехала в Узбекистан, совсем тоскливо стало в нашем коллективе.{w} Аж спать хочется.."
g "Буду ждать вас на месте."
hide gark norm
jump final