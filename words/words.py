import re


class Word(object):

    def get_concordanse(self, text):
        result = []

        sentence_split_regex = re.compile("[?!.]\s(?=[A-Z])")
        words_split_regex = re.compile("[,:;\s]")

        words_result = dict()

        sentences = sentence_split_regex.split(text)
        current_sentence = 1
        for sentence in sentences:
            sentence = sentence.rstrip('.?!')
            # print('sentence = ' + sentence)
            words = words_split_regex.split(sentence)
            for word in words:
                word = word.strip().lower()
                if word:
                    # print('word = ' + word)
                    if word in words_result:
                        word_result = words_result[word]
                    else:
                        word_result = dict()
                        word_result['occurrences'] = 0
                        word_result['sentences'] = []
                    word_result['occurrences'] += 1
                    word_result['sentences'].append(str(current_sentence))
                    words_result[word] = word_result
            current_sentence += 1

        # print(str(words_result))

        keys_sorted = sorted(words_result)
        # print(str(keys_sorted))

        sorted_result = [(key, '{' + str(words_result[key]['occurrences']) + ':' + (','.join(words_result[key]['sentences'])) + '}') for key in keys_sorted]
        # print(str(sorted_result))

        indexed_results = []
        # print(len(sorted_result))
        for i in range(len(sorted_result)):
            letters = 26
            num_char_code = i % letters
            num_char_count = i // letters
            ind = chr(97 + int(num_char_code)) * (num_char_count+1)
            # print('sr = ' + ind + '. ' + sorted_result[i][0] + ' ' + sorted_result[i][1])
            indexed_results.append(ind + '. ' + sorted_result[i][0] + ('&nbsp;'*10) + sorted_result[i][1])

        result = indexed_results

        return result