import vtk
import numpy as np
import gmsh
from math import pi, sin, cos
import os


class CalcMesh:

    def __init__(self, nodes_coords, tetrs_points):
        self.nodes = np.array([nodes_coords[0::3],nodes_coords[1::3],nodes_coords[2::3]])
        self.size = int(len(nodes_coords) / 3)

        self.smth = [0] * self.size

        self.velocity = np.zeros(shape=(3, self.size), dtype=np.double)

        self.tetrs = np.array([tetrs_points[0::4],tetrs_points[1::4],tetrs_points[2::4],tetrs_points[3::4]])
        self.tetrs -= 1

    def move(self, t, tau):
        p = 0.5
        w = 2 * pi / p

        h = 40
        c = h * sin(w * t) + h / 2
        for i in range(self.size):
            self.smth[i] = 300 * (self.nodes[2][i] - c) ** 2

        v = 10
        a = (pi / 4) * sin(w * t)
        ex = -110
        ey = 75
        ez = 14
        spy = []
        spz = []
        for i in range(self.size):
            if self.nodes[2][i] <= ez:
                if (self.nodes[0][i] <= ex and self.nodes[1][i] <= ey) or \
                        (self.nodes[0][i] >= ex and self.nodes[1][i] >= ey):
                    spy.append(-v * cos(w * t) * cos(a) * (ez - self.nodes[2][i]))
                    spz.append(v * cos(w * t) * sin(a) * (ez - self.nodes[2][i]))
                elif (self.nodes[0][i] <= ex and self.nodes[1][i] >= ey) or \
                          (self.nodes[0][i] >= ex and self.nodes[1][i] <= ey):
                    spy.append(v * cos(w * t) * cos(a) * (ez - self.nodes[2][i]))
                    spz.append(v * cos(w * t) * sin(a) * (ez - self.nodes[2][i]))
            else:
                spy.append(0)
                spz.append(0)
        self.velocity[1] = spy
        self.velocity[2] = spz
        self.nodes += self.velocity * tau

    def snapshot(self, snap_number):
        unstructuredGrid = vtk.vtkUnstructuredGrid()
        points = vtk.vtkPoints()

        smth = vtk.vtkDoubleArray()
        smth.SetName("smth")

        vel = vtk.vtkDoubleArray()
        vel.SetNumberOfComponents(3)
        vel.SetName("vel")

        for i in range(0, len(self.nodes[0])):
            points.InsertNextPoint(self.nodes[0,i], self.nodes[1,i], self.nodes[2,i])
            smth.InsertNextValue(self.smth[i])
            vel.InsertNextTuple((self.velocity[0,i], self.velocity[1,i], self.velocity[2,i]))

        unstructuredGrid.SetPoints(points)

        unstructuredGrid.GetPointData().AddArray(smth)
        unstructuredGrid.GetPointData().AddArray(vel)

        for i in range(0, len(self.tetrs[0])):
            tetr = vtk.vtkTetra()
            for j in range(0, 4):
                tetr.GetPointIds().SetId(j, self.tetrs[j,i])
            unstructuredGrid.InsertNextCell(tetr.GetCellType(), tetr.GetPointIds())

        writer = vtk.vtkXMLUnstructuredGridWriter()
        writer.SetInputDataObject(unstructuredGrid)
        writer.SetFileName("pig3d-step-" + str(snap_number) + ".vtu")
        writer.Write()


gmsh.initialize()

try:
    path = os.path.dirname(os.path.abspath(__file__))
    gmsh.merge(os.path.join(path, 'minecraft_pig.stl'))
except:
    print("Could not load STL mesh: bye!")
    gmsh.finalize()
    exit(-1)

angle = 40
forceParametrizablePatches = False
includeBoundary = True
curveAngle = 180
gmsh.model.mesh.classifySurfaces(angle * pi / 180., includeBoundary, forceParametrizablePatches, curveAngle * pi / 180.)
gmsh.model.mesh.createGeometry()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

f = gmsh.model.mesh.field.add("MathEval")
gmsh.model.mesh.field.setString(f, "F", "4")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(3)

nodeTags, nodesCoord, parametricCoord = gmsh.model.mesh.getNodes()

GMSH_TETR_CODE = 4
tetrsNodesTags = None
elementTypes, elementTags, elementNodeTags = gmsh.model.mesh.getElements()
for i in range(0, len(elementTypes)):
    if elementTypes[i] != GMSH_TETR_CODE:
        continue
    tetrsNodesTags = elementNodeTags[i]

if tetrsNodesTags is None:
    print("Can not find tetra data. Exiting.")
    gmsh.finalize()
    exit(-2)

print("The model has %d nodes and %d tetrs" % (len(nodeTags), len(tetrsNodesTags) / 4))

for i in range(0, len(nodeTags)):
    assert (i == nodeTags[i] - 1)
assert(len(tetrsNodesTags) % 4 == 0)


mesh = CalcMesh(nodesCoord, tetrsNodesTags)
mesh.snapshot(0)

gmsh.finalize()

tau = 0.01
t = 0

for i in range(1, 100):
    mesh.move(t, tau)
    t += tau
    mesh.snapshot(i)