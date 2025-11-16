package main

import (
	"flag"
	"fmt"
	"math"
)

// Physical constants (order-of-magnitude usage)
const (
	c      = 2.99792458e8   // speed of light [m/s]
	g      = 6.67430e-11    // gravitational constant [m^3 kg^-1 s^-2]
	hbar   = 1.054571817e-34 // reduced Planck constant [J s]
	kmToM  = 1000.0
	mpcToM = 3.085677581e22
)

func planckLength() float64 {
	return math.Sqrt(hbar * g / math.Pow(c, 3))
}

func planckTime() float64 {
	return planckLength() / c
}

func clicheLength(H0_km_s_Mpc float64) float64 {
	H0_SI := (H0_km_s_Mpc * kmToM) / mpcToM // [1/s]
	return c / H0_SI
}

func main() {
	H0 := flag.Float64("H0", 70.0, "Hubble constant in km/s/Mpc")
	flag.Parse()

	lp := planckLength()
	tp := planckTime()
	lr := clicheLength(*H0)

	fmt.Printf("=== Cliche Constants (order-of-magnitude) ===

")
	fmt.Printf("Input:\n")
	fmt.Printf("  H0            ~ %.2f km/s/Mpc\n\n", *H0)

	fmt.Printf("Planck scale:\n")
	fmt.Printf("  l_P (length)  ~ %.3e m\n", lp)
	fmt.Printf("  t_P (time)    ~ %.3e s\n\n", tp)

	fmt.Printf("Cliche scale:\n")
	fmt.Printf("  l_R (length)  ~ %.3e m   (Cliche Length: c / H0)\n", lr)
	fmt.Printf("  tau_R (time)  ~ exp(S_dS) * t_P   (symbolic)\n\n")

	fmt.Println("Notes:")
	fmt.Println("  - S_dS is the de Sitter entropy, often quoted as ~1e122.")
	fmt.Println("  - tau_R is printed symbolically because exp(1e122) is far beyond")
	fmt.Println("    any reasonable numerical representation.")
}

             
