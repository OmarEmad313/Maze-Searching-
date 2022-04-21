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
    h_score = {cell: float("inf") for cell in m.grid}
    h_score[startCell]=heuristicCost(startCell, goalCell)

    cellPriorityQueue=PriorityQueue()
    cellPriorityQueue.put( (heuristicCost(startCell, goalCell), startCell))
    pathWithReservedArrows = {}
    while not cellPriorityQueue.empty():
        currCell=cellPriorityQueue.get()[1]
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
                tempHScore=heuristicCost(childCell, goalCell)

                if tempHScore < h_score[childCell]:
                 h_score[childCell] = tempHScore
                 cellPriorityQueue.put((tempHScore, childCell))
                 pathWithReservedArrows[childCell] = currCell

    path={}
    cell=goalCell
    while cell!=startCell:
         path[pathWithReservedArrows[cell]]=cell
         cell=pathWithReservedArrows[cell]
    return path


m=maze(30,30)
m.CreateMaze(theme='light',loopPercent=30,saveMaze=True)
ag=agent(m,footprints=True,color="yellow")
path =aStar(m)
print({ag:path})
m.tracePath({ag:path})
l = textLabel(m, 'A Star Path Length', len(path) + 1)
m.run()
