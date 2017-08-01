def count_bits(x):
    num_bits = 0
    while bool(x):
        num_bits += x + 1 #num_bits = num_bits + 1        
        x >>= 1
   return num_bits     
