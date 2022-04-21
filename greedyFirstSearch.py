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
    searchPath=[startCell]
    while not cellPriorityQueue.empty():
        currCell=cellPriorityQueue.get()[1]
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
    return searchPath,path,pathWithReservedArrows



m=maze(30,30)
m.CreateMaze(theme='light',loadMaze="maze--2022-04-20--17-49-46.csv")
searchPath, aPath, fwdPath = aStar(m)
a = agent(m, footprints=True, color=COLOR.blue, filled=True)
b = agent(m, footprints=True, color=COLOR.yellow, filled=True)
c = agent(m, footprints=True, color=COLOR.red)

m.tracePath({a: searchPath}, delay=300)
m.tracePath({b: aPath}, delay=300)
m.tracePath({c: fwdPath}, delay=300)

l = textLabel(m, 'A Star Path Length', len(aPath) + 1)
l = textLabel(m, 'A Star Search Length', len(searchPath))
m.run()
