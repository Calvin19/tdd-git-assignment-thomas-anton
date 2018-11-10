def mean(alist):
    try:
        listclone = alist
        numsum = 0
        numnum = 0
        for item in listclone:
            numsum = numsum + item
            numnum += 1
        finalnum = numsum / numnum
        return finalnum
    except:
        return "Invalid Input, please try again!"


def numrange(alist):
    try:
        fRange = max(alist) - min(alist)
        return fRange
    except:
        return "Invalid Input, please try again!"


def standev(alist):
    return

def variance(alist):
    return
