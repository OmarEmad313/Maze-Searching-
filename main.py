import pyMaze,AStar,greedyFirstSearch
m=maze(15,15)
m.CreateMaze(theme='light')
searchPath, aPath, fwdPath = aStar(m)
a = agent(m, footprints=True, color=COLOR.blue, filled=True)
b = agent(m, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))
c = agent(m, footprints=True, color=COLOR.red)

m.tracePath({a: searchPath}, delay=300)
m.tracePath({b: aPath}, delay=300)
m.tracePath({c: fwdPath}, delay=300)

l = textLabel(m, 'A Star Path Length', len(aPath) + 1)
l = textLabel(m, 'A Star Search Length', len(searchPath))
m.run()
