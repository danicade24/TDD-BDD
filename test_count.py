from count import CountWords

# El if se evalúa como True y se incrementa words
def test_two_words_ending_with_s():
    words = CountWords().count("dogs cats")
    assert words == 2
    
# El if se evalúa como False y no se incrementa words
def test_no_words_at_all():
    words = CountWords().count("dog cat")
    assert words == 0

# Al final del string, la última palabra termina en "r"
def test_words_that_end_in_r():
    words = CountWords().count("car bar")
    assert words == 2

# Al final del string, la última palabra termina en "s" 
def test_word_ending_with_s_at_end():
    words = CountWords().count("cats")
    assert words == 1

# Combinación de palabras que terminan en "r" y "s"
def test_mixed_endings():
    words = CountWords().count("car cats")
    assert words == 2

# Palabras con caracteres no alfabéticos intermedios
def test_non_alpha_characters():
    words = CountWords().count("dogs, cats.")
    assert words == 2
    
# String vacío
def test_empty_string():
    words = CountWords().count("")
    assert words == 0
    
# String con solo caracteres no alfabéticos
def test_only_non_alpha():
    words = CountWords().count("!!!")
    assert words == 0