
plast(A,[A,B]).
plast(C,[Head|T]) :- plast(C,T).
