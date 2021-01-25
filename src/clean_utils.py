
def cleaning(string):
    words = ["usa","australia","south africa"]
    for w in words:
        if w in str(string).lower(): 
            return w.upper()
    else:
         return "other"

def contains(string):
    words = ["tiger","brown","blue","black", "large", "dog", "grey", "sand", "small", "zambesi", "wobbegong","lemon","hammerhead","carpet","white", "raggedtooth","bronze","spinner", "Whale","threser","mako","bull","nurse","silky","reef"]
    for w in words: 
        if w in string.lower(): 
            return w
    else:
         return "others"

