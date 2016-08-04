from processing import *



apple_calorie = 40
apple_fat = 2
apple_sugar = 10
apple_number = 0

donut_calorie = 200
donut_fat = 25
donut_sugar = 27
donut_number = 0

calorie = 0
fat = 0 
sugar = 0





def setup():
    global donut, apple
    size(700, 700)
    background(255, 255, 255);
    # you may want to change the image url below
    donut = requestImage("http://www.clipartlord.com/wp-content/uploads/2015/08/doughnut9.png")
    apple = requestImage("http://previews.123rf.com/images/chudtsankov/chudtsankov1208/chudtsankov120800002/14670247-Cartoon-Red-Apple-Stock-Vector-fruit.jpg")

      
def draw():
    

    image(apple, 100, 50, 65, 65) 
    stroke(192,192,192)
    fill(192,192, 192)
    rect(97, 125, 100, 35,15)
    textSize(15)
    fill(0, 0, 0)
    text("Apples", 100, 150)
    fill(255, 153, 51)
    rect(150, 130, 40, 25,10)
    fill(255, 255, 255)
    text(str(apple_number), 165, 147)
    
    # text("", 400, 40)
    fill(0, 255, 0)
    rect(200, 55, 50, 20)
    fill(0, 0, 0)
    text("+", 218,70)
    fill(255, 0, 0)
    rect(200,80, 50, 20)
    fill(0, 0, 0)
    text("-", 218,95)
    
    
    image(donut, 100, 160, 65, 65)
    fill(192,192,192)
    rect(97, 225, 100, 35,15)
    textSize(15)
    fill(0, 0, 0)
    text("Donuts", 100, 250)
    fill(255, 153, 51)
    rect(150, 230, 40, 25,10)
    fill(255, 255, 255)
    text(str(donut_number), 165, 247)
    
    
    fill(0, 255, 0)
    rect(200, 165, 50, 20)
    fill(0, 0, 0)
    text("+", 218, 180)
    fill(255, 0, 0)
    rect(200, 195, 50, 20)
    fill(0, 0, 0)
    text("-", 218, 210)
    
    fill(0, 255, 0)
    rect(458, 2, 40, 14)
    fill(0, 0, 0)
    text("clear", 463, 15)
    
    calorie = apple_number * apple_calorie + donut_number * donut_calorie
    fill(192,192,192)
    rect(388, 22, 160, 25,15)
    fill(0,0,0)
    text("Calories", 400, 40)
    fill(255, 153, 51)
    rect(458, 25, 80, 20,10)
    fill(255, 255, 255)
    text(str(calorie), 470,40)
    
    
    sugar = apple_number * apple_sugar + donut_number * donut_sugar
    fill(192,192,192)
    rect(388, 52, 160, 25,15)
    fill(0,0,0)
    text("Sugar", 400, 70)
    fill(255, 153, 51)
    rect(458, 55, 80, 20,10)
    fill(255,255,255)
    text(str(sugar), 470, 70)
    
    
    fat = apple_number * apple_fat + donut_number * donut_fat
    fill(192,192,192)
    rect(388, 82, 160, 25,15)
    fill(0,0,0)
    text("Fat", 400, 100)
    fill(255, 153, 51)
    rect(458,85, 80, 20,10)
    fill(255,255,255)
    text(str(fat), 470, 100)
    
def mousePressed():
    global apple_number, donut_number;
    currx = mouse.x
    curry = mouse.y
    if mouse.button == 37:
        if currx <= 250 and currx >= 200:
            if curry <= 75 and curry >= 55:
                apple_number += 1
            elif curry <= 100 and curry >= 80:
                apple_number -= 1
            elif curry <= 185 and curry >= 165:
                donut_number += 1
            elif curry <= 215 and curry >= 195:
                donut_number -= 1
        elif currx <=498 and currx >= 458 and curry <= 16 and curry >= 2:
            apple_number = 0
            donut_number = 0

run()