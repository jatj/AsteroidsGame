import pygame
from pygame.locals import *
from random import randint

pygame.init()

wind_width = 800
wind_height = 640

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

font = pygame.font.SysFont("Nonserif",32)

gameDisplay = pygame.display.set_mode((wind_width,wind_height))
pygame.display.set_caption('Tests')

spaceShipIMG = pygame.image.load('spaceship.png')
spaceShipRedIMG = pygame.image.load('spaceshipRed.png')
laserIMG = pygame.image.load('laserShoot.png')
asteroidIMG = pygame.image.load('asteroid.png')
asteroidICO = pygame.image.load('asteroidICO.png')
lifeICO = pygame.image.load('life.png')
backgroundIMG = pygame.image.load('background.png')
gameOverIMG = pygame.image.load('gameOver.png')
youWinIMG = pygame.image.load('youWin.png')
pygame.mixer.music.load("chiptuneMusic.wav")
pygame.mixer.music.play(-1,0.0)
Asteroids = []
Lasers = []

class Nave():
    "Clase de nave"
    def __init__(self,x,y,inc):
        self.X = x
        self.Y = y
        self.incX = inc
        self.incY = inc
        self.rect = pygame.Rect(self.X,self.Y,spaceShipIMG.get_width(),spaceShipIMG.get_height())
        self.l=False
        self.r=False
        self.u=False
        self.d=False
        self.col = False
        print "Nave iniciada"
    
    "Metodo que mueve por la escena a la nave"
    def Move(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and not self.l:
                "print ('left')"
                self.incX=-3
            if event.key==pygame.K_RIGHT and not self.r:
                "print ('right')"
                self.incX=3
            if event.key==pygame.K_UP and not self.u:
                "print ('up')"
                self.incY=-3
            if event.key==pygame.K_DOWN and not self.d:
                "print ('down')"
                self.incY=3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                self.incX=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                self.incY=0
        
    "Hace que la nave se mantenga en la ventana"
    def Limit(self):
        if(self.X>=wind_width - 50):
            self.r=True
            self.X=wind_width - 50
        else:
            self.r=False
        if(self.X<=0):
            self.l=True
            self.X=0
        else:
            self.l=False
        if(self.Y>=wind_height - 64):
            self.d=True
            self.Y=wind_height - 64
        else:
            self.d=False
        if(self.Y<=0):
            self.u=True
            self.Y=0
        else:
            self.u=False
        "Actualiza la posicion de la nave"
        self.X+=self.incX
        self.Y+=self.incY
        self.rect = pygame.Rect(self.X,self.Y,spaceShipIMG.get_width(),spaceShipIMG.get_height())
        
    "Metodo que dibuja al asteroide"
    def Draw(self):
        if(self.col):
            gameDisplay.blit(spaceShipRedIMG,(self.X,self.Y))
            self.col = False
        else:
            gameDisplay.blit(spaceShipIMG,(self.X,self.Y))

    "Metodo que regresa el rect Completo"
    def getRect(self):
        return self.rect

    def Collision(self, col):
        temp = col
        if(temp or col):
            self.col = True

class Asteroid():
    """Clase de asteroide"""
    def __init__(self,x,y,incX,incY):
        self.X = x
        self.Y = y
        self.incX = incX
        self.incY = incY
        self.rect = pygame.Rect(self.X,self.Y,asteroidIMG.get_width(),asteroidIMG.get_height())
        print "Asteroide iniciado"
    
    """Metodo que mueve por la escena al asteroide"""
    def Move(self):
        "Hace que el asteroide se rebote en la ventana"
        if((self.X>=wind_width - 50) or (self.X<=0)):
            self.incX = self.incX*(-1)
        if((self.Y>=wind_height - 64) or (self.Y<=0)):
            self.incY = self.incY*(-1)
        "Actualiza la posicion deL asteroide"
        self.X+=self.incX
        self.Y+=self.incY
        self.rect = pygame.Rect(self.X,self.Y,asteroidIMG.get_width(),asteroidIMG.get_height())
        
    """Metodo que dibuja al asteroide"""
    def Draw(self):
        gameDisplay.blit(asteroidIMG,(self.X,self.Y))

    "Metodo que regresa un rect"
    def getRect(self):
        return self.rect

    "Metodo que checa colision con un rect"
    def checkCollision(self, rect):
        if(self.rect.colliderect(rect)):
            return True
        else:
            return False
        
    "Metodo que cambia la direccion del asteroid"
    def setDirection(self,x,y):
        self.incX = self.incX*(x)
        self.X+=20*x;
        self.incY = self.incY*(y)
        self.Y+=20*y;

class Laser():
    "Clase para los disparos"

    def __init__(self,x,y,incY):
        self.X = x
        self.Y = y
        self.incY = incY
        self.rect = pygame.Rect(self.X,self.Y,laserIMG.get_width(),laserIMG.get_height())
        print "Laser iniciado"

    """Metodo que mueve por la escena al asteroide"""
    def Move(self):
        "Actualiza la posicion deL asteroide"
        self.Y+=self.incY
        self.rect = pygame.Rect(self.X,self.Y,laserIMG.get_width(),laserIMG.get_height())
        
    """Metodo que dibuja al asteroide"""
    def Draw(self):
        gameDisplay.blit(laserIMG,(self.X,self.Y))

    "Metodo que regresa un rect"
    def getRect(self):
        return self.rect

def LoadAsteroid():
    """Metodo para cargar asteroides al arreglo"""
    x=randint(1,3)
    y=randint(1,3)
    if(randint(0,10)%2==0):
        a = Asteroid(randint(1,wind_width-64),randint(1,wind_height-64),-x,y)
    else:
        a = Asteroid(randint(1,wind_width-64),randint(1,wind_height-64),x,-y)
    Asteroids.append(a)

def LoadLaser(x,y):
    """Metodo para cargar asteroides al arreglo"""
    x+=4
    y-=5
    l = Laser(x,y,-5)
    Lasers.append(l)

def Update():
    points = 0
    life = 3
    nave = Nave(wind_width*0.45,wind_height*0.8,0)
    time = pygame.time.Clock()
    end = False
    quitGame=False
    ciclos = 0
    ciclosLife=0

    while not end:

        "Event handler"
        for event in pygame.event.get():

            "Control del juego"
            if event.type==pygame.QUIT:
                end = True
                quitGame=True
            if event.type==pygame.KEYDOWN:
                if event.key==27:
                    print ('quit')
                    end=True
                    quitGame=True
                if event.key==32:
                    print ('Shoot laser')
                    LoadLaser(nave.getRect().x,nave.getRect().y)
            
            "Control del usuario"
            nave.Move(event);

        "Carga asteroides cada 100 ciclos"
        if(ciclos%100==0):
            LoadAsteroid()
        
        "Limita la nave a moverse por la ventan"
        nave.Limit()
        
        "Mueve a los lasers"
        l=0
        for Laser in Lasers:
            Laser.Move()
            if(Laser.getRect().y<=-laserIMG.get_height()):
                Lasers.pop(l)
            l+=1
            
        "Mueve a los asteroides"
        a=0
        for Asteroid in Asteroids:
            Asteroid.Move()
            "Checa colisiones"
            if(Asteroid.checkCollision(nave.getRect())):
                nave.Collision(True)
                if(ciclosLife>50):
                    life-=1
                    ciclosLife=0
            else:
                nave.Collision(False)
            l=0
            for Laser in Lasers:
                if(Asteroid.checkCollision(Laser.getRect())):
                    Asteroids.pop(a)
                    Lasers.pop(l)
                    points+=1
                l+=1
            a+=1
        
        "Dibuja el fondo"       
        gameDisplay.blit(backgroundIMG,(0,0))

        "Dibuja el puntaje"
        gameDisplay.blit(lifeICO,(5,5))
        text = font.render("x "+str(life), 1, white)
        gameDisplay.blit(text,(37,5))
        gameDisplay.blit(asteroidICO,(75,5))
        text = font.render("x "+str(points), 1, white)
        gameDisplay.blit(text,(107,5))
        
        "Dibuja el asteroide"
        for Asteroid in Asteroids:
            Asteroid.Draw()
            
        "Dibuja a los lasers"
        for Laser in Lasers:
            Laser.Draw()
        
        "Dibuja el personaje"
        nave.Draw()

        if(life<=0):
            end=True
            gameDisplay.blit(gameOverIMG,(0,100))
            #pygame.mixer.music.load("lose.wav")
            #pygame.mixer.music.play(1,0.0)
        if(points>=25):
            end=True
            gameDisplay.blit(youWinIMG,(0,20))
            #pygame.mixer.music.load("success.wav")
            #pygame.mixer.music.play(1,0.0)

        ciclos+=1
        ciclosLife+=1
        
        pygame.display.update()
        time.tick(60)

    return quitGame    

def End(quitGame):
    while not quitGame:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print ('quit')
                quitGame=True 
            if event.type==pygame.KEYDOWN:
                if event.key==27:
                    print ('quit')
                    quitGame=True  

quitGame=Update()
End(quitGame)
pygame.quit()  
