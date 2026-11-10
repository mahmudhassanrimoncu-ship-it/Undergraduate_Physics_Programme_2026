# Semester 4: Autumn 2028 (Mon 17 Jul – Sun 17 Dec 2028)

**Year 2, Core Physics I.** 4 courses. Midterms in week 11 (25 Sep – 1 Oct). Revision in week 20 (27 Nov – 3 Dec). Finals in week 21 (4–10 Dec). **Part A and viva in week 22 (11–17 Dec).**

| Code | Course | Credits | Type | Was in (12-term) |
|---|---|---|---|---|
| PHY 201 | Quantum Physics I | 4 | Theory | S4 |
| PHY 205 | Electrodynamics | 4 | Theory | S6 |
| CMP 201 | Computational Physics II: Numerical Methods | 4 | Computational | S6 |
| PHY 306 | Fluids, Nonlinear Dynamics & Complexity | 4 | Theory | S9 |
| EXM 200 | **Part A** (Annual Examination II) | 4 | Exam + viva | S6 |

**Prerequisites taken alongside rather than before** (the only changes from the 12-term version):

- **PHY 306:** CMP 201 taken concurrently.

> **About the week numbers.** The course syllabi below are the same as in the 12-term version, but each course now runs over a 22-week semester at about two-thirds of the pace. The week numbers in the course tables have been converted: syllabus weeks 1–6 now spread over weeks 1–10, the midterm is in week 11, weeks 8–13 spread over weeks 12–19, revision is week 20 and finals are week 21. Problem sets come every two weeks per course instead of every week, so the work per course stays about the same.

---

## PHY 201: Quantum Physics I

**Modelled on:** MIT 8.04, Harvard Physics 143a, Oxford A3, Princeton PHY 208, Caltech Ph 12b, Dhaka PH 302.
**Prerequisites:** PHY 103, MTH 103, MTH 104.
**Primary:** Griffiths & Schroeter, *Introduction to Quantum Mechanics* (3rd ed.), ch. 1–4.
**Lectures:** MIT OCW 8.04 Quantum Physics I (Zwiebach).
**Supplements:** Zwiebach, *Mastering Quantum Mechanics*; French & Taylor; Feynman Vol. III ch. 1–3.

1. The experimental basis: photoelectric effect, Compton scattering, de Broglie waves, the Mach–Zehnder interferometer
2. Wavefunctions, the Born rule, normalisation, expectation values
3. Momentum space, Fourier transforms, the uncertainty principle
4. The Schrödinger equation, stationary states, the infinite well
5. The harmonic oscillator: analytic and ladder-operator methods
6. Free particle, wave packets, group velocity
7. **Midterm**
8. The delta potential, scattering in 1D, transmission and reflection, tunnelling
9. The finite well, bound states, the variational principle (intro)
10. Formalism: Hermitian operators, eigenfunctions, the generalised uncertainty principle
11. 3D: separation in spherical coordinates, angular momentum, spherical harmonics
12. The hydrogen atom
13. Spin ½, the Stern–Gerlach experiment, Pauli matrices
14. Revision
15. **Final**

---

## PHY 205: Electrodynamics

**Modelled on:** MIT 8.07, Harvard Physics 153, Oxford A2, Princeton PHY 304, Caltech Ph 106bc, Dhaka PH 305.
**Prerequisites:** PHY 102, PHY 103, MTH 201.
**Primary:** Griffiths, *Introduction to Electrodynamics* (4th/5th ed.), ch. 1–12.
**Lectures:** MIT OCW 8.07 Electromagnetism II notes.
**Supplements:** Zangwill, *Modern Electrodynamics* (honours); Jackson (reference).

1. Vector analysis and the Dirac delta; electrostatics revisited formally
2. Laplace's equation, uniqueness theorems, images
3. Separation of variables in Cartesian, spherical and cylindrical coordinates
4. The multipole expansion
5. Electric fields in matter: polarisation, D, linear dielectrics, boundary conditions
6. Magnetostatics: the vector potential, multipoles; magnetic fields in matter
7. **Midterm**
8. Electrodynamics: EMF, Faraday, Maxwell's equations in matter
9. Conservation laws: Poynting's theorem, the Maxwell stress tensor, field momentum and angular momentum
10. EM waves in vacuum, in matter and in conductors; dispersion; waveguides
11. Potentials and gauges, retarded potentials, Jefimenko's equations, Liénard–Wiechert potentials
12. Radiation: electric and magnetic dipole radiation, the Larmor formula
13. Relativistic electrodynamics: the field tensor, covariant Maxwell equations
14. Revision
15. **Final**

---

## CMP 201: Computational Physics II, Numerical Methods

**Modelled on:** Caltech Ph 21/22/121, MIT 8.16 (part), Dhaka PH 307.
**Prerequisites:** CMP 101, MTH 104.
**Primary:** Newman, *Computational Physics* (ch. 6–10).
**Supplements:** Gezerlis, *Numerical Methods in Physics with Python*; *Numerical Recipes*.

1. Numerical linear algebra: LU, conditioning, sparse systems
2. Eigenvalue problems: a finite-difference Schrödinger solver (links to PHY 206)
3. The shooting method; bound states of arbitrary potentials
4. Elliptic PDEs: Jacobi, Gauss–Seidel and SOR relaxation for Laplace and Poisson (links to PHY 205)
5. Parabolic PDEs: FTCS, stability, Crank–Nicolson; the heat equation and the time-dependent Schrödinger equation
6. Hyperbolic PDEs: the wave equation, the CFL condition
7–8. **Midterm project**: wave-packet scattering off a barrier (time-dependent Schrödinger equation)
9. Spectral methods and the FFT for PDEs
10. Monte Carlo II: importance sampling, Markov chains, the Metropolis algorithm
11. The 2D Ising model: phase transition, critical temperature, finite-size effects (links to PHY 302)
12. Molecular dynamics: Lennard-Jones gas, thermostats, radial distribution function
13. Optimisation and model fitting; an introduction to machine learning for physics data
14. Final project
15. **Code review / oral**

**Assessment:** assignments 35% · midterm project 20% · final project 30% · code review 15%.

---

## PHY 306: Fluids, Nonlinear Dynamics & Complexity

**Modelled on:** Oxford B1 (Flows, Fluctuations & Complexity), MIT 8.09 (fluids and chaos parts), MIT 8.292J Fluid Physics, Harvard AM 108.
**Prerequisites:** PHY 204, MTH 201, CMP 201.
**Primary:** Acheson, *Elementary Fluid Dynamics* (weeks 1–10), then Strogatz, *Nonlinear Dynamics and Chaos* (weeks 8–13).
**Supplements:** Tong, *Fluid Mechanics*; Sethna; Tritton.

1. The continuum hypothesis, the material derivative, mass conservation
2. Euler's equations, Bernoulli, hydrostatics
3. Vorticity, Kelvin's circulation theorem, potential flow
4. Viscosity, the Navier–Stokes equations, Poiseuille and Couette flow
5. The Reynolds number, Stokes flow, boundary layers, drag
6. Waves on water, instabilities, a qualitative account of turbulence (Kolmogorov scaling)
7. **Midterm**
8. 1D flows and bifurcations: saddle-node, transcritical, pitchfork
9. 2D flows, the phase plane, limit cycles, the Hopf bifurcation
10. The Lorenz equations, strange attractors, chaos
11. 1D maps, the logistic map, period doubling, Feigenbaum's constant
12. Fractals, Lyapunov exponents, the onset of chaos in experiments
13. Complexity: random walks, diffusion, self-organised criticality, an introduction to networks
14. Revision
15. **Final**

---

## EXM 200: Part A (Annual Examination II)

**Week 22 (11–17 Dec 2028).** Modelled on Oxford's Part A.

| Paper | Content | Time |
|---|---|---|
| A1: Waves & Quantum Physics | PHY 103, PHY 201 | 3 h |
| A2: Thermal Physics, Classical Mechanics & Electrodynamics | PHY 202, PHY 204, PHY 205, PHY 306 | 3 h |
| A3: Mathematical & Computational Methods | MTH 201, CMP 201 (written questions only, no coding) | 2 h |
| Viva voce | The year's physics plus your LAB 201 project | 30 min |

You need ≥ 50% to progress to Year 3.
