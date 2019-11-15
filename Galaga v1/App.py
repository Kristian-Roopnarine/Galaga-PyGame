class App:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.block = 10
        self.background = (0,0,0)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.running = True
        self.clock = pygame.time.Clock()
    
    def drawGame(self):
        for y in range(self.height//5):
            for x in range(self.width//5):
                rect = pygame.Rect(x * self.block, y * self.block, self.block, self.block)
                pygame.draw.rect(self.screen,self.background,rect)
    
    def drawPlayer(self):
        ship = pygame.Rect(player.x,player.y,player.width,player.height)
        pygame.draw.rect(self.screen,player.color,ship)
    
    def drawBullet(self,bullets):
        for bullet in bullets:
            b = pygame.Rect(bullet.x,bullet.y,bullet.width,bullet.height)
            pygame.draw.rect(self.screen,bullet.color,b)
    
    def createEnemies(self,list):
        for x in range(100-(25//2),301,100):
            for y in range(25,301,100):
                if y == 225:
                    enemy = create_enemies(x,y,True,1)
                elif y == 125:
                    enemy = create_enemies(x,y,False,2)
                elif y == 25: 
                    enemy = create_enemies(x,y,False,3)
                list.append(enemy)
                
    def drawEnemies(self,enemies):
        for enemy in enemies:
            e = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            pygame.draw.rect(self.screen, enemy.color , e)
    
    def redraw(self,el,pblist,eblist):
        self.screen.fill(self.background)
        self.drawPlayer()    
        self.drawEnemies(el)
        self.drawBullet(pblist)
        self.drawBullet(eblist)
        pygame.display.update()
         
    def endGame(self):
        self.running = False

    def startApp(self):
        player_bullet_list = []
        enemy_list = []
        enemy_bullet_list = []
        self.drawGame()
        self.createEnemies(enemy_list)
        pygame.display.flip()
        
        while self.running:
            self.clock.tick(60)
            shooter_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
        
            for bullet in player_bullet_list:
                if 0 < bullet.y < 600:
                    bullet.moveUp()   
                else:
                    player_bullet_list.pop(player_bullet_list.index(bullet))
            
            for bullet in enemy_bullet_list:
                if 600 > bullet.y > 0:
                    bullet.moveDown()  
                else:
                    enemy_bullet_list.pop(enemy_bullet_list.index(bullet))
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player.x > 0:
                player.moveLeft()
            
            if keys[pygame.K_RIGHT] and player.x < self.width - player.width:
                player.moveRight()
            
            if keys[pygame.K_SPACE] and not self.playerOnCooldown(player.cooldown):
                player.createBullet(player_bullet_list)
                self.resetCooldown('player')
            
            if not self.enemyOnCooldown(1):
                for enemies in enemy_list:
                    if enemies.canShoot:
                        enemies.createBullet(enemy_bullet_list)
                self.resetCooldown('enemy')
                
            if player.isHit(enemy_bullet_list):
                player.loseHealth()
                if player.health == 0:
                    self.endGame()
            
            for enemies in enemy_list:
                if enemies.isHit(player_bullet_list):
                    enemies.loseHealth()
                    if enemies.health == 0:
                        enemy_list.pop(enemy_list.index(enemies))
            
            for enemies in enemy_list:
                if enemies.row == 1:
                    shooter_count += 1
                
            if shooter_count == 0:
                for enemies in enemy_list:
                    if enemies.row == 2:
                        enemies.canShoot = True
            
            if len(enemy_list) == 0:
                self.endGame()

            '''
            self.screen.fill(self.background)
            self.drawPlayer()    
            self.drawEnemies(enemy_list)
            self.drawBullet(player_bullet_list)
            self.drawBullet(enemy_bullet_list)
            pygame.display.update()
            '''
            self.redraw(enemy_list,player_bullet_list,enemy_bullet_list)