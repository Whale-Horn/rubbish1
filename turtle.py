import turtle 
#绘图窗口类的定义
class Win:
    def __init__(self):    #构造函数    
        turtle.TurtleScreen._RUNNING=True#spyder运行turtle库有兼容性问题，此语句可以解决
        turtle.screensize(800,600)#绘图窗口大小
        turtle.title('hello')#绘图窗口标题
    def create(self):
        bob = turtle.Turtle()#定义绘图对象
        return bob
    def finish(self):
        turtle.done()#绘制结束
#画线笔类的定义
class Line:
    count=0#类属性，用于计算已绘制线条的数量
    def __init__(self,bob,color):
        self.__pos=[0,0]#实例属性，笔的坐标
        self.__long=0#实例属性，线条长度
        self.pen=bob#实例属性，其值为一个绘图对象
        self.color=color#实例属性，笔的颜色
        self.pen.penup()#抬起画笔，此时移动画笔，不会绘制图形
        self.pen.color(self.color,'red')#绘制的线条颜色和画笔颜色
        self.pen.goto(self.__pos[0],self.__pos[1])#画笔初始坐标
        self.pen.pendown()#按下画笔，准备绘制图形
    #类方法，返回已绘制线条的数量
    @classmethod
    def get_total(cls):
        t = cls.count
        return t

     #静态方法，计算面积并返回
    @staticmethod
    def get_area(longth,width=None):
        #接受一个参数，计算正方形面积
        if width is None:
            s = longth * longth
            return s
        #接受两个参数，计算矩形面积
        else:
            s= longth * width
            return s
    #实例方法，返回当前坐标
    def getpos(self):
        return self.__pos
    #实例方法，返回线条长度
    def getlong(self):
        return self.__long
    #实例方法，设置当前坐标
    def setpos(self,pos):
        self.__pos=pos
        self.pen.goto(pos[0],pos[1])
     #实例方法，绘制一个长度为step的垂直向上的线条   
    def up(self,step):
        self.__pos[1]=self.__pos[1]+step
        self.pen.goto(self.__pos[0],self.__pos[1])
        Line.count+=1
        self.__long+=step
     #实例方法，绘制一个长度为step的垂直向下的线条    
    def down(self,step):
        self.__pos[1]=self.__pos[1]-step
        self.pen.goto(self.__pos[0],self.__pos[1])
        Line.count+=1
        self.__long+=step
     #实例方法，绘制一个长度为step的水平向左的线条    
    def left(self,step):
        self.__pos[0]=self.__pos[0]+step
        self.pen.goto(self.__pos[0],self.__pos[1])
        Line.count+=1
        self.__long+=step
      #实例方法，绘制一个长度为step的水平向右的线条    
    def right(self,step):
        self.__pos[0]=self.__pos[0]-step
        self.pen.goto(self.__pos[0],self.__pos[1])
        Line.count+=1
        self.__long+=step
    #实例方法，抬起笔  ，此时移动画笔也不产生线条
    def disable(self):
        self.pen.penup()#抬起画笔
      #实例方法，按下笔  ，此时移动画笔产生线条
    def enable(self):
        self.pen.pendown()#按下画笔，绘制图形
    # 实例方法，绘制一个正方形，边长是step   
    def draw_square(self,step):
        self.left(step)
        self.up(step)
        self.right(step)
        self.down(step)
    # 实例方法，绘制一个矩形，长为longth，宽为width   
    def draw_rectangle(self,longth,width):
        self.left(longth)
        self.up(width)
        self.right(longth)
        self.down(width)
        #实例方法，输出字符串到绘图窗口
    def out_info(self,msg,pos):
        self.disable()#抬起笔  
        c=self.color#暂存画笔原来颜色
        self.pen.color("black") #设置画笔为黑色     
        self.setpos(pos)#移动画笔，到打印文字的坐标处
        #输出信息
        bob.write(msg, move=False, align='left', font=('宋体', 12, 'normal'))       
        self.pen.color(c)#恢复画笔颜色
#main
w1=Win()#基于绘图窗口类创建一个绘图窗口实例(对象)
bob=w1.create()#调用对象的方法，创建绘图对象

step=200#设置线条长度
line1=Line(bob,"red")#基于画线笔类创建一个画笔实例(对象)并设置线条颜色
#调用对象的方法，绘制正方形
line1.draw_square(step)
#调用对象的属性，创建输出字符串
pos=line1.getpos()
long=line1.getlong()
target_word=f"1：画笔1的当前坐标是{pos},线条长度是{long}"
line1.out_info(target_word,[-300,350])#在指定坐标输出字符串

#如果继续绘制正方形，需要重新打印一个起点坐标
#用对象的方法，设置一个新坐标，并移动画笔到此处
line1.setpos([0,-350])
line1.enable()#输出字符串时，是抬笔状态。现在需要按下画笔
line1.draw_square(step)
#调用对象的属性，创建输出字符串，也可以直接嵌入到{ }中
target_word=f"2:画笔1的当前坐标是{line1.getpos()},线条长度是{line1.getlong()}"
line1.out_info(target_word,[-300,300])
#基于画线笔类创建一个绿色画笔
line2=Line(bob,"green")#新建的画笔，初始坐标是[0,0],需要新坐标，否则与第一个重叠
line2.disable()#新建的画笔，初始状态是按下的，需要取消
line2.setpos([-300,0])#移动画笔到新坐标
line2.enable()#按下画笔
line2.draw_square(step)
target_word=f"3:画笔2的当前坐标是{line2.getpos()},线条长度是{line2.getlong()}"
line2.out_info(target_word,[-300,250])
#基于画线笔类创建一个蓝色画笔
line3=Line(bob,"blue")
line3.disable()
line3.setpos([-300,-350])
line3.enable()
line3.draw_square(step)
target_word=f"4:画笔3的当前坐标是{line3.getpos()},线条长度是{line3.getlong()}"
line3.out_info(target_word,[-300,200])
#调用类方法和静态方法
target_word=f"画线的数量是{line3.get_total()},正方形的面积是{line3.get_area(step)}"
line3.out_info(target_word,[-300,-100])

longth = 200
width = 80
line4=Line(bob,"orange")
line4.disable()#新建的画笔，初始状态是按下的，需要取消
line4.setpos([-300,-300])#移动画笔到新坐标
line4.enable()#按下画笔
line4.draw_rectangle(longth,width)
target_word=f"5:画笔4的当前坐标是{line4.getpos()},线条长度是{line4.getlong()}"
line4.out_info(target_word,[-300,-350])
w1.finish()
