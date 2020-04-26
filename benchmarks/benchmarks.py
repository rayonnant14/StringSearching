import sys
sys.path.append('../')
from algorithms import common
from algorithms import naive 
from algorithms import Rabin_Karp as rk
from algorithms import Boyer_Moore_Horspool as bmh
from algorithms import KMP as kmp
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

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

def get_report(data_path, testdata_type):
  median = [[]] * 4
  std = [[]] * 4
  comparison = [[]] * 4
  text_names = []
  pattern_names = [] 
  for i in range(0, 4):
    for j in range(0, 4):
      text_names.append(testdata_type + "_t_" + str(i + 1) + ".txt")
      pattern_names.append(testdata_type + "_w_" + str(i + 1) + ".txt")
    median[i], std[i], comparison[i] = benchmarks(data_path + "/" + testdata_type + "_t_" + str(i + 1) + ".txt", 
                                                  data_path + "/" + testdata_type + "_w_" + str(i + 1) + ".txt")
  median_for_table = []
  std_for_table = []
  comparisons_for_table = []

  for i in range(4):
    for j in range(4):
      median_for_table.append(median_good[i][j])
      std_for_table.append(std_good[i][j])
      comparisons_for_table.append(comparison_good[i][j])

  median = np.array(median).T.tolist()
  std = np.array(std).T.tolist()
  comparison = np.array(comparison).T.tolist()

  fig, ax = plt.subplots(figsize=(13, 9))

  labels = [testdata_type + '1', 
            testdata_type + '2',
            testdata_type + '3',
            testdata_type + '4']

  x = np.arange(len(labels)) 
  width = 0.2  

  rects1 = ax.bar(x, median[:][0], width, label='Naive string matcher', yerr = std[:][0], color = 'PaleVioletRed')
  rects2 = ax.bar(x + width, median_good[:][1], width, label='Rabin-Karp',yerr = std[:][1],  color = 'Aquamarine')
  rects3 = ax.bar(x + (width * 2), median[:][2], width, label='Boyer-Moore-Horspool', yerr = std[:][2], color = 'LimeGreen')
  rects4 = ax.bar(x + (width * 3), median[:][3], width, label='Knuth–Morris–Pratt', yerr = std[:][3], color = 'MediumBlue')

  ax.set_ylabel('Median time in microseconds', fontsize = 14)
  ax.set_title('Tests on ' + testdata_type + ' patterns', fontsize = 20)
  ax.set_xticks(x + width + width/2)
  ax.set_xticklabels(labels, fontsize = 14)
  ax.legend(fontsize = 14)

  data = {'testdata text name':  text_names,
          'testdata pattern name':  pattern_names,
          'algorithm' : ['Naive string matcher', 'Rabin-Karp', 'Boyer-Moore-Horspool', 'Knuth–Morris–Pratt'] * 4,
          'median time': median_for_table,
          'std': std_for_table, 
          'number of comparisons' : comparisons_for_table
          }

  df = pd.DataFrame (data, columns = ['testdata text name','testdata pattern name','algorithm',
                                      'median time', 'std', 'number of comparisons'])

  print(df)

