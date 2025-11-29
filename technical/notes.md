# Technical notes for Cliche Constants

These notes sketch the approximations and formulae used in the reference implementation.

## 1. Hubble radius and Cliche Length

We define the Hubble constant input as

- $H_0$ in units of km s$^{-1}$ Mpc$^{-1}$.

To convert to SI units:

$$
H_0^{\text{(SI)}} = H_0 \times \frac{10^3\,\text{m s}^{-1}}{1\,\text{km s}^{-1}}
\times \frac{1}{1\,\text{Mpc}}.
$$

Using

$$
1\,\text{Mpc} \approx 3.08567758 \times 10^{22}\,\text{m},
$$

we obtain the Hubble radius

$$
\ell^R = \frac{c}{H_0^{\text{(SI)}}}.
$$

For $H_0 \approx 70\,\text{km s}^{-1} \text{Mpc}^{-1}$, this gives $\ell^R \sim 10^{26}\,\text{m}$.

## 2. De Sitter entropy

For a universe with positive cosmological constant $\Lambda$, the de Sitter horizon has area

$$
A = 4 \pi R^2, \qquad R = \sqrt{\frac{3}{\Lambda}}.
$$

In semiclassical gravity, the horizon entropy is

$$
S_{\text{dS}} = \frac{A}{4 \, \ell_P^2} = \frac{A c^3}{4 G \hbar}.
$$

Using $R = \sqrt{3/\Lambda}$, this can be written as

$$
S_{\text{dS}} = \frac{3 \pi c^3}{G \hbar \Lambda}.
$$

If we relate $\Lambda$ to $H_0$ through a late-time de Sitter phase,

$$
\Lambda \approx \frac{3 H_0^2}{c^2},
$$

then

$$
S_{\text{dS}} \approx \frac{\pi c^5}{G \hbar H_0^2}.
$$

For realistic cosmological parameters this is of order

$$
S_{\text{dS}} \sim 10^{122}.
$$

## 3. Cliche Time and logarithms

We define the Cliche Time as

$$
\tau^R = e^{S_{\text{dS}}} t_P,
$$

where $t_P$ is the Planck time.

Numerically, $\tau^R$ is far beyond what can be represented as a floating-point number. Instead, we work with its base-10 logarithm:

$$
\log_{10} \tau^R
= \log_{10} t_P + \frac{S_{\text{dS}}}{\ln 10}.
$$

The Python API therefore exposes `cliche_time_log10_seconds`, which returns $\log_{10}(\tau^R / \text{s})$ directly.

This keeps the implementation simple and avoids overflow while still conveying the correct scale.

## 4. Temperature bounds and Cliche-Hot

We model a region of characteristic size $L$ filled with thermal radiation at temperature $T$. The radiation energy density is

$$
\rho(T) = a T^4, \qquad
a = \frac{\pi^2 k_B^4}{15 \, \hbar^3 c^3}.
$$

For a sphere of radius $L$, the total energy is

$$
E(T,L) = \rho(T) V
       = a T^4 \cdot \frac{4\pi}{3} L^3.
$$

A Schwarzschild black hole of mass $M = E/c^2$ has radius

$$
R_s = \frac{2 G M}{c^2} = \frac{2 G E}{c^4}.
$$

Gravitational collapse occurs when this Schwarzschild radius is comparable to the region size:

$$
R_s \sim L.
$$

Taking $R_s = L$ gives

$$
L = \frac{2 G E}{c^4}
  = \frac{2 G}{c^4} a T^4 \frac{4\pi}{3} L^3.
$$

Solving for $T$ yields the collapse temperature

$$
T_{\mathrm{BH}}(L)
 = \left[\frac{3 c^4}{8\pi G a \, L^2}\right]^{1/4}.
$$

This defines an upper temperature for “freely specifiable thermal states” in a region of size $L$; above this, further energy increase drives the region into a black hole.

### 4.1 Cliche-Hot

For the **local** predictive ceiling, we choose $L = \ell_P$, the Planck length, and define

$$
T_{\mathrm{cliche\text{-}hot}} \equiv T_{\mathrm{BH}}(\ell_P).
$$

This is parametrically similar to the Planck temperature

$$
T_P = \sqrt{\frac{\hbar c^5}{G k_B^2}},
$$

and marks the scale where local quantum field theory on a smooth background is no longer a meaningful approximation.

### 4.2 Cliche-Very-Hot

For the **cosmic** predictive ceiling, we choose $L = \ell^R = c / H_0$ and define

$$
T_{\mathrm{cliche\text{-}very\text{-}hot}}
  \equiv T_{\mathrm{BH}}(\ell^R)
  = T_{\mathrm{BH}}\!\left(\frac{c}{H_0}\right).
$$

At this scale, filling the entire Hubble volume with radiation would imply that the whole region is inside a black hole, so any finer-grained description of “what happens inside” is inaccessible to external observers.

## 5. Limitations

- The formulas above ignore the detailed time evolution of $H(t)$ and treat the late universe as effectively de Sitter.
- Order-unity factors in the de Sitter entropy and collapse conditions are left as-is; the main aim is to capture scaling and magnitudes.
- Quantum gravity and microscopic details of horizon entropy and information recovery are not modeled; the construction is semiclassical.
- The temperature bounds assume an ideal radiation-dominated equation of state; more realistic matter content would shift prefactors but not the qualitative picture.

