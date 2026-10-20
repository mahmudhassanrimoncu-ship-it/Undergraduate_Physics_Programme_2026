# Semester 2: Summer 2027 (Mon 3 May – Sun 22 Aug 2027)

**Year 1, Foundations.** Midterms in week 7 (14–20 Jun). Revision in week 14 (2–8 Aug). Finals in week 15 (9–15 Aug).

| Code | Course | Credits | Type |
|---|---|---|---|
| PHY 102 | Electricity & Magnetism I | 4 | Theory |
| MTH 102 | Multivariable & Vector Calculus | 4 | Theory |
| LAB 101 | Experimental Physics I: Measurement & Uncertainty | 4 | Laboratory |

---

## PHY 102: Electricity & Magnetism I

**Modelled on:** MIT 8.02/8.022, Harvard Physics 15b, Oxford CP2, Dhaka PH 103.
**Prerequisites:** PHY 101, MTH 101 (C or better). MTH 102 taken concurrently.
**Description:** Electrostatics, potential, conductors, currents and circuits, the fields of moving charges (where magnetism emerges from relativity, which is Purcell's signature approach), magnetostatics, induction, AC circuits, Maxwell's equations, electromagnetic waves, and fields in matter.

**Primary:** Purcell & Morin, *Electricity and Magnetism* (3rd ed.), "P&M" below.
**Lectures:** MIT OCW 8.02 (Lewin / TEAL). MITx 8.02x for practice.
**Supplements:** Feynman Vol. II; Tong, *Electromagnetism*; Halliday-Resnick-Walker for an easier pass.

| Week | Topic | Reading | Assessed |
|---|---|---|---|
| 1 | Charge, Coulomb's law, the electric field, continuous distributions | P&M 1.1–1.8 | PS1 |
| 2 | Flux and Gauss's law, with symmetric applications | P&M 1.9–1.15 | PS2 |
| 3 | Electric potential, gradient, divergence, Laplacian | P&M 2 | PS3 |
| 4 | Conductors, capacitance, energy in the field, the method of images (intro) | P&M 3 | PS4 |
| 5 | Currents, Ohm's law, DC circuits, RC circuits | P&M 4 | PS5 |
| 6 | Fields of moving charges; magnetism as a relativistic effect | P&M 5 | PS6 |
| 7 | **Midterm**; light week | – | Midterm |
| 8 | Magnetic field: Biot–Savart, Ampère, vector potential | P&M 6 | PS7 |
| 9 | Electromagnetic induction, Faraday, Lenz, inductance, energy in B | P&M 7 | PS8 |
| 10 | AC circuits, phasors, resonance, impedance | P&M 8 | PS9 |
| 11 | Maxwell's equations, displacement current, EM waves, the Poynting vector | P&M 9 | PS10 |
| 12 | Dielectrics: polarisation, D, bound charge | P&M 10 | PS11 |
| 13 | Magnetic materials: dia-, para- and ferromagnetism, H, hysteresis | P&M 11 | Quiz |
| 14 | Revision | – | – |
| 15 | **Final exam** (3 h) | – | Final |

**Assessment:** problem sets 25% · quizzes 5% · tutorials 10% · midterm 20% · final 40%.

---

## MTH 102: Multivariable & Vector Calculus

**Modelled on:** MIT 18.02, Harvard Math 21a, Oxford CP4 (part), Caltech Ma 1bc, Dhaka Math-103.
**Prerequisites:** MTH 101. **ASE available.**
**Description:** Vectors and matrices, partial derivatives, gradients, optimisation with constraints, multiple integrals in curvilinear coordinates, and the vector calculus of line and surface integrals and the theorems of Green, Gauss and Stokes. This is the language of PHY 102 and PHY 205.

**Primary:** Colley, *Vector Calculus* (or Marsden & Tromba).
**Lectures:** MIT OCW 18.02SC Multivariable Calculus.
**Supplements:** Schey, *Div, Grad, Curl, and All That* (read alongside weeks 9–13); Boas ch. 4–6; Tong, *Vector Calculus*.

| Week | Topic | Assessed |
|---|---|---|
| 1 | Vectors, dot and cross product, lines and planes, determinants | PS1 |
| 2 | Matrices and linear systems (intro), parametric curves, velocity and acceleration | PS2 |
| 3 | Functions of several variables, partial derivatives, the tangent plane | PS3 |
| 4 | Chain rule, gradient, directional derivative, Taylor expansion in 2D/3D | PS4 |
| 5 | Optimisation, the second-derivative test, Lagrange multipliers | PS5 |
| 6 | Double integrals; polar coordinates; the Jacobian | PS6 |
| 7 | **Midterm** | Midterm |
| 8 | Triple integrals; cylindrical and spherical coordinates; moments of inertia | PS7 |
| 9 | Vector fields, line integrals, work, conservative fields and potentials | PS8 |
| 10 | Green's theorem; flux in 2D | PS9 |
| 11 | Surface integrals, flux; the divergence theorem | PS10 |
| 12 | Curl and Stokes' theorem; the physical meaning of div and curl | PS11 |
| 13 | Curvilinear coordinates: grad, div, curl and ∇² in spherical and cylindrical; index notation and ε_ijk | Quiz |
| 14–15 | Revision and **final exam** | Final |

**Assessment:** problem sets 25% · quizzes 5% · tutorials 10% · midterm 20% · final 40%.

---

## LAB 101: Experimental Physics I, Measurement & Uncertainty

**Modelled on:** Harvard 15a/b PSI labs, MIT 8.01/8.02 TEAL labs, Oxford first-year practicals, Caltech Ph 3, Dhaka PL 101.
**Prerequisites:** PHY 101, CMP 101.
**Description:** How to measure, estimate and report uncertainty; propagate errors; fit models with χ²; keep a lab notebook; and write a report in journal style. The experiments are done at home with a smartphone (phyphox), an Arduino and simple apparatus, and every analysis is done in Python.

**Primary:** Hughes & Hase, *Measurements and their Uncertainties* (Oxford).
**Supplements:** Taylor, *An Introduction to Error Analysis*; the phyphox experiment documentation.

| Weeks | Experiment / topic | Report? |
|---|---|---|
| 1 | Lab safety, the notebook, significant figures, types of error, histograms | – |
| 2–3 | **E1 Pendulum and g**: period vs length and amplitude with phyphox; finite-amplitude correction; χ² fit | **Report 1** |
| 4 | Error propagation, weighted means, the Gaussian and Poisson distributions | Pre-lab quiz |
| 5–6 | **E2 Damped oscillator**: spring-mass with the phone accelerometer; measure γ and Q; fit an exponential envelope | **Report 2** |
| 7 | **Oral presentation 1**: E1 or E2 (10 min plus questions) | Oral |
| 8–9 | **E3 RC circuit and the Arduino ADC**: charging and discharging, time constant, calibration of the ADC, systematic errors | **Report 3** |
| 10 | Least squares in depth: residuals, correlated parameters, the goodness of fit | Pre-lab quiz |
| 11–12 | **E4 Magnetic field of a coil or of a long wire**: phone magnetometer vs Biot–Savart; distance dependence; Earth's field as a background | **Report 4** |
| 13 | **E5 Mini-experiment of your own design** (for example, the speed of sound or Newton's law of cooling); notebook only | Notebook |
| 14 | **Oral presentation 2** | Oral |
| 15 | **Final practical**: analyse an unseen dataset under time pressure (2 h) | Final |

**Assessment:** notebook 15% · reports 45% · oral presentations 15% · pre-lab quizzes 10% · final practical 15%.

**Safety:** use a Class 2 laser pointer only and never look into the beam. Use only low-voltage (≤ 12 V DC) circuits, and never work on mains electricity.
