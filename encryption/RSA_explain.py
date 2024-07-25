# modula arithmetic, some times called clock arithmetic
# this is a one way function, in which we can't go back to, e.g:
#     12 / 5 = 2,
#     11 % 5 = 1,
#     15 % 5 = 0


"""Diffie-Hellman-Merkle key exchange"""
# Y ^ X (mod P)  ---   equivalent of   <ascii_number> ^ <random_number> (mod <public_key>)
# let Y be 7 and P be 13 (Note: we have to use prime number for both)

"""Alice"""
# picks a random number for X, say 10
# 7 ^ 10 (mod 13) = 4
# sends 4 to Bob.
# repeate the formula, alice uses bobs `10` as Y
# 10 ^ 10 (mod 13) = 3

"""Bob"""
# picks a random number for X, say 2
# 7 ^ 2 (mod 13) = 10
# sends 10 to Alice.
# repeate the formula, bob uses alice `4` as Y
# 4 ^ 2 (mod 13) = 3

"""
    now both Alice and Bob have the number `3`,
    if there is any one between `Alice` and `Bobs`
    communication what he/she will see is only
    Alice's `4` and Bobs `10`, he/she doesn't know
    the random number choosen by Alice and Bobs.
    And know after applying this they both have the number `3`
    the number `3` can be use for a key to encrypt a message
    between each other.

    the numbers should be very big such as 2087
"""


"""---------------------------------------------------------------------------------------"""
# RSA public key cryptography
# using M ^ E (mod N) where `E` is 7
"""
    Alice picks two primes `P` and `Q`,
    say 17 and 19.

    And multiplies them together to get
    323, we call this `N`

    Now we choose another prime number that is publicly known is called `E`
    `N` (along with `E` which is 7) can be published publicly.

    -----------------------------------------------------------------------------

    If Bob wants to send the letter `H` to Alice
    then he takes the ascii value of `H` which is `72`
    and encrypts it with the `N` of 323 using M ^ E (mod N):
    72 ^ 7 (mod 323) = 13

    Bob sends the result (the number 13) to Alice.
    Now if some one see that 13 he can't use it to recreate Bob message, it is impossible

    -----------------------------------------------------------------------------

    To decrypt the message Alice needs to calculate a number called `D` where:
    (7 * D) (mod ((P - 1) * (Q - 1))) = 1
    (P - 1) * (Q - 1) = 16 * 18
    16 * 18 = 288

    In this case `D` is 247 as
    (7 * 247) (mod 288) = 1

    To decrypt the message Alice uses
    M = C ^ D (mod N)
    M = 13 ^ 247 (mod 323)
    M = 72, which is `H` in ascii

    find more explanation on:
    https://www.androidauthority.com/public-key-cryptography-717863/
"""
