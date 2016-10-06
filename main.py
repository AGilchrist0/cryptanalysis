import FrequencyAnalysis
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'YOUR API KEY HERE'
client = swagger.ApiClient(apiKey, apiUrl)

cyphertext = input('Please enter the cyphertext.\n--> ').lower()
print(frequency_analyser.analyse_all_characters(cyphertext))


input('')
