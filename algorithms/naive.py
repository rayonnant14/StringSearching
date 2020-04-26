def naive_string_matcher(text, search_string):
  M = len(search_string)
  if( M == 0):
    raise TypeError("Error! Empty searching string!")
  N = len(text)
  if(N < M):
    raise TypeError("Error! Length of the text smaller than length of the pattern!")
  comparison_counter = 0
  for i in range(0, N - M + 1):
    comparison_counter += M
    if text[i : i + M] == search_string:
      return (i, comparison_counter)
  return (None, comparison_counter)