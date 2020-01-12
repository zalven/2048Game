# 2048Game
begginer Pygame 2048 :&lt;














import pygame 
import random
from pygame import *
pygame.init() 
pygame.display.set_caption('2048 Game') 
class game2048(): 
    def __init__(self,sizeX,sizeY,BgColor,gameSize,score):
        self.score = score 
        self.sizeX = sizeX 
        self.sizeY = sizeY 
        self.gameRun = True 
        self.BgColor = BgColor
        self.gameSize = gameSize
        self.clock = pygame.time.Clock()
        self.mouse = pygame.mouse.get_pos() 
        self.grid = [[0]*gameSize for i in range(gameSize)]
        self.screen = pygame.display.set_mode([self.sizeX,self.sizeY])
    
        '''
        self.grid = [[2,2,4,8],
                     [16,32,64,128],
                     [256,512,1024,2048],
                     [4096,16384,32768,2]]
        '''
        self.color =  { 2:      [(235, 223, 199),32 , (119, 111, 100) ,0],
                        4:      [(235, 223, 199),32 , (119, 111, 100) ,0],
                        8:      [(243, 176, 121),32 , (253, 244, 235) ,0],
                        16:     [(245, 149, 99),30  , (253, 244, 235) ,10],
                        32:     [(245, 124, 95),30  , (253, 244, 235) ,10],
                        64:     [(246, 93, 59),30   , (253, 244, 235) ,10],
                        128:    [(237, 206, 113),27 , (253, 244, 235) ,15],
                        256:    [(237, 204, 97),27  , (253, 244, 235) ,15],
                        512:    [(236, 200, 80),27  , (253, 244, 235) ,15],
                        1024:   [(237, 197, 63),25  , (253, 244, 235) ,22],
                        2048:   [(238, 194, 46),25  , (253, 244, 235) ,22],
                        4096:   [(61, 58, 51),23    , (253, 244, 235) ,22],
                        16384:  [(61, 58, 51),23    , (253, 244, 235) ,26],
                        32768:  [(61, 58, 51),23    , (253, 244, 235) ,26]}
                    # Valie : Box Color , FontSize , FontColor ,CenterAlignment
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
    def quitgame():
        pygame.quit()
        quit()
    

    def loseTurn(grid):
        if grid == False:
            return False
        g = sum([sum([1 for p in _ if p != 0 ] ) for _ in grid])
        for i,y in zip(grid,zip(*grid)):
            if any([i[j] == i[j+1] for j in range(len(i)-1)]+([y[j] == y[j+1] for j in range(len(y)-1)])):
                return True 
        if g == 16:
            return False 
        return True   

    def background(self):
        self.screen.fill(self.BgColor)
        size = self.sizeY-90
        gap = 10
        squareSize = int(size/self.gameSize)-gap
        pygame.draw.rect(self.screen,(164, 147, 129),[50,50,size,size])
        for j in range(self.gameSize):
            for i in range(self.gameSize):
                pygame.draw.rect(self.screen, (191, 175, 160),
                [50*(i*3-i+1)+gap,50*(j*3-j+1)+gap,squareSize ,squareSize ])
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != 0:
                    self.font = pygame.font.Font('freesansbold.ttf', 
                    self.color[self.grid[i][j]][1] ) 
                    pygame.draw.rect(self.screen, self.color[self.grid[i][j]][0],
                [50*(j*3-j+1)+gap,50*(i*3-i+1)+gap,squareSize ,squareSize])
                    self.screen.blit(self.font.render(f'{self.grid[i][j]}', True,
                                            self.color[self.grid[i][j]][2])
                                        ,( (50*(j*3-j+1)+gap)+40-self.color[self.grid[i][j]][3] , 
                                            50*(i*3-i+1)+gap +30  )) 
    post = lambda grid:[i for i in grid if i == 0]+[i for i in grid if i!= 0]
    def ajust(self,grid):
        for every in range(len(grid)):
            push = game2048.post(grid[every]) 
            element = len(push )-1
            while element > 0:
                if push[element] == push[element-1]:
                    push[element-1],push[element]  = push[element-1]+push[element],0 
                    self.score += push[element-1]+push[element]
                    element-=1 
                element-=1
            grid[every] = game2048.post(push)
        return grid

    def game2048(self,grid, path):
        for moves in path:
            if moves == "R": 
                grid = [[*_] for _ in game2048.ajust(self,grid)]
                
            elif moves == "L" : 
                grid = [_[::-1] for _ in game2048.ajust(self,[_[::-1] for _ in grid])]
                
            elif moves == 'D': 
                grid = [[*i] for i in zip(*game2048.ajust(self,[*zip(*grid)]))]
                
            else:
                grid = [[*i] for i in zip(*game2048.ajust(self,[*zip(*grid[::-1])]))][::-1]
              
        return grid
    def button(self):
        center = self.sizeY//2-150
        
        pygame.draw.rect(self.screen, (0, 127, 194),(center,center,center,center))
        pygame.draw.rect(self.screen, (244, 102, 116), (center+200,center,center,center))
        myfont = pygame.font.SysFont('freesansbold.ttf', 25)
        
        textsurface = myfont.render('Continue', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+12,center+30))

        textsurface = myfont.render('[ space ]', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+12,center+50))

        textsurface = myfont.render('Quit', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+230,center+30))

        textsurface = myfont.render('[ Esc ]', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+230,center+50))


    def display(self):
        
        game2048.background(self)  

        center = self.sizeY//2
    
        myfont = pygame.font.SysFont('freesansbold.ttf', 35)
        textsurface = myfont.render('Gener', False, (119, 111, 100))
        self.screen.blit(textsurface,(0 ,0))

        game2048.messageScore(self) 
        game2048.highScores(self)
        self.clock.tick(2000)
        pygame.display.flip()
        pygame.display.update()  

    def restart(self):
        

        clicked = pygame.mouse.get_pressed()[0]
        if (self.mouse[0] > 100 and self.mouse[0] <200 and 
            self.mouse[1] > 100 and self.mouse[1] <200 and clicked == 1 ):
            self.grid  = [[0]*self.gameSize for i in range(self.gameSize)]
            
            game2048.readifOver(self)
            self.grid = [[0]*self.gameSize for i in range(self.gameSize)]
            game2048.main(self)
            
            self.score = 0
        if (self.mouse[0] > 300 and self.mouse[0] <400 and 
            self.mouse[1] > 100 and self.mouse[1] <200 and clicked == 1):
        
            game2048.readifOver(self)
            game2048.quitgame()
            self.grid = [[0]*self.gameSize for i in range(self.gameSize)]
            
            

    def messageScore(self):

        center = self.sizeY//2
        pygame.draw.rect(self.screen, (186, 174, 160),(center ,0,100,50))
        myfont = pygame.font.SysFont('freesansbold.ttf', 25)
        textsurface = myfont.render(f'{self.score:08d}', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+10 ,15))

        textsurface = myfont.render('score', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+30 ,30))

    def readifOver(self):
        if (self.score > max([ int(i) for i in eval(open('Scores.txt','r').read()) ] ) ):
            file = eval(open('Scores.txt','r').read())
            file.add(int(self.score))
            file = open('Scores.txt','w').write(str(file))
        self.score = 0
    
    def highScores(self):

        center = self.sizeY//2
        pygame.draw.rect(self.screen, (186, 174, 160),(center+110,0,100,50))
        myfont = pygame.font.SysFont('freesansbold.ttf', 25)
        scores = eval(open('Scores.txt','r').read())
        textsurface = myfont.render(f'{max([int(i) for i in scores]):08d}', False, (253, 244, 235))
        myfont = pygame.font.SysFont('freesansbold.ttf', 20)
        self.screen.blit(textsurface,(center+122 ,15))
        textsurface = myfont.render('Hish-Score', False, (253, 244, 235))
        self.screen.blit(textsurface,(center+130,35))

    def randomNum(self):
        animation = True 
        squareSize = int(self.sizeY-90/self.gameSize)-10
        if sum([sum(1 for j in i if j != 0) for i in self.grid]) != 16:
            self.grid  = [[*i] for i in  self.grid]
            count = 30 
            x = random.choice(range(len( self.grid)))
            y = random.choice(range(len( self.grid)))
            
            while ( self.grid[x][y]!=0):
                x = random.choice(range(len( self.grid)))
                y = random.choice(range(len( self.grid)))
            if  self.grid[x][y] == 0:
                self.grid[x][y] = random.choice([2,2,2,2,2,4]) 
              
                while animation:
        
                    if count == 50:
                        animation = False 
                    # 30 - 50 / 0032 
                    pygame.draw.rect(self.screen, (235, 223, 199),
                [50*(y*3-y+1)+10,50*(x*3-x+1)+10,count ,count  ])
                    self.font = pygame.font.Font('freesansbold.ttf',count-10 ) 
                    self.screen.blit(self.font.render(f'{self.grid[x][y]}', True,
                                            self.color[self.grid[x][y]][2])
                                        ,( (50*(y*3-y+1)+10)+40-self.color[self.grid[x][y]][3] , 
                                            50*(x*3-x+1)+10 +30  )) 
                    count +=1 
                    self.clock.tick(5000)
                    pygame.display.flip()
                    pygame.display.update()
    def main(self,*args, **kwargs):
        game2048.randomNum(self)
        n = self.grid
        while self.gameRun:
            self.mouse = pygame.mouse.get_pos()
            recentGrid = self.grid
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.gameRun = False
                    game2048.quitgame()
                if game2048.loseTurn(self.grid):
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_s:
                            self.grid = game2048.game2048(self,self.grid, 'D')
                            if recentGrid != self.grid:
                                game2048.randomNum(self) 
                        elif events.key == pygame.K_a:
                            self.grid = game2048.game2048(self,self.grid, 'L')
                            if recentGrid != self.grid:
                                game2048.randomNum(self) 
                        elif events.key == pygame.K_w:
                            self.grid = game2048.game2048(self,self.grid, 'U')
                            if recentGrid != self.grid:
                                game2048.randomNum(self) 
                        elif events.key == pygame.K_d:                      
                            self.grid = game2048.game2048(self,self.grid, 'R')
                            game2048.randomNum(self) 
                        
                    game2048.display(self)             
                else: 
                    game2048.display(self)
                    game2048.button(self)
                    pygame.display.flip()
                    pygame.display.update()
                    self.clock.tick(2000) 
                    game2048.restart(self)
game2048(500,500,           # X , Y 
        (251, 248, 239),    #BACKGROUND COLOR   
        4, 0                 #Game Size
        ).main()
{0, 10404, 1160}
