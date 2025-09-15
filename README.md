Explanation:
Imports:
pygame is the main library, and sys is used for exiting the program. pygame.locals provides constants like QUIT.
Initialization:
pygame.init() initializes all Pygame modules. pygame.display.set_mode() creates the game window, and pygame.display.set_caption() sets the window's title.
Game Loop:
The while running: loop keeps the game running until the user quits.
Event Handling: pygame.event.get() retrieves all events (like mouse clicks or key presses). The code checks for QUIT events (when the user clicks the close button) to set running to False and exit the loop.
Drawing: screen.fill() clears the screen with a specified color.
Text Rendering: pygame.font.SysFont() creates a font object. font.render() creates a Surface object containing the rendered text. text_surface.get_rect() gets a rectangle representing the text's boundaries, and center positions it in the middle of the screen. screen.blit() draws the text surface onto the main screen.
Update Display: pygame.display.update() refreshes the entire screen to show the changes.
Quit:
pygame.quit() uninitializes Pygame modules, and sys.exit() exits the Python program.