from PIL import Image, ImageColor, ImageDraw, ImageFont

cherry = {"name": "cherry", "color_range": range(100, 150 + 1), "hex": "#7f0320"}
pumpkin_spice = {"name": "pumpkin spice", "color_range": range(90, 99 + 1), "hex": "#af0013"}
honey_bee = {"name": "honey bee", "color_range": range(80, 89 + 1), "hex": "#fcee6f"}
wintergreen = {"name": "wintergreen", "color_range": range(70, 79 + 1), "hex": "#007c46"}
fern = {"name": "fern", "color_range": range(60, 69 + 1), "hex": "#418d6f"}
waterfall = {"name": "waterfall", "color_range": range(50, 59 + 1), "hex": "#5db2ac"}
pastel_blue = {"name": "pastel blue", "color_range": range(40, 49 + 1), "hex": "#a3d1e7"}
denim = {"name": "denim", "color_range": range(30, 39 + 1), "hex": "#446ab7"}
cornflower = {"name": "cornflower", "color_range": range(21, 29 + 1), "hex": "#3e5d8d"}
thistle = {"name": "thistle", "color_range": range(15, 20 + 1), "hex": "#696496"}
navy = {"name": "navy", "color_range": range(-40, 14 + 1), "hex": "#322c40"}

yarns = [
    cherry,
    pumpkin_spice,
    honey_bee,
    wintergreen,
    fern,
    waterfall,
    pastel_blue,
    denim,
    cornflower,
    thistle,
    navy,
]

example_set = [39, 26, 22, 33, 30, 18, 16, 32, 32, 16, 36, 41, 40, 36, 36, 28, 28, 32, 48, 45, 19, 27, 32, 25, 27, 14, 14, 31, 25, 24, 32, 34, 45, 30, 25, 25, 20]


im = Image.new("RGB", (300, len(example_set) * 50), (128, 128, 128))
draw = ImageDraw.Draw(im)

class YarnShit():
    def __init__(self, draw_obj, increment: int = 50):
        self.draw_obj = draw_obj
        self.increment = increment
    
    def img_start_coords(self, x1: int = 0, y1: int = 0, x2: int = 300, y2: int = 50):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        return(self)
    
    def text_start_coords(self, text_x: int = 20, text_y: int = 15):
        self.text_x = text_x
        self.text_y = text_y
        return(self)

    def setup_defaults(self):
        self.img_start_coords()
        self.text_start_coords()

    def draw_block(self, hex_color: str):
        self.draw_obj.rectangle(((self.x1, self.y1), (self.x2, self.y2)), fill=ImageColor.getrgb(hex_color))
    
    def write_text(self, text: str):
        font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf",27)
        self.draw_obj.text((self.text_x, self.text_y), text)

    def increment_block(self):
        self.y1 += self.increment
        self.y2 += self.increment
        return(self)
    
    def increment_text(self):
        self.text_y += self.increment
        return(self)
    
    def increment_all(self):
        self.increment_block()
        self.increment_text()

heregoes = YarnShit(draw)
heregoes.setup_defaults()
for temp in example_set:
    for yarn in yarns:
        if temp in yarn['color_range']:
            heregoes.draw_block(yarn['hex'])
            heregoes.write_text(yarn['name'] + ' ' + str(temp))
            heregoes.increment_all()

im.save("out_file.jpg", "JPEG")
