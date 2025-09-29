import numpy as np
from utils.parser import InpParser
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import os
import imageio


def plot_region(ax, X, conn_list, color, label=None):
    """
    Plot a region made of triangular elements.

    Parameters:
      ax         : matplotlib axis
      X          : (Nnodes, 3) array of coordinates
      conn_list  : list of connectivity arrays (each is (Ne, 3))
      color      : facecolor for the region
      label      : optional label for legend
    """
    X = X[:, :2]  # Reduce to 2d (x,y coords only)
    polys = []
    for conn in conn_list:
        # Loop through each connectivity in the list
        for tri in conn:
            # Extract the node coordinates for the triangle
            polys.append(X[tri])

    coll = PolyCollection(
        polys, facecolors=color, edgecolors="k", linewidths=0.03, label=label
    )
    ax.add_collection(coll)
    return


def plot_edge(ax, X, node_tags, color, linestyle="-"):
    coords = X[node_tags, :]  # Extract x, y, z coordinates
    ax.plot(coords[:, 0], coords[:, 1], color=color, linewidth=0.5, linestyle=linestyle)
    return


def plot_motor(
    total_length,
    airgap,
    copper_slot_height,
    tooth_tip_thickness,
    bell_width,
    tooth_width,
    magnet_length,
    magnet_thickness,
    back_iron_thickness,
    mesh_refinement,
    npts_airgap,
    slide_number,
):

    # Define the offset for the y coordinates for each mesh
    y_offset1 = 0.5 * copper_slot_height + tooth_tip_thickness + 0.5 * airgap
    y_offset2 = back_iron_thickness + 0.5 * airgap + magnet_thickness
    y_offset = y_offset1 + y_offset2

    # Define the offset to slide the stator mesh to the right
    if slide_number > npts_airgap:
        raise Exception("Slide number excedes npts in airgap")
    slide_offset = (total_length / (npts_airgap - 1)) * slide_number

    # Define the filenames for the mesh
    fname_stator = "stator.inp"
    fname_inner_rotor = "inner_rotor.inp"
    fname_outter_rotor = "outter_rotor.inp"

    # Instance of InpParser for stator, inner rotor, and outter rotor
    parser_stator = InpParser()
    parser_stator.parse_inp(fname_stator)

    parser_inner_rotor = InpParser()
    parser_inner_rotor.parse_inp(fname_inner_rotor)

    parser_outter_rotor = InpParser()
    parser_outter_rotor.parse_inp(fname_outter_rotor)

    # Extract node coords for each mesh
    X_stator = parser_stator.get_nodes()
    X_inner_rotor = parser_inner_rotor.get_nodes()
    X_outter_rotor = parser_outter_rotor.get_nodes()

    # Update the node coordinates for the offset of the outter and inner rotors
    X_inner_rotor[:, 1] -= y_offset
    X_outter_rotor[:, 1] += y_offset

    # Update the node coordinates of the stator to slide to the right
    X_stator[:, 0] += slide_offset

    #################################
    # Stator connectivity information
    #################################
    # Get the connectivity for the slot regions
    # conn_s1 = connectivity of slot 1 surface
    stator_conn_s1 = parser_stator.get_conn("SURFACE1", "CPS3")
    stator_conn_s2 = parser_stator.get_conn("SURFACE2", "CPS3")
    stator_conn_s3 = parser_stator.get_conn("SURFACE3", "CPS3")
    stator_conn_s4 = parser_stator.get_conn("SURFACE4", "CPS3")
    stator_conn_s5 = parser_stator.get_conn("SURFACE5", "CPS3")
    stator_conn_s6 = parser_stator.get_conn("SURFACE6", "CPS3")
    stator_conn_s7 = parser_stator.get_conn("SURFACE7", "CPS3")
    stator_conn_s8 = parser_stator.get_conn("SURFACE8", "CPS3")
    stator_conn_s9 = parser_stator.get_conn("SURFACE9", "CPS3")
    stator_conn_s10 = parser_stator.get_conn("SURFACE10", "CPS3")
    stator_conn_s11 = parser_stator.get_conn("SURFACE11", "CPS3")
    stator_conn_s12 = parser_stator.get_conn("SURFACE12", "CPS3")
    stator_conn_s13 = parser_stator.get_conn("SURFACE13", "CPS3")
    stator_conn_s14 = parser_stator.get_conn("SURFACE14", "CPS3")
    stator_conn_s15 = parser_stator.get_conn("SURFACE15", "CPS3")
    stator_conn_s16 = parser_stator.get_conn("SURFACE16", "CPS3")
    stator_conn_s17 = parser_stator.get_conn("SURFACE17", "CPS3")
    stator_conn_s18 = parser_stator.get_conn("SURFACE18", "CPS3")
    stator_conn_s19 = parser_stator.get_conn("SURFACE19", "CPS3")
    stator_conn_s20 = parser_stator.get_conn("SURFACE20", "CPS3")
    stator_conn_s21 = parser_stator.get_conn("SURFACE21", "CPS3")
    stator_conn_s22 = parser_stator.get_conn("SURFACE22", "CPS3")
    stator_conn_s23 = parser_stator.get_conn("SURFACE23", "CPS3")
    stator_conn_s24 = parser_stator.get_conn("SURFACE24", "CPS3")

    # Stator teeth connectivity
    # conn_t1 = connectivity for tooth 1 surface
    stator_conn_t1 = parser_stator.get_conn("SURFACE25", "CPS3")
    stator_conn_t2 = parser_stator.get_conn("SURFACE26", "CPS3")
    stator_conn_t3 = parser_stator.get_conn("SURFACE27", "CPS3")
    stator_conn_t4 = parser_stator.get_conn("SURFACE28", "CPS3")
    stator_conn_t5 = parser_stator.get_conn("SURFACE29", "CPS3")
    stator_conn_t6 = parser_stator.get_conn("SURFACE30", "CPS3")
    stator_conn_t7 = parser_stator.get_conn("SURFACE31", "CPS3")
    stator_conn_t8 = parser_stator.get_conn("SURFACE32", "CPS3")
    stator_conn_t9 = parser_stator.get_conn("SURFACE33", "CPS3")
    stator_conn_t10 = parser_stator.get_conn("SURFACE34", "CPS3")
    stator_conn_t11 = parser_stator.get_conn("SURFACE35", "CPS3")
    stator_conn_t12 = parser_stator.get_conn("SURFACE36", "CPS3")
    stator_conn_t13 = parser_stator.get_conn("SURFACE37", "CPS3")

    # Airgap connectivity
    stator_conn_ag_inner = parser_stator.get_conn("SURFACE39", "CPS3")
    stator_conn_ag_outter = parser_stator.get_conn("SURFACE38", "CPS3")

    # Line on the left edge of the stator (goes from bottom to top)
    stator_conn_left_edge1 = parser_stator.get_conn("LINE212", "T3D2")
    stator_conn_left_edge2 = parser_stator.get_conn("LINE97", "T3D2")
    stator_conn_left_edge3 = parser_stator.get_conn("LINE211", "T3D2")
    stator_conn_pbc_left = np.concatenate(
        (
            stator_conn_left_edge1.flatten(),
            stator_conn_left_edge2.flatten(),
            stator_conn_left_edge3.flatten(),
        ),
        axis=None,
    )
    # Turn into a single unique list of nodes preserving the order from bottom to top
    stator_pbc_nodes_left = np.array(list(dict.fromkeys(stator_conn_pbc_left)))

    # Line on the right edge of the stator (goes from bottom to top)
    stator_conn_right_edge1 = parser_stator.get_conn("LINE214", "T3D2")
    stator_conn_right_edge2 = parser_stator.get_conn("LINE122", "T3D2")
    stator_conn_right_edge3 = parser_stator.get_conn("LINE210", "T3D2")
    stator_conn_pbc_right = np.concatenate(
        (
            stator_conn_right_edge1.flatten(),
            stator_conn_right_edge2.flatten(),
            stator_conn_right_edge3.flatten(),
        ),
        axis=None,
    )
    # Turn into a single unique list of nodes preserving the order from bottom to top
    stator_pbc_nodes_right = np.array(list(dict.fromkeys(stator_conn_pbc_right)))

    # Line on the top edge of the stator (oriented from left to right)
    stator_conn_top_edge = parser_stator.get_conn("LINE209", "T3D2")
    stator_pbc_nodes_top = np.array(list(dict.fromkeys(stator_conn_top_edge.flatten())))

    # Line on the bottom edge of the stator
    stator_conn_bottom_edge = parser_stator.get_conn("LINE213", "T3D2")
    stator_pbc_nodes_bottom = np.array(
        list(dict.fromkeys(stator_conn_bottom_edge.flatten()))
    )

    #######################################
    # Outter rotor connectivity information
    #######################################
    # Get the connectivity for each of the magnets
    # conn_m1 = connectivity for magnet 1 (starting from far left)
    outter_rotor_conn_m1 = parser_outter_rotor.get_conn("SURFACE11", "CPS3")
    outter_rotor_conn_m2 = parser_outter_rotor.get_conn("SURFACE10", "CPS3")
    outter_rotor_conn_m3 = parser_outter_rotor.get_conn("SURFACE9", "CPS3")
    outter_rotor_conn_m4 = parser_outter_rotor.get_conn("SURFACE8", "CPS3")
    outter_rotor_conn_m5 = parser_outter_rotor.get_conn("SURFACE7", "CPS3")
    outter_rotor_conn_m6 = parser_outter_rotor.get_conn("SURFACE6", "CPS3")
    outter_rotor_conn_m7 = parser_outter_rotor.get_conn("SURFACE5", "CPS3")
    outter_rotor_conn_m8 = parser_outter_rotor.get_conn("SURFACE4", "CPS3")
    outter_rotor_conn_m9 = parser_outter_rotor.get_conn("SURFACE3", "CPS3")
    outter_rotor_conn_m10 = parser_outter_rotor.get_conn("SURFACE2", "CPS3")

    # Get the back iron connectivity
    outter_rotor_conn_back_iron = parser_outter_rotor.get_conn("SURFACE1", "CPS3")

    # Get the airgap connectivity
    outter_rotor_conn_airgap = parser_outter_rotor.get_conn("SURFACE12", "CPS3")

    # Line on the left edge
    outter_rotor_left_edge1 = parser_outter_rotor.get_conn("LINE54", "T3D2")
    outter_rotor_left_edge2 = parser_outter_rotor.get_conn("LINE55", "T3D2")
    outter_rotor_conn_pbc_left = np.concatenate(
        (outter_rotor_left_edge1.flatten(), outter_rotor_left_edge2.flatten()), axis=0
    )

    # Turn into a single unique list of nodes preserving the order from bottom to top
    # Oriented from bottom to top
    outter_rotor_pbc_nodes_left = np.array(
        list(dict.fromkeys(outter_rotor_conn_pbc_left))
    )

    # Line of the right edge
    outter_rotor_right_edge1 = parser_outter_rotor.get_conn("LINE57", "T3D2")
    outter_rotor_right_edge2 = parser_outter_rotor.get_conn("LINE52", "T3D2")
    outter_rotor_conn_pbc_right = np.concatenate(
        (outter_rotor_right_edge1.flatten(), outter_rotor_right_edge2.flatten()), axis=0
    )

    # Turn into a single unique list of nodes preserving the order from bottom to top
    # Oriented from bottom to top
    outter_rotor_pbc_nodes_right = np.array(
        list(dict.fromkeys(outter_rotor_conn_pbc_right))
    )

    # Need to flip to make the orientation from bottom to top
    outter_rotor_pbc_nodes_right = np.flip(outter_rotor_pbc_nodes_right)

    # Line on the top and bottom edges
    outter_rotor_top_edge = parser_outter_rotor.get_conn("LINE56", "T3D2")
    outter_rotor_bottom_edge = parser_outter_rotor.get_conn("LINE53", "T3D2")
    outter_rotor_dirichlet_nodes = np.array(
        list(dict.fromkeys(outter_rotor_top_edge.flatten()))
    )  # Left to right
    outter_rotor_pbc_nodes_bottom = np.array(
        list(dict.fromkeys(outter_rotor_bottom_edge.flatten()))
    )
    outter_rotor_pbc_nodes_bottom = np.flip(outter_rotor_pbc_nodes_bottom)

    ######################################
    # Inner rotor connectivity information
    ######################################
    # Get the connectivity for each of the magnets
    # conn_m1 = connectivity for magnet 1 (starting from far left)
    inner_rotor_conn_m1 = parser_inner_rotor.get_conn("SURFACE11", "CPS3")
    inner_rotor_conn_m2 = parser_inner_rotor.get_conn("SURFACE10", "CPS3")
    inner_rotor_conn_m3 = parser_inner_rotor.get_conn("SURFACE9", "CPS3")
    inner_rotor_conn_m4 = parser_inner_rotor.get_conn("SURFACE8", "CPS3")
    inner_rotor_conn_m5 = parser_inner_rotor.get_conn("SURFACE7", "CPS3")
    inner_rotor_conn_m6 = parser_inner_rotor.get_conn("SURFACE6", "CPS3")
    inner_rotor_conn_m7 = parser_inner_rotor.get_conn("SURFACE5", "CPS3")
    inner_rotor_conn_m8 = parser_inner_rotor.get_conn("SURFACE4", "CPS3")
    inner_rotor_conn_m9 = parser_inner_rotor.get_conn("SURFACE3", "CPS3")
    inner_rotor_conn_m10 = parser_inner_rotor.get_conn("SURFACE2", "CPS3")

    # Get the back iron connectivity
    inner_rotor_conn_back_iron = parser_inner_rotor.get_conn("SURFACE1", "CPS3")

    # Get the airgap connectivity
    inner_rotor_conn_airgap = parser_inner_rotor.get_conn("SURFACE12", "CPS3")

    # Line on the left edge
    inner_rotor_left_edge1 = parser_inner_rotor.get_conn("LINE54", "T3D2")
    inner_rotor_left_edge2 = parser_inner_rotor.get_conn("LINE55", "T3D2")
    inner_rotor_conn_pbc_left = np.concatenate(
        (inner_rotor_left_edge1.flatten(), inner_rotor_left_edge2.flatten()), axis=0
    )

    # Turn into a single unique list of nodes preserving the order from bottom to top
    # Oriented from bottom to top
    inner_rotor_pbc_nodes_left = np.array(
        list(dict.fromkeys(inner_rotor_conn_pbc_left))
    )
    inner_rotor_pbc_nodes_left = np.flip(inner_rotor_pbc_nodes_left)

    # Line of the right edge
    inner_rotor_right_edge1 = parser_inner_rotor.get_conn("LINE57", "T3D2")
    inner_rotor_right_edge2 = parser_inner_rotor.get_conn("LINE52", "T3D2")
    inner_rotor_conn_pbc_right = np.concatenate(
        (inner_rotor_right_edge1.flatten(), inner_rotor_right_edge2.flatten()), axis=0
    )

    # Turn into a single unique list of nodes preserving the order from bottom to top
    # Oriented from bottom to top
    inner_rotor_pbc_nodes_right = np.array(
        list(dict.fromkeys(inner_rotor_conn_pbc_right))
    )

    # Line on the top and bottom edges
    inner_rotor_bottom_edge = parser_inner_rotor.get_conn("LINE56", "T3D2")
    inner_rotor_top_edge = parser_inner_rotor.get_conn("LINE53", "T3D2")
    inner_rotor_dirichlet_nodes = np.array(
        list(dict.fromkeys(inner_rotor_bottom_edge.flatten()))
    )  # Left to right
    inner_rotor_pbc_nodes_top = np.array(
        list(dict.fromkeys(inner_rotor_top_edge.flatten()))
    )

    inner_rotor_pbc_nodes_top = np.flip(inner_rotor_pbc_nodes_top)

    #############################
    # Interface node connectivity
    #############################

    #####################################################################################
    #####################################################################################

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 2))

    #########################
    # Plot the Stator Regions
    #########################
    # Plot slots (left half) (orange)
    slot_conns_left_half = [
        stator_conn_s1,
        stator_conn_s3,
        stator_conn_s5,
        stator_conn_s7,
        stator_conn_s9,
        stator_conn_s11,
        stator_conn_s13,
        stator_conn_s15,
        stator_conn_s17,
        stator_conn_s19,
        stator_conn_s21,
        stator_conn_s23,
    ]
    plot_region(ax, X_stator, slot_conns_left_half, color="#FF7B00", label="Copper")

    # Plot slots (Right half) (orange)
    slot_conns_right_half = [
        stator_conn_s2,
        stator_conn_s4,
        stator_conn_s6,
        stator_conn_s8,
        stator_conn_s10,
        stator_conn_s12,
        stator_conn_s14,
        stator_conn_s16,
        stator_conn_s18,
        stator_conn_s20,
        stator_conn_s22,
        stator_conn_s24,
    ]
    plot_region(ax, X_stator, slot_conns_right_half, color="#FFBB00", label="Copper")

    # Plot stator iron (gray = teeth surfaces)
    iron_conns = [
        stator_conn_t1,
        stator_conn_t2,
        stator_conn_t3,
        stator_conn_t4,
        stator_conn_t5,
        stator_conn_t6,
        stator_conn_t7,
        stator_conn_t8,
        stator_conn_t9,
        stator_conn_t10,
        stator_conn_t11,
        stator_conn_t12,
        stator_conn_t13,
    ]
    plot_region(ax, X_stator, iron_conns, color="#939393", label="Iron")

    # Plot stator airgap (green)
    airgap_conns = [stator_conn_ag_inner, stator_conn_ag_outter]
    plot_region(ax, X_stator, airgap_conns, color="#7BE7FF", label="Airgap")

    # Plot the PBC edges
    plot_edge(ax, X_stator, stator_pbc_nodes_left, color="#FF00F2")
    plot_edge(ax, X_stator, stator_pbc_nodes_right, color="#0077FF")
    plot_edge(
        ax,
        X_stator,
        stator_pbc_nodes_bottom[-slide_number:-1] if slide_number > 0 else [],
        color="#FF006A",
    )
    plot_edge(
        ax,
        X_stator,
        stator_pbc_nodes_top[-slide_number:-1] if slide_number > 0 else [],
        color="#00FFD5",
    )

    ###############################
    # Plot the Outter Rotor Regions
    ###############################
    # Plot the magnets for the outter rotor (set1)
    outter_rotor_magnets_conn_set1 = [
        outter_rotor_conn_m1,
        outter_rotor_conn_m3,
        outter_rotor_conn_m5,
        outter_rotor_conn_m7,
        outter_rotor_conn_m9,
    ]
    plot_region(
        ax,
        X_outter_rotor,
        outter_rotor_magnets_conn_set1,
        color="#0026FF",
        label="Magnet",
    )

    # Plot the magnets for the outter rotor (set2)
    outter_rotor_magnets_conn_set2 = [
        outter_rotor_conn_m2,
        outter_rotor_conn_m4,
        outter_rotor_conn_m6,
        outter_rotor_conn_m8,
        outter_rotor_conn_m10,
    ]
    plot_region(
        ax,
        X_outter_rotor,
        outter_rotor_magnets_conn_set2,
        color="#FF0000",
        label="Magnet",
    )

    # Plot the back iron region for the outter rotor
    plot_region(
        ax,
        X_outter_rotor,
        [outter_rotor_conn_back_iron],
        color="#4F4F4F",
        label="Back Iron",
    )

    # Plot the airgap region for the outter rotor
    plot_region(
        ax, X_outter_rotor, [outter_rotor_conn_airgap], color="#7BE7FF", label="Airgap"
    )

    # Plot the left and right edge pbc
    plot_edge(
        ax,
        X_outter_rotor,
        (
            outter_rotor_pbc_nodes_left[:-1]
            if slide_number > 0
            else outter_rotor_pbc_nodes_left[1:-1]
        ),
        color="#FF6200",
    )
    plot_edge(
        ax,
        X_outter_rotor,
        (
            outter_rotor_pbc_nodes_right[:-1]
            if slide_number > 0
            else outter_rotor_pbc_nodes_right[1:-1]
        ),
        color="#9A7BFF",
    )

    # Plot the dirichlet bc edge
    plot_edge(ax, X_outter_rotor, outter_rotor_dirichlet_nodes, color="#2B19E9")

    # Plot the airgap pbc
    plot_edge(
        ax,
        X_outter_rotor,
        outter_rotor_pbc_nodes_bottom[1:slide_number] if slide_number > 0 else [],
        color="#8041BF",
    )

    ##############################
    # Plot the Inner Rotor Regions
    ##############################
    # Plot the magnets for the inner rotor (set1)
    inner_rotor_magnets_conn_set1 = [
        inner_rotor_conn_m1,
        inner_rotor_conn_m3,
        inner_rotor_conn_m5,
        inner_rotor_conn_m7,
        inner_rotor_conn_m9,
    ]
    plot_region(
        ax,
        X_inner_rotor,
        inner_rotor_magnets_conn_set1,
        color="#0026FF",
        label="Magnet",
    )

    # Plot the magnets for the inner rotor (set2)
    inner_rotor_magnets_conn_set2 = [
        inner_rotor_conn_m2,
        inner_rotor_conn_m4,
        inner_rotor_conn_m6,
        inner_rotor_conn_m8,
        inner_rotor_conn_m10,
    ]
    plot_region(
        ax,
        X_inner_rotor,
        inner_rotor_magnets_conn_set2,
        color="#FF0000",
        label="Magnet",
    )

    # Plot the back iron region for the inner rotor
    plot_region(
        ax,
        X_inner_rotor,
        [inner_rotor_conn_back_iron],
        color="#4F4F4F",
        label="Back Iron",
    )

    # Plot the airgap region for the inner rotor
    plot_region(
        ax,
        X_inner_rotor,
        [inner_rotor_conn_airgap],
        color="#7BE7FF",
        label="Airgap",
    )

    # Plot the left and right edge pbc
    plot_edge(
        ax,
        X_inner_rotor,
        (
            inner_rotor_pbc_nodes_left[1:]
            if slide_number > 0
            else inner_rotor_pbc_nodes_left[1:-1]
        ),
        color="#FFB07B",
    )
    plot_edge(
        ax,
        X_inner_rotor,
        (
            inner_rotor_pbc_nodes_right[1:]
            if slide_number > 0
            else inner_rotor_pbc_nodes_right[1:-1]
        ),
        color="#FB7BFF",
    )

    # Plot the dirichlet bc edge
    plot_edge(ax, X_inner_rotor, inner_rotor_dirichlet_nodes, color="#2CB0FC")

    # Plot the airgap pbc edge
    plot_edge(
        ax,
        X_inner_rotor,
        inner_rotor_pbc_nodes_top[1:slide_number] if slide_number > 0 else [],
        color="#BF4141",
    )

    ###################################
    # Plot the overlapped airgap region
    ###################################
    plot_edge(
        ax,
        X_stator,
        stator_pbc_nodes_top[1 : -slide_number - 1],
        color="#246317",
        linestyle="-",
    )
    plot_edge(
        ax,
        X_stator,
        stator_pbc_nodes_bottom[1 : -slide_number - 1],
        color="#63175F",
        linestyle="-",
    )

    plot_edge(
        ax,
        X_outter_rotor,
        outter_rotor_pbc_nodes_bottom[slide_number + 1 : -1],
        color="#FBFF00",
        linestyle=":",
    )
    plot_edge(
        ax,
        X_inner_rotor,
        inner_rotor_pbc_nodes_top[slide_number + 1 : -1],
        color="#FF008C",
        linestyle=":",
    )

    # Formatting
    # ax.set_aspect("equal")
    # ax.legend()
    ax.set_xlim(-1, 2 * total_length)
    ylim = (
        0.5 * copper_slot_height
        + tooth_tip_thickness
        + airgap
        + magnet_thickness
        + back_iron_thickness
    ) + 1
    ax.set_ylim(-ylim, ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.savefig(f"Figures/{slide_number}.png", dpi=800)
    print(f"Saved figure: {slide_number}")
    # plt.show()
    return


def create_gif():
    folder = "/Users/seiyonarulampalam/git/AFPM/Figures"

    # Only keep PNGs named as numbers
    images = [f for f in os.listdir(folder) if f.endswith(".png")]

    # Sort numerically by the filename (strip extension and convert to int)
    images = sorted(images, key=lambda x: int(os.path.splitext(x)[0]))

    image_paths = [os.path.join(folder, img) for img in images]
    output_gif = os.path.join(
        "/Users/seiyonarulampalam/git/AFPM/Animations", "sliding_mesh_bc.gif"
    )

    imageio.mimsave(
        output_gif, [imageio.imread(img) for img in image_paths], duration=0.5
    )
    return


# Generate a plot for each slide number
for i in range(0, 100, 1):
    # Loop through each slide number
    plot_motor(
        total_length=36.0,
        airgap=1.0,
        copper_slot_height=4.0,
        tooth_tip_thickness=1.0,
        bell_width=2.5,
        tooth_width=1.5,
        magnet_length=3.0,
        magnet_thickness=2,
        back_iron_thickness=1.0,
        mesh_refinement=2e-1,
        npts_airgap=100,
        slide_number=i,
    )


# Create the gif
create_gif()
