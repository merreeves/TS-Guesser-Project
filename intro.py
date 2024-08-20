# Project Overview: 
    # Input and Output
        # Input: carestian (given from a database) and internal (marcos code) coordinates of the reactant(t=0) and product(t=1) stuctures, their density matrices(gamma), 
        # their energies(E) (get from pyscf (preferred) or guassian) and corresponding energy gradient(gradE) (same as before, can use calc from marcos opt code, will give E and gradE, gradE will be CC but can convert to IC with marcos code)

        # Output: the 't' corresponding to the reaction's transition state, the number of incorrect negative Hessian eigenvalues at the TS,
        # and the number of iterations to converge to the TS. There will be four different models to obtain this 't'.     
    
    # Models
        # 1) Set t=0.5, compute the average between the internal coordinates of the reactant and the product, then compute the energy at the
        #    average (transition state).

        # 2) Start with the function x(t) = t*qr + (1-t)*qp, carry out one-dimensional optimization (use scipy opt) to find 't' such that 
        #    the energy of the structure corresponding to said 't' is maximized, this structure will be the transition state: 
        #    t = max(t) E(x(t)). Solve for energy using SE.

        # 3) Use approximate density matrices(gamma~) and atomic orbitals. First compute the overlap matrix of xt; S(xt) 
        #    yt = t*gamma~r + (1-t)*gamma~q. Compute the eigenvalues of S(xt)^(1/2)*gamma~t*S(xt)^(1/2), then find the closest idempotent 
        #    matrix M. Replace the first n eigenvalues with 1, and set the rest to zero.
                # ask if he can walk through this with me because I'm pretty confused

        #    There are three errors associated with this model are the following:
        #    errorA = (1/sqrt(n)) * sum(eigenvalues after - eigenvalues before)
        #    errorB = last eigenvalue in - first eigenvalue out
        #    errorC = eigenvalue(n-1) - eigenalue(1?)
        
        # 4) Fitting the intrinstic reaction coordinate into a quadratic/sextic model, use sympy to find all the parameters. I'll need to
        #    sit down with Dr. Ayers for this. 

# Questions:
    # 1) Is there a test reaction I can use?
    # H + H2 -> H2 + H, then LiH + H -> H2 + Li

    # 2) Exactly what code am I using for this project? I know Marco is managing mulitple different branches, do I just use main?
    # only thing i really need is main, ask marco 

    # 3) How do I compute the average between the internal coordinates? V- space level?
    # see notes

    # 4) How to I solve the SE for the second model, if I use Gaussian to do that how exactly do I do that? What methods, basis, etc.?
    # Hartree Fock, see note, can also use pyscf

    # 5) Could you please walk me through the third model? I am pretty confused for stuff like finding overlap matrix.
    # 

    # 6) I want to start my own branch for this code, where should I begin a folder with this code?
    #  folder called ts guesser in gopt/gopt

    # 7) How am I receiving the input? Is it from a file?
    # iodata object, 