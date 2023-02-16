import gmsh
import sys

gmsh.initialize()

gmsh.model.add("tt1")

lc = 3e-2

gmsh.model.geo.addPoint(0, 0, -0.2, lc, 1)
gmsh.model.geo.addPoint(0, 0, -0.1, lc, 2)
gmsh.model.geo.addPoint(0, 0, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0, 0.1, lc, 4)
gmsh.model.geo.addPoint(0, 0, 0.2, lc, 5)


gmsh.model.geo.addPoint(0.3, 0, 0, lc, 6)

gmsh.model.geo.addPoint(0.4, 0, 0, lc, 7)
gmsh.model.geo.addPoint(0.3, 0, 0.1, lc, 8)
gmsh.model.geo.addPoint(0.2, 0, 0, lc, 9)
gmsh.model.geo.addPoint(0.3, 0, -0.1, lc, 10)

gmsh.model.geo.addPoint(0.5, 0, 0, lc, 16)
gmsh.model.geo.addPoint(0.3, 0, 0.2, lc, 17)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 18)
gmsh.model.geo.addPoint(0.3, 0, -0.2, lc, 19)


gmsh.model.geo.addPoint(0, 0.3, 0, lc, 11)

gmsh.model.geo.addPoint(0, 0.4, 0, lc, 12)
gmsh.model.geo.addPoint(0, 0.3, 0.1, lc, 13)
gmsh.model.geo.addPoint(0, 0.2, 0, lc, 14)
gmsh.model.geo.addPoint(0, 0.3, -0.1, lc, 15)

gmsh.model.geo.addPoint(0, 0.5, 0, lc, 20)
gmsh.model.geo.addPoint(0, 0.3, 0.2, lc, 21)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 22)
gmsh.model.geo.addPoint(0, 0.3, -0.2, lc, 23)


gmsh.model.geo.addPoint(-0.3, 0, 0, lc, 24)

gmsh.model.geo.addPoint(-0.4, 0, 0, lc, 25)
gmsh.model.geo.addPoint(-0.3, 0, 0.1, lc, 26)
gmsh.model.geo.addPoint(-0.2, 0, 0, lc, 27)
gmsh.model.geo.addPoint(-0.3, 0, -0.1, lc, 28)

gmsh.model.geo.addPoint(-0.5, 0, 0, lc, 29)
gmsh.model.geo.addPoint(-0.3, 0, 0.2, lc, 30)
gmsh.model.geo.addPoint(-0.1, 0, 0, lc, 31)
gmsh.model.geo.addPoint(-0.3, 0, -0.2, lc, 32)


gmsh.model.geo.addPoint(0, -0.3, 0, lc, 33)

gmsh.model.geo.addPoint(0, -0.4, 0, lc, 34)
gmsh.model.geo.addPoint(0, -0.3, 0.1, lc, 35)
gmsh.model.geo.addPoint(0, -0.2, 0, lc, 36)
gmsh.model.geo.addPoint(0, -0.3, -0.1, lc, 37)

gmsh.model.geo.addPoint(0, -0.5, 0, lc, 38)
gmsh.model.geo.addPoint(0, -0.3, 0.2, lc, 39)
gmsh.model.geo.addPoint(0, -0.1, 0, lc, 40)
gmsh.model.geo.addPoint(0, -0.3, -0.2, lc, 41)


gmsh.model.geo.addCircleArc(7, 6, 8, 1)
gmsh.model.geo.addCircleArc(8, 6, 9, 2)
gmsh.model.geo.addCircleArc(9, 6, 10, 3)
gmsh.model.geo.addCircleArc(10, 6, 7, 4)

gmsh.model.geo.addCircleArc(16, 6, 17, 5)
gmsh.model.geo.addCircleArc(17, 6, 18, 6)
gmsh.model.geo.addCircleArc(18, 6, 19, 7)
gmsh.model.geo.addCircleArc(19, 6, 16, 8)


gmsh.model.geo.addCircleArc(12, 11, 13, 9)
gmsh.model.geo.addCircleArc(13, 11, 14, 10)
gmsh.model.geo.addCircleArc(14, 11, 15, 11)
gmsh.model.geo.addCircleArc(15, 11, 12, 12)

gmsh.model.geo.addCircleArc(20, 11, 21, 13)
gmsh.model.geo.addCircleArc(21, 11, 22, 14)
gmsh.model.geo.addCircleArc(22, 11, 23, 15)
gmsh.model.geo.addCircleArc(23, 11, 20, 16)


gmsh.model.geo.addCircleArc(7, 3, 12, 17)
gmsh.model.geo.addCircleArc(8, 4, 13, 18)
gmsh.model.geo.addCircleArc(9, 3, 14, 19)
gmsh.model.geo.addCircleArc(10, 2, 15, 20)


gmsh.model.geo.addCurveLoop([17, 9, -18, -1], 5)
gmsh.model.geo.addSurfaceFilling([5], 3)

gmsh.model.geo.addCurveLoop([18, 10, -19, -2], 6)
gmsh.model.geo.addSurfaceFilling([6], 4)

gmsh.model.geo.addCurveLoop([19, 11, -20, -3], 7)
gmsh.model.geo.addSurfaceFilling([7], 5)

gmsh.model.geo.addCurveLoop([20, 12, -17, -4], 8)
gmsh.model.geo.addSurfaceFilling([8], 6)


gmsh.model.geo.addCircleArc(16, 3, 20, 21)
gmsh.model.geo.addCircleArc(17, 5, 21, 22)
gmsh.model.geo.addCircleArc(18, 3, 22, 23)
gmsh.model.geo.addCircleArc(19, 1, 23, 24)


gmsh.model.geo.addCurveLoop([21, 13, -22, -5], 9)
gmsh.model.geo.addSurfaceFilling([9], 7)

gmsh.model.geo.addCurveLoop([22, 14, -23, -6], 10)
gmsh.model.geo.addSurfaceFilling([10], 8)

gmsh.model.geo.addCurveLoop([23, 15, -24, -7], 11)
gmsh.model.geo.addSurfaceFilling([11], 9)

gmsh.model.geo.addCurveLoop([24, 16, -21, -8], 12)
gmsh.model.geo.addSurfaceFilling([12], 10)


gmsh.model.geo.addCircleArc(25, 24, 26, 25)
gmsh.model.geo.addCircleArc(26, 24, 27, 26)
gmsh.model.geo.addCircleArc(27, 24, 28, 27)
gmsh.model.geo.addCircleArc(28, 24, 25, 28)

gmsh.model.geo.addCircleArc(29, 24, 30, 29)
gmsh.model.geo.addCircleArc(30, 24, 31, 30)
gmsh.model.geo.addCircleArc(31, 24, 32, 31)
gmsh.model.geo.addCircleArc(32, 24, 29, 32)


gmsh.model.geo.addCircleArc(12, 3, 25, 33)
gmsh.model.geo.addCircleArc(13, 4, 26, 34)
gmsh.model.geo.addCircleArc(14, 3, 27, 35)
gmsh.model.geo.addCircleArc(15, 2, 28, 36)


gmsh.model.geo.addCurveLoop([9, 34, -25, -33], 13)
gmsh.model.geo.addSurfaceFilling([13], 11)

gmsh.model.geo.addCurveLoop([10, 35, -26, -34], 14)
gmsh.model.geo.addSurfaceFilling([14], 12)

gmsh.model.geo.addCurveLoop([11, 36, -27, -35], 15)
gmsh.model.geo.addSurfaceFilling([15], 13)

gmsh.model.geo.addCurveLoop([12, 33, -28, -36], 16)
gmsh.model.geo.addSurfaceFilling([16], 14)


gmsh.model.geo.addCircleArc(20, 3, 29, 37)
gmsh.model.geo.addCircleArc(21, 5, 30, 38)
gmsh.model.geo.addCircleArc(22, 3, 31, 39)
gmsh.model.geo.addCircleArc(23, 1, 32, 40)


gmsh.model.geo.addCurveLoop([13, 38, -29, -37], 17)
gmsh.model.geo.addSurfaceFilling([17], 15)

gmsh.model.geo.addCurveLoop([14, 39, -30, -38], 18)
gmsh.model.geo.addSurfaceFilling([18], 16)

gmsh.model.geo.addCurveLoop([15, 40, -31, -39], 19)
gmsh.model.geo.addSurfaceFilling([19], 17)

gmsh.model.geo.addCurveLoop([16, 37, -32, -40], 20)
gmsh.model.geo.addSurfaceFilling([20], 18)


gmsh.model.geo.addCircleArc(34, 33, 35, 44)
gmsh.model.geo.addCircleArc(35, 33, 36, 45)
gmsh.model.geo.addCircleArc(36, 33, 37, 46)
gmsh.model.geo.addCircleArc(37, 33, 34, 47)

gmsh.model.geo.addCircleArc(38, 33, 39, 48)
gmsh.model.geo.addCircleArc(39, 33, 40, 49)
gmsh.model.geo.addCircleArc(40, 33, 41, 50)
gmsh.model.geo.addCircleArc(41, 33, 38, 51)


gmsh.model.geo.addCircleArc(25, 3, 34, 52)
gmsh.model.geo.addCircleArc(26, 4, 35, 53)
gmsh.model.geo.addCircleArc(27, 3, 36, 54)
gmsh.model.geo.addCircleArc(28, 2, 37, 55)


gmsh.model.geo.addCurveLoop([25, 53, -44, -52], 21)
gmsh.model.geo.addSurfaceFilling([21], 19)

gmsh.model.geo.addCurveLoop([26, 54, -45, -53], 22)
gmsh.model.geo.addSurfaceFilling([22], 20)

gmsh.model.geo.addCurveLoop([27, 55, -46, -54], 23)
gmsh.model.geo.addSurfaceFilling([23], 21)

gmsh.model.geo.addCurveLoop([28, 52, -47, -55], 24)
gmsh.model.geo.addSurfaceFilling([24], 22)


gmsh.model.geo.addCircleArc(29, 3, 38, 56)
gmsh.model.geo.addCircleArc(30, 5, 39, 57)
gmsh.model.geo.addCircleArc(31, 3, 40, 58)
gmsh.model.geo.addCircleArc(32, 1, 41, 59)


gmsh.model.geo.addCurveLoop([29, 57, -48, -56], 25)
gmsh.model.geo.addSurfaceFilling([25], 23)

gmsh.model.geo.addCurveLoop([30, 58, -49, -57], 26)
gmsh.model.geo.addSurfaceFilling([26], 24)

gmsh.model.geo.addCurveLoop([31, 59, -50, -58], 27)
gmsh.model.geo.addSurfaceFilling([27], 25)

gmsh.model.geo.addCurveLoop([32, 56, -51, -59], 28)
gmsh.model.geo.addSurfaceFilling([28], 26)


gmsh.model.geo.addCircleArc(34, 3, 7, 60)
gmsh.model.geo.addCircleArc(35, 4, 8, 61)
gmsh.model.geo.addCircleArc(36, 3, 9, 62)
gmsh.model.geo.addCircleArc(37, 2, 10, 63)


gmsh.model.geo.addCurveLoop([44, 61, -1, -60], 29)
gmsh.model.geo.addSurfaceFilling([29], 27)

gmsh.model.geo.addCurveLoop([45, 62, -2, -61], 30)
gmsh.model.geo.addSurfaceFilling([30], 28)

gmsh.model.geo.addCurveLoop([46, 63, -3, -62], 31)
gmsh.model.geo.addSurfaceFilling([31], 29)

gmsh.model.geo.addCurveLoop([47, 60, -4, -63], 32)
gmsh.model.geo.addSurfaceFilling([32], 30)


gmsh.model.geo.addCircleArc(38, 3, 16, 64)
gmsh.model.geo.addCircleArc(39, 5, 17, 65)
gmsh.model.geo.addCircleArc(40, 3, 18, 66)
gmsh.model.geo.addCircleArc(41, 1, 19, 67)


gmsh.model.geo.addCurveLoop([48, 65, -5, -64], 33)
gmsh.model.geo.addSurfaceFilling([33], 31)

gmsh.model.geo.addCurveLoop([49, 66, -6, -65], 34)
gmsh.model.geo.addSurfaceFilling([34], 32)

gmsh.model.geo.addCurveLoop([50, 67, -7, -66], 35)
gmsh.model.geo.addSurfaceFilling([35], 33)

gmsh.model.geo.addCurveLoop([51, 64, -8, -67], 36)
gmsh.model.geo.addSurfaceFilling([36], 34)


l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(2, 34)])
gmsh.model.geo.addVolume([l])


gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("tt1.msh")
gmsh.write("tt1.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

