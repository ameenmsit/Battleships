from battleship import EMPTY_CLICKED

def emptyGrid(rows, cols):
    outer=[]
    for i in range(rows):
        inner=[]
        for j in range(cols):
            inner.append(1)
        outer.append(inner)
    return outer

print(emptyGrid(5,5))