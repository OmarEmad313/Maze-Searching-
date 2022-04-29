from pyMaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
def heuristicCost(cell1, cell2):
    #manhattan distance
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
    
def aStar(m,startCell=None):
    if startCell is None:
        startCell=(m.rows, m.cols)
    cellPiorityQueue = PriorityQueue()
    cellPiorityQueue.put((heuristicCost(startCell, m._goal), heuristicCost(startCell, m._goal), startCell))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[startCell] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[startCell] = heuristicCost(startCell, m._goal)
    searchPath=[startCell]
    while not cellPiorityQueue.empty():
        currCell = cellPiorityQueue.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + heuristicCost(childCell, m._goal)

                if temp_f_score < f_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + heuristicCost(childCell, m._goal)
                    cellPiorityQueue.put((f_score[childCell], heuristicCost(childCell, m._goal), childCell))


    fwdPath={}
    cell=m._goal
    while cell!=startCell:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze(theme="purple")

    searchPath,aPath,fwdPath= aStar(m)
    a=agent(m,footprints=True,color=COLOR.maroon,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red,shape="arrow")

    m.tracePath({a:searchPath},delay=300)
    m.tracePath({b:aPath},delay=300)
    m.tracePath({c:fwdPath},delay=300)

    l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
    l=textLabel(m,'A Star Search Length',len(searchPath))
    m.run()
