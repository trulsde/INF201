import meshio

def read_mesh(msh_name):
    msh = meshio.read(msh_name)
    points = msh.points
    cells = msh.cells

    return points, cells

if __name__ == "__main__":
    msh_name = 'simple.msh'
    points, cells = read_mesh(msh_name)

    lines_dict = {}
    triangles_dict = {}

    i = 0
    while i <= 1:
        if i == 0:

            for j in range(69):
                lines_dict[j] = cells[i].data[j]
            i += 1
        else:
            for j in range(418):
                triangles_dict[j] = cells[i].data[j]
            i += 1
    for i in lines_dict:
        print(i, lines_dict[i])

    for i in triangles_dict:
        print(i, triangles_dict[i])

