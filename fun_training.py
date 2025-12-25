with open(r'spam.bin', 'bw') as f:
    for i in range(10):
        f.write(b'\x3d')
        
