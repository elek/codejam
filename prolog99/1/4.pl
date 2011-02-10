
count(0,[]).
count(1,[A]).
count(C,[H|T]) :- count(D,T), C is D + 1.
