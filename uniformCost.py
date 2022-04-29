from pyMaze import maze,agent,COLOR,textLabel
def uniformCost(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
            



if __name__=='__main__':
    myMaze=maze(10,10)
    myMaze.CreateMaze(1,4,loopPercent=100,theme='purple',saveMaze=True)
    hurdle1=agent(myMaze, 2, 4, color=COLOR.red)
    hurdle2=agent(myMaze, 5, 6, color=COLOR.red)
    hurdle3=agent(myMaze, 2, 1, color=COLOR.red)
    hurdle4=agent(myMaze, 3, 6, color=COLOR.red)
    hurdle5=agent(myMaze, 4, 5, color=COLOR.red)

    hurdle1.cost=80
    hurdle2.cost=50
    hurdle3.cost=30
    hurdle4.cost=10
    hurdle5.cost=100
    path,c= uniformCost(myMaze, hurdle1, hurdle2, hurdle3, hurdle4, hurdle5, start=(9, 7))
    textLabel(myMaze,'Total UFS PATH',c)
    a=agent(myMaze,9,7,color=COLOR.maroon,shape="arrow",footprints=True)
    myMaze.tracePath({a:path})


    myMaze.run()
