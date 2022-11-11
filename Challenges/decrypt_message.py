enc = 'PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm'
next = False
woord = ''
uitroep_gevonden = False
vraagteken_gevonden = False


for c in enc:
    print(c)
    print(next)
    print(uitroep_gevonden)
    print(vraagteken_gevonden)
    
    if next:
        woord += c
        next = False
    
    vraagteken_gevonden = c == '?'
    next = vraagteken_gevonden and uitroep_gevonden
    uitroep_gevonden = c == '!'
    
    print(next)
print(woord)


'bericht u juist verwerkt!'