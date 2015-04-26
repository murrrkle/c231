def draw(x1,y1,x2,y2,x3,y3,x4,y4,level):
    if level > 0:
        print('polygon',x1,y1,x2,y2,x3,y3,x4,y4)
        xA = (3*x1+x2)/4
        yA = (3*y1+y2)/4
        xB = (3*x2+x3)/4
        yB = (3*y2+y3)/4
        xC = (3*x3+x4)/4
        yC = (3*y3+y4)/4
        xD = (3*x4+x1)/4
        yD = (3*y4+y1)/4
        draw(xA,yA,xB,yB,xC,yC,xD,yD,level-1) 



draw(100,100,500,100,500,500,100,500,10)
