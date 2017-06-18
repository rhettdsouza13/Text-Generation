import numpy

gen = numpy.load("/home/rhett/Documents/TextGen/Lyrics/generated.npy")

for val in gen:
    index = numpy.where(val==1)[0][0]
    if index==26:
        print " ",
    elif index==27:
        print "'",
    else:
        print chr(index+97),
