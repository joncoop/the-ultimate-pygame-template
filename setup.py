from config import *
from tools import *

# Make window
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(TITLE)

# Load assets
''' fonts '''
font_sm = pygame.font.Font(DEFAULT_FONT, 24)
font_md = pygame.font.Font(DEFAULT_FONT, 32)
font_lg = pygame.font.Font(DEFAULT_FONT, 64)
font_xl = pygame.font.Font(TITLE_FONT, 96)

GFX = load_all_gfx('assets/images/')
FONTS = load_all_fonts('assets/fonts/')
SFX = load_all_sfx('assets/sounds/')
MUSIC = load_all_music('assets/music/')
