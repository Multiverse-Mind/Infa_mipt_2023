import meshio



print("название файла:")
mesh_name = input()

msh = meshio.read(mesh_name)

print(msh.cell_data_dict["gmsh:geometrical"].keys())

tet_data = msh.cell_data_dict["gmsh:geometrical"]["tetra"]
meshio.write(mesh_name+".xdmf",
    meshio.Mesh(points=msh.points,
        cells={"tetra": msh.cells_dict["tetra"]},
        cell_data={"dom_marker": [tet_data]}
    )
)

tri_data = msh.cell_data_dict["gmsh:geometrical"]["triangle"]
meshio.write(mesh_name+"_surf.xdmf",
    meshio.Mesh(points=msh.points,
        cells={"triangle": msh.cells_dict["triangle"]},
        cell_data={"bnd_marker": [tri_data]}
    )
)
