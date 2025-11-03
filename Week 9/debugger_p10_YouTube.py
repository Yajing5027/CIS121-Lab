def like_or_dislike(events):
	# state = "like"	
	state = None

	# for event in range(events):	
	for event in events:
		# if event != state:	
		if event == state:
			state = "nothing"
		else:
			state = event

	return state

print(like_or_dislike(["like"]))
