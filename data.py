from PIL import Image
from heapq import nlargest
from operator import itemgetter

def get_data(file):
    img = Image.open(file)
    colors_rgb = {}
    for pixel in img.getdata():
        if pixel in colors_rgb:
            colors_rgb[pixel] += 1
        else:
            colors_rgb[pixel] = 1
    return colors_rgb

def get_top_10(colors_rgb):
    top_10 = dict(sorted(colors_rgb.items(), key=itemgetter(1), reverse=True)[:10])
    return top_10

def rgb_to_hex(dict):
    hex_color = []
    for color in dict:
        hex_color.append('#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2]))
    return hex_color

def percentage(dict, total):
    perc = []
    for color in dict:
        perc.append(round(100*dict[color]/total, 4))
    return perc

def total_color(dict):
    sum = 0
    for color in dict:
        sum += dict[color]
    return sum

def main(file_name):
    file = file_name
    colors_rgb = get_data(file)
    total_all_color = total_color(colors_rgb)
    top_10 = get_top_10(colors_rgb)
    hex_list = rgb_to_hex(top_10)
    percentage_list = percentage(top_10, total_all_color)
    return hex_list, percentage_list
