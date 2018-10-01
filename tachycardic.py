
def is_tachycardic(myString):

	Count = 0 ;
	myString = myString.strip()
	myString = myString.lower()

	for myChar in myString:
		if myChar == 't' or myChar == 'a' or myChar == 'c' or myChar == 'h' or myChar == 'y' or myChar == 'r' or myChar == 'd':
			Count = Count + 1 

	if Count >= 9 and Count < 13:
		return True

	return False
