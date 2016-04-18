import language_check
import re

# Function to test whether a sentence is grammatical
def isGrammatical(sentence):
	tool = language_check.LanguageTool('en-US')
	matches = tool.check(sentence)
	print(matches[0])
	return len(matches) == 0

def languageFilter(sentence):
	badWords = ['fuck', 'shit', 'asshole', 'cunt', 'fag', 'fuk', 'fck', 'fcuk', 'assfuck', 'assfucker', 'fucker',
	'motherfucker', 'asscock', 'asshead', 'asslicker', 'asslick', 'assnigger', 'nigger', 'asssucker', 'bastard', 
	'bitch', 'bitchtits', 'bitches', 'bitch', 'brotherfucker', 'bullshit', 'bumblefuck', 'buttfucka', 'fucka', 
	'buttfucker', 'buttfucka', 'fagbag', 'fagfucker', 'faggit', 'faggot', 'faggotcock', 'fagtard', 'fatass', 'fuckoff', 
	'fuckstick', 'fucktard', 'fuckwad', 'fuckwit', 'dick', 'dickfuck', 'dickhead', 'dickjuice', 'dickmilk', 'doochbag', 
	'douchebag', 'douche', 'dickweed', 'dyke', 'dumbass', 'dumass', 'fuckboy', 'fuckbag', 'gayass', 'gayfuck', 'gaylord', 
	'gaytard', 'nigga', 'niggers', 'niglet', 'paki', 'piss', 'prick', 'pussy', 'poontang', 'poonany', 'porchmonkey',
	'porch monkey', 'poon', 'queer', 'queerbait', 'queerhole', 'queef', 'renob', 'rimjob', 'ruski', 'sandnigger', 'sand nigger', 
	'schlong', 'shitass', 'shitbag', 'shitbagger', 'shitbreath', 'chinc', 'carpetmuncher', 'chink', 'choad', 'clitface', 
	'clusterfuck', 'cockass', 'cockbite', 'cockface', 'skank', 'skeet', 'skullfuck', 'slut', 'slutbag', 'splooge', 'twatlips', 
	'twat', 'twats', 'twatwaffle', 'vaj', 'vajayjay', 'va-j-j', 'wank', 'wankjob', 'wetback', 'whore', 'whorebag', 'whoreface']
	
	wordList = re.sub("[^\w]", " ",  sentence).split()
	
	for x in wordList:
		if x in badWords:
			return true
	return false
			
	