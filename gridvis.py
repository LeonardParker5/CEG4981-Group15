from PIL import Image, ImageDraw

def grid_visualize(grid):
    grid_len = len(grid)

    im = Image.new("RGB", (1000, 1000), "#000000")
    
    draw = ImageDraw.Draw(im)
    
    #draw.ellipse((50, 50, 450, 450), fill=(255, 255, 255), outline=(0, 0, 0))
    draw.rectangle((10, 10, 990, 990), fill=(255, 255, 255), outline=(0, 0, 0))
    
    #draw.line((0, 0) + im.size, fill=128)
    #draw.line((0, im.size[1], im.size[0], 0), fill=128)
    
    step_size = int(im.width / (grid_len))
    y_start = 0
    y_end = im.height
    
    for x in range(0, im.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=(200,200,200))
    
    x_start = 0
    x_end = im.width
    
    for y in range(0, im.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=(200,200,200))
        
    del draw
    
    return im
    #im.show()
    #im = im.save("Resources/grid.jpg")

def init_pos(im, x_pos, y_pos):
    draw = ImageDraw.Draw(im)
    draw.ellipse(((x_pos * 10), (y_pos * 10), (x_pos * 10) + 10, (y_pos * 10) + 10), fill=(255, 0, 0), outline=(0, 0, 0))
    del draw
    return im
    
def render_grid(im):
    im.show()
    im = im.save("Resources/grid.jpg")