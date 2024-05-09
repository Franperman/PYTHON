def ips_between(start, end):
    start_duo = [int(x) for x in start.split('.')]
    end_duo = [int(x) for x in end.split('.')]
    
    conce = end_duo[3] - start_duo[3]
    conce += (end_duo[2] - start_duo[2]) * 256
    conce += (end_duo[1] - start_duo[1]) * 256 * 256
    conce += (end_duo[0] - start_duo[0]) * 256 * 256 * 256
    
    return conce


print(ips_between("10.0.0.0", "10.0.0.50"))  # return 50
print(ips_between("20.0.0.10", "20.0.1.0"))  # return 246
print(ips_between("10.0.0.0", "11.0.0.50"))  # return 50 
print(ips_between("10.0.0.0", "10.0.1.0"))   # return 256 
print(ips_between("20.0.0.10", "20.0.1.0"))  # return 246