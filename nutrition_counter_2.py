from processing import *

calories = 0
sugar = 0
fat = 0
apple_number = 0
donut_number = 0
banana_number = 0
apple_info = {
    "calories": 100,
    "sugar": 10,
    "fat": 5
}
donut_info = {
    "calories": 200,
    "sugar": 30,
    "fat": 40
}
banana_info = {
    "calories": 80,
    "sugar": 20,
    "fat": 10
}

apple_url = "http://previews.123rf.com/images/chudtsankov/chudtsankov1208/chudtsankov120800002/14670247-Cartoon-Red-Apple-Stock-Vector-fruit.jpg"
donut_url = "http://www.clipartlord.com/wp-content/uploads/2015/08/doughnut9.png"
banana_url = "http://img0.imgtn.bdimg.com/it/u=1946168957,2843989391&fm=21&gp=0.jpg"
#banana_url = "http://cliparts.co/cliparts/ATb/r4d/ATbr4dxpc.png"
class BigButton:
    def __init__(self, x, y,number,im):
        self.x = x
        self.y = y
        self.number = number
        self.im = im
        
    def draw(self):
        image(self.im, self.x, self.y, 85,85)
        #the plus
        stroke(152,152,152)
        fill(126, 212, 33)
        rect(self.x + 95, self.y, 47, 25)
        
        fill(255, 255, 255)
        textSize(20)
        text("+", self.x + 111, self.y + 20)
        # the number
        fill(217, 217, 217)
        rect(self.x + 95, self.y + 30, 47, 25)
        
        fill(0,0,0)
        textSize(20)
        text(str(self.number), self.x + 111, self.y + 50)
        #the minus
        
        fill(244, 167, 49)
        rect(self.x + 95, self.y + 60, 47, 25)
        
        fill(255, 255, 255)
        textSize(20)
        text("-", self.x + 112, self.y + 80)
        
def setup():
    global apple, donut, banana
    apple = requestImage(apple_url)
    donut = requestImage(donut_url)
    banana = requestImage(banana_url)
    
    
def draw():
    size(500, 600)
    background(255,255,255)
    
    calories = apple_number * apple_info["calories"] + donut_number * donut_info["calories"] + banana_number * banana_info["calories"]
    sugar = apple_number * apple_info["sugar"] + donut_number * donut_info["sugar"] + banana_number * banana_info["sugar"]
    fat = apple_number * apple_info["fat"] + donut_number * donut_info["fat"] + banana_number * banana_info["fat"]
    #calories
    fill(0, 0, 0)
    textSize(20)
    text("Calories: " + str(calories), 25, 35);
    # sugar
    fill(0, 0, 0)
    textSize(20)
    text("Sugar: " + str(sugar), 190, 35);
    
    # fat
    fill(0, 0, 0)
    textSize(20)
    text("Fat: " + str(fat), 320, 35);
    # The line
    fill(0,0,0)
    rect(0, 40, 600, 2)
    
    #reset key
    stroke(152,152,152)
    fill(74,144,227)
    rect(443, 11, 47,24)
    fill(255,255,255)
    text("reset", 445, 32)
    
    
    # apple part
    apple_im = BigButton(8,60, apple_number, apple)
    apple_im.draw()
    
    #donut part
    donut_im = BigButton(178,60, donut_number, donut)
    donut_im.draw()
    
    #banana part
    banana_im = BigButton(348,60, banana_number, banana)
    banana_im.draw()
    
# when the mouse is pressed    
def mousePressed():
    global apple_number, donut_number, banana_number
    currx = mouse.x
    curry = mouse.y
    if mouse.button == 37:
        if curry <= 85 and curry >= 60:
            if currx <= 150 and currx >= 103:
                apple_number += 1
            elif currx <= 320 and currx >= 273:
                donut_number += 1
            elif currx <= 490 and currx >= 443:
                banana_number += 1
        elif curry <= 145 and curry >= 120:
            if currx <= 150 and currx >= 103 and apple_number > 0:
                apple_number -= 1
            elif currx <= 320 and currx >= 273 and donut_number > 0:
                donut_number -= 1
            elif currx <= 490 and currx >= 443 and banana_number > 0:
                banana_number -= 1
        elif currx >= 443 and currx <= 490 and curry >= 12 and curry <= 37:
            apple_number = 0
            donut_number = 0
            banana_number = 0
            
            
    
run()