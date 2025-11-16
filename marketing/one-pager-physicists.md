# One-Pager for Physicists

## The pitch

We already speak fluently about **UV cutoffs**: Planck length, Planck time, Planck energy.  
We are less disciplined about **IR cutoffs**, despite routinely invoking:

- Hubble radius,  
- de Sitter entropy,  
- recurrence times,  
- horizons and holography.

**Cliche Constants** are a naming scheme that "hardens" these IR limits into two labeled constructs:

- **Cliche Length ℓ^R**  
  \[
  \ell^R = \frac{c}{H_0}
  \]  
  A causal-coherence scale, essentially the Hubble radius.

- **Cliche Time τ^R**  
  \[
  \tau^R = e^{S_{\text{dS}}} t_P
  \]  
  A formal recurrence-style timescale derived from de Sitter entropy and Planck time.

## Why bother?

1. **Pedagogical clarity**

   Students hear "Planck scale" constantly but get a fuzzier story about IR limits: "the universe will eventually do something weird after 10^{10^{120}} years..."  
   Giving those limits names makes the discussion cleaner.

2. **Model-building shorthand**

   In toy models of:

   - emergent spacetime / tensor networks,  
   - cosmological decoherence,  
   - finite-Hilbert-space cosmology,

   it is convenient to say "we cap IR behavior at ℓ^R and τ^R" instead of carrying the full expressions around.

3. **Framing the "end of predictability"**

   τ^R is an explicit symbol you can drop into talks about:

   - loss of predictability in a finite-entropy universe,  
   - whether "history" is a well-defined concept beyond some scale,  
   - what a "final" time slice might mean in theories with de Sitter asymptotics.

## What it is not

- Not a claim that physics **literally breaks** at ℓ^R or τ^R.  
- Not a new dynamical principle or modified gravity theory.  
- Not a replacement for careful treatment of horizons, measure problems, or quantum gravity.

It is:

> A compact notation and story for the IR regime, complementing the Planck story in the UV.

## How to use it in your work

- In papers or talks, you can write:  
  > "We assume that no observer can operationally distinguish histories beyond the Cliche Time τ^R."

- In code, you can use the provided `cliche_constants.py` as a simple helper or define your own variants (for example, replacing H_0 with a time-dependent H(t)).

If you like the idea but prefer different definitions, you can fork the repo and define your own "house IR constants" while keeping the Cliche name as a recognizable meme.
