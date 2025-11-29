"""Reference implementation of Planck and Cliche scales.

This module provides:

- Planck length and time (using CODATA 2018 values).
- Cliche length: c / H0.
- De Sitter entropy for a late-time cosmology.
- log10 of the Cliche time in seconds, avoiding overflow.
- Planck temperature.
- Cliche-Hot and Cliche-Very-Hot temperatures:
  - cliche-hot: local "absolute hot" at the Planck length scale.
  - cliche-very-hot: cosmic "absolute hot" at the Hubble radius scale.

The functions are intentionally simple and have only one physical input:
the present-day Hubble constant H0 in km s^-1 Mpc^-1.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

# Fundamental constants (CODATA 2018, rounded)
C = 299_792_458.0               # m / s
G = 6.67430e-11                 # m^3 / (kg s^2)
HBAR = 1.054_571_817e-34        # J s
K_B = 1.380_649e-23             # J / K
MPC_IN_METERS = 3.085_677_581_491_367e22  # m

# Radiation constant a = pi^2 k_B^4 / (15 hbar^3 c^3)
RADIATION_A = math.pi**2 * K_B**4 / (15.0 * HBAR**3 * C**3)


def planck_length() -> float:
    """Return the Planck length in meters."""
    return math.sqrt(HBAR * G / C**3)


def planck_time() -> float:
    """Return the Planck time in seconds."""
    return math.sqrt(HBAR * G / C**5)


def planck_temperature() -> float:
    """Return the Planck temperature in kelvin.

    T_P = sqrt(hbar c^5 / (G k_B^2)).
    """
    return math.sqrt(HBAR * C**5 / (G * K_B**2))


def hubble_si(H0_km_s_Mpc: float = 70.0) -> float:
    """Convert H0 from km s^-1 Mpc^-1 to s^-1 (SI).

    Parameters
    ----------
    H0_km_s_Mpc:
        Hubble constant in km s^-1 Mpc^-1.

    Returns
    -------
    float
        H0 in s^-1.
    """
    return H0_km_s_Mpc * 1_000.0 / MPC_IN_METERS


def cliche_length(H0_km_s_Mpc: float = 70.0) -> float:
    """Return the Cliche length (Hubble radius) in meters.

    l^R = c / H0

    Parameters
    ----------
    H0_km_s_Mpc:
        Hubble constant in km s^-1 Mpc^-1.

    Returns
    -------
    float
        Cliche length in meters.
    """
    H0_si = hubble_si(H0_km_s_Mpc)
    return C / H0_si


def de_sitter_entropy(H0_km_s_Mpc: float = 70.0) -> float:
    """Estimate the de Sitter entropy as a function of H0.

    Uses the semiclassical expression

        S_dS = 3 pi c^3 / (G hbar Lambda)

    with Lambda ~ 3 H0^2 / c^2.

    This yields

        S_dS ~ pi c^5 / (G hbar H0^2).

    For realistic cosmological parameters this is ~ 1e122.
    """
    H0_si = hubble_si(H0_km_s_Mpc)
    return math.pi * C**5 / (G * HBAR * H0_si**2)


def cliche_time_log10_seconds(H0_km_s_Mpc: float = 70.0) -> float:
    """Return log10 of the Cliche time in seconds.

    Cliche time is defined as

        tau^R = exp(S_dS) * t_P

    where S_dS is the de Sitter entropy and t_P is the Planck time.

    The number tau^R is far beyond what can be represented as a float,
    so we work in log10:

        log10(tau^R) = log10(t_P) + S_dS / ln(10).
    """
    t_p = planck_time()
    S_dS = de_sitter_entropy(H0_km_s_Mpc)
    return math.log10(t_p) + S_dS / math.log(10.0)


def collapse_temperature(L_m: float) -> float:
    """Return the collapse temperature T_BH(L) in kelvin for a region of size L.

    T_BH(L) = [ 3 c^4 / (8 pi G a L^2) ]^(1/4)

    where a is the radiation constant.
    """
    if L_m <= 0:
        raise ValueError("L_m must be positive")
    return (3.0 * C**4 / (8.0 * math.pi * G * RADIATION_A * L_m**2)) ** 0.25


def cliche_hot_temperature() -> float:
    """Return the Cliche-Hot temperature in kelvin.

    Defined as the collapse temperature at the Planck length:

        T_cliche-hot = T_BH(l_P).
    """
    return collapse_temperature(planck_length())


def cliche_very_hot_temperature(H0_km_s_Mpc: float = 70.0) -> float:
    """Return the Cliche-Very-Hot (cosmic) temperature in kelvin.

    Defined as the collapse temperature at the Hubble radius:

        T_cliche-very-hot = T_BH(l^R) = T_BH(c / H0).
    """
    L_R = cliche_length(H0_km_s_Mpc)
    return collapse_temperature(L_R)


@dataclass
class Scales:
    """Container for all scales at a chosen H0."""

    H0_km_s_Mpc: float
    planck_length_m: float
    planck_time_s: float
    cliche_length_m: float
    de_sitter_entropy: float
    log10_cliche_time_s: float
    planck_temperature_K: float
    cliche_hot_K: float
    cliche_very_hot_K: float


def compute_scales(H0_km_s_Mpc: float = 70.0) -> Scales:
    """Compute all reference scales for a given H0."""
    lp = planck_length()
    tp = planck_time()
    lR = cliche_length(H0_km_s_Mpc)
    SdS = de_sitter_entropy(H0_km_s_Mpc)
    log10_tau = cliche_time_log10_seconds(H0_km_s_Mpc)
    Tp = planck_temperature()
    Thot = cliche_hot_temperature()
    Tvery = cliche_very_hot_temperature(H0_km_s_Mpc)
    return Scales(
        H0_km_s_Mpc=H0_km_s_Mpc,
        planck_length_m=lp,
        planck_time_s=tp,
        cliche_length_m=lR,
        de_sitter_entropy=SdS,
        log10_cliche_time_s=log10_tau,
        planck_temperature_K=Tp,
        cliche_hot_K=Thot,
        cliche_very_hot_K=Tvery,
    )


def _format_scales(scales: Scales) -> str:
    """Format scales for human-readable CLI output."""
    lines = []
    lines.append(f"H0 = {scales.H0_km_s_Mpc:.3f} km s^-1 Mpc^-1\n")
    lines.append("Planck scales:")
    lines.append(f"  l_P   = {scales.planck_length_m:.3e} m")
    lines.append(f"  t_P   = {scales.planck_time_s:.3e} s")
    lines.append(f"  T_P   = {scales.planck_temperature_K:.3e} K\n")
    lines.append("Cliche length/time scales:")
    lines.append(f"  l^R   = {scales.cliche_length_m:.3e} m (Hubble radius)")
    lines.append(f"  S_dS  ~ {scales.de_sitter_entropy:.3e} (dimensionless)")
    lines.append(
        "  log10(tau^R / s) ~= {:.3e}".format(scales.log10_cliche_time_s)
    )
    lines.append("\nTemperature ceilings:")
    lines.append(f"  T_cliche-hot       ~ {scales.cliche_hot_K:.3e} K (local absolute hot)")
    lines.append(f"  T_cliche-very-hot  ~ {scales.cliche_very_hot_K:.3e} K (cosmic absolute hot)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Entry point for the command-line helper."""
    parser = argparse.ArgumentParser(
        description="Compute Planck and Cliche scales for a given H0."
    )
    parser.add_argument(
        "--H0",
        type=float,
        default=70.0,
        help="Hubble constant in km s^-1 Mpc^-1 (default: 70.0)",
    )
    args = parser.parse_args(argv)
    scales = compute_scales(args.H0)
    print(_format_scales(scales))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
