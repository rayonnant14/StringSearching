def Rabin_Karp(text, search_string):
  M = len(search_string)
  if( M == 0):
    raise TypeError("Error! Empty searching string!")
  N = len(text)
  if(N < M):
    raise TypeError("Error! Length of the text smaller than searching string!")

  # search for P ≈ M
  if(sympy.isprime(M)):
    P = M 
  else:
    P = sympy.nextprime(M)

  #create dictionary
  keys = list(set(text))
  values = []
  search_window = text[0 : M]
  for i in range(0, len(keys)):
      values.append(i)
  text_dict = dict(zip(keys, values)) 

  
  hash_value = 0
  curr_hash = 0
  P_i = 0
  for i in range(M):
    P_i = P ** i
    hash_value += P_i * text_dict[search_string[i]]
    curr_hash += P_i * text_dict[search_window[i]]
  P_M = P_i

  comparison_counter = 0
  prev_hash = 0

  for i in range(0, N - M + 1):
    if(i != 0):
      search_window = text[i : (M + i)]
      curr_hash = prev_hash + (text_dict[search_window[-1]] * P_M)

    if (curr_hash == hash_value):
      comparison_counter += M
      if search_string == search_window:
        return (i , comparison_counter)
    
    prev_hash = (curr_hash - text_dict[search_window[0]]) // P

  return (None, comparison_counter)