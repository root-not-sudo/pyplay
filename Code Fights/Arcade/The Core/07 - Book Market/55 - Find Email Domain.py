def findEmailDomain(address):

    beginat = address.rfind('@')
    return(address[beginat+1:])
