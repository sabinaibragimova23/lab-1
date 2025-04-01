import pygame
from math import sqrt

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()

# Setting window size
win_x = 500
win_y = 500
win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Paint')

class Drawing(object):
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 6  # Default brush/pen radius
        self.tick = 0
        self.time = 0
        self.play = False
        # Added new modes for additional shapes
        self.mode = "pen"  # "pen", "rect", "circle", "eraser", "square", "triangle", "eq_triangle", "rhombus"
        self.start_pos = None
        self.drawing_preview = False
        
    def draw(self, win, pos):
        """Draw freehand with pen or eraser"""
        if self.mode == "pen":
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        elif self.mode == "eraser":
            pygame.draw.circle(win, (255, 255, 255), (pos[0], pos[1]), self.rad*2)
    
    def draw_shape(self, win, current_pos):
        """Draw geometric shapes based on current mode"""
        if not self.start_pos:
            return
            
        if self.mode == "rect":
            # Rectangle - drawn between start point and current mouse position
            rect = pygame.Rect(self.start_pos[0], self.start_pos[1],
                             current_pos[0] - self.start_pos[0], 
                             current_pos[1] - self.start_pos[1])
            pygame.draw.rect(win, self.color, rect, self.rad)
            
        elif self.mode == "circle":
            # Circle - radius is distance from start point to current position
            radius = int(sqrt((current_pos[0] - self.start_pos[0])**2 + 
                            (current_pos[1] - self.start_pos[1])**2))
            pygame.draw.circle(win, self.color, self.start_pos, radius, self.rad)
            
        elif self.mode == "square":
            # Square - maintains equal width and height
            side = min(abs(current_pos[0] - self.start_pos[0]), 
                      abs(current_pos[1] - self.start_pos[1]))
            # Adjust side based on mouse position direction
            if current_pos[0] < self.start_pos[0]:
                x = self.start_pos[0] - side
            else:
                x = self.start_pos[0]
            if current_pos[1] < self.start_pos[1]:
                y = self.start_pos[1] - side
            else:
                y = self.start_pos[1]
            pygame.draw.rect(win, self.color, (x, y, side, side), self.rad)
            
        elif self.mode == "triangle":
            # Right triangle - hypotenuse from start to current position
            points = [self.start_pos,
                     (current_pos[0], self.start_pos[1]),
                     (self.start_pos[0], current_pos[1])]
            pygame.draw.polygon(win, self.color, points, self.rad)
            
        elif self.mode == "eq_triangle":
            # Equilateral triangle - height based on width
            width = abs(current_pos[0] - self.start_pos[0])
            height = int(width * sqrt(3) / 2)
            # Determine direction
            if current_pos[0] < self.start_pos[0]:
                x = self.start_pos[0] - width
            else:
                x = self.start_pos[0]
            
            points = [(x, self.start_pos[1] + height),
                     (x + width//2, self.start_pos[1]),
                     (x + width, self.start_pos[1] + height)]
            pygame.draw.polygon(win, self.color, points, self.rad)
            
        elif self.mode == "rhombus":
            # Rhombus (diamond shape) - points calculated from center
            center_x = (self.start_pos[0] + current_pos[0]) // 2
            center_y = (self.start_pos[1] + current_pos[1]) // 2
            width = abs(current_pos[0] - self.start_pos[0])
            height = abs(current_pos[1] - self.start_pos[1])
            
            points = [(center_x, self.start_pos[1]),
                     (current_pos[0], center_y),
                     (center_x, current_pos[1]),
                     (self.start_pos[0], center_y)]
            pygame.draw.polygon(win, self.color, points, self.rad)

    def click(self, win, color_buttons, tool_buttons):
        """Handle mouse clicks for drawing and UI"""
        pos = pygame.mouse.get_pos()

        # Drawing area click handling
        if pygame.mouse.get_pressed() == (1, 0, 0) and pos[0] < 400:
            if pos[1] > 25:  # Below header
                if self.mode in ["pen", "eraser"]:
                    self.draw(win, pos)
                elif self.mode in ["rect", "circle", "square", "triangle", "eq_triangle", "rhombus"] and not self.start_pos:
                    self.start_pos = pos
                    
        # Mouse button released - finalize shape
        elif pygame.mouse.get_pressed() == (0, 0, 0) and self.start_pos:
            self.draw_shape(win, pos)
            self.start_pos = None
                
        # Toolbar button clicks
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            # Color buttons
            for button in color_buttons:
                if button.x <= pos[0] <= button.x + button.width and button.y <= pos[1] <= button.y + button.height:
                    self.color = button.color2
                    
            # Tool buttons
            for button in tool_buttons:
                if button.x <= pos[0] <= button.x + button.width and button.y <= pos[1] <= button.y + button.height:
                    if self.tick == 0:  # Button cooldown check
                        if button.action == 1:  # Clear
                            win.fill((255, 255, 255))
                            self.tick += 1
                        elif button.action == 2 and self.rad > 4:  # Smaller brush
                            self.rad -= 1
                            self.tick += 1
                        elif button.action == 3 and self.rad < 20:  # Bigger brush
                            self.rad += 1
                            self.tick += 1
                        elif button.action == 8:  # Pen
                            self.mode = "pen"
                        elif button.action == 9:  # Rectangle
                            self.mode = "rect"
                        elif button.action == 10:  # Circle
                            self.mode = "circle"
                        elif button.action == 11:  # Eraser
                            self.mode = "eraser"
                        elif button.action == 12:  # Square
                            self.mode = "square"
                        elif button.action == 13:  # Right triangle
                            self.mode = "triangle"
                        elif button.action == 14:  # Equilateral triangle
                            self.mode = "eq_triangle"
                        elif button.action == 15:  # Rhombus
                            self.mode = "rhombus"

        # Update button states
        for button in tool_buttons:
            if button.action == 4:  # Size display
                button.text = str(self.rad)
            # Update button colors to show active tool
            if button.action == 8:  # Pen
                button.color = (100, 100, 100) if self.mode == "pen" else (201, 201, 201)
            elif button.action == 9:  # Rectangle
                button.color = (100, 100, 100) if self.mode == "rect" else (201, 201, 201)
            elif button.action == 10:  # Circle
                button.color = (100, 100, 100) if self.mode == "circle" else (201, 201, 201)
            elif button.action == 11:  # Eraser
                button.color = (100, 100, 100) if self.mode == "eraser" else (201, 201, 201)
            elif button.action == 12:  # Square
                button.color = (100, 100, 100) if self.mode == "square" else (201, 201, 201)
            elif button.action == 13:  # Right triangle
                button.color = (100, 100, 100) if self.mode == "triangle" else (201, 201, 201)
            elif button.action == 14:  # Equilateral triangle
                button.color = (100, 100, 100) if self.mode == "eq_triangle" else (201, 201, 201)
            elif button.action == 15:  # Rhombus
                button.color = (100, 100, 100) if self.mode == "rhombus" else (201, 201, 201)

class Button(object):
    """Button class for UI elements"""
    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text
        
    def draw(self, win):
        """Draw the button on screen"""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.text, 1, self.color2)
        win.blit(text, (int(self.x+self.width/2-text.get_width()/2),
                        int(self.y+self.height/2-text.get_height()/2)))

def drawHeader(win):
    """Draw the application header"""
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 500, 25))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 25), 2)
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 25), 2)

    font = pygame.font.SysFont('comicsans', 20)
    canvasText = font.render('Paint', 1, (0, 0, 0))
    win.blit(canvasText, (int(200 - canvasText.get_width() / 2),
                        int(26 / 2 - canvasText.get_height() / 2) + 2))

    toolsText = font.render('Tools', 1, (0, 0, 0))
    win.blit(toolsText, (int(450 - toolsText.get_width() / 2),
                        int(26 / 2 - toolsText.get_height() / 2 + 2)))

def draw(win):
    """Main drawing function that updates the display"""
    player1.click(win, Buttons_color, Buttons_other)
    
    # Draw shape preview while dragging
    if player1.start_pos:
        current_pos = pygame.mouse.get_pos()
        temp_surface = pygame.Surface((win_x, win_y), pygame.SRCALPHA)
        player1.draw_shape(temp_surface, current_pos)
        win.blit(temp_surface, (0, 0))

    # Draw UI elements
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 500), 2)
    pygame.draw.rect(win, (255, 255, 255), (400, 0, 100, 500))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 500), 2)
    drawHeader(win)

    for button in Buttons_color + Buttons_other:
        button.draw(win)

    pygame.display.update()

def main_loop():
    """Main application loop"""
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        draw(win)

        # Button cooldown timer
        if 0 < player1.tick < 40:
            player1.tick += 1
        else:
            player1.tick = 0

        FramePerSec.tick(FPS)

    pygame.quit()

# Initialize drawing controller
player1 = Drawing()
win.fill((255, 255, 255))

# Color buttons
redButton = Button(453, 30, 40, 40, (255, 0, 0), (255, 0, 0))
blueButton = Button(407, 30, 40, 40, (0, 0, 255), (0, 0, 255))
greenButton = Button(407, 76, 40, 40, (0, 255, 0), (0, 255, 0))
orangeButton = Button(453, 76, 40, 40, (255, 192, 0), (255, 192, 0))
yellowButton = Button(407, 122, 40, 40, (255, 255, 0), (255, 255, 0))
purpleButton = Button(453, 122, 40, 40, (112, 48, 160), (112, 48, 160))
blackButton = Button(407, 168, 40, 40, (0, 0, 0), (0, 0, 0))
whiteButton = Button(453, 168, 40, 40, (0, 0, 0), (255, 255, 255), 1)

# Tool buttons
clrButton = Button(407, 214, 86, 40, (201, 201, 201), (0, 0, 0), 0, 1, 'Clear')
smallerButton = Button(407, 260, 40, 40, (201, 201, 201), (0, 0, 0), 0, 2, '-')
biggerButton = Button(453, 260, 40, 40, (201, 201, 201), (0, 0, 0), 0, 3, '+')
sizeDisplay = Button(407, 306, 86, 40, (0, 0, 0), (0, 0, 0), 1, 4, 'Size')

# Drawing tool buttons
penButton = Button(407, 352, 40, 40, (201, 201, 201), (0, 0, 0), 0, 8, 'P')
rectButton = Button(453, 352, 40, 40, (201, 201, 201), (0, 0, 0), 0, 9, 'R')
circleButton = Button(407, 398, 40, 40, (201, 201, 201), (0, 0, 0), 0, 10, 'C')
eraserButton = Button(453, 398, 40, 40, (201, 201, 201), (0, 0, 0), 0, 11, 'E')
squareButton = Button(407, 444, 40, 40, (201, 201, 201), (0, 0, 0), 0, 12, 'S')
triangleButton = Button(453, 444, 40, 40, (201, 201, 201), (0, 0, 0), 0, 13, 'T')
eqTriangleButton = Button(407, 490, 40, 40, (201, 201, 201), (0, 0, 0), 0, 14, 'ET')
rhombusButton = Button(453, 490, 40, 40, (201, 201, 201), (0, 0, 0), 0, 15, 'Rh')

Buttons_color = [blueButton, redButton, greenButton, orangeButton,
                yellowButton, purpleButton, blackButton, whiteButton]
Buttons_other = [clrButton, smallerButton, biggerButton, sizeDisplay,
                penButton, rectButton, circleButton, eraserButton,
                squareButton, triangleButton, eqTriangleButton, rhombusButton]

main_loop()