def found_prefix(string):
  M = len(string)
  pi = [0] * M

  for i in range(1, M):
    j = pi[i-1]
    while ((j > 0) and (string[i] != string[j])):
      j = pi[j-1]

    if (string[i] == string[j]):
       j += 1
    pi[i] = j
  return pi

def KMP(text, search_string):
  M = len(search_string)
  if( M == 0):
    raise TypeError("Error! Empty searching string!")
  N = len(text)
  if(N < M):
    raise TypeError("Error! Length of the text smaller than length of the pattern!")

  pi = found_prefix(search_string)
  k = 0
  l = 0
  comparison_counter = 0
  while(k < N):
    comparison_counter += 1
    if (text[k] == search_string[l]):
      k += 1
      l += 1
      if (l == M):
        return (k - M, comparison_counter) 

    elif(l == 0):
      k += 1
      if (k == N):
        return (None, comparison_counter)
    
    else:
      l = pi[l-1]

  return (None, comparison_counter) 