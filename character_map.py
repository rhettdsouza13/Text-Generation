import numpy

fsong = open("/home/rhett/Documents/TextGen/Lyrics/1.txt")

data = []

for line in fsong.readlines():
    data.append(line.lower())
data.append("what is li")
mapping=[]

for line in data:
    line = line.replace('\n',' ')
    line = line.replace(',',' ')
    for char in line:
        toadd = numpy.zeros(28)
        if char==" ":
            toadd[26]=1
            # print "Space"
            # print toadd
            mapping.append(toadd)
            continue
        if char=="'":
            toadd[27]=1
            # print "IC"
            # print toadd
            mapping.append(toadd)
            continue
        try:
            toadd[ord(char)-97]=1
            # print "Is a char"
            # print char
            # print toadd
            mapping.append(toadd)

        except:
            # print "Not a letter"
            # print char
            continue
numpy.save("/home/rhett/Documents/TextGen/Lyrics/maps.npy",numpy.array(mapping))

n_input=5
inputs=[]
outputs=[]
for offset in xrange(len(mapping)-n_input):
    inputn = [mapping[i] for i in range(offset, offset+n_input)]
    inputs.append(inputn)
    outputs.append(mapping[offset+n_input])
    out = [inputs,outputs]
numpy.save("/home/rhett/Documents/TextGen/Lyrics/parse.npy",out)
