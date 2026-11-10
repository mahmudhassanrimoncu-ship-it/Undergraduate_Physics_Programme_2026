"""Write the Semester 1 class timetable for the 8-semester version."""
import datetime as dt, os
from plan import SEMESTERS, week, week_span, fmt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "semesters", "timetables", "S1-2027-spring-timetable.md")
start = SEMESTERS[0][3]
TEACH = list(range(1, 11)) + list(range(12, 20))   # 18 teaching weeks

PHY = [
    "Vectors, coordinate systems, kinematics in 1D (K&K ch. 1)",
    "Kinematics in 2D/3D, polar coordinates, circular motion (K&K ch. 1)",
    "Newton's laws, inertial frames, free-body diagrams (K&K ch. 2)",
    "Friction, drag, tension, constraints; solving equations of motion (K&K ch. 3)",
    "Momentum, centre of mass, systems of particles (K&K ch. 4)",
    "Variable mass, rockets, impulse (K&K ch. 4)",
    "Work, kinetic energy, the work–energy theorem (K&K ch. 5)",
    "Potential energy, conservative forces, F = −∇U (K&K ch. 5)",
    "Energy diagrams, equilibrium, stability, small oscillations (K&K ch. 6)",
    "Collisions: elastic, inelastic, the CM frame (K&K ch. 6)",
    "Angular momentum, torque, fixed-axis rotation, moment of inertia (K&K ch. 7)",
    "Rigid-body dynamics, rolling motion (K&K ch. 7, 8)",
    "Gyroscopes and precession (K&K ch. 8)",
    "Non-inertial frames: centrifugal and Coriolis forces, tides (K&K ch. 9)",
    "Central forces, reduced mass, the effective potential (K&K ch. 10)",
    "Kepler orbits and Kepler's laws (K&K ch. 10)",
    "Damped and driven oscillators, resonance, Q factor (K&K ch. 11)",
    "Fluids: pressure, buoyancy, continuity, Bernoulli, viscosity (8.01SC fluids notes; DU PH 101 §8–9)",
]
MTH1 = [
    "Limits and continuity (18.01SC Unit 1; Strang ch. 2)",
    "The derivative as a rate of change (18.01SC Unit 1; Strang ch. 2)",
    "Differentiation rules, the chain rule (18.01SC Unit 1; Strang ch. 4)",
    "Implicit differentiation; inverse, exponential and log functions (18.01SC Unit 1; Strang ch. 4, 6)",
    "Linear and quadratic approximation, Newton's method (18.01SC Unit 2; Strang ch. 3)",
    "Curve sketching and optimisation (18.01SC Unit 2; Strang ch. 3)",
    "Related rates, the mean value theorem, differentials (18.01SC Unit 2; Strang ch. 3)",
    "Definite integrals, Riemann sums, the fundamental theorem (18.01SC Unit 3; Strang ch. 5)",
    "Substitution (18.01SC Unit 3; Strang ch. 5)",
    "Areas, volumes, work, centre of mass, averages (18.01SC Unit 3; Strang ch. 8)",
    "Integration by parts; trigonometric integrals and substitutions (18.01SC Unit 4; Strang ch. 7)",
    "Partial fractions; improper integrals, Gaussian integrals (18.01SC Unit 4; Strang ch. 7)",
    "Sequences, series and convergence tests (18.01SC Unit 5; Strang ch. 10)",
    "Power series and Taylor series (18.01SC Unit 5; Strang ch. 10)",
    "Taylor error bounds and physics approximations (18.01SC Unit 5; Boas 1)",
    "Complex numbers, polar form, Euler's formula (Boas 2.1–2.11)",
    "Complex exponentials for oscillations, roots of unity (Boas 2.12–2.17)",
    "First-order ODEs: separable and linear, integrating factors (Boas 8.1–8.3)",
]
MTH3 = [
    "Vectors, linear combinations, the geometry of linear equations (18.06SC Unit I)",
    "Elimination and matrix multiplication (18.06SC Unit I)",
    "LU factorisation, inverses, transposes and permutations (18.06SC Unit I)",
    "Vector spaces and subspaces; column space and null space (18.06SC Unit I)",
    "Solving Ax = 0 and Ax = b; the four fundamental subspaces (18.06SC Unit I)",
    "Independence, basis, dimension, rank (18.06SC Unit I)",
    "Orthogonality and projections (18.06SC Unit II)",
    "Least squares (links to CMP 101 fitting and LAB 101) (18.06SC Unit II)",
    "Gram–Schmidt, QR, orthogonal matrices (18.06SC Unit II)",
    "Determinants (18.06SC Unit II)",
    "Eigenvalues and eigenvectors (18.06SC Unit II)",
    "Diagonalisation, powers of matrices, systems of linear ODEs (18.06SC Unit II)",
    "Symmetric matrices and the spectral theorem (18.06SC Unit III)",
    "Positive definite matrices (18.06SC Unit III)",
    "Complex vectors, Hermitian and unitary matrices, Dirac notation preview (18.06SC Unit III)",
    "The SVD and principal components (18.06SC Unit III)",
    "Linear transformations and change of basis (18.06SC Unit III)",
    "Function spaces: Fourier series as an orthogonal basis (18.06SC Unit II)",
]
CMP = {
    1: ("Python for scientists: NumPy arrays, vectorisation", "Plotting trajectories, unit handling"),
    2: ("Plotting, notebooks and Git for code", "Visualising PHY 101 kinematics"),
    3: ("Floating point, round-off and truncation error", "Numerical derivatives of x(t)"),
    4: ("Numerical integration: trapezoid and Simpson", "Work by variable forces"),
    5: ("Gaussian quadrature and error estimates", "Period of a pendulum at large amplitude"),
    6: ("Root finding: bisection, Newton, secant", "Equilibria; Kepler's equation"),
    7: ("ODEs I: Euler's method and why it fails", "Projectile with drag"),
    8: ("ODEs II: RK4, adaptive steps, solve_ivp", "Damped driven oscillator"),
    9: ("Linear algebra in NumPy: solving systems, eigenvalues", "Normal modes of coupled oscillators (with MTH 103)"),
    10: ("Midterm project kickoff", "Your PHY 101 simulation"),
    12: ("Midterm project clinic", "Your PHY 101 simulation"),
    13: ("Symplectic integrators (leapfrog, Verlet)", "Planetary orbits"),
    14: ("Random numbers, Monte Carlo integration", "Estimating π; volumes"),
    15: ("Random walks and diffusion", "Brownian motion"),
    16: ("Data, uncertainties, least squares, χ²", "Fitting g from phyphox data"),
    17: ("Fourier transforms and the FFT", "Spectrum of your phone's accelerometer"),
    18: ("Final project kickoff", "Choose and scope your project"),
    19: ("Final project clinic", "Your project"),
}
GROUP_A = [2, 4, 6, 8, 10, 13, 15, 17, 19]   # PHY 101 and MTH 103 problem sets due (Sun)
GROUP_B = [3, 5, 7, 9, 12, 14, 16, 18]       # MTH 101 problem sets and CMP 101 assignments due (Sun)


def d(w, off, pad=True):
    x = week(start, w) + dt.timedelta(days=off)
    return f"{x.strftime('%a')} {x.day:02d} {x.strftime('%b')}"


L = []
L.append("# Semester 1 Timetable (8-semester version): Spring 2027")
L.append("")
L.append(f"**Teaching starts Monday 1 February 2027.** All times are **Bangladesh time (UTC+6)**. Course content is in [S1-2027-spring.md](../S1-2027-spring.md). The 12-term version of this timetable is [here](../../../semesters/timetables/S01-2027-spring-timetable.md), for comparison.")
L.append("")
L.append("This semester has **4 courses over 22 weeks** (the 12-term S1 has 3 courses over 16 weeks). Each theory course has **1 lecture and 1 recitation a week** instead of 2 lectures and 1 recitation, and **problem sets are due every two weeks** per course, staggered so that two are due each Sunday.")
L.append("")
L.append("## Weekly timetable (teaching weeks 1–10 and 12–19)")
L.append("")
L.append("| Time | Mon | Tue | Wed | Thu | Fri | Sat | Sun |")
L.append("|---|---|---|---|---|---|---|---|")
L.append("| 09:00–12:00 | | | | | **Problem-set block** (self-study) | | |")
L.append("| 10:00–12:30 | | | | | | **Problem-set block** (self-study) | |")
L.append("| 16:00–17:00 | | | | | | **Tutorials**: the two courses whose sets came back that week (30 min each) | |")
L.append("| 17:30–18:30 | | | | | | **Office hours** (any question, any course) | |")
L.append("| 19:30–20:50 | **PHY 101 Lecture** | **MTH 103 Lecture** | **PHY 101 Recitation** (19:30–20:30; opens with the quiz) | **CMP 101 Lab** | | | **Problem-set wrap-up** (19:30–21:30) |")
L.append("| 21:00–22:20 | **MTH 101 Lecture** | **CMP 101 Lecture** | **MTH 101 Recitation** (21:00–22:00; opens with the quiz) | **MTH 103 Recitation** (21:00–22:00; opens with the quiz) | | | **Two problem sets due 23:59** |")
L.append("")
L.append("**Weekly totals:** lectures, recitations and lab about 9.7 h · tutorials and office hours 2 h · problem-set blocks 7.5 h · **about 19–20 h**, the same as the 12-term version.")
L.append("")
L.append("**Problem-set rhythm.** PHY 101 and MTH 103 sets are due on the Sundays of weeks " + ", ".join(map(str, GROUP_A)) + ". MTH 101 sets and CMP 101 assignments are due on the Sundays of weeks " + ", ".join(map(str, GROUP_B)) + ". Each set is about one and a half times the length of a 12-term weekly set.")
L.append("")
L.append("## Lecture calendar: PHY 101, MTH 101 and MTH 103")
L.append("")
L.append("| Week | Mon | PHY 101, Mon 19:30 | MTH 101, Mon 21:00 | MTH 103, Tue 19:30 |")
L.append("|---|---|---|---|---|")
for i, w in enumerate(TEACH):
    L.append(f"| **{w}** | {d(w, 0)} | **L{i+1}**: {PHY[i]} | **L{i+1}**: {MTH1[i]} | **L{i+1}**: {MTH3[i]} |")
    if w == 10:
        L.append(f"| **11** | {d(11, 0)} | **Midterm week** (see below) | | |")
L.append("")
L.append("## Lecture calendar: CMP 101")
L.append("")
L.append("| Week | Lecture (Tue) / Lab (Thu) | Method | Physics application |")
L.append("|---|---|---|---|")
for w in range(1, 20):
    if w == 11:
        L.append(f"| **11** | – | Midterm week: project work (no CMP sessions) | |")
        continue
    m, a = CMP[w]
    L.append(f"| **{w}** | {d(w, 1)} / {d(w, 3)} | {m} | {a} |")
L.append("")
L.append("## Exam and special weeks")
L.append("")
L.append("| Week | Dates | What happens |")
L.append("|---|---|---|")
L.append(f"| 1 | Mon 1 Feb | Teaching starts. No Collection this semester because it's the first one |")
L.append(f"| 11 | {week_span(start, 11)} | **Midterm week.** **PHY 101 midterm {d(11,0)}, 19:30–21:00.** **MTH 103 midterm {d(11,1)}, 19:30–21:00.** **MTH 101 midterm {d(11,2)}, 19:30–21:00.** CMP 101 midterm project work. No problem sets due |")
L.append(f"| 12 | {week_span(start, 12)} | CMP 101 midterm project due {d(12,6)}, 23:59 |")
L.append(f"| 20 | {week_span(start, 20)} | **Revision week.** Lecture slots become review lectures. Recitations become practice-paper sessions. CMP 101 final project due {d(20,6)} |")
L.append(f"| 21 | {week_span(start, 21)} | **Finals.** **PHY 101 final {d(21,0)}, 18:30–21:30.** **MTH 103 final {d(21,1)}, 18:30–21:30.** **MTH 101 final {d(21,2)}, 18:30–21:30.** **CMP 101 code review {d(21,3)}, 19:30** |")
L.append(f"| 22 | {week_span(start, 22)} | Grades, written feedback and your **Semester Report**. Two-week break, then S2 starts on Mon 19 Jul |")
L.append("")
L.append("## Ramadan and Eid")
L.append("")
L.append("Ramadan 2027 is expected to run from about **8 February to 9 March**, with **Eid al-Fitr around 10 March**, subject to the moon sighting. That is weeks 2–6. Eid falls in week 6, five weeks before the midterms (in the 12-term version it falls the week before them). If you are fasting:")
L.append("")
L.append("1. **Ramadan timetable.** Evening slots move to **21:30–23:30**, after tarawih, and the weekend blocks move to late morning.")
L.append("2. **Eid break.** A one-week pause in week 6 (8–14 Mar). The rest of the semester moves one week later and the July break shrinks from two weeks to one, so S2 still starts on Mon 19 Jul.")
L.append("")
L.append("## How a 5-course semester differs")
L.append("")
L.append("S2, S3, S6 and S7 have five courses. There each theory course keeps its weekly lecture but has a recitation **every other week**, alternating with another course, so the class load stays at about 10 h a week. Problem sets are still fortnightly, so two or three are due each Sunday.")
open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote", OUT)
