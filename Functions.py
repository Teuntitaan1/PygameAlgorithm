def generatelocation(width, height, tilesize):

    positionlistx = []
    positionlisty = []

    pos = 0

    for j in range(int(width/tilesize)):
        positionlistx.append(pos)
        pos += tilesize

    pos = 0

    for i in range(int(height/tilesize)):
        positionlisty.append(pos)
        pos += tilesize

    return positionlistx, positionlisty

def returnpositive(number):
    if number < 0:
        number *= -1
        return number
    if number == 0 or number > 0:
        return number