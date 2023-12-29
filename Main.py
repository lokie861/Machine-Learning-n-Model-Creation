def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    pattern = ['T','_','_','X','_','_','_','T']
    result = []
    px = 0
    for x in range(len(entries)):
      if x > (len(pattern) - 1):
        px = 0
        
      if pattern[px] == '_':
        result.append(0)
      else:
        result.append(entries[x])
      
      px += 1
      print(result)
    # Write your code here
    return result

records = [19, 2, 0, 87, 1, 40, 80, 77, 77, 77, 77]
print(simulate(records))
# Expected output
# [19, 0, 0, 87, 0, 0, 0, 77, 77, 0, 0]