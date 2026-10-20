# Course data for Year 2 (S4-S6). Strings are LaTeX-ready.

def wk(topics, mid="\\textit{Midterm examination}.", end="Revision; \\textit{final examination}."):
    """Build a 1-6 / 7 / 8-13 / 14-15 schedule from 12 teaching topics."""
    s = [(str(i + 1), t) for i, t in enumerate(topics[:6])]
    s.append(("7", mid))
    s += [(str(i + 8), t) for i, t in enumerate(topics[6:12])]
    s.append(("14--15", end))
    return s

PHY201 = dict(
    code="PHY 201", title="Quantum Physics I", kind="theory", hours="4 Hours/Week",
    prereq="PHY 103, MTH 103, MTH 104",
    models="MIT 8.04; Harvard Physics 143a; Oxford A3; Princeton PHY~208; Caltech Ph~12b; Dhaka PH~302",
    rationale=r"""Quantum mechanics is the course that separates physicists from everyone else. Starting from the experiments that forced it into existence, the student learns wave mechanics, solves the canonical one-dimensional problems and the hydrogen atom, and meets spin --- the foundation for all of modern physics.""",
    clos=[
        ("Explain the experimental evidence for quantisation and wave--particle duality.", "Understand", "PLO1"),
        ("Solve the time-independent Schr\\\"odinger equation for standard 1D potentials.", "Apply", "PLO1, PLO2"),
        ("Use operators, expectation values and the uncertainty principle.", "Apply", "PLO1, PLO2"),
        ("Solve central-potential problems and the hydrogen atom using separation of variables.", "Apply", "PLO1, PLO2"),
        ("Describe spin-$\\tfrac12$ systems with Pauli matrices.", "Understand", "PLO1"),
    ],
    schedule=wk([
        "Experimental basis: photoelectric effect, Compton scattering, de Broglie waves, Mach--Zehnder interferometer.",
        "Wavefunctions, Born rule, normalisation, expectation values.",
        "Momentum space, Fourier transforms, the uncertainty principle.",
        "The Schr\\\"odinger equation, stationary states, the infinite well.",
        "The harmonic oscillator: analytic and ladder-operator methods.",
        "Free particle, wave packets, group velocity.",
        "Delta potential, 1D scattering, transmission and reflection, tunnelling.",
        "Finite well, bound states, introduction to the variational principle.",
        "Formalism: Hermitian operators, eigenfunctions, generalised uncertainty principle.",
        "3D: separation in spherical coordinates, angular momentum, spherical harmonics.",
        "The hydrogen atom.",
        "Spin-$\\tfrac12$, Stern--Gerlach, Pauli matrices.",
    ]),
    texts=[
        r"D.~J.~Griffiths and D.~F.~Schroeter. \emph{Introduction to Quantum Mechanics}, 3rd ed. Cambridge University Press. (Chapters 1--4.) \textbf{(Primary text)}",
        r"B.~Zwiebach. \emph{Mastering Quantum Mechanics}. MIT Press.",
        r"A.~P.~French and E.~F.~Taylor. \emph{An Introduction to Quantum Physics}. MIT Introductory Physics Series.",
        r"MIT OpenCourseWare 8.04 \emph{Quantum Physics I} (Zwiebach).",
        r"R.~P.~Feynman et al. \emph{The Feynman Lectures on Physics}, Vol.~III.",
    ],
)

PHY202 = dict(
    code="PHY 202", title="Thermal and Statistical Physics I", kind="theory", hours="4 Hours/Week",
    prereq="PHY 101, MTH 102; PHY 201 concurrently recommended",
    models="MIT 8.044; Oxford A1; Princeton PHY~301; Caltech Ph~12c; Dhaka PH~102",
    rationale=r"""Thermodynamics tells us what is possible; statistical mechanics tells us why. Beginning with probability, the course builds entropy from counting, derives the laws of thermodynamics, treats engines and phase changes, and introduces the Boltzmann factor and quantum statistics.""",
    clos=[
        ("Use probability distributions and the central limit theorem in physical contexts.", "Apply", "PLO2"),
        ("Apply the laws of thermodynamics to processes, engines and refrigerators.", "Apply", "PLO1, PLO3"),
        ("Derive entropy, temperature and chemical potential from multiplicity.", "Analyze", "PLO1"),
        ("Use free energies, Maxwell relations and phase-equilibrium conditions.", "Apply", "PLO1, PLO2"),
        ("Compute partition functions and apply Boltzmann, Fermi--Dirac and Bose--Einstein statistics.", "Apply", "PLO1, PLO2"),
    ],
    schedule=wk([
        "Probability: random variables, distributions, central limit theorem.",
        "Temperature, ideal gases, equipartition; heat, work and the first law.",
        "Heat capacities, enthalpy; kinetic theory and the Maxwell--Boltzmann distribution.",
        "The second law: multiplicity, Einstein solids, entropy.",
        "Interactions: temperature, pressure and chemical potential from entropy.",
        "Engines and refrigerators; Carnot, Otto and Diesel cycles.",
        "Free energies, Maxwell relations, thermodynamic identities.",
        "Phase transformations, Clausius--Clapeyron, van der Waals.",
        "The Boltzmann factor, partition function, canonical ensemble.",
        "Paramagnetism; equipartition revisited; Maxwell speed distribution.",
        "Quantum statistics: Fermi--Dirac and Bose--Einstein distributions.",
        "Blackbody radiation, degenerate Fermi gases, Debye solids (preview).",
    ]),
    texts=[
        r"D.~V.~Schroeder. \emph{An Introduction to Thermal Physics}. Oxford University Press / Addison-Wesley. (Chapters 1--7.) \textbf{(Primary text)}",
        r"S.~J.~Blundell and K.~M.~Blundell. \emph{Concepts in Thermal Physics}, 2nd ed. Oxford University Press.",
        r"C.~Kittel and H.~Kroemer. \emph{Thermal Physics}, 2nd ed. W.~H.~Freeman.",
        r"MIT OpenCourseWare 8.044 \emph{Statistical Physics I}.",
        r"M.~W.~Zemansky and R.~H.~Dittman. \emph{Heat and Thermodynamics}. McGraw-Hill. (Dhaka reference.)",
    ],
)

PHY203 = dict(
    code="PHY 203", title="Special Relativity", kind="theory", hours="4 Hours/Week",
    prereq="PHY 102, MTH 103",
    models="MIT 8.033/8.20; Oxford CP1 and B2 (part); Harvard 15a (part); Dhaka PH~301 (part)",
    rationale=r"""Relativity rebuilds space and time from two postulates. The course develops Lorentz transformations, spacetime diagrams and four-vectors, relativistic dynamics and collisions, the unification of electric and magnetic fields, and --- following MIT's 8.033 --- a first look at gravity, the Schwarzschild metric and cosmology.""",
    clos=[
        ("Derive and apply the Lorentz transformation, time dilation and length contraction.", "Apply", "PLO1"),
        ("Resolve relativistic paradoxes using spacetime diagrams and invariants.", "Analyze", "PLO1, PLO3"),
        ("Use four-vectors to solve collision and decay problems.", "Apply", "PLO1, PLO2"),
        ("Show how electric and magnetic fields transform between frames.", "Understand", "PLO1"),
        ("Explain the equivalence principle and simple consequences of curved spacetime.", "Understand", "PLO1, PLO9"),
    ],
    schedule=wk([
        "Galilean relativity, Michelson--Morley, Einstein's postulates.",
        "Simultaneity, time dilation, length contraction, clock synchronisation.",
        "Lorentz transformation, velocity addition, relativistic Doppler effect.",
        "Spacetime diagrams, invariant intervals, causality, paradoxes.",
        "Four-vectors, proper time, four-velocity and four-momentum.",
        "Energy and momentum, $E=mc^2$, massless particles.",
        "Collisions, decays, threshold energies, the centre-of-momentum frame.",
        "Relativistic forces, acceleration, hyperbolic motion, rapidity.",
        "Relativity and electromagnetism: transformation of $\\mathbf{E}$ and $\\mathbf{B}$.",
        "Equivalence principle, accelerated frames, gravitational redshift.",
        "Schwarzschild metric (introduction): geodesics, light deflection, Shapiro delay, GPS.",
        "Newtonian cosmology (introduction).",
    ]),
    texts=[
        r"D.~Morin. \emph{Special Relativity for the Enthusiastic Beginner}. CreateSpace. \textbf{(Primary text)}",
        r"E.~F.~Taylor and J.~A.~Wheeler. \emph{Spacetime Physics}, 2nd ed. W.~H.~Freeman.",
        r"A.~P.~French. \emph{Special Relativity}. MIT Introductory Physics Series.",
        r"A.~M.~Steane. \emph{Relativity Made Relatively Easy}. Oxford University Press.",
        r"MIT OpenCourseWare 8.033 \emph{Relativity} and 8.20 \emph{Introduction to Special Relativity}.",
    ],
)

PHY204 = dict(
    code="PHY 204", title="Classical Mechanics II: Lagrangian and Hamiltonian Dynamics", kind="theory", hours="4 Hours/Week",
    prereq="PHY 101, MTH 104",
    models="MIT 8.223 and 8.09; Harvard Physics 151; Princeton PHY~205; Caltech Ph~106a; Dhaka PH~301",
    rationale=r"""The Lagrangian and Hamiltonian formulations are the bridge from Newton to quantum mechanics and field theory. The course develops variational principles, symmetries and conservation laws, rigid bodies, normal modes, phase space and canonical transformations, and ends with chaos and continuous systems.""",
    clos=[
        ("Derive equations of motion with the Euler--Lagrange equations, including constraints.", "Apply", "PLO1, PLO2"),
        ("Relate symmetries to conservation laws through Noether's theorem.", "Understand", "PLO1"),
        ("Analyse rigid-body motion with the inertia tensor and Euler's equations.", "Analyze", "PLO1"),
        ("Formulate Hamiltonian mechanics, Poisson brackets and canonical transformations.", "Apply", "PLO1, PLO2"),
        ("Investigate nonlinear and chaotic dynamics numerically.", "Analyze", "PLO5"),
    ],
    schedule=wk([
        "Calculus of variations, Euler--Lagrange equation, brachistochrone, geodesics.",
        "Lagrangian mechanics, generalised coordinates, constraints.",
        "Lagrange multipliers and constraint forces; symmetries and Noether's theorem.",
        "Two-body problem and central forces; Rutherford scattering.",
        "Rigid bodies: inertia tensor, principal axes, Euler's equations, symmetric top.",
        "Small oscillations: normal-mode matrix method.",
        "Hamiltonian, Hamilton's equations, phase space, Liouville's theorem.",
        "Poisson brackets, canonical transformations; link to quantum commutators.",
        "Hamilton--Jacobi theory, action-angle variables, adiabatic invariants.",
        "Nonlinear dynamics and chaos: driven damped pendulum, Poincar\\'e sections.",
        "Continuous systems: Lagrangian density for the string.",
        "Relativistic Lagrangian; charged particle in an EM field; the Maxwell action.",
    ]),
    texts=[
        r"J.~R.~Taylor. \emph{Classical Mechanics}. University Science Books. (Chapters 6--16.) \textbf{(Primary text)}",
        r"D.~Tong. \emph{Classical Dynamics} (lecture notes), University of Cambridge.",
        r"L.~N.~Hand and J.~D.~Finch. \emph{Analytical Mechanics}. Cambridge University Press.",
        r"H.~Goldstein, C.~Poole and J.~Safko. \emph{Classical Mechanics}, 3rd ed. Addison-Wesley. (Reference.)",
        r"L.~D.~Landau and E.~M.~Lifshitz. \emph{Mechanics}, 3rd ed. (Honours reading.)",
        r"MIT OpenCourseWare 8.223 \emph{Classical Mechanics II} and 8.09 \emph{Classical Mechanics III}.",
    ],
)

MTH201 = dict(
    code="MTH 201", title="Mathematical Methods: Complex Analysis, PDEs and Special Functions", kind="theory", hours="4 Hours/Week",
    prereq="MTH 102, MTH 104",
    models="MIT 18.04/18.075; Harvard AM~104; Oxford Part~A Mathematical Methods; Caltech ACM~95ab; Dhaka PH~203",
    rationale=r"""Upper-level physics needs a larger mathematical toolbox: contour integration, Fourier transforms, Sturm--Liouville theory, Legendre and Bessel functions, Green's functions and tensors. This course supplies them one semester before electrodynamics, quantum mechanics and general relativity use them.""",
    clos=[
        ("Evaluate contour integrals and real integrals using residues.", "Apply", "PLO2"),
        ("Use Fourier transforms to solve diffusion and wave problems.", "Apply", "PLO2"),
        ("Expand functions in orthogonal eigenfunctions from Sturm--Liouville problems.", "Apply", "PLO2"),
        ("Solve Laplace, heat, wave and Schr\\\"odinger equations in curvilinear coordinates with special functions.", "Apply", "PLO2, PLO1"),
        ("Construct Green's functions and manipulate Cartesian tensors.", "Analyze", "PLO2"),
    ],
    schedule=wk([
        "Complex functions, analyticity, Cauchy--Riemann equations, harmonic functions.",
        "Contour integrals; Cauchy's theorem and integral formula.",
        "Laurent series, singularities, residues.",
        "Real integrals by residues; branch cuts.",
        "Conformal mapping: 2D electrostatics and potential flow.",
        "Fourier transforms: convolution, Parseval, diffusion and waves.",
        "Sturm--Liouville theory, orthogonal functions, eigenfunction expansions.",
        "Legendre polynomials, associated Legendre functions, spherical harmonics.",
        "Bessel functions; Laplace's equation in cylindrical and spherical coordinates.",
        "Separation of variables for heat, wave and Schr\\\"odinger equations in 2D/3D.",
        "Green's functions for ODEs and PDEs; method of images.",
        "Tensors: index notation, summation convention, Cartesian tensors.",
    ]),
    texts=[
        r"M.~L.~Boas. \emph{Mathematical Methods in the Physical Sciences}, 3rd ed. Wiley. (Chapters 10--15.) \textbf{(Primary text)}",
        r"K.~F.~Riley, M.~P.~Hobson and S.~J.~Bence. \emph{Mathematical Methods for Physics and Engineering}, 3rd ed. Cambridge University Press.",
        r"T.~Needham. \emph{Visual Complex Analysis}. Oxford University Press.",
        r"G.~B.~Arfken, H.~J.~Weber and F.~E.~Harris. \emph{Mathematical Methods for Physicists}. Academic Press. (Reference.)",
        r"MIT OpenCourseWare 18.04 \emph{Complex Variables with Applications}.",
    ],
)

LAB201 = dict(
    code="LAB 201", title="Electronics for Physicists", kind="lab", hours="5 Hours/Week",
    prereq="PHY 102, LAB 101",
    models="Harvard Physics 113/123; Caltech APh/EE~23--24; Dhaka PH~202, PH~403",
    rationale=r"""Every modern experiment is read out through electronics. In the spirit of Harvard's laboratory electronics course, the student builds and debugs filters, transistor and op-amp circuits, digital logic, data converters and a feedback controller on a home bench, learning to design instruments rather than merely use them.""",
    clos=[
        ("Analyse linear circuits in time and frequency domains, including Bode plots.", "Analyze", "PLO1, PLO4"),
        ("Design and build diode, transistor and op-amp circuits to specification.", "Create", "PLO4"),
        ("Interface sensors with a microcontroller, accounting for sampling and noise.", "Apply", "PLO4, PLO5"),
        ("Implement a PID feedback controller and characterise its response.", "Apply", "PLO4"),
        ("Debug circuits systematically using a multimeter and oscilloscope.", "Evaluate", "PLO4"),
    ],
    schedule=wk([
        "DC circuits, dividers, Th\\'evenin and Norton equivalents, instrument loading.",
        "RC circuits in the frequency domain: filters, Bode plots, phasors.",
        "Diodes: rectifiers, clamps, Zener regulation, LEDs.",
        "BJTs: switch, follower, common-emitter amplifier, biasing.",
        "FETs and MOSFET switches; current sources and mirrors.",
        "Op-amps I: golden rules, inverting and non-inverting amplifiers.",
        "Op-amps II: integrators, differentiators, active filters, non-idealities.",
        "Oscillators, comparators, Schmitt triggers, 555 timers.",
        "Digital logic: gates, flip-flops, counters.",
        "ADC/DAC, sampling, aliasing, Arduino interfacing.",
        "Noise, grounding, shielding; the lock-in amplifier concept.",
        "PID feedback control project.",
    ], mid="\\textit{Midterm practical}: design, build and measure against specification.",
       end="Project completion; \\textit{final practical} (build and debug)."),
    texts=[
        r"T.~C.~Hayes and P.~Horowitz. \emph{Learning the Art of Electronics}. Cambridge University Press. \textbf{(Primary text)}",
        r"P.~Horowitz and W.~Hill. \emph{The Art of Electronics}, 3rd ed. Cambridge University Press.",
        r"R.~L.~Boylestad and L.~Nashelsky. \emph{Electronic Devices and Circuit Theory}. Pearson. (Dhaka reference.)",
        r"Falstad circuit simulator; LTspice.",
    ],
)

PHY205 = dict(
    code="PHY 205", title="Electrodynamics", kind="theory", hours="4 Hours/Week",
    prereq="PHY 102, PHY 103, MTH 201",
    models="MIT 8.07; Harvard Physics 153; Oxford A2; Princeton PHY~304; Caltech Ph~106bc; Dhaka PH~305",
    rationale=r"""This is electromagnetism at full mathematical strength: boundary-value problems, multipoles, fields in matter, conservation laws with the stress tensor, waves in media and guides, retarded potentials, radiation, and the covariant formulation that unites it with relativity.""",
    clos=[
        ("Solve electrostatic boundary-value problems with images, separation of variables and multipoles.", "Apply", "PLO1, PLO2"),
        ("Analyse fields in dielectric and magnetic media.", "Analyze", "PLO1"),
        ("Apply conservation of energy and momentum to electromagnetic fields.", "Apply", "PLO1"),
        ("Derive wave propagation in vacuum, matter, conductors and waveguides.", "Analyze", "PLO1, PLO2"),
        ("Calculate radiation from accelerating charges and dipoles; write Maxwell's equations covariantly.", "Apply", "PLO1, PLO9"),
    ],
    schedule=wk([
        "Vector analysis and the Dirac delta; electrostatics revisited formally.",
        "Laplace's equation, uniqueness theorems, images.",
        "Separation of variables in Cartesian, spherical and cylindrical coordinates.",
        "The multipole expansion.",
        "Electric fields in matter: polarisation, $\\mathbf{D}$, linear dielectrics.",
        "Magnetostatics: vector potential, multipoles; magnetic fields in matter.",
        "Electrodynamics: EMF, Faraday, Maxwell's equations in matter.",
        "Conservation laws: Poynting's theorem, Maxwell stress tensor, field momentum.",
        "EM waves in vacuum, matter and conductors; dispersion; waveguides.",
        "Potentials and gauges; retarded potentials; Jefimenko; Li\\'enard--Wiechert.",
        "Radiation: electric and magnetic dipole; Larmor formula.",
        "Relativistic electrodynamics: the field tensor and covariant Maxwell equations.",
    ]),
    texts=[
        r"D.~J.~Griffiths. \emph{Introduction to Electrodynamics}, 4th/5th ed. Cambridge University Press. \textbf{(Primary text)}",
        r"A.~Zangwill. \emph{Modern Electrodynamics}. Cambridge University Press. (Honours reading.)",
        r"J.~D.~Jackson. \emph{Classical Electrodynamics}, 3rd ed. Wiley. (Reference.)",
        r"MIT OpenCourseWare 8.07 \emph{Electromagnetism II}.",
    ],
)

PHY206 = dict(
    code="PHY 206", title="Quantum Physics II", kind="theory", hours="4 Hours/Week",
    prereq="PHY 201, MTH 103",
    models="MIT 8.05; Harvard Physics 143a/b; Oxford A3/B3; Princeton PHY~305; Caltech Ph~125a; Dhaka PH~402",
    rationale=r"""The second quantum course recasts the subject in its true language: vector spaces, Dirac notation and operators. With it come two-state systems, entanglement and Bell's theorem, angular-momentum algebra and its addition, and mixed states --- the formalism used in all research-level quantum physics and quantum computing.""",
    clos=[
        ("Use Dirac notation, the spectral theorem and commuting observables.", "Apply", "PLO1, PLO2"),
        ("Evolve states in the Schr\\\"odinger and Heisenberg pictures.", "Apply", "PLO1"),
        ("Analyse two-state dynamics including spin precession and Rabi oscillations.", "Analyze", "PLO1"),
        ("Describe entanglement, test Bell inequalities and explain teleportation.", "Understand", "PLO1, PLO9"),
        ("Add angular momenta with Clebsch--Gordan coefficients; use density matrices.", "Apply", "PLO1, PLO2"),
    ],
    schedule=wk([
        "Two-state systems, Stern--Gerlach, spin as a vector space.",
        "Vector spaces, linear operators, inner products, adjoints.",
        "Dirac notation, spectral theorem, complete sets of commuting observables.",
        "Uncertainty principle (rigorous) and energy--time relation.",
        "Schr\\\"odinger and Heisenberg pictures; time evolution.",
        "Harmonic oscillator algebraically; coherent and squeezed states.",
        "Two-state dynamics: spin precession, NMR, Rabi oscillations.",
        "Multiparticle states, tensor products, entanglement.",
        "EPR, Bell inequalities, teleportation.",
        "Angular-momentum algebra; central potentials revisited.",
        "Addition of angular momentum; Clebsch--Gordan coefficients.",
        "Density matrices, mixed states, introduction to decoherence.",
    ]),
    texts=[
        r"B.~Zwiebach. \emph{Mastering Quantum Mechanics}. MIT Press. \textbf{(Primary text)}",
        r"R.~Shankar. \emph{Principles of Quantum Mechanics}, 2nd ed. Springer.",
        r"J.~Binney and D.~Skinner. \emph{The Physics of Quantum Mechanics}. Oxford University Press.",
        r"J.~S.~Townsend. \emph{A Modern Approach to Quantum Mechanics}, 2nd ed. University Science Books.",
        r"MIT OpenCourseWare 8.05 \emph{Quantum Physics II} (Zwiebach).",
    ],
)

CMP201 = dict(
    code="CMP 201", title="Computational Physics II: Numerical Methods", kind="comp", hours="3.5 Hours/Week",
    prereq="CMP 101, MTH 104",
    models="Caltech Ph~21/22/121; MIT 8.16 (part); Dhaka PH~307",
    rationale=r"""This course gives the student the numerical methods of working physicists: linear algebra and eigenproblems, shooting and relaxation, stable time-stepping of PDEs, spectral methods, Markov-chain Monte Carlo, molecular dynamics and an introduction to machine learning --- each applied to a problem from the concurrent courses.""",
    clos=[
        ("Solve eigenvalue problems numerically, including bound states of arbitrary potentials.", "Apply", "PLO5"),
        ("Implement stable schemes for elliptic, parabolic and hyperbolic PDEs and analyse stability.", "Analyze", "PLO5, PLO2"),
        ("Simulate statistical systems with Metropolis Monte Carlo and molecular dynamics.", "Apply", "PLO5, PLO1"),
        ("Validate numerical results against analytic limits and convergence tests.", "Evaluate", "PLO5, PLO3"),
        ("Present a computational study in a written report and code review.", "Create", "PLO8"),
    ],
    schedule=[
        ("1", "Numerical linear algebra: LU, conditioning, sparse systems."),
        ("2", "Eigenvalue problems: finite-difference Schr\\\"odinger solver."),
        ("3", "Shooting method; bound states of arbitrary potentials."),
        ("4", "Elliptic PDEs: Jacobi, Gauss--Seidel and SOR for Laplace and Poisson."),
        ("5", "Parabolic PDEs: FTCS, stability, Crank--Nicolson; time-dependent Schr\\\"odinger."),
        ("6", "Hyperbolic PDEs: the wave equation, the CFL condition."),
        ("7--8", "\\textit{Midterm project}: wave-packet scattering off a barrier."),
        ("9", "Spectral methods and the FFT for PDEs."),
        ("10", "Monte Carlo II: importance sampling, Markov chains, Metropolis."),
        ("11", "2D Ising model: phase transition, critical temperature, finite-size effects."),
        ("12", "Molecular dynamics: Lennard-Jones gas, thermostats, radial distribution."),
        ("13", "Optimisation and model fitting; introduction to machine learning for physics data."),
        ("14--15", "\\textit{Final project}; code review and oral."),
    ],
    texts=[
        r"M.~Newman. \emph{Computational Physics}. CreateSpace. (Chapters 6--10.) \textbf{(Primary text)}",
        r"A.~Gezerlis. \emph{Numerical Methods in Physics with Python}, 2nd ed. Cambridge University Press.",
        r"W.~H.~Press et al. \emph{Numerical Recipes}, 3rd ed. Cambridge University Press. (Reference.)",
    ],
)

SEMESTERS_Y2 = [
    ("Fourth Semester", "Spring 2028 (3 Jan -- 23 Apr 2028)", [PHY201, PHY202, PHY203]),
    ("Fifth Semester", "Summer 2028 (1 May -- 20 Aug 2028)", [PHY204, MTH201, LAB201]),
    ("Sixth Semester", "Autumn 2028 (28 Aug -- 17 Dec 2028)", [PHY205, PHY206, CMP201]),
]
