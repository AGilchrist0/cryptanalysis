class frequency_analyser(object):


    def analyse_all_characters(self,cyphertext):
        characters = set(cyphertext)
        frequency = dict()
        for character in characters:
            n = 0
            for index in cyphertext:
                if character == index: n += 1
            frequency[character] = n
        return frequency

    def character_percentages(self,cyphertext):
        characters = set(cyphertext)
        frequency = dict()
        total_characters = float(len(cyphertext))
        print(total_characters)
        for character in characters:
            n = 0
            for index in cyphertext:
                if character == index: n += 1
            frequency[character] = "{0:.2f}".format(n/total_characters*100)
        return frequency
