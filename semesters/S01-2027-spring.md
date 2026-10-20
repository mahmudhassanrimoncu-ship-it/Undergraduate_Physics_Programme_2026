# Semester 1: Spring 2027 (Mon 4 Jan – Sun 25 Apr 2027)

**Year 1, Foundations.** Midterms in week 7 (15–21 Feb). Revision in week 14 (5–11 Apr). Finals in week 15 (12–18 Apr). Feedback and Semester Report in week 16.

| Code | Course | Credits | Type |
|---|---|---|---|
| PHY 101 | Classical Mechanics I | 4 | Theory |
| MTH 101 | Calculus for Physicists | 4 | Theory |
| CMP 101 | Computational Physics I: Scientific Python | 4 | Computational |

---

## PHY 101: Classical Mechanics I

**Modelled on:** MIT 8.01/8.012, Harvard Physics 15a/16, Oxford CP1, Caltech Ph 1a, Dhaka PH 101.
**Prerequisites:** A-level physics. MTH 101 taken concurrently.
**Description:** Newtonian mechanics taught with calculus and at the depth of MIT 8.012. Covers kinematics in 1D, 2D and 3D; Newton's laws; momentum and systems of particles; work and energy; oscillations; angular momentum and rigid bodies; non-inertial frames; central forces and orbits. A short survey of fluid statics and dynamics is included, following MIT 8.01 and DU PH 101.

**Primary text:** Kleppner & Kolenkow, *An Introduction to Mechanics* (2nd ed.), "K&K" below.
**Lectures:** MIT OCW 8.01SC Classical Mechanics. Walter Lewin's 8.01 lectures as an alternative.
**Supplements:** Morin, *Introduction to Classical Mechanics*; Feynman Vol. I; Tong, *Dynamics and Relativity*.
**Problem sources:** K&K end-of-chapter problems, Morin, 8.01SC and 8.012 problem sets, Irodov (for starred problems).

| Week | Topic | Reading | Assessed |
|---|---|---|---|
| 1 | Vectors, kinematics, polar coordinates | K&K 1 | PS1 |
| 2 | Newton's laws, inertial frames, free-body diagrams | K&K 2 | PS2 |
| 3 | Forces: friction, drag, tension, constraints; solving equations of motion | K&K 3 | PS3 |
| 4 | Momentum, centre of mass, variable mass (rockets), impulse | K&K 4 | PS4 |
| 5 | Work and kinetic energy, potential energy, conservative forces, ∇U | K&K 5 | PS5 |
| 6 | Energy diagrams, stability, small oscillations; collisions | K&K 6 | PS6 |
| 7 | **Midterm** (90 min, covers weeks 1–6); light week | – | Midterm |
| 8 | Angular momentum of a particle, torque, fixed-axis rotation, moment of inertia | K&K 7 | PS7 |
| 9 | Rigid body motion, rolling, gyroscopes and precession | K&K 8 | PS8 |
| 10 | Non-inertial frames, centrifugal and Coriolis forces, tides | K&K 9 | PS9 |
| 11 | Central forces, the effective potential, Kepler orbits | K&K 10 | PS10 |
| 12 | Harmonic oscillator: damped and driven, resonance, Q factor | K&K 11 | PS11 |
| 13 | Fluids: pressure, buoyancy, continuity, Bernoulli, viscosity basics | 8.01SC fluids notes; DU PH 101 §8–9 | Quiz |
| 14 | Revision. Past MIT 8.01/8.012 finals | – | – |
| 15 | **Final exam** (3 h, cumulative) | – | Final |

**Assessment:** problem sets 25% (lowest dropped) · quizzes 5% · tutorials 10% · midterm 20% · final 40%.

---

## MTH 101: Calculus for Physicists

**Modelled on:** MIT 18.01, Harvard Math 1b, Oxford CP3 (part), Caltech Ma 1a, Dhaka Math-102.
**Prerequisites:** A-level mathematics. **ASE available** (Orientation Term).
**Description:** Single-variable calculus as a physicist uses it: approximation, Taylor series, integration techniques, and series convergence. It ends with complex numbers and first-order ODEs, which are needed for PHY 101 oscillators and for PHY 103.

**Primary:** Strang, *Calculus* (free, MIT OCW).
**Lectures:** MIT OCW 18.01SC Single Variable Calculus.
**Supplements:** Stewart, *Calculus*; 3Blue1Brown, *Essence of Calculus*; Boas ch. 1–2 (series, complex numbers). Apostol, *Calculus* Vol. 1 for honours.

| Week | Topic | 18.01SC unit | Assessed |
|---|---|---|---|
| 1 | Limits, continuity, the derivative, rates of change | Unit 1 | PS1 |
| 2 | Differentiation rules, implicit differentiation, inverse and exponential functions | Unit 1 | PS2 |
| 3 | Linear and quadratic approximation, Newton's method, curve sketching | Unit 2 | PS3 |
| 4 | Optimisation, related rates, mean value theorem, differentials | Unit 2 | PS4 |
| 5 | The definite integral, the fundamental theorem, substitution | Unit 3 | PS5 |
| 6 | Applications: areas, volumes, work, centre of mass, averages | Unit 3 | PS6 |
| 7 | **Midterm**; light week | – | Midterm |
| 8 | Integration by parts, trigonometric integrals and substitutions | Unit 4 | PS7 |
| 9 | Partial fractions, improper integrals, Gaussian and exponential integrals | Unit 4 | PS8 |
| 10 | Sequences, series, convergence tests | Unit 5 | PS9 |
| 11 | Power series, Taylor and Maclaurin series, error bounds, physics approximations | Unit 5 | PS10 |
| 12 | Complex numbers, Euler's formula, polar form, roots of unity | Boas 2 | PS11 |
| 13 | First-order ODEs: separable and linear, with applications (cooling, RC circuits, drag) | Boas 8.1–8.3 | Quiz |
| 14 | Revision | – | – |
| 15 | **Final exam** (3 h) | – | Final |

**Assessment:** problem sets 25% · quizzes 5% · tutorials 10% · midterm 20% · final 40%.

---

## CMP 101: Computational Physics I, Scientific Python

**Modelled on:** Harvard Physics 20 / Applied Math 10, MIT 8.006, Dhaka PH 104 Part II.
**Prerequisites:** None. You already program, so the Python basics move quickly and the course concentrates on physics. **ASE available** as a take-home coding task.
**Description:** Scientific computing applied to the physics of PHY 101 and MTH 101. NumPy, Matplotlib, numerical differentiation and integration, root finding, ODE integrators, Monte Carlo methods, and fitting data with uncertainties. Every week has a small physics model.

**Primary:** Newman, *Computational Physics*, ch. 1–5 and 8.
**Supplements:** Scipy Lecture Notes; NumPy, SciPy and Matplotlib documentation.
**Environment:** Python 3.12+, Jupyter, NumPy, SciPy, Matplotlib. Code goes in `work/S01-2027-spring/CMP101/`.

| Week | Topic | Physics application | Assessed |
|---|---|---|---|
| 1 | Python for scientists: NumPy arrays, vectorisation, plotting | Plotting trajectories, unit handling | A1 |
| 2 | Floating point, round-off and truncation error | Numerical derivatives of x(t); error vs step size | A2 |
| 3 | Numerical integration: trapezoid, Simpson, Gaussian quadrature | Work done by variable forces; the period of a pendulum | A3 |
| 4 | Root finding: bisection, Newton, secant | Equilibria; Kepler's equation | A4 |
| 5 | ODEs I: Euler, and why it fails; energy drift | Projectile with drag | A5 |
| 6 | ODEs II: RK4, adaptive steps, `scipy.integrate.solve_ivp` | Damped driven oscillator, resonance curves | A6 |
| 7–8 | **Midterm project**: simulate a physical system from PHY 101 (for example a non-small-angle pendulum, or rolling with slipping) and validate it against analytic limits | – | Midterm project |
| 9 | Symplectic integrators (leapfrog, Verlet), conservation laws | Planetary orbits; Kepler's laws checked numerically | A7 |
| 10 | Random numbers and Monte Carlo integration | Estimating π; volumes; random walks | A8 |
| 11 | Data, uncertainties and least squares; χ² | Fitting g from phyphox pendulum data | A9 |
| 12 | Fourier transforms (FFT) | The spectrum of an oscillator; your phone's accelerometer | A10 |
| 13–14 | **Final project**: a physics simulation or data analysis of your choice, with a 6–8 page report | – | Final project |
| 15 | **Code review / oral walkthrough** of the final project | – | Oral |

**Assessment:** weekly assignments 35% · midterm project 20% · final project 30% · code review 15%.
