# Pushpop
Pushpop is a lazily interpreted language I meant as a tool for learning a programming language(I also just felt like making it)

If you can write this in the language you're trying to learn, you can probably do pretty much anything(unless your're learning Haskell, in which case you were doomed from the start)

### Syntax
Pushpop uses an accumulator(intialized to 0) and a stack as memory<br>
The accumulator can be incremented and decremented by the `inc` and `inc` instructions, respectively<br>
And the accumulator pushed to and popped from the stack by the `push` and `pop` instructions, respectively

The accumulator has a max of 127 and wraps around to 0 if it's incremented above 127

Line Comments are started with `.`

See [instructions.pp](./scripts/instructions.pp) for all explanations of all the instructions

See the [interpreters](./interpreters) folder for all the interpreters I've written

<br>

If you ask me to write a Pushpop interpreter in Haskell, I'll steal your kneecaps

<br>

**Licensed under the [MIT License](./LICENSE)**<br>
(tl;dr, you're completely free to do whatever you want with this repo)
