# Agnes Agersborg (agnes.agersborg@nmbu.no), Truls de Lange (truls.de.lange@nmbu.no)

import meshio

def read_mesh(msh_name):
    msh = meshio.read(msh_name)
    points = msh.points
    cells = msh.cells

    return points, cells

if __name__ == "__main__":
    msh_name = 'simple.msh'
    points, cells = read_mesh(msh_name)

    cell = cells[1].data[222]
    print (cell)
    print (cells[1].type)

