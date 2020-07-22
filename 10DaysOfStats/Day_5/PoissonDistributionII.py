import math

lambda_A = 0.88
lambda_B = 1.55

EX_A = lambda_A + lambda_A ** 2
EX_B = lambda_B + lambda_B ** 2

C_A = 160 + 40 * EX_A
C_B = 128 + 40 * EX_B

print (round(C_A, 3))
print (round(C_B, 3))


