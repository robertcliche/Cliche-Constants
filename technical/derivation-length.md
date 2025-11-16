# Derivation of the Cliche Length ℓ^R

## 1. FRW background

Start with a spatially homogeneous and isotropic Friedmann-Robertson-Walker (FRW) metric:

\[
ds^2 = -c^2 dt^2 + a(t)^2 \left[ \frac{dr^2}{1 - k r^2} + r^2 d\Omega^2 \right],
\]

where a(t) is the scale factor and H(t) = dot{a}/a is the Hubble parameter.

For late times in our universe, observations suggest a Lambda-dominated phase, so H(t) tends toward a nearly constant value H_0 on cosmological timescales.

---

## 2. Hubble radius as a causal scale

Define the **Hubble radius**:

\[
R_H(t) = \frac{c}{H(t)}.
\]

Heuristically, this length marks the distance at which the Hubble flow recessional speed v = H(t) d approaches the speed of light:

\[
v \sim c \quad \text{when} \quad d \sim R_H(t).
\]

While not a strict event horizon, R_H provides a natural **causal coherence scale**: modes with physical wavelength much larger than R_H are effectively super-horizon and cannot maintain simple causal contact with a given observer.

---

## 3. Definition of the Cliche Length

The **Cliche Length** is defined by taking the Hubble radius at (approximately) the current epoch:

\[
\ell^R \equiv R_H(t_0) = \frac{c}{H_0}.
\]

Key points:

- This definition uses only standard cosmological quantities.  
- H_0 is understood as the observational Hubble constant today.  
- ℓ^R is therefore a time-dependent notion in general, but for the conceptual purposes of this repo we freeze it at t_0.

---

## 4. Physical interpretation

- For an observer at t_0, regions on scales much smaller than ℓ^R can exchange signals in principle.  
- On scales much larger than ℓ^R, any notion of **coherent geometry** tied to a single causal patch becomes strained.

Thus, we interpret:

\[
\ell^R = \frac{c}{H_0}
\]

as a **soft upper bound** on the spatial size of a region that can reasonably be treated as a single, causally coherent spacetime domain for that observer.

This is the IR counterpart to the Planck length, where small scales challenge the validity of classical geometry.
