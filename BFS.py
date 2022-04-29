from pyMaze import maze,agent,textLabel,COLOR
from collections import deque

def BFS(m,startCell=None):
    if startCell is None:
     startCell=(m.rows, m.cols)
    frontier = deque()
    frontier.append(startCell)
    Path = {}
    explored = [startCell]
    bfsSearch=[]
    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                Path[childCell] = currCell
                bfsSearch.append(childCell)
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[Path[cell]]=cell
        cell=Path[cell]
    return bfsSearch, Path, fwdPath

if __name__=='__main__':
    m=maze(12,10)
    # m.CreateMaze(5,4,loopPercent=100)
    m.CreateMaze(5,4,loopPercent=10,theme='purple')
    bfsSearch, bfsPath, fwdPath= BFS(m)
    a=agent(m,footprints=True,color=COLOR.maroon,shape='square',filled=True)
    b=agent(m,footprints=True,color=COLOR.yellow,filled=False ,shape="arrow")
    c=agent(m,5,4,footprints=True,color=COLOR.red,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:bfsSearch}, delay=100)
    m.tracePath({c:bfsPath},delay=100)
    m.tracePath({b:fwdPath},delay=100)
    l = textLabel(m, 'BFS path Length', len(bfsPath) + 1)
    l = textLabel(m, 'Bfs search length', len(bfsSearch))
    m.run()