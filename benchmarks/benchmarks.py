import sys
sys.path.append('../')
from algorithms import common
from algorithms import naive 
from algorithms import Rabin_Karp as rk
from algorithms import Boyer_Moore_Horspool as bmh
from algorithms import KMP as kmp

def benchmarks(text_path, pattern_path):
  handle_t_1 = open(text_path, 'r')
  handle_w_1 = open(pattern_path, 'r')
  test_t_1 = handle_t_1.read()
  test_w_1 = handle_w_1.read()
  search_time_naive = []
  search_time_rabin_karp = []
  search_time_boyer_moore_horspool = []
  search_time_kmp = []
  index = 0
  comparison_counter_naive = 0
  comparison_counter_rabin_karp = 0
  comparison_counter_boyer_moore_horspool = 0
  comparison_counter_kmp = 0
  for i in range(100):
    start = datetime.now()
    index, comparison_counter_naive = naive.naive_string_matcher(test_t_1, test_w_1)
    end = datetime.now()
    search_time_naive.append((end - start).total_seconds() * 1000000)

    start = datetime.now()
    index, comparison_counter_rabin_karp = rb.Rabin_Karp(test_t_1, test_w_1)
    end = datetime.now()
    search_time_rabin_karp.append((end - start).total_seconds() * 1000000)

    start = datetime.now()
    index, comparison_counter_boyer_moore_horspool = bmh.Boyer_Moore_Horspool(test_t_1, test_w_1)
    end = datetime.now()
    search_time_boyer_moore_horspool.append((end - start).total_seconds() * 1000000)

    start = datetime.now()
    index, comparison_counter_kmp = kmp.KMP(test_t_1, test_w_1)
    end = datetime.now()
    search_time_kmp.append((end - start).total_seconds() * 1000000)
 
 
  medians = [statistics.median(search_time_naive), statistics.median(search_time_rabin_karp),
             statistics.median(search_time_boyer_moore_horspool), statistics.median(search_time_kmp) ]
  comparisons = [comparison_counter_naive, comparison_counter_rabin_karp, 
                 comparison_counter_boyer_moore_horspool, comparison_counter_kmp]

  return (medians, comparisons)