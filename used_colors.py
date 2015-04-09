import pygame

colors = {
    "amber": (254, 179, 8, 255),
    "amethyst": (155, 95, 192, 255),
    "apricot": (255, 177, 109, 255),
    "aqua": (19, 234, 201, 255),
    "aquamarine": (4, 216, 178, 255),
    "aubergine": (61, 7, 52, 255),
    "avocado": (144, 177, 52, 255),
    "azure": (6, 154, 243, 255),
    "baby blue": (162, 207, 254, 255),
    "banana": (255, 255, 126, 255),
    "beige": (230, 218, 166, 255),
    "black": (0, 0, 0, 255),
    "blood orange": (254, 75, 3, 255),
    "blood red": (152, 0, 2, 255),
    "blue": (3, 67, 223, 255),
    "blueberry": (70, 65, 150, 255),
    "brick": (160, 54, 35, 255),
    "bright green": (1, 255, 7, 255),
    "bright orange": (255, 91, 0, 255),
    "bright purple": (190, 3, 253, 255),
    "bright red": (255, 0, 0, 255),
    "bright yellow": (255, 253, 1, 255),
    "bronze": (168, 121, 0, 255),
    "brown": (101, 55, 0, 255),
    "bubblegum": (255, 108, 181, 255),
    "burgundy": (97, 0, 35, 255),
    "carnation": (253, 121, 143, 255),
    "cerulean": (4, 133, 209, 255),
    "charcoal": (52, 56, 55, 255),
    "chartreuse": (193, 248, 10, 255),
    "cherry red": (247, 2, 42, 255),
    "chocolate": (61, 28, 2, 255),
    "cinnamon": (172, 79, 6, 255),
    "cobalt blue": (3, 10, 167, 255),
    "coffee": (166, 129, 76, 255),
    "copper": (182, 99, 37, 255),
    "coral": (252, 90, 80, 255),
    "cornflower blue": (81, 112, 215, 255),
    "cream": (255, 255, 194, 255),
    "crimson": (140, 0, 15, 255),
    "cyan": (0, 255, 255, 255),
    "dandelion": (254, 223, 8, 255),
    "dark blue": (0, 3, 91, 255),
    "dark brown": (52, 28, 2, 255),
    "dark green": (3, 53, 0, 255),
    "dark grey": (54, 55, 55, 255),
    "dark orange": (198, 81, 2, 255),
    "dark purple": (53, 6, 62, 255),
    "dark red": (132, 0, 0, 255),
    "dark yellow": (213, 182, 10, 255),
    "denim blue": (59, 91, 146, 255),
    "dull blue": (73, 117, 156, 255),
    "dull green": (116, 166, 98, 255),
    "dull orange": (216, 134, 59, 255),
    "dull purple": (132, 89, 126, 255),
    "eggplant": (56, 8, 53, 255),
    "emerald": (1, 160, 73, 255),
    "forest green": (6, 71, 12, 255),
    "fuchsia": (237, 13, 217, 255),
    "gold": (219, 180, 12, 255),
    "golden rod": (249, 188, 8, 255),
    "grape": (108, 52, 97, 255),
    "grass": (92, 172, 45, 255),
    "green": (21, 176, 26, 255),
    "green yellow": (201, 255, 39, 255),
    "grey": (146, 149, 145, 255),
    "hazel": (142, 118, 24, 255),
    "hot pink": (255, 2, 141, 255),
    "ice blue": (215, 255, 254, 255),
    "indigo": (56, 2, 130, 255),
    "ivory": (255, 255, 203, 255),
    "jade": (31, 167, 116, 255),
    "kelly green": (2, 171, 46, 255),
    "khaki": (170, 166, 98, 255),
    "lavender": (199, 159, 239, 255),
    "lemon": (253, 255, 82, 255),
    "light blue": (149, 208, 252, 255),
    "light brown": (173, 129, 80, 255),
    "light green": (150, 249, 123, 255),
    "light orange": (253, 170, 72, 255),
    "light pink": (255, 209, 223, 255),
    "light purple": (191, 119, 246, 255),
    "light red": (255, 71, 76, 255),
    "light yellow": (255, 254, 122, 255),
    "lime": (170, 255, 50, 255),
    "magenta": (194, 0, 120, 255),
    "mahogany": (74, 1, 0, 255),
    "maize": (244, 208, 84, 255),
    "mango": (255, 166, 43, 255),
    "maroon": (101, 0, 33, 255),
    "mauve": (174, 113, 129, 255),
    "midnight blue": (2, 0, 53, 255),
    "mint": (159, 254, 176, 255),
    "mud": (115, 92, 18, 255),
    "navy": (1, 21, 62, 255),
    "neon blue": (4, 217, 255, 255),
    "neon green": (12, 255, 12, 255),
    "neon pink": (254, 1, 154, 255),
    "neon yellow": (207, 255, 4, 255),
    "olive green": (103, 122, 4, 255),
    "orange": (249, 115, 6, 255),
    "orchid": (200, 117, 196, 255),
    "pale blue": (208, 254, 254, 255),
    "pale green": (199, 253, 181, 255),
    "pale orange": (255, 167, 86, 255),
    "pale pink": (255, 207, 220, 255),
    "pale purple": (183, 144, 212, 255),
    "pale red": (217, 84, 77, 255),
    "pale yellow": (255, 255, 132, 255),
    "pastel blue": (162, 191, 254, 255),
    "pastel green": (176, 255, 157, 255),
    "pastel pink": (255, 186, 205, 255),
    "pastel purple": (202, 160, 255, 255),
    "pastel yellow": (255, 254, 113, 255),
    "peach": (255, 176, 124, 255),
    "periwinkle": (142, 130, 254, 255),
    "pine green": (10, 72, 30, 255),
    "pink": (255, 129, 192, 255),
    "plum": (88, 15, 65, 255),
    "puce": (165, 126, 82, 255),
    "pumpkin": (225, 119, 1, 255),
    "purple": (126, 30, 156, 255),
    "raspberry": (176, 1, 73, 255),
    "red": (229, 0, 0, 255),
    "red orange": (253, 60, 6, 255),
    "red violet": (158, 1, 104, 255),
    "red wine": (140, 0, 52, 255),
    "robin's egg": (109, 237, 253, 255),
    "rose": (207, 98, 117, 255),
    "royal blue": (5, 4, 170, 255),
    "royal purple": (75, 0, 110, 255),
    "ruby": (202, 1, 71, 255),
    "russet": (161, 57, 5, 255),
    "sage": (135, 174, 115, 255),
    "salmon": (255, 121, 108, 255),
    "sand": (226, 202, 118, 255),
    "sapphire": (33, 56, 171, 255),
    "scarlet": (190, 1, 25, 255),
    "sea green": (83, 252, 161, 255),
    "sepia": (152, 94, 43, 255),
    "sienna": (169, 86, 30, 255),
    "silver": (197, 201, 199, 255),
    "sky blue": (117, 187, 253, 255),
    "slate": (81, 101, 114, 255),
    "squash": (242, 171, 21, 255),
    "steel blue": (90, 125, 154, 255),
    "strawberry": (251, 41, 67, 255),
    "sunflower": (255, 197, 18, 255),
    "tan": (209, 178, 111, 255),
    "tangerine": (255, 148, 8, 255),
    "taupe": (185, 162, 129, 255),
    "teal": (2, 147, 134, 255),
    "tomato": (239, 64, 38, 255),
    "turquoise": (6, 194, 172, 255),
    "vermillion": (244, 50, 12, 255),
    "violet": (154, 14, 234, 255),
    "violet red": (165, 0, 85, 255),
    "watermelon": (253, 70, 89, 255),
    "white": (255, 255, 255, 255),
    "yellow": (255, 255, 20, 255)
}

reverse_colors = {
    (0, 0, 0, 255): "black",
    (0, 3, 91, 255): "dark blue",
    (0, 255, 255, 255): "cyan",
    (1, 21, 62, 255): "navy",
    (1, 160, 73, 255): "emerald",
    (1, 255, 7, 255): "bright green",
    (2, 0, 53, 255): "midnight blue",
    (2, 147, 134, 255): "teal",
    (2, 171, 46, 255): "kelly green",
    (3, 10, 167, 255): "cobalt blue",
    (3, 53, 0, 255): "dark green",
    (3, 67, 223, 255): "blue",
    (4, 133, 209, 255): "cerulean",
    (4, 216, 178, 255): "aquamarine",
    (4, 217, 255, 255): "neon blue",
    (5, 4, 170, 255): "royal blue",
    (6, 71, 12, 255): "forest green",
    (6, 154, 243, 255): "azure",
    (6, 194, 172, 255): "turquoise",
    (10, 72, 30, 255): "pine green",
    (12, 255, 12, 255): "neon green",
    (19, 234, 201, 255): "aqua",
    (21, 176, 26, 255): "green",
    (31, 167, 116, 255): "jade",
    (33, 56, 171, 255): "sapphire",
    (52, 28, 2, 255): "dark brown",
    (52, 56, 55, 255): "charcoal",
    (53, 6, 62, 255): "dark purple",
    (54, 55, 55, 255): "dark grey",
    (56, 2, 130, 255): "indigo",
    (56, 8, 53, 255): "eggplant",
    (59, 91, 146, 255): "denim blue",
    (61, 7, 52, 255): "aubergine",
    (61, 28, 2, 255): "chocolate",
    (70, 65, 150, 255): "blueberry",
    (73, 117, 156, 255): "dull blue",
    (74, 1, 0, 255): "mahogany",
    (75, 0, 110, 255): "royal purple",
    (81, 101, 114, 255): "slate",
    (81, 112, 215, 255): "cornflower blue",
    (83, 252, 161, 255): "sea green",
    (88, 15, 65, 255): "plum",
    (90, 125, 154, 255): "steel blue",
    (92, 172, 45, 255): "grass",
    (97, 0, 35, 255): "burgundy",
    (101, 0, 33, 255): "maroon",
    (101, 55, 0, 255): "brown",
    (103, 122, 4, 255): "olive green",
    (108, 52, 97, 255): "grape",
    (109, 237, 253, 255): "robin's egg",
    (115, 92, 18, 255): "mud",
    (116, 166, 98, 255): "dull green",
    (117, 187, 253, 255): "sky blue",
    (126, 30, 156, 255): "purple",
    (132, 0, 0, 255): "dark red",
    (132, 89, 126, 255): "dull purple",
    (135, 174, 115, 255): "sage",
    (140, 0, 15, 255): "crimson",
    (140, 0, 52, 255): "red wine",
    (142, 118, 24, 255): "hazel",
    (142, 130, 254, 255): "periwinkle",
    (144, 177, 52, 255): "avocado",
    (146, 149, 145, 255): "grey",
    (149, 208, 252, 255): "light blue",
    (150, 249, 123, 255): "light green",
    (152, 0, 2, 255): "blood red",
    (152, 94, 43, 255): "sepia",
    (154, 14, 234, 255): "violet",
    (155, 95, 192, 255): "amethyst",
    (158, 1, 104, 255): "red violet",
    (159, 254, 176, 255): "mint",
    (160, 54, 35, 255): "brick",
    (161, 57, 5, 255): "russet",
    (162, 191, 254, 255): "pastel blue",
    (162, 207, 254, 255): "baby blue",
    (165, 0, 85, 255): "violet red",
    (165, 126, 82, 255): "puce",
    (166, 129, 76, 255): "coffee",
    (168, 121, 0, 255): "bronze",
    (169, 86, 30, 255): "sienna",
    (170, 166, 98, 255): "khaki",
    (170, 255, 50, 255): "lime",
    (172, 79, 6, 255): "cinnamon",
    (173, 129, 80, 255): "light brown",
    (174, 113, 129, 255): "mauve",
    (176, 1, 73, 255): "raspberry",
    (176, 255, 157, 255): "pastel green",
    (182, 99, 37, 255): "copper",
    (183, 144, 212, 255): "pale purple",
    (185, 162, 129, 255): "taupe",
    (190, 1, 25, 255): "scarlet",
    (190, 3, 253, 255): "bright purple",
    (191, 119, 246, 255): "light purple",
    (193, 248, 10, 255): "chartreuse",
    (194, 0, 120, 255): "magenta",
    (197, 201, 199, 255): "silver",
    (198, 81, 2, 255): "dark orange",
    (199, 159, 239, 255): "lavender",
    (199, 253, 181, 255): "pale green",
    (200, 117, 196, 255): "orchid",
    (201, 255, 39, 255): "green yellow",
    (202, 1, 71, 255): "ruby",
    (202, 160, 255, 255): "pastel purple",
    (207, 98, 117, 255): "rose",
    (207, 255, 4, 255): "neon yellow",
    (208, 254, 254, 255): "pale blue",
    (209, 178, 111, 255): "tan",
    (213, 182, 10, 255): "dark yellow",
    (215, 255, 254, 255): "ice blue",
    (216, 134, 59, 255): "dull orange",
    (217, 84, 77, 255): "pale red",
    (219, 180, 12, 255): "gold",
    (225, 119, 1, 255): "pumpkin",
    (226, 202, 118, 255): "sand",
    (229, 0, 0, 255): "red",
    (230, 218, 166, 255): "beige",
    (237, 13, 217, 255): "fuchsia",
    (239, 64, 38, 255): "tomato",
    (242, 171, 21, 255): "squash",
    (244, 50, 12, 255): "vermillion",
    (244, 208, 84, 255): "maize",
    (247, 2, 42, 255): "cherry red",
    (249, 115, 6, 255): "orange",
    (249, 188, 8, 255): "golden rod",
    (251, 41, 67, 255): "strawberry",
    (252, 90, 80, 255): "coral",
    (253, 60, 6, 255): "red orange",
    (253, 70, 89, 255): "watermelon",
    (253, 121, 143, 255): "carnation",
    (253, 170, 72, 255): "light orange",
    (253, 255, 82, 255): "lemon",
    (254, 1, 154, 255): "neon pink",
    (254, 75, 3, 255): "blood orange",
    (254, 179, 8, 255): "amber",
    (254, 223, 8, 255): "dandelion",
    (255, 0, 0, 255): "bright red",
    (255, 2, 141, 255): "hot pink",
    (255, 71, 76, 255): "light red",
    (255, 91, 0, 255): "bright orange",
    (255, 108, 181, 255): "bubblegum",
    (255, 121, 108, 255): "salmon",
    (255, 129, 192, 255): "pink",
    (255, 148, 8, 255): "tangerine",
    (255, 166, 43, 255): "mango",
    (255, 167, 86, 255): "pale orange",
    (255, 176, 124, 255): "peach",
    (255, 177, 109, 255): "apricot",
    (255, 186, 205, 255): "pastel pink",
    (255, 197, 18, 255): "sunflower",
    (255, 207, 220, 255): "pale pink",
    (255, 209, 223, 255): "light pink",
    (255, 253, 1, 255): "bright yellow",
    (255, 254, 113, 255): "pastel yellow",
    (255, 254, 122, 255): "light yellow",
    (255, 255, 20, 255): "yellow",
    (255, 255, 126, 255): "banana",
    (255, 255, 132, 255): "pale yellow",
    (255, 255, 194, 255): "cream",
    (255, 255, 203, 255): "ivory",
    (255, 255, 255, 255): "white",
}
