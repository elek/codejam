my_flatten([],[]).
my_flatten([H|T],[H|D]) :- \+ is_list(H), my_flatten(T,D).
my_flatten([H|T],D) :- is_list(H), append(X,Y,D),my_flatten(H,X), my_flatten(T,Y).  
