import turtle 
def create():
#这是一个闭包函数，内部嵌套定义的一个函数
    pos=[0,0]#初始坐标
    #计算新坐标
    def go(direction,step):
        new_x=pos[0]+direction[0]*step
        new_y=pos[1]+direction[1]*step
        
        pos[0]=new_x
        pos[1]=new_y
        #返回新坐标
        return pos
    return go
#调用外部函数，返回内部函数对象
player=create()

#定义画笔绘制时移动方向和步长，[1,0]表示沿水平方向向左移动，[0,1]表示沿垂直方向向上移动，
#[-1,0]表示沿水平方向向右移动，[0,-1]表示沿垂直方向向下移动
directions = [[-1, 0], [0, 1], [-1, 0], [0, -1], [-1, 0], [0, -1], [1, 0], [0, -1], [1, 0], [0, 1], [1, 0], [0, 1]]
steps = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,]

# # (--------绘图过程----------)
turtle.TurtleScreen._RUNNING=True#spyder运行turtle库有兼容性问题，此语句可以解决
turtle.screensize(800,600)#绘图窗口大小
turtle.title('hello')#绘图窗口标题

bob = turtle.Turtle()#定义绘图对象
bob.penup()#抬起画笔，此时移动画笔，不会绘制图形
bob.color('green','red')#绘制的线条颜色和画笔颜色
bob.goto(0,0)#画笔初始坐标
bob.pendown()#发下画笔，准备绘制图形
#下列程序的功能：绘制一个矩形
for i in range(12):#矩形有4个线条组成，需要4次循环
    current_pos=player(directions[i],steps[i]).copy()#没有copy()返回的数据是[0,0]
    bob.goto(current_pos[0],current_pos[1])#按新坐标，移动画笔
    target_word=str(current_pos[0])+","+str(current_pos[1])
    bob.color('black')
    bob.write(target_word, move=False, align='left', font=('宋体', 12, 'normal'))
    bob.color('green','red')
turtle.done()#绘制结束
