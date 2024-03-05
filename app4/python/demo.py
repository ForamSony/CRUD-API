sample_sentence = [
    "Python is a versatile Programming language",
    "Programming with Python is fun and efficient",
    "Python developers love the simplicity of the language"
]
def word_frequencies_counter(sentences):
  word_frequencies = {}
  for sentence in sentences:
    words = sentence.split()
    for word in words:
      word_frequencies[word] = word_frequencies.get(word, 0) + 1
  return word_frequencies

def most_frequent_words(sentences):
  word_freq_couter = word_frequencies_counter(sentences)
  print(word_freq_couter.get)
  most_freq_words = max(word_freq_couter, key=word_freq_couter.get)
  return most_freq_words, word_freq_couter[most_freq_words]
  

print(word_frequencies_counter(sample_sentence))
print(most_frequent_words(sample_sentence))