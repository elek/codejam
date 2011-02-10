
element_at(Head,[Head|Tail],1).
element_at(X,[Head|Tail],I) :- Y is I-1,element_at(X,Tail,Y).

