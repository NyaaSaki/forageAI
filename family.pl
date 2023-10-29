woman(saki).
woman(slepo).
woman(gucci).
woman(zofia).
woman(alia).
woman(ciara).
man(jingyuan).
man(neuvilette).
man(zahleh).



married(saki,ciara).

married(ciara,saki).

married(gucci,jingyuan).

married(gucci,neuvilette).

married(X,Y):- married(Y,X).

% parent(A,B) means A is the parent of B

parent(saki,zofia).

parent(saki,zahleh).

parent(saki,alia).

parent(gucci,zofia).

parent(gucci,zahleh).

parent(slepo,alia).





child(X,Y):- parent(Y,X).


siblings(saki,gucci).


siblings(X,Y):- parent(X,Z),parent(Y,Z),!.
siblings(X,Y):- siblings(Y,X).

