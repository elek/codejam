
palindrome(A) :- palindrome(A,[]).

palindrome(A,A).
palindrome([A|B],Z) :- palindrome(B,X), append([A],Z,X).

