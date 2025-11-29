# Cliche Constants

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Cliche-Constants is a small, tongue-in-cheek but technically serious way to talk about *infrared* cutoffs in cosmology, in the same spirit that Planck units describe *ultraviolet* cutoffs.

- **Planck Length / Time** $ \ell_P, t_P $: smallest meaningful scales where quantum gravity becomes unavoidable.  
- **Cliche Length / Time** $ \ell^R, \tau^R $: largest meaningful spatial and temporal scales suggested by late-time cosmology.  
- **Cliche-Hot / Cliche-Very-Hot**: upper temperature scales beyond which detailed, local quantum predictions cease to be meaningful, either locally or on cosmic scales.

The goal is not to introduce new fundamental physics, but to give memorable names and symbols to scales that already appear in standard cosmology and semiclassical gravity.

---

## 1. Length and time scales

We work in an FRW universe that is approximately $\Lambda$-dominated at late times and use SI units unless stated otherwise.

### 1.1 Planck scales (UV cutoffs)

$$
\ell_P = \sqrt{\frac{\hbar G}{c^3}}, \qquad
t_P = \sqrt{\frac{\hbar G}{c^5}}.
$$

These are the usual Planck length and time.

### 1.2 Cliche Length (IR length scale)

We define the **Cliche Length** as the Hubble radius for a given value of the Hubble constant $H_0$:

$$
\ell^R \equiv \frac{c}{H_0}.
$$

For a fiducial $H_0 \approx 70\,\text{km}\,\text{s}^{-1}\,\text{Mpc}^{-1}$, this is of order

$$
\ell^R \sim 10^{26}\,\text{m},
$$

comparable to the radius of the observable universe. Intuitively: beyond this scale, structure is no longer causally coherent in any simple, everyday sense.

### 1.3 Cliche Time (IR time scale)

For a late-time de Sitter universe with cosmological constant $\Lambda$, the de Sitter entropy is

$$
S_{\text{dS}} \sim 10^{122}
$$

in dimensionless units for our cosmos (up to order-unity factors).

We define the **Cliche Time** as

$$
\tau^R \equiv e^{S_{\text{dS}}}\, t_P.
$$

This is unimaginably large; instead of attempting to store $\tau^R$ directly as a float, the reference implementation reports

$$
\log_{10}\!\left(\frac{\tau^R}{\text{s}}\right) \approx 10^{122},
$$

which is already far beyond any realistic physical process in our universe.

---

## 2. Temperature scales: Cliche-Hot constants

In addition to length and time, we can ask for **upper temperature scales** beyond which local quantum microphysics ceases to be predictively accessible.

We work with thermal radiation in a region of characteristic size $L$ and use the standard radiation energy density

$$
\rho(T) = a T^4,
\qquad
a = \frac{\pi^2 k_B^4}{15 \hbar^3 c^3}.
$$

The total energy in a sphere of radius $L$ is then

$$
E(T,L) = \rho(T) \cdot \frac{4\pi}{3} L^3.
$$

Gravitational collapse occurs when this energy lies within its own Schwarzschild radius,

$$
R_s = \frac{2 G E}{c^4} \sim L.
$$

Solving for the threshold temperature yields

$$
T_{\mathrm{BH}}(L)
 = \left[\frac{3 c^4}{8\pi G a \, L^2}\right]^{1/4}.
$$

This marks the temperature at which a region of size $L$, filled with radiation, becomes a black hole.

### 2.1 Cliche-Hot (local absolute hot)

We define the **Cliche-Hot temperature** as the collapse temperature for a microscopic reference scale. A natural choice is the Planck length:

$$
T_{\mathrm{cliche\text{-}hot}} \equiv T_{\mathrm{BH}}(\ell_P).
$$

Up to order-unity factors this is comparable to the **Planck temperature**

$$
T_P = \sqrt{\frac{\hbar c^5}{G k_B^2}},
$$

and marks a local *predictive ceiling*: above this, conventional quantum field theory and semiclassical gravity are no longer reliable descriptions of local microphysics.

### 2.2 Cliche-Very-Hot (cosmic absolute hot)

We also define a **cosmic** predictive ceiling by taking the region size to be the Hubble radius:

$$
T_{\mathrm{cliche\text{-}very\text{-}hot}}
  \equiv T_{\mathrm{BH}}(\ell^R)
  = T_{\mathrm{BH}}\!\left(\frac{c}{H_0}\right).
$$

At this temperature, filling the entire Hubble volume with radiation would make it one enormous black hole. You can still talk about coarse observables (total mass, horizon temperature, etc.), but detailed, local quantum state predictions “inside” are no longer accessible to any external observer.

We can summarize:

- **Cliche-Hot**: local absolute hot, where local microphysical predictions fail in principle.  
- **Cliche-Very-Hot**: cosmic absolute hot, where the entire Hubble volume has collapsed.

---

## 3. Conceptual summary

| Quantity           | Symbol                                      | Rough scale                               | Interpretation                                           |
|--------------------|---------------------------------------------|-------------------------------------------|----------------------------------------------------------|
| Planck Length      | $\ell_P$                                   | $\sim 1.6 \times 10^{-35}\,\text{m}$   | Smallest meaningful unit of space                        |
| Cliche Length      | $\ell^R$                                   | $\sim 10^{26}\,\text{m}$               | Largest meaningful coherent length scale (Hubble)        |
| Planck Time        | $t_P$                                       | $\sim 5.4 \times 10^{-44}\,\text{s}$   | Shortest meaningful unit of time                         |
| Cliche Time        | $\tau^R$                                   | $\log_{10} \tau^R \sim 10^{122}$       | Longest meaningful time before exact recurrences         |
| Planck Temperature | $T_P$                                       | $\sim 10^{32}\,\text{K}$               | Onset of local quantum gravity                           |
| Cliche-Hot         | $T_{\mathrm{cliche\text{-}hot}}$          | $\sim T_P$                                | Local “absolute hot” predictive ceiling                  |
| Cliche-Very-Hot    | $T_{\mathrm{cliche\text{-}very\text{-}hot}}$ | Scale set by $T_{\mathrm{BH}}(\ell^R)$ | Cosmic “absolute hot” where the Hubble volume collapses  |

The names *Cliche-Hot* and *Cliche-Very-Hot* are playful, but the underlying scales are standard semiclassical constructions.

---

## 4. Assumptions and caveats

This construction is intentionally simple and pedagogical:

- Background spacetime is taken to be spatially flat FRW with a positive cosmological constant.  
- Late-time evolution is approximated by a de Sitter phase.  
- The Hubble constant $H_0$ is treated as a fixed input; in realistic cosmology it evolves with time.  
- De Sitter entropy is used with its standard semiclassical expression; its fundamental status is still debated.  
- The radiation model assumes an ideal thermal bath with Stefan–Boltzmann scaling.  
- Both Planck and Cliche-style scales are **soft** cutoffs: they mark the breakdown of simple effective descriptions, not exact hard limits.

---

## 5. Python usage

The repository provides a small Python reference implementation.

### 5.1 As a command-line helper

From the top-level directory:

```bash
python cliche_constants.py --H0 70.0
```

This assumes $H_0$ in $\text{km}\,\text{s}^{-1}\,\text{Mpc}^{-1}$ and prints:

- Planck length and time  
- Cliche length for the chosen $H_0$  
- De Sitter entropy estimate  
- $\log_{10}(\tau^R / \text{s})$, the base-10 logarithm of Cliche Time  
- Planck temperature  
- Cliche-Hot temperature (local absolute hot, using $\ell_P$)  
- Cliche-Very-Hot temperature (cosmic absolute hot, using $\ell^R$)

Run with `-h` or `--help` to see command-line options.

### 5.2 As a Python module

After installing the package or adding it to your `PYTHONPATH`:

```python
from cliche_constants import (
    planck_length,
    planck_time,
    cliche_length,
    de_sitter_entropy,
    cliche_time_log10_seconds,
    planck_temperature,
    cliche_hot_temperature,
    cliche_very_hot_temperature,
)

# Default H0 ~ 70 km s^-1 Mpc^-1
lp = planck_length()
tp = planck_time()
lR = cliche_length()
SdS = de_sitter_entropy()
log10_tau = cliche_time_log10_seconds()

Tp = planck_temperature()
T_hot = cliche_hot_temperature()            # local absolute hot
T_very_hot = cliche_very_hot_temperature()  # cosmic absolute hot
```

---

## 6. Language bindings

The intent is to keep the core definitions extremely light so they can be ported to multiple languages:

- `code/python/` – reference implementation and CLI support  
- `code/c/`, `code/cpp/`, `code/go/` – minimal ports for embedding in other projects (numerical values only)

Each directory contains a short `README` and one small source file.

---

## 7. Technical notes and references

For more detailed derivations and discussion, see:

- [`technical/notes.md`](technical/notes.md)

---

## 8. License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute it, with attribution.

See [`LICENSE`](LICENSE) for the full text.
