def generate_sentence(num_of_words, hash_table):
    print('REDOOOOOOOO')
    sentence = ''
    distribution = hash_table.return_distribution()

    for i in range(num_of_words):
        word_to_add = hash_table.select_random_word(distribution)
        sentence += word_to_add + ' '

    return sentence
