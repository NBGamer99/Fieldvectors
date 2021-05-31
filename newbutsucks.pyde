arr = []

def setup():
    arrwd = 50
    global arr
    size(1000,1000)
    background(255)
    for i in range(0,width+1,width/arrwd):
        for j in range(0,height+1,height/arrwd):
            arr.append(Arrow(i,j,5))
            
    
    
def draw():
    global arr
    background(255)
    # print(arr)
    for k in range(0,len(arr)):
        fill('#FF841F')
        arr[k].update()
    
    
class Arrow:
        
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
        
    def update(self):
        angle = atan2(mouseY-self.y,mouseX-self.x)
        pushMatrix()
        translate(self.x,self.y)
        rotate(angle)
        beginShape()
        vertex(0,-self.length)
        vertex(5*self.length,-self.length)
        vertex(5*self.length,-3*self.length)
        vertex(9*self.length,0)
        vertex(5*self.length,3*self.length)
        vertex(5*self.length,self.length)
        vertex(0,self.length)
        endShape(CLOSE)
        popMatrix()
    
# def mousePressed():
#     global mX,mY
#     mX = mouseX
#     mY = mouseY
