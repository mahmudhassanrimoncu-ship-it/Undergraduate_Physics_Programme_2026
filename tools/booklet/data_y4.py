# Course data for Year 4 (S10-S12), major options and electives. Strings are LaTeX-ready.
from data_y2 import wk

PHY401 = dict(
    code="PHY 401", title="General Relativity and Cosmology", kind="theory", hours="4 Hours/Week",
    prereq="PHY 203, PHY 204, MTH 201",
    models="Oxford B5; MIT 8.962, 8.286 and 8.224; Harvard Physics 210; Caltech Ph~236; Dhaka PH~308 (part)",
    rationale=r"""Einstein's theory of gravity is taught physics-first, as in Hartle: the student meets the equivalence principle, the Schwarzschild geometry, black holes and gravitational waves before the tensor machinery, then derives the field equations and applies them to the expanding universe, its thermal history and the open problems of dark matter and dark energy.""",
    clos=[
        ("Compute geodesics and observable effects in the Schwarzschild spacetime.", "Apply", "PLO1, PLO2"),
        ("Explain black-hole horizons and the generation and detection of gravitational waves.", "Understand", "PLO1, PLO9"),
        ("Manipulate tensors, covariant derivatives and curvature tensors.", "Apply", "PLO2"),
        ("Derive the Einstein field equations and their Newtonian limit.", "Analyze", "PLO1, PLO2"),
        ("Solve the Friedmann equations and relate cosmological observations to the thermal history of the universe.", "Apply", "PLO1, PLO6, PLO9"),
    ],
    schedule=wk([
        "The equivalence principle; gravity as geometry.",
        "Metrics, the line element, geodesics from the variational principle.",
        "The Schwarzschild geometry: orbits, perihelion precession.",
        "Light bending, gravitational lensing, the Shapiro delay, GPS.",
        "Black holes: horizons, Kruskal coordinates, Hawking radiation (qualitative).",
        "Gravitational waves in linearised gravity; LIGO.",
        "Tensors and differential geometry: covariant derivatives, Christoffel symbols.",
        "Curvature: the Riemann, Ricci and Einstein tensors.",
        "The Einstein field equations; the stress--energy tensor; the Newtonian limit.",
        "FRW cosmology, the Friedmann equations, cosmic expansion, the Hubble constant.",
        "Thermal history: nucleosynthesis, recombination, the cosmic microwave background.",
        "Inflation, dark matter, dark energy, open problems.",
    ]),
    texts=[
        r"J.~B.~Hartle. \emph{Gravity: An Introduction to Einstein's General Relativity}. Addison-Wesley / Cambridge University Press. (Weeks 1--10.) \textbf{(Primary text)}",
        r"B.~Ryden. \emph{Introduction to Cosmology}, 2nd ed. Cambridge University Press. (Weeks 11--13.) \textbf{(Primary text)}",
        r"S.~M.~Carroll. \emph{Spacetime and Geometry}. Addison-Wesley / Cambridge University Press.",
        r"B.~F.~Schutz. \emph{A First Course in General Relativity}, 2nd ed. Cambridge University Press.",
        r"MIT OpenCourseWare 8.962 \emph{General Relativity} (Hughes) and 8.286 \emph{The Early Universe} (Guth).",
    ],
)

PHY402 = dict(
    code="PHY 402", title="Quantum Information and Computation", kind="theory", hours="4 Hours/Week",
    prereq="PHY 206",
    models="MIT 8.370/8.371; Harvard Physics 160; Oxford C2 (part); Caltech Ph~219",
    rationale=r"""Quantum information is where physics meets computer science, and where the student's CSE background becomes an advantage. The course develops qubits, circuits and entanglement, the major quantum algorithms and their complexity, noise and error correction, cryptography and physical implementations, and ends with a project run on real IBM Quantum hardware.""",
    clos=[
        ("Represent qubit states, gates and measurements and build quantum circuits.", "Apply", "PLO1, PLO5"),
        ("Analyse the Deutsch--Jozsa, Simon, phase-estimation, Shor and Grover algorithms and their complexity.", "Analyze", "PLO2, PLO9"),
        ("Describe open systems with density matrices and quantum channels.", "Apply", "PLO1, PLO2"),
        ("Construct and analyse simple quantum error-correcting codes and cryptographic protocols.", "Analyze", "PLO1, PLO3"),
        ("Implement and evaluate a variational algorithm on real quantum hardware.", "Create", "PLO5, PLO6"),
    ],
    schedule=[
        ("1", "Qubits, the Bloch sphere, measurement, multi-qubit states."),
        ("2", "Gates and circuits; universality."),
        ("3", "Entanglement, Bell/CHSH, teleportation, superdense coding."),
        ("4", "Oracle algorithms: Deutsch--Jozsa, Bernstein--Vazirani, Simon."),
        ("5", "The quantum Fourier transform and phase estimation."),
        ("6", "Shor's algorithm; the complexity class BQP."),
        ("7", "\\textit{Midterm examination}."),
        ("8", "Grover's search; amplitude amplification."),
        ("9", "Density matrices, quantum channels, decoherence."),
        ("10", "Quantum error correction: bit-flip and Shor codes, stabiliser codes."),
        ("11", "Quantum cryptography: BB84, no-cloning."),
        ("12", "Physical implementations: superconducting qubits, trapped ions, photons, NV centres."),
        ("13", "NISQ algorithms: VQE and QAOA; project on IBM Quantum hardware."),
        ("14--15", "Project write-up; \\textit{final examination}."),
    ],
    assess=[
        ("Problem sets", "25\\%"),
        ("Concept quizzes", "5\\%"),
        ("Tutorials", "10\\%"),
        ("Midterm examination (week 7)", "20\\%"),
        ("Final examination (week 15)", "30\\%"),
        ("Qiskit project on IBM Quantum hardware", "10\\%"),
    ],
    texts=[
        r"M.~A.~Nielsen and I.~L.~Chuang. \emph{Quantum Computation and Quantum Information}. Cambridge University Press. \textbf{(Primary text)}",
        r"J.~Preskill. Lecture notes for Caltech Ph~219 \emph{Quantum Computation}.",
        r"N.~D.~Mermin. \emph{Quantum Computer Science: An Introduction}. Cambridge University Press.",
        r"MITx 8.370x \emph{Quantum Information Science}; IBM Qiskit tutorials. \url{https://qiskit.org}",
    ],
)

LAB401 = dict(
    code="LAB 401", title="Advanced Laboratory II: Experiment Design Project", kind="lab", hours="6 Hours/Week",
    prereq="LAB 301",
    models="MIT 8.14 (exploratory project); Caltech Ph~77; Harvard Physics 191; Dhaka PH~404, PL~401",
    rationale=r"""In the final laboratory course the student stops following manuals. After one guided experiment with a desktop cosmic-ray muon detector, the student designs an experiment of their own: proposing a physics question, budgeting uncertainties, building and debugging the apparatus, taking and analysing data, and defending the result at a poster session, as in MIT 8.14.""",
    clos=[
        ("Measure the angular distribution of cosmic-ray muons with a scintillator and SiPM detector.", "Apply", "PLO4, PLO6"),
        ("Propose an experiment with a physics question, expected signal and uncertainty budget.", "Create", "PLO4, PLO7"),
        ("Build, calibrate and debug original apparatus.", "Create", "PLO4"),
        ("Analyse data critically, including systematic errors, and iterate the design.", "Evaluate", "PLO6"),
        ("Communicate results in a journal-style report, a poster and an oral defence.", "Create", "PLO8"),
    ],
    schedule=[
        ("1--3", "Guided: cosmic-ray muons with a CosmicWatch-style detector; rate versus angle ($\\cos^2\\theta$) and elevation."),
        ("4", "\\textit{Project proposal}: question, apparatus, expected signal, uncertainty budget, risks."),
        ("5--6", "Design review and build."),
        ("7", "\\textit{Oral}: design review."),
        ("8--12", "Data taking, analysis, iteration."),
        ("13", "Poster and report draft. Senior Thesis proposal due."),
        ("14", "Final report (journal style)."),
        ("15", "\\textit{Poster session and oral defence}."),
    ],
    assess=[
        ("Laboratory notebook", "15\\%"),
        ("Guided-experiment report", "15\\%"),
        ("Project report", "30\\%"),
        ("Orals", "15\\%"),
        ("Proposal and design review", "10\\%"),
        ("Poster and defence", "15\\%"),
    ],
    assess_note=r"Project ideas: a Michelson interferometer measuring thermal expansion; a Kater reversible pendulum ($g$ to $10^{-4}$); a chaotic double pendulum versus simulation; an optical-lever torsion balance; acoustic levitation; a home-made magnetometer tracking geomagnetic variation; Planck's constant from blackbody radiation; laser speckle statistics. The \textbf{Senior Thesis proposal} (3--4 pages) is due at the end of week~13 and must be approved before THS~401.",
    texts=[
        r"CosmicWatch desktop muon detector project (MIT). \url{http://www.cosmicwatch.lns.mit.edu}",
        r"P.~Horowitz and W.~Hill. \emph{The Art of Electronics}, 3rd ed. Cambridge University Press. (Reference.)",
        r"I.~G.~Hughes and T.~P.~A.~Hase. \emph{Measurements and their Uncertainties}. Oxford University Press.",
    ],
)

THS401 = dict(
    code="THS 401", title="Senior Thesis I", kind="ths", hours="7 Hours/Week",
    prereq="IND 302; thesis proposal approved at the end of Semester~10",
    models="MIT 8.THU; Princeton senior thesis; Oxford MPhys project",
    rationale=r"""The senior thesis is the summit of the programme: a year-long piece of original research. It may be computational or theoretical (a numerical study of a model system, or an analytic extension of a published calculation), an open-data analysis (LIGO, CERN, SDSS, TESS/Kepler, Gaia or Planck), or an experiment that extends the LAB~401 project to research quality. The first semester establishes the literature, method and first results.""",
    clos=[
        ("Review the literature of a research area critically in a written chapter.", "Evaluate", "PLO7, PLO8"),
        ("Design and carry out a research plan with appropriate methods.", "Create", "PLO7, PLO5, PLO4"),
        ("Report progress clearly and respond to supervision.", "Apply", "PLO8, PLO10"),
        ("Present interim results to an examiner.", "Evaluate", "PLO8"),
    ],
    schedule=[
        ("1", "Kick-off: refine the plan; set up the thesis repository."),
        ("2--5", "Literature review (written chapter, about 3,000 words)."),
        ("6", "\\textit{Proposal and literature review} submitted (graded)."),
        ("7--12", "Research; weekly progress meetings with the supervisor."),
        ("12", "\\textit{Progress report} (graded)."),
        ("13--14", "Research continues; presentation preparation."),
        ("15", "\\textit{Interim results presentation} (25 minutes plus questions)."),
    ],
    assess=[
        ("Proposal and literature review", "25\\%"),
        ("Progress report", "25\\%"),
        ("Interim results presentation", "25\\%"),
        ("Supervisor's assessment of progress (effort, independence, rigour)", "25\\%"),
    ],
    texts=[
        r"The primary literature for the thesis topic.",
        r"Open-data portals: GWOSC, CERN Open Data, SDSS, MAST (TESS/Kepler), Gaia Archive, Planck Legacy Archive.",
        r"U.~Alon. ``How to choose a good scientific problem''. \emph{Molecular Cell} \textbf{35}, 726 (2009).",
    ],
)

THS402 = dict(
    code="THS 402", title="Senior Thesis II and Defence", kind="ths", hours="8 Hours/Week",
    prereq="THS 401",
    models="MIT 8.THU; Princeton senior thesis and departmental exam; Oxford MPhys",
    rationale=r"""The second semester completes the research and turns it into a 10,000--15,000-word thesis written in \LaTeX, presented publicly and defended orally before the examiner together with the Part~C viva. The thesis must earn C or better for the degree to be awarded, and A$-$ or better for First Class Honours.""",
    clos=[
        ("Complete an original piece of physics research.", "Create", "PLO7"),
        ("Write a thesis that meets professional standards of rigour, clarity and presentation.", "Create", "PLO8"),
        ("Evaluate the significance and limitations of the work.", "Evaluate", "PLO7, PLO3"),
        ("Defend the thesis in an oral examination.", "Evaluate", "PLO8, PLO1"),
    ],
    schedule=[
        ("1--8", "Complete the research."),
        ("9", "Full thesis draft (10,000--15,000 words, \\LaTeX)."),
        ("10--11", "Editor's feedback; revisions."),
        ("12", "Final checks: figures, references, reproducibility of code and data."),
        ("13", "\\textit{Thesis submitted}."),
        ("14", "\\textit{Poster or public talk}."),
        ("16", "\\textit{Oral defence} (45 minutes), combined with the Part~C viva."),
    ],
    assess=[
        ("Thesis document", "60\\%"),
        ("Oral defence", "25\\%"),
        ("Poster or public talk", "15\\%"),
    ],
    assess_note=r"Thesis marking rubric: originality and significance 20\% $\cdot$ correctness and rigour 30\% $\cdot$ command of the literature 15\% $\cdot$ quality of analysis and uncertainty 15\% $\cdot$ clarity of writing and figures 20\%.",
    texts=[
        r"The primary literature for the thesis topic.",
        r"N.~J.~Higham. \emph{Handbook of Writing for the Mathematical Sciences}, 3rd ed. SIAM.",
        r"A.~Gopen and J.~Swan. ``The science of scientific writing''. \emph{American Scientist} \textbf{78} (1990).",
    ],
)

# Placeholders shown in the semester tables for S11-S12.
OPT1 = dict(code="OPT 4x1", title="Major Option I", kind="opt", hours="4 Hours/Week")
ELE1 = dict(code="ELE 4xx", title="Elective I", kind="opt", hours="4 Hours/Week")
OPT2 = dict(code="OPT 4x2", title="Major Option II", kind="opt", hours="4 Hours/Week")
ELE2 = dict(code="ELE 4xx", title="Elective II", kind="opt", hours="4 Hours/Week")

SEMESTERS_Y4 = [
    ("Tenth Semester", "Spring 2030 (7 Jan -- 28 Apr 2030)", [PHY401, PHY402, LAB401]),
    ("Eleventh Semester", "Summer 2030 (6 May -- 25 Aug 2030)", [OPT1, ELE1, THS401]),
    ("Twelfth Semester", "Autumn 2030 (2 Sep -- 22 Dec 2030)", [OPT2, ELE2, THS402]),
]

# Major options: (code, title, Oxford model, prerequisites, texts, topics)
OPTIONS = [
    ("OPT 4A", "Astrophysics", "Oxford C1", "PHY 302, PHY 305; PHY 401 recommended",
     r"B.~W.~Carroll and D.~A.~Ostlie, \emph{An Introduction to Modern Astrophysics}",
     "Radiative transfer; stellar structure and the equations of stellar evolution; nuclear burning; white dwarfs, neutron stars and black holes; the interstellar medium; galaxies and galactic dynamics; active galactic nuclei; exoplanet detection (TESS/Kepler data project); large-scale structure."),
    ("OPT 4Q", "Laser Science, Quantum Optics and Quantum Information Processing", "Oxford C2", "PHY 303, PHY 402",
     r"M.~Fox, \emph{Quantum Optics}; C.~J.~Foot, \emph{Atomic Physics}",
     "Quantisation of the electromagnetic field; Fock, coherent and squeezed states; the Jaynes--Cummings model and cavity QED; Bloch equations; photon statistics (Hanbury Brown--Twiss); trapped ions and neutral atoms as qubits; photonic quantum computing; quantum metrology."),
    ("OPT 4C", "Advanced Condensed Matter", "Oxford C3", "PHY 304",
     r"S.~M.~Girvin and K.~Yang, \emph{Modern Condensed Matter Physics}; Ashcroft and Mermin",
     "Second quantisation; Fermi liquids; BCS superconductivity; magnetism and spin waves; the quantum Hall effects; Berry phase and topological insulators; graphene and 2D materials; a computational project (DFT or tight-binding)."),
    ("OPT 4P", "Particle Physics", "Oxford C4", "PHY 305",
     r"M.~Thomson, \emph{Modern Particle Physics}",
     "The Dirac equation; QED calculations ($e^+e^-\\to\\mu^+\\mu^-$); deep inelastic scattering and partons; QCD; the weak interaction and its V$-$A structure; electroweak unification and the Higgs; neutrino physics; a CMS open-data analysis project."),
    ("OPT 4E", "Physics of Atmospheres, Oceans and Climate", "Oxford C5", "PHY 306, PHY 302",
     r"G.~K.~Vallis, \emph{Atmospheric and Oceanic Fluid Dynamics}; R.~T.~Pierrehumbert, \emph{Principles of Planetary Climate}",
     "Atmospheric thermodynamics; radiative balance and the greenhouse effect; rotating fluids, geostrophy and Rossby waves; ocean circulation; climate feedbacks and sensitivity; a reanalysis-data project (ERA5)."),
    ("OPT 4T", "Theoretical Physics", "Oxford C6", "PHY 301, PHY 204, PHY 205; ELE 410 recommended",
     r"T.~Lancaster and S.~J.~Blundell, \emph{Quantum Field Theory for the Gifted Amateur}; D.~Tong, QFT lecture notes",
     "Classical field theory and Noether's theorem; canonical quantisation of the scalar field; path integrals in quantum mechanics and field theory; Feynman rules and perturbation theory; the Dirac field; symmetry breaking and the Goldstone theorem; introduction to renormalisation; the link to statistical field theory."),
    ("OPT 4B", "Biological Physics", "Oxford C7", "PHY 302, PHY 306",
     r"P.~Nelson, \emph{Biological Physics}; R.~Phillips et al., \emph{Physical Biology of the Cell}",
     "Life at low Reynolds number; diffusion and random walks in cells; entropic forces and polymer elasticity; molecular motors; membranes and electrostatics in solution; nerve impulses; gene regulation as dynamics; single-molecule data analysis."),
]

# Electives: (code, title, prerequisites, text, notes)
ELECTIVES = [
    ("ELE 410", "Mathematical Methods III: group theory, Lie algebras, tensors, differential forms, manifolds", "MTH 201, PHY 206", "Jeevanjee; Zee", "Recommended with OPT 4T"),
    ("ELE 411", "Astrophysics (if not taken as an option)", "PHY 302", "Ryden and Peterson", "--"),
    ("ELE 412", "Plasma Physics", "PHY 205, PHY 302", "Chen", "--"),
    ("ELE 413", "Physics of Energy", "PHY 202, PHY 205", "Jaffe and Taylor", "--"),
    ("ELE 414", "String Theory for Undergraduates", "PHY 401, PHY 301", "Zwiebach", "MIT 8.251 model"),
    ("ELE 415", "Data Science and Machine Learning in Physics", "CMP 201", "MIT 8.16 modules", "Computational weights"),
    ("ELE 416", "Philosophy of Quantum Theory", "PHY 301", "Albert; Maudlin", "3 essays 60\\%, final paper 40\\%"),
    ("ELE 417", "History of 20th-Century Physics", "--", "MIT STS.042J; Pais", "Essay-based, as ELE 416"),
    ("ELE 418", "Materials Science and Nanotechnology", "PHY 304", "Callister; Dhaka PH~407", "--"),
    ("ELE 419", "Supervised Reading Course", "Instructor's approval", "Agreed reading list", "Weekly summaries 50\\%, essay 50\\%"),
]
