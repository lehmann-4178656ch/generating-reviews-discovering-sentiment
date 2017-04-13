from colour import Color
from PIL import Image, ImageDraw, ImageFont

NUM_COLORS = 15

def shrink_result(text, value):
    return [(text[i][i], value[i]) for i in range(len(text[-1]))]

def rgbf_to_rgbi(rgbf):
    return (int(255 * rgbf[0]), int(255 * rgbf[1]), int(255 * rgbf[2]))


def color_result(res):
    char_count = len(res)
    font = ImageFont.load_default()
    font_color = (0, 0, 0)
    w_size = font.getsize('W')

    color_base = Color('#ffffff')
    color_green = Color('#00ff00')
    color_greens = list(color_base.range_to(color_green, NUM_COLORS))
    color_red = Color('#ff0000')
    color_reds = list(color_base.range_to(color_red, NUM_COLORS))

    img = Image.new('RGB', (w_size[0] * char_count + 4, w_size[1] + 4),
            rgbf_to_rgbi(color_base.rgb))
    draw = ImageDraw.Draw(img)
    for idx, tup in enumerate(res):
        if tup[1] > 0:
            cidx = min(int(tup[1] * 10), len(color_greens)-1)
            color = color_greens[cidx]
        else:
            cidx = min(int(-tup[1] * 10), len(color_reds)-1)
            color = color_reds[cidx]
        draw.rectangle([2 + w_size[0] * idx, 2, 2 + w_size[0] * (idx + 1),
                w_size[1] + 2], fill=rgbf_to_rgbi(color.rgb))
        draw.text((2 + w_size[0] * idx, 2), tup[0], font=font, fill=font_color)
    return img

def gen_image(texts, values):
    return color_result(shrink_result(texts, values))


if __name__ == '__main__':
    demo_text = ["Hello World"] * 11
    demo_values = [-0.02, 0.03, 0.1, 0.2, 0.25, 0.29, 0.4, 0.6, -0.4, -0.8, 0.8]
    gen_image(demo_text, demo_values).show()
    demo_values = [-v for v in demo_values]
    gen_image(demo_text, demo_values).show()
