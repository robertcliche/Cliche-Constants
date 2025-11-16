// cliche_constants.cpp
//
// Simple CLI to print Planck and Cliche scales.
//
// Build:  g++ -O2 -o cliche_constants_cpp cliche_constants.cpp
// Usage:  ./cliche_constants_cpp [H0]
//   H0 is the Hubble constant in km/s/Mpc (default: 70.0)

#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>

// Physical constants (order-of-magnitude usage)
const double C_LIGHT = 2.99792458e8;     // m/s
const double G_CONST = 6.67430e-11;      // m^3 kg^-1 s^-2
const double H_BAR   = 1.054571817e-34;  // J s
const double KM_TO_M = 1000.0;
const double MPC_TO_M = 3.085677581e22;

double planck_length() {
    return std::sqrt(H_BAR * G_CONST / std::pow(C_LIGHT, 3.0));
}

double planck_time() {
    return planck_length() / C_LIGHT;
}

double cliche_length(double H0_km_s_Mpc) {
    // Convert H0 from km/s/Mpc to 1/s
    double H0_SI = (H0_km_s_Mpc * KM_TO_M) / MPC_TO_M;
    return C_LIGHT / H0_SI;
}

int main(int argc, char* argv[]) {
    double H0 = 70.0; // default

    if (argc >= 2) {
        H0 = std::atof(argv[1]);
        if (H0 <= 0.0) {
            std::cerr << "Invalid H0 value. Must be positive." << std::endl;
            return 1;
        }
    }

    double lp = planck_length();
    double tp = planck_time();
    double lr = cliche_length(H0);

    std::cout << "=== Cliche Constants (order-of-magnitude) ===" << std::endl << std::endl;
    std::cout << "Input:" << std::endl;
    std::cout << "  H0            ~ " << std::fixed << std::setprecision(2)
              << H0 << " km/s/Mpc" << std::endl << std::endl;

    std::cout << "Planck scale:" << std::endl;
    std::cout << "  l_P (length)  ~ " << std::scientific << std::setprecision(3)
              << lp << " m" << std::endl;
    std::cout << "  t_P (time)    ~ " << tp << " s" << std::endl << std::endl;

    std::cout << "Cliche scale:" << std::endl;
    std::cout << "  l_R (length)  ~ " << lr
              << " m   (Cliche Length: c / H0)" << std::endl;
    std::cout << "  tau_R (time)  ~ exp(S_dS) * t_P   (symbolic)" << std::endl << std::endl;

    std::cout << "Notes:" << std::endl;
    std::cout << "  - S_dS is the de Sitter entropy, often quoted as ~1e122." << std::endl;
    std::cout << "  - tau_R is printed symbolically because exp(1e122) is far beyond" << std::endl;
    std::cout << "    any reasonable numerical representation." << std::endl;

    return 0;
}
