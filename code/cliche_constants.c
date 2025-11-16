/*
 * cliche_constants.c
 *
 * Simple CLI to print Planck and Cliche scales.
 *
 * Build:  cc -O2 -o cliche_constants_c cliche_constants.c -lm
 * Usage:  ./cliche_constants_c [H0]
 *   H0 is the Hubble constant in km/s/Mpc (default: 70.0)
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Physical constants (order-of-magnitude usage) */
const double C_LIGHT = 2.99792458e8;     /* m/s */
const double G_CONST = 6.67430e-11;      /* m^3 kg^-1 s^-2 */
const double H_BAR   = 1.054571817e-34;  /* J s */
const double KM_TO_M = 1000.0;
const double MPC_TO_M = 3.085677581e22;

double planck_length(void) {
    return sqrt(H_BAR * G_CONST / pow(C_LIGHT, 3.0));
}

double planck_time(void) {
    return planck_length() / C_LIGHT;
}

double cliche_length(double H0_km_s_Mpc) {
    /* Convert H0 from km/s/Mpc to 1/s */
    double H0_SI = (H0_km_s_Mpc * KM_TO_M) / MPC_TO_M;
    return C_LIGHT / H0_SI;
}

int main(int argc, char *argv[]) {
    double H0 = 70.0; /* default Hubble constant */

    if (argc >= 2) {
        H0 = atof(argv[1]);
        if (H0 <= 0.0) {
            fprintf(stderr, "Invalid H0 value. Must be positive.\n");
            return 1;
        }
    }

    double lp = planck_length();
    double tp = planck_time();
    double lr = cliche_length(H0);

    printf("=== Cliche Constants (order-of-magnitude) ===\n\n");
    printf("Input:\n");
    printf("  H0            ~ %.2f km/s/Mpc\n\n", H0);

    printf("Planck scale:\n");
    printf("  l_P (length)  ~ %.3e m\n", lp);
    printf("  t_P (time)    ~ %.3e s\n\n", tp);

    printf("Cliche scale:\n");
    printf("  l_R (length)  ~ %.3e m   (Cliche Length: c / H0)\n", lr);
    printf("  tau_R (time)  ~ exp(S_dS) * t_P   (symbolic)\n\n");

    printf("Notes:\n");
    printf("  - S_dS is the de Sitter entropy, often quoted as ~1e122.\n");
    printf("  - tau_R is printed symbolically because exp(1e122) is far beyond\n");
    printf("    any reasonable numerical representation.\n");

    return 0;
}
