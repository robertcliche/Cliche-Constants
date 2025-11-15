#!/usr/bin/env python3
# cliche_constants.py
#
# Tiny helper for computing the Cliche Length ℓ^R and representing
# the Cliche Time τ^R symbolically.
#
# Usage:
#     python cliche_constants.py --H0 70.0

import argparse
import math
from textwrap import dedent

# Physical constants (CODATA-ish; order-of-magnitude is what matters here)
C = 2.99792458e8          # speed of light [m/s]
G = 6.67430e-11           # gravitational constant [m^3 kg^-1 s^-2]
H_BAR = 1.054571817e-34   # reduced Planck constant [J s]


def planck_length() -> float:
    """Return the Planck length ℓ_P in meters."""
    return math.sqrt(H_BAR * G / C**3)


def planck_time() -> float:
    """Return the Planck time t_P in seconds."""
    return planck_length() / C


def cliche_length(H0_km_s_Mpc: float) -> float:
    """
    Compute the Cliche Length ℓ^R = c / H0 in meters.

    Parameters
    ----------
    H0_km_s_Mpc : float
        Hubble constant in km/s/Mpc (e.g. ~70).

    Returns
    -------
    float
        Cliche Length in meters.
    """
    # Convert H0 from km/s/Mpc to 1/s
    km_to_m = 1_000.0
    Mpc_to_m = 3.085677581e22
    H0_SI = (H0_km_s_Mpc * km_to_m) / Mpc_to_m  # [1/s]

    return C / H0_SI


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute the Cliche Length ℓ^R and represent Cliche Time τ^R."
    )
    parser.add_argument(
        "--H0",
        type=float,
        default=70.0,
        help="Hubble constant in km/s/Mpc (default: 70.0)",
    )
    args = parser.parse_args()

    lp = planck_length()
    tp = planck_time()
    lr = cliche_length(args.H0)

    print(dedent(
        f"""
        === Cliche Constants (order-of-magnitude) ===

        Input:
          H0           ~ {args.H0:.2f} km/s/Mpc

        Planck scale:
          ℓ_P (length) ~ {lp:.3e} m
          t_P (time)   ~ {tp:.3e} s

        Cliche scale:
          ℓ^R (length) ~ {lr:.3e} m   (Cliche Length: c / H0)
          τ^R (time)   ~ exp(S_dS) * t_P

        Notes:
          - S_dS is the de Sitter entropy, often quoted as ~1e122.
          - τ^R is printed symbolically because exp(1e122) is far beyond
            any reasonable numerical representation.
        """
    ).strip())


if __name__ == "__main__":
    main()
