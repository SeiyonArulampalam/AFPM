import gmsh
import sys
from utils import orientation

gmsh.initialize()
gmsh.model.add("inner_rotor")
lc = 1e-1

# Dimensions
L = 10.0
Lm = 0.5
Ls = (L - 10 * Lm) / 10  # space between magnets
t = 1.0  # Thickness of the rotor back iron
tm = 1.0  # Thickness of the magnet
t_ag = 2  # airgap thickness

# Magnet 1
start = 0.5 * Ls
gmsh.model.geo.addPoint(0.0, -t, 0, lc, 1)
gmsh.model.geo.addPoint(start, -t, 0, lc, 2)
gmsh.model.geo.addPoint(start + Lm, -t, 0, lc, 3)
gmsh.model.geo.addPoint(start + Lm + Ls, -t, 0, lc, 4)
gmsh.model.geo.addPoint(start + 2 * Lm + Ls, -t, 0, lc, 5)
gmsh.model.geo.addPoint(start + 2 * Lm + 2 * Ls, -t, 0, lc, 6)
gmsh.model.geo.addPoint(start + 3 * Lm + 2 * Ls, -t, 0, lc, 7)
gmsh.model.geo.addPoint(start + 3 * Lm + 3 * Ls, -t, 0, lc, 8)
gmsh.model.geo.addPoint(start + 4 * Lm + 3 * Ls, -t, 0, lc, 9)
gmsh.model.geo.addPoint(start + 4 * Lm + 4 * Ls, -t, 0, lc, 10)
gmsh.model.geo.addPoint(start + 5 * Lm + 4 * Ls, -t, 0, lc, 11)
gmsh.model.geo.addPoint(start + 5 * Lm + 5 * Ls, -t, 0, lc, 12)
gmsh.model.geo.addPoint(start + 6 * Lm + 5 * Ls, -t, 0, lc, 13)
gmsh.model.geo.addPoint(start + 6 * Lm + 6 * Ls, -t, 0, lc, 14)
gmsh.model.geo.addPoint(start + 7 * Lm + 6 * Ls, -t, 0, lc, 15)
gmsh.model.geo.addPoint(start + 7 * Lm + 7 * Ls, -t, 0, lc, 16)
gmsh.model.geo.addPoint(start + 8 * Lm + 7 * Ls, -t, 0, lc, 17)
gmsh.model.geo.addPoint(start + 8 * Lm + 8 * Ls, -t, 0, lc, 18)
gmsh.model.geo.addPoint(start + 9 * Lm + 8 * Ls, -t, 0, lc, 19)
gmsh.model.geo.addPoint(start + 9 * Lm + 9 * Ls, -t, 0, lc, 20)
gmsh.model.geo.addPoint(start + 10 * Lm + 9 * Ls, -t, 0, lc, 21)
gmsh.model.geo.addPoint(2 * start + 10 * Lm + 9 * Ls, -t, 0, lc, 22)

gmsh.model.geo.addPoint(start, -(t + tm), 0, lc, 23)
gmsh.model.geo.addPoint(start + Lm, -(t + tm), 0, lc, 24)
gmsh.model.geo.addPoint(start + Lm + Ls, -(t + tm), 0, lc, 25)
gmsh.model.geo.addPoint(start + 2 * Lm + Ls, -(t + tm), 0, lc, 26)
gmsh.model.geo.addPoint(start + 2 * Lm + 2 * Ls, -(t + tm), 0, lc, 27)
gmsh.model.geo.addPoint(start + 3 * Lm + 2 * Ls, -(t + tm), 0, lc, 28)
gmsh.model.geo.addPoint(start + 3 * Lm + 3 * Ls, -(t + tm), 0, lc, 29)
gmsh.model.geo.addPoint(start + 4 * Lm + 3 * Ls, -(t + tm), 0, lc, 30)
gmsh.model.geo.addPoint(start + 4 * Lm + 4 * Ls, -(t + tm), 0, lc, 31)
gmsh.model.geo.addPoint(start + 5 * Lm + 4 * Ls, -(t + tm), 0, lc, 32)
gmsh.model.geo.addPoint(start + 5 * Lm + 5 * Ls, -(t + tm), 0, lc, 33)
gmsh.model.geo.addPoint(start + 6 * Lm + 5 * Ls, -(t + tm), 0, lc, 34)
gmsh.model.geo.addPoint(start + 6 * Lm + 6 * Ls, -(t + tm), 0, lc, 35)
gmsh.model.geo.addPoint(start + 7 * Lm + 6 * Ls, -(t + tm), 0, lc, 36)
gmsh.model.geo.addPoint(start + 7 * Lm + 7 * Ls, -(t + tm), 0, lc, 37)
gmsh.model.geo.addPoint(start + 8 * Lm + 7 * Ls, -(t + tm), 0, lc, 38)
gmsh.model.geo.addPoint(start + 8 * Lm + 8 * Ls, -(t + tm), 0, lc, 39)
gmsh.model.geo.addPoint(start + 9 * Lm + 8 * Ls, -(t + tm), 0, lc, 40)
gmsh.model.geo.addPoint(start + 9 * Lm + 9 * Ls, -(t + tm), 0, lc, 41)
gmsh.model.geo.addPoint(start + 10 * Lm + 9 * Ls, -(t + tm), 0, lc, 42)
gmsh.model.geo.addPoint(L, -(t + 0.5 * t_ag + tm * 0.5), 0, lc, 43)
gmsh.model.geo.addPoint(0, -(t + 0.5 * t_ag + tm * 0.5), 0, lc, 44)
gmsh.model.geo.addPoint(0, 0, 0, lc, 45)
gmsh.model.geo.addPoint(L, 0, 0, lc, 46)


gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 5, 4)
gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(6, 7, 6)
gmsh.model.geo.addLine(7, 8, 7)
gmsh.model.geo.addLine(8, 9, 8)
gmsh.model.geo.addLine(9, 10, 9)
gmsh.model.geo.addLine(10, 11, 10)
gmsh.model.geo.addLine(11, 12, 11)
gmsh.model.geo.addLine(12, 13, 12)
gmsh.model.geo.addLine(13, 14, 13)
gmsh.model.geo.addLine(14, 15, 14)
gmsh.model.geo.addLine(15, 16, 15)
gmsh.model.geo.addLine(16, 17, 16)
gmsh.model.geo.addLine(17, 18, 17)
gmsh.model.geo.addLine(18, 19, 18)
gmsh.model.geo.addLine(19, 20, 19)
gmsh.model.geo.addLine(20, 21, 20)
gmsh.model.geo.addLine(21, 22, 21)
gmsh.model.geo.addLine(21, 42, 22)
gmsh.model.geo.addLine(42, 41, 23)
gmsh.model.geo.addLine(41, 20, 24)
gmsh.model.geo.addLine(19, 40, 25)
gmsh.model.geo.addLine(40, 39, 26)
gmsh.model.geo.addLine(39, 18, 27)
gmsh.model.geo.addLine(17, 38, 28)
gmsh.model.geo.addLine(38, 37, 29)
gmsh.model.geo.addLine(37, 16, 30)
gmsh.model.geo.addLine(15, 36, 31)
gmsh.model.geo.addLine(36, 35, 32)
gmsh.model.geo.addLine(35, 14, 33)
gmsh.model.geo.addLine(13, 34, 34)
gmsh.model.geo.addLine(34, 33, 35)
gmsh.model.geo.addLine(33, 12, 36)
gmsh.model.geo.addLine(11, 32, 37)
gmsh.model.geo.addLine(32, 31, 38)
gmsh.model.geo.addLine(31, 10, 39)
gmsh.model.geo.addLine(9, 30, 40)
gmsh.model.geo.addLine(30, 29, 41)
gmsh.model.geo.addLine(29, 8, 42)
gmsh.model.geo.addLine(7, 28, 43)
gmsh.model.geo.addLine(28, 27, 44)
gmsh.model.geo.addLine(27, 6, 45)
gmsh.model.geo.addLine(5, 26, 46)
gmsh.model.geo.addLine(26, 25, 47)
gmsh.model.geo.addLine(25, 4, 48)
gmsh.model.geo.addLine(3, 24, 49)
gmsh.model.geo.addLine(24, 23, 50)
gmsh.model.geo.addLine(23, 2, 51)
gmsh.model.geo.addLine(22, 43, 52)
gmsh.model.geo.addLine(43, 44, 53)
gmsh.model.geo.addLine(44, 1, 54)
gmsh.model.geo.addLine(1, 45, 55)
gmsh.model.geo.addLine(45, 46, 56)
gmsh.model.geo.addLine(46, 22, 57)

# Back iron curve loop
gmsh.model.geo.addCurveLoop(
    [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        -57,
        -56,
        -55,
    ],
    1,
)

# Magnets
gmsh.model.geo.addCurveLoop([-20, -22, -23, -24], 2)
gmsh.model.geo.addCurveLoop([-18, -25, -26, -27], 3)
gmsh.model.geo.addCurveLoop([-16, -28, -29, -30], 4)
gmsh.model.geo.addCurveLoop([-14, -31, -32, -33], 5)
gmsh.model.geo.addCurveLoop([-12, -34, -35, -36], 6)
gmsh.model.geo.addCurveLoop([-10, -37, -38, -39], 7)
gmsh.model.geo.addCurveLoop([-8, -40, -41, -42], 8)
gmsh.model.geo.addCurveLoop([-6, -43, -44, -45], 9)
gmsh.model.geo.addCurveLoop([-4, -46, -47, -48], 10)
gmsh.model.geo.addCurveLoop([-2, -49, -50, -51], 11)

# Airgap
gmsh.model.geo.addCurveLoop(
    [
        -1,
        51,
        50,
        49,
        -3,
        48,
        47,
        46,
        -5,
        45,
        44,
        43,
        -7,
        42,
        41,
        40,
        -9,
        39,
        38,
        37,
        -11,
        36,
        35,
        34,
        -13,
        33,
        32,
        31,
        -15,
        30,
        29,
        28,
        -17,
        27,
        26,
        25,
        -19,
        24,
        23,
        22,
        -21,
        -52,
        -53,
        -54,
    ],
    12,
)

# Back iron surface
gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)
gmsh.model.geo.addPlaneSurface([3], 3)
gmsh.model.geo.addPlaneSurface([4], 4)
gmsh.model.geo.addPlaneSurface([5], 5)
gmsh.model.geo.addPlaneSurface([6], 6)
gmsh.model.geo.addPlaneSurface([7], 7)
gmsh.model.geo.addPlaneSurface([8], 8)
gmsh.model.geo.addPlaneSurface([9], 9)
gmsh.model.geo.addPlaneSurface([10], 10)
gmsh.model.geo.addPlaneSurface([11], 11)
gmsh.model.geo.addPlaneSurface([12], 12)

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(2)

# Check the areas to make sure elements are not flipped
nodeTags, X, _ = gmsh.model.mesh.getNodes(-1, -1)
elementType = gmsh.model.mesh.getElementType("Triangle", 1)
elemTags, conn = gmsh.model.mesh.getElementsByType(elementType)
orientation.check_areas(X, conn, len(elemTags))

if "-nopopup" not in sys.argv:
    gmsh.fltk.run()
