from pyMaze import maze,agent,COLOR,textLabel
def BFS(m,start,goal):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    child=(currCell[0],currCell[1]+1)
                elif d=='W':
                    child=(currCell[0],currCell[1]-1)
                elif d=='N':
                    child=(currCell[0]-1,currCell[1])
                elif d=='S':
                    child =(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                frontier.append(child)
                explored.append(child)
                bfsPath[child]=currCell
    fwdPath={}
    cell=(3,4)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,5)
    start = (m.rows, m.cols)
    goal = (3,4)
    m.CreateMaze(goal[0],goal[1],theme='purple')

    path=BFS(m,start,goal)

    a=agent(m,footprints=True,filled=True,color=COLOR.maroon)
    m.tracePath({a:path})

    l=textLabel(m,'Length of Shortest Path',len(path)+1)



    m.run()
