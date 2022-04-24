from pyMaze import maze,COLOR,agent,textLabel
from queue import PriorityQueue
def heuristicCost(cell1,cell2):
    #manhattan distance
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2)+abs(y1-y2)
def aStar(inputMaze,startCell,goalCell):
    h_score={cell: float("inf") for cell in m.grid}
    h_score[startCell]=0
    h2_score = {cell: float("inf") for cell in m.grid}
    h2_score[startCell]=heuristicCost(startCell, goalCell)

    cellPriorityQueue=PriorityQueue()
    cellPriorityQueue.put((heuristicCost(startCell, goalCell) + h_score[startCell], heuristicCost(startCell, goalCell), startCell))
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
                    child =(currCell[0],currCell[1]+1)
                elif direction == 'S':
                    child  = (currCell[0]+1, currCell[1] )
                elif direction == 'N':
                    child = (currCell[0]-1, currCell[1] )
                elif direction == 'W':
                    child = (currCell[0], currCell[1]-1 )

                tempGScore= h_score[currCell] + 1
                tempFScore= tempGScore + heuristicCost(child, goalCell)

                if tempFScore < h2_score[child]:
                 h_score[child] = tempGScore
                 h2_score[child] = tempFScore
                 cellPriorityQueue.put((tempFScore, heuristicCost(child, goalCell), child))
                 pathWithReservedArrows[child] = currCell

    path={}
    cell=goalCell
    while cell!=startCell:
         path[pathWithReservedArrows[cell]]=cell
         cell=pathWithReservedArrows[cell]
    return searchPath,path

m=maze(5,5)
sourceCell=(m.rows,m.cols)
goalCell=(4,4)
m.CreateMaze(goalCell[0],goalCell[1],theme="purple")
searchPath, aPath= aStar(m,sourceCell,goalCell)
a = agent(m, footprints=True, color=COLOR.maroon, filled=True)
b = agent(m, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))



m.tracePath({a: searchPath}, delay=300)
m.tracePath({b: aPath}, delay=300)

l = textLabel(m, 'A Star Path Length', len(aPath) + 1)
l = textLabel(m, 'A Star Search Length', len(searchPath))
m.run()

