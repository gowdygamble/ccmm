import captions 

z = len(captions.shapes) * len(captions.directions) * len(captions.colors)

print("Total combinations:", z)

# plan:
# iterate over all combinations
# up to some maximum in case it gets crazy
# create the caption
# create the video
# save both with some id
# write id + combo to a csv
# can just write the caption to the csv...