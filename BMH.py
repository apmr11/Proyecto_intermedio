class BMHMatching:
    def __init__(self):
        self.text = ""
        self.ALPHABET_SIZE = 256  # Asegúrate de que el tamaño del alfabeto sea suficiente para cubrir todos los posibles valores ASCII.

    def set_text(self, text):
        self.text = text

    def __char_to_index(self, char):
        return ord(char)

    def __calculate_bad_match_table(self, pattern):
        table = [len(pattern)] * self.ALPHABET_SIZE

        for i in range(len(pattern)):
            table[self.__char_to_index(pattern[i])] = len(pattern) - i - 1

        return table

    def search(self, pattern):
        matches = []
        bad_match_table = self.__calculate_bad_match_table(pattern)
        patt_size = len(pattern)
        text_idx = patt_size - 1 #Pivote

        while text_idx < len(self.text):  #Mientras el pivote esté dentro del texto
            shared_substr = 0 #Te dice cuánto del patrón comparte con el texto

            while shared_substr < patt_size:
                if self.text[text_idx - shared_substr] == pattern[patt_size - shared_substr - 1]:
                    shared_substr += 1
                else:
                    break

            # Checa si el patron fue encontrado, si se encuentra se va a guardar en los matches
            if shared_substr == patt_size:
                matches.append(text_idx - (patt_size - 1)) #Tiene que regresar el índice donde empieza la palabra
                text_idx += patt_size
            else:
                bad_char_index = self.__char_to_index(self.text[text_idx])
                text_idx += max(1, bad_match_table[bad_char_index] - shared_substr)

                

        return matches



