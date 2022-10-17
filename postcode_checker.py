import postcodeDetails as pc

def findMyDetails(postcode):
    d = pc.PostcodeDetails(postcode)
    print("\n")
    print(d.get_newURL())
    print("Postcode:", d.get_postcode())
    print("Latitude:", d.get_latitude())
    print("Longitude",d.get_longitude())
    print("Region:",d.get_region())

findMyDetails("po20uj")