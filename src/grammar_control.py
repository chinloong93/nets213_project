import language_check

# Function to test whether a sentence is grammatical
def isGrammatical(sentence):
	tool = language_check.LanguageTool('en-US')
	matches = tool.check(sentence)
	print(matches[0])
	return len(matches) == 0
