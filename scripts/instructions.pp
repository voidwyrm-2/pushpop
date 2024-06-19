. all the instruction in Pushpop


. creates a constant that can be used anywhere(e.g. '(X) inc')
define X 20


. increments the accumulator
inc

. decrements the accumulator
dec

. prints the accumulator
put


. pushes the accumulator to the stack
push


. pops the latest value from the stack and and sets the accumulator to that value
. errors if the stack is empty
pop

. a shortening of 'pop no return'; like pop, but the accumulator isn't changed
popn

. a shortening 'put stack'; prints the stack
puts


. prints the stack as a ascii string
. the bottom of the stack is the first character in the string
show


. do-end block let you separate out chunks of code
do
    inc
end


. loops are done with the amount of loops inbetween parentheses before an instruction
(5) inc


. func-end blocks declare functions
. they don't have names
func
    (10) dec
end

. functions are called by using 'call'
. the input is the Nth function you want to call
. functions are 1-indexed(Lua enjoyers will rejoice)
call 1