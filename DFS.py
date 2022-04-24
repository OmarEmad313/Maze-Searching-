
from pyMaze import maze,agent,textLabel,COLOR
def DFS(m,startCell=None):
    if startCell is None:
        startCell=(m.rows, m.cols)
    explored=[startCell]
    frontier=[startCell]
    dfsPath={}
    dfsSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dfsSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    childCell=(currCell[0], currCell[1] + 1)
                if d =='W':
                    childCell=(currCell[0], currCell[1] - 1)
                if d =='N':
                    childCell=(currCell[0] - 1, currCell[1])
                if d =='S':
                    childCell=(currCell[0] + 1, currCell[1])
                if childCell in explored:
                    continue
                poss+=1
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=startCell:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dfsSeacrh, dfsPath, fwdPath

if __name__=='__main__':
    m = maze(12, 10)
    m.CreateMaze(5, 4, loopPercent=10, theme='purple')
    dfsSearch, dfsPath, fwdPath = DFS(m)
    a = agent(m, footprints=True, color=COLOR.maroon, shape='square', filled=True)
    b = agent(m, footprints=True, color=COLOR.yellow, filled=False, shape="arrow")
    c = agent(m, 5, 4, footprints=True, color=COLOR.red, shape='square', filled=True, goal=(m.rows, m.cols))
    m.tracePath({a: dfsSearch}, delay=100)
    m.tracePath({c: dfsPath}, delay=100)
    m.tracePath({b: fwdPath}, delay=100)
    l = textLabel(m, 'DFS path Length', len(dfsPath) + 1)
    l = textLabel(m, 'DFS search length', len(dfsSearch))
    m.run()