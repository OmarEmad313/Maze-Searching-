from pyMaze import maze,COLOR,agent,textLabel
from queue import PriorityQueue
def heuristicCost(cell1,cell2):
    #manhattan distance
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2)+abs(y1-y2)
def aStar(inputMaze):
    startCell=(m.rows,m.cols)
    goalCell=(1, 1)
    g_score={cell: float("inf") for cell in m.grid}
    g_score[startCell]=0
    f_score = {cell: float("inf") for cell in m.grid}
    f_score[startCell]=heuristicCost(startCell, goalCell)

    cellPriorityQueue=PriorityQueue()
    cellPriorityQueue.put((heuristicCost(startCell, goalCell) + g_score[startCell], heuristicCost(startCell, goalCell), startCell))
    pathWithReservedArrows = {}
    searchPath=[startCell]
    while not cellPriorityQueue.empty():
        currCell=cellPriorityQueue.get()[2]
        searchPath.append(currCell)
        if currCell==goalCell:
            break
        for direction in 'ESNW':
            if m.maze_map[currCell][direction]==True:
                if direction == 'E':
                    childCell=(currCell[0],currCell[1]+1)
                elif direction == 'S':
                    childCell = (currCell[0]+1, currCell[1] )
                elif direction == 'N':
                    childCell = (currCell[0]-1, currCell[1] )
                elif direction == 'W':
                    childCell = (currCell[0], currCell[1]-1 )

                tempGScore= g_score[currCell] + 1
                tempFScore= tempGScore + heuristicCost(childCell, goalCell)

                if tempFScore < f_score[childCell]:
                 g_score[childCell] = tempGScore
                 f_score[childCell] = tempFScore
                 cellPriorityQueue.put((tempFScore, heuristicCost(childCell, goalCell), childCell))
                 pathWithReservedArrows[childCell] = currCell

    path={}
    cell=goalCell
    while cell!=startCell:
         path[pathWithReservedArrows[cell]]=cell
         cell=pathWithReservedArrows[cell]
    return searchPath,path


m=maze(15,15)
m.CreateMaze(theme='light')
searchPath, aPath= aStar(m)
a = agent(m, footprints=True, color=COLOR.blue, filled=True)
b = agent(m, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))


m.tracePath({a: searchPath}, delay=300)
m.tracePath({b: aPath}, delay=300)

l = textLabel(m, 'A Star Path Length', len(aPath) + 1)
l = textLabel(m, 'A Star Search Length', len(searchPath))
m.run()
