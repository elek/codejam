
my_reverse([],[]).
my_reverse([A],[A]).
my_reverse(R,[H|T]) :- append(X,[H],R), my_reverse(X,T).

