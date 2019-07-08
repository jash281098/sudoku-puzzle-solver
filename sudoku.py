
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
s={}
rows=['A','B','C','D','E','F','G','H','I']
cols=['1','2','3','4','5','6','7','8','9']
def cross(r,c):
    return [s+t for s in r for t in c]
row_units=[cross(s,cols) for s in rows]
col_units=[cross(rows,s) for s in cols]
squares=[cross(r,s) for r in ('ABC','DEF','GHI') for s in ('123','456','789')]
boxes=cross(rows,cols)
unitlist = row_units + col_units + squares
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
s=input()


def grid_val(grid):
    entries=[]
    g={}
    all_val="123456789"
    for i in grid:
        if i=='.':
            entries.append(all_val)
        else:
            entries.append(i)
    c=0
    for i in boxes:
        g[i]=entries[c]
        c+=1
    return g
gr=grid_val(s)

def eliminate(grid):
    for i in grid:
        if len(grid[i]) is 1:
            for j in peers[i]:
                    k=grid[j].replace(grid[i],'')
                    grid[j]=k
    return(grid)



def only_choice(gr):
#     t=[0,0,0,0,0,0,0,0,0]
    t={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    print(t)
    c=0
    
    for i in range(1,10):
        for j in squares[i-1]:
            if len(gr[j])==1:
                t[int(gr[j])].append(j)
            else:
                 for k in gr[j]:
                    t[int(k)].append(j)
            
        for n in t:
            if len(t[n])==1:
                gr[t[n][0]]=gr[t[n][0]].replace(gr[t[n][0]],str(n))
        t={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}


def reduce_puzzle(grid):
    stalled=False
    while not stalled:
        values=len([x for x in grid if len(grid[x])==1])
        grid=eliminate(grid)
        print(grid)
        grid=only_choice(grid)
        print(grid)
        after=len([x for x in grid if len(grid[x])==1])
        stalled=values==after
        if len([x for x in grid if len(grid[x])==0]):
            return false
    return grid


gr=reduce_puzzle(gr)