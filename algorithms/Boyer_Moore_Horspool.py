def Boyer_Moore_Horspool(text, search_string):
  M = len(search_string)
  if( M == 0):
    raise TypeError("Error! Empty searching string!")
  N = len(text)
  if(N < M):
    raise TypeError("Error! Length of the text smaller than length of the pattern!")
  
  #create dictionary
  keys = list(set(text))
  values = [M] * len(keys)
  text_dict = dict(zip(keys, values)) 
  for key, val in zip(reversed(search_string[0 : M - 1]), range(1, M)):
    if(text_dict[key] == M):
      text_dict[key] = val
  
  search_window =  text[curr_ind : M]
  curr_ind = 0
  comparison_counter = 0
  while(curr_ind <= (N - M)):
    for key, i in zip(reversed(search_window), range(M - 1, -1, -1)):
      comparison_counter += 1
      if(key != search_string[i]):
        if(i < (M - 1)):
          curr_ind += text_dict[search_string[-1]]
        else:
          curr_ind += text_dict[key]
        search_window = text[curr_ind : M + curr_ind ]
        break
      if (i == 0):
        return (curr_ind, comparison_counter)
  return (None, comparison_counter)
