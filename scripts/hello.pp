. this script prints "Hello, Catdog!"


. 72, 101, 108, 108, 111, 44, 32, 67, 97, 116, 100, 111, 103, 33


. first we push 72 to the stack for 'H'
(72) inc
push


. add 29 for 'e'
(29) inc
push


. add 7 for 'l'
do 7
    inc
end
. push 2 times for the 'll'
push
push


. add 3 for 'o'
inc
inc
inc
push


. add 17 to set the accumulator to 0, 44 for ','
(61) inc


. subtract 12 for ' '
(12) dec