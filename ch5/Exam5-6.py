mg=[[1,1,1,1,1,1],[1,0,1,0,0,1],[1,0,0,1,1,1], \
[1,0,1,0,0,1],[1,0,0,0,0,1],[1,1,1,1,1,1]]
#mg=[[1,1,1,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
dx=[-1,0,1,0]                               #x方向的偏移量
dy=[0,1,0,-1]                               #y方向的偏移量
cnt=0                                       #累计迷宫路径数
def  mgpath(xi,yi,xe,ye,path,d):            #求解迷宫路径为:(xi,yi)->(xe,ye)
    global cnt
    d+=1; path[d]=[xi,yi]                   #将(xi,yi)方块对象添加的路径中
    mg[xi][yi]=-1						    #mg[xi][yi]=-1		
    if xi==xe and yi==ye:				    #找到了出口,输出一个迷宫路径
        cnt+=1
        print("迷宫路径%d: " %(cnt),end='')	#输出第cnt条迷宫路径
        for k in range(d+1):
            print("(%d,%d)" %(path[k][0],path[k][1]),end=' ')
        print()
        mg[xi][yi]=0                        #从出口回退，恢复其mg值
        return
        
    else:								    #(xi,yi)不是出口
        di=0
        while di<4:							#处理(xi,yi)四周的每个相邻方块(i,j)
            i,j=xi+dx[di],yi+dy[di]         #找(xi,yi)的di方位的相邻方块(i,j)
            if mg[i][j]==0:					#若(i,j)可走时
                mgpath(i,j,xe,ye,path,d)    #从(i,j)出发查找迷宫路径
            di+=1							#继续处理(xi,yi)的下一个相邻方块
        mg[xi][yi]=0                        #(xi,yi)的所有相邻方块处理完毕，从其回退，恢复其mg值

#主程序
xi,yi=1,1
xe,ye=4,4
print("[%d,%d]到[%d,%d]的所有的迷宫路径:" %(xi,yi,xe,ye))
path=[None]*100
d=-1
mgpath(xi,yi,xe,ye,path,d)
