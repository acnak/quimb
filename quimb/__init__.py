"""
Quantum Information for Many-Body calculations.
"""
try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    try:
        # use setuptools_scm to get the current version from src using git
        from setuptools_scm import get_version as _gv
        from pathlib import Path as _Path

        __version__ = _gv(_Path(__file__).parent.parent)
    except ImportError:
        # setuptools_scm is not available, use a default version
        __version__ = "0.0.0+unknown"

import warnings

# some useful math
from math import pi, cos, sin, tan, exp, log, log2, log10, sqrt

# Core functions
from .core import (
    qarray,
    prod,
    isket,
    isbra,
    isop,
    isvec,
    issparse,
    isdense,
    isreal,
    isherm,
    ispos,
    mul,
    dag,
    dot,
    vdot,
    rdot,
    ldmul,
    rdmul,
    outer,
    explt,
    get_thread_pool,
    normalize,
    chop,
    quimbify,
    qu,
    ket,
    bra,
    dop,
    sparse,
    infer_size,
    trace,
    identity,
    eye,
    speye,
    dim_map,
    dim_compress,
    kron,
    kronpow,
    ikron,
    pkron,
    permute,
    itrace,
    partial_trace,
    expectation,
    expec,
    nmlz,
    tr,
    ptr,
)

# Linear algebra functions
from .linalg.base_linalg import (
    eigensystem,
    eig,
    eigh,
    eigvals,
    eigvalsh,
    eigvecs,
    eigvecsh,
    eigensystem_partial,
    groundstate,
    groundenergy,
    bound_spectrum,
    eigh_window,
    eigvalsh_window,
    eigvecsh_window,
    svd,
    svds,
    norm,
    expm,
    sqrtm,
    expm_multiply,
    Lazy,
)
from .linalg.rand_linalg import rsvd, estimate_rank
from .linalg.mpi_launcher import get_mpi_pool, can_use_mpi_pool

# Generating objects
from .gen.operators import (
    spin_operator,
    pauli,
    hadamard,
    phase_gate,
    S_gate,
    T_gate,
    U_gate,
    rotation,
    Rx,
    Ry,
    Rz,
    Xsqrt,
    Ysqrt,
    Zsqrt,
    Wsqrt,
    swap,
    iswap,
    fsim,
    fsimg,
    ncontrolled_gate,
    controlled,
    CNOT,
    cX,
    cY,
    cZ,
    ccX,
    ccY,
    ccZ,
    controlled_swap,
    cswap,
    fredkin,
    toffoli,
    ham_heis,
    ham_ising,
    ham_XY,
    ham_XXZ,
    ham_j1j2,
    ham_mbl,
    ham_heis_2D,
    zspin_projector,
    create,
    destroy,
    num,
    ham_hubbard_hardcore,
)
from .gen.states import (
    basis_vec,
    up,
    zplus,
    down,
    zminus,
    plus,
    xplus,
    minus,
    xminus,
    yplus,
    yminus,
    bloch_state,
    bell_state,
    singlet,
    thermal_state,
    neel_state,
    singlet_pairs,
    werner_state,
    ghz_state,
    w_state,
    levi_civita,
    perm_state,
    graph_state_1d,
    computational_state,
)
from .gen.rand import (
    randn,
    rand,
    rand_matrix,
    rand_herm,
    rand_pos,
    rand_rho,
    rand_ket,
    rand_uni,
    rand_haar_state,
    gen_rand_haar_states,
    rand_mix,
    rand_product_state,
    rand_matrix_product_state,
    rand_mps,
    rand_seperable,
    rand_iso,
    rand_mera,
    seed_rand,
    set_rand_bitgen,
)

# Functions for calculating properties
from .calc import (
    fidelity,
    purify,
    entropy,
    entropy_subsys,
    mutual_information,
    mutinf,
    mutinf_subsys,
    schmidt_gap,
    tr_sqrt,
    tr_sqrt_subsys,
    partial_transpose,
    negativity,
    logarithmic_negativity,
    logneg,
    logneg_subsys,
    concurrence,
    one_way_classical_information,
    quantum_discord,
    trace_distance,
    cprint,
    decomp,
    pauli_decomp,
    bell_decomp,
    correlation,
    pauli_correlations,
    ent_cross_matrix,
    qid,
    is_degenerate,
    is_eigenvector,
    page_entropy,
    heisenberg_energy,
    dephase,
    kraus_op,
    projector,
    measure,
    simulate_counts,
)

# Evolution class and methods
from .evo import Evolution

from .linalg.approx_spectral import (
    approx_spectral_function,
    tr_abs_approx,
    tr_exp_approx,
    tr_sqrt_approx,
    tr_xlogx_approx,
    entropy_subsys_approx,
    logneg_subsys_approx,
    negativity_subsys_approx,
    xlogx,
)
from .utils import (
    save_to_disk,
    load_from_disk,
    oset,
    LRU,
    tree_map,
    tree_apply,
    tree_flatten,
    tree_unflatten,
    format_number_with_error,
    NEUTRAL_STYLE,
    default_to_neutral_style,
)


warnings.filterwarnings("ignore", message="Caching is not available when ")


__all__ = [
    # Accel ----------------------------------------------------------------- #
    "qarray",
    "prod",
    "isket",
    "isbra",
    "isop",
    "isvec",
    "issparse",
    "isdense",
    "isreal",
    "isherm",
    "ispos",
    "mul",
    "dag",
    "dot",
    "vdot",
    "rdot",
    "ldmul",
    "rdmul",
    "outer",
    "explt",
    # Core ------------------------------------------------------------------ #
    "normalize",
    "chop",
    "quimbify",
    "qu",
    "ket",
    "bra",
    "dop",
    "sparse",
    "infer_size",
    "trace",
    "identity",
    "eye",
    "speye",
    "dim_map",
    "dim_compress",
    "kron",
    "kronpow",
    "ikron",
    "pkron",
    "permute",
    "itrace",
    "partial_trace",
    "expectation",
    "expec",
    "nmlz",
    "tr",
    "ptr",
    # Linalg ---------------------------------------------------------------- #
    "eigensystem",
    "eig",
    "eigh",
    "eigvals",
    "eigvalsh",
    "eigvecs",
    "eigvecsh",
    "eigensystem_partial",
    "groundstate",
    "groundenergy",
    "bound_spectrum",
    "eigh_window",
    "eigvalsh_window",
    "eigvecsh_window",
    "svd",
    "svds",
    "norm",
    "Lazy",
    "rsvd",
    "estimate_rank",
    # Gen ------------------------------------------------------------------- #
    "spin_operator",
    "pauli",
    "hadamard",
    "phase_gate",
    "T_gate",
    "S_gate",
    "U_gate",
    "rotation",
    "Rx",
    "Ry",
    "Rz",
    "Xsqrt",
    "Ysqrt",
    "Zsqrt",
    "Wsqrt",
    "swap",
    "iswap",
    "fsim",
    "fsimg",
    "ncontrolled_gate",
    "controlled",
    "CNOT",
    "cX",
    "cY",
    "cZ",
    "ccX",
    "ccY",
    "ccZ",
    "controlled_swap",
    "cswap",
    "fredkin",
    "toffoli",
    "ham_heis",
    "ham_ising",
    "ham_XY",
    "ham_XXZ",
    "ham_j1j2",
    "ham_mbl",
    "ham_heis_2D",
    "create",
    "destroy",
    "num",
    "ham_hubbard_hardcore",
    "zspin_projector",
    "basis_vec",
    "up",
    "zplus",
    "down",
    "zminus",
    "plus",
    "xplus",
    "minus",
    "xminus",
    "yplus",
    "yminus",
    "bloch_state",
    "bell_state",
    "singlet",
    "thermal_state",
    "neel_state",
    "singlet_pairs",
    "werner_state",
    "ghz_state",
    "w_state",
    "levi_civita",
    "perm_state",
    "graph_state_1d",
    "rand_matrix",
    "rand_herm",
    "rand_pos",
    "rand_rho",
    "rand_ket",
    "rand_uni",
    "rand_haar_state",
    "gen_rand_haar_states",
    "rand_mix",
    "rand_mps",
    "randn",
    "rand",
    "rand_product_state",
    "rand_matrix_product_state",
    "rand_seperable",
    "rand_iso",
    "rand_mera",
    "seed_rand",
    "set_rand_bitgen",
    "computational_state",
    # Calc ------------------------------------------------------------------ #
    "expm",
    "sqrtm",
    "expm_multiply",
    "fidelity",
    "purify",
    "entropy",
    "entropy_subsys",
    "mutual_information",
    "mutinf",
    "mutinf_subsys",
    "schmidt_gap",
    "tr_sqrt",
    "tr_sqrt_subsys",
    "partial_transpose",
    "negativity",
    "logarithmic_negativity",
    "logneg",
    "logneg_subsys",
    "concurrence",
    "one_way_classical_information",
    "quantum_discord",
    "trace_distance",
    "cprint",
    "decomp",
    "pauli_decomp",
    "bell_decomp",
    "correlation",
    "pauli_correlations",
    "ent_cross_matrix",
    "qid",
    "is_degenerate",
    "is_eigenvector",
    "page_entropy",
    "heisenberg_energy",
    "dephase",
    "kraus_op",
    "projector",
    "measure",
    "simulate_counts",
    # Evo ------------------------------------------------------------------- #
    "Evolution",
    # Approx spectral ------------------------------------------------------- #
    "approx_spectral_function",
    "tr_abs_approx",
    "tr_exp_approx",
    "tr_sqrt_approx",
    "tr_xlogx_approx",
    "entropy_subsys_approx",
    "logneg_subsys_approx",
    "negativity_subsys_approx",
    # Some misc useful math ------------------------------------------------- #
    "pi",
    "cos",
    "sin",
    "tan",
    "exp",
    "log",
    "log2",
    "log10",
    "sqrt",
    "xlogx",
    # Utils ----------------------------------------------------------------- #
    "save_to_disk",
    "load_from_disk",
    "get_thread_pool",
    "get_mpi_pool",
    "can_use_mpi_pool",
    "oset",
    "LRU",
    "tree_map",
    "tree_apply",
    "tree_flatten",
    "tree_unflatten",
    "format_number_with_error",
    "NEUTRAL_STYLE",
    "default_to_neutral_style",
]
