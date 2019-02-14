########################
#
#KPK - 2019
#DefinitelyNotMastermind
#
#Ceyhun "CengizDegilim" Gülbaş: "Nesne yükseltmesi başarıyla tamamlandı."
#Buğra "Sasu" Marsak: "Ya hek!"
#Oğuzhan "Susa" Dublezeks: "Pipimiz küçük kodumuz düşük."
#
#
#Biz yapamadık, allah kahretsin böyle projeyi.
#Destek olmak isteyenler seri layklıyor.
#Twitter'dan ulaşabilirsiniz. https://twitter.com/cengizdegilim -Ceyhun 14/02/19
#########################

import pygame

pygame.init()

pencere = pygame.display.set_mode((480,720))
baslik = pygame.display.set_caption("Mastermind")
fps = pygame.time.Clock()

Backgr = (208,219,255)


green = pygame.image.load('green-ball.png')
green = pygame.transform.scale(green, (50, 50))

lblue = pygame.image.load('light-blue-ball.png')
lblue = pygame.transform.scale(lblue, (50, 50))

dblue = pygame.image.load('dark-blue-ball.png')
dblue = pygame.transform.scale(dblue, (50, 50))

maroon = pygame.image.load('maroon-ball.png')
maroon = pygame.transform.scale(maroon, (50, 50))

orange = pygame.image.load('orange-ball.png')
orange = pygame.transform.scale(orange, (50, 50))

purple = pygame.image.load('purple-ball.png')
purple = pygame.transform.scale(purple, (50, 50))

red = pygame.image.load('red-ball.png')
red = pygame.transform.scale(red, (50, 50))

yellow = pygame.image.load('yellow-ball.png')
yellow = pygame.transform.scale(yellow, (50, 50))




kapat = False
while kapat == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kapat = True

        #if event.type == pygame.KEYDOWN:
          #  if event.key == pygame.K_SPACE:
           #     bir seyler yapsin


    pencere.fill((Backgr))
    pencere.blit(green, (0,0))
    pencere.blit(dblue,(60,0))
    pencere.blit(lblue,(120,0))
    pencere.blit(maroon,(180,0))
    pencere.blit(orange,(240,0))
    pencere.blit(purple,(300,0))
    pencere.blit(red,(360,0))
    pencere.blit(yellow,(420,0))
    
    pygame.display.flip()

    fps.tick(60)
    pygame.display.flip()
    pencere.fill(Backgr)
   
pygame.quit()
