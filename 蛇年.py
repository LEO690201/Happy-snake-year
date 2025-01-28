import pygame
import random
# 初始化 
pygame.init()#调用pygame.init()初始化pygame。
font = pygame.font.SysFont('宋体', 25)#创建字体对象并设置字体样式和大小。
screen = pygame.display.set_mode((360,600))#创建一个800x600的窗口。
screenwidth = screen.get_width() #获取屏幕的宽度和高度。
screenheight = screen.get_height()
surface = pygame.Surface((screenwidth, screenheight), pygame.SRCALPHA)
#创建一个Surface对象用于在屏幕上绘制透明效果。
pygame.Surface.convert(surface)#对Surface对象进行转换和填充颜色。
surface.fill((0, 0, 0, 10)) 
screen.fill((0, 0, 0, 10))#在屏幕上填充黑色背景。
# 内容
#定义一个包含数字和小写字母的列表，用于生成字符对象。
hgl_str=[chr(72), chr(65), chr(80), chr(80), chr(89), chr(32),chr(32), chr(83), chr(78), chr(65), chr(75), chr(69),chr(32),chr(32), chr(89), chr(69), chr(65), chr(82)]#72 65 80 80 89 83 78 65 75 69 89 69 65 82

# 示例
hgl_text = [font.render(hgl_str[i], True, (255, 0, 0) if i < 5 else (0, 255, 0) if i < 13 else (255, 255, 255)) for i in range(len(hgl_str))]       #
#将字符列表中的每个字符渲染为字体对象，并放入一个新的列表中。 
hgl_lst = list(range(99))
while True:#进入循环,不断处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(20)#设置延迟时间为50毫秒，控制字符下落速度。
    screen.blit(surface, (0, 0))#在屏幕上绘制透明背景。
    for i in range(len(hgl_lst)):
                
        screen.blit(hgl_text[i%18], (i * 20, hgl_lst[i] * 20))   # 
        #遍历整数列表，每次循环选择一个随机字符，
        # 并在对应的位置绘制到屏幕上。
        hgl_lst[i] += 1  
        if random.random() < 0.05:
            #以5%的概率将整数列表中的元素重置为0，实现字符重新开始下落的效果。
            hgl_lst[i] = 0
    
    pygame.display.flip() #调用pygame.display.flip()更新屏幕显示。

