
my_last(A,[A]).
my_last(A,[Head|Tail]) :- my_last(A,Tail).
