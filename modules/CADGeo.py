PROVINCE:dict = {
    "YT" : "Yukon",
    "SK" : "Saskatchewan",
    "PE" : "Prince Edward Island",
    "NU" : "Nunavut",
    "NS" : "Nova Scotia",
    "NL" : "Newfoundland",
    "BC" : "British Columbia",
    "AB" : "Alberta",
    "MB" : "Manitoba",
    "NB" : "New Brunswick",
    "QC" : "Quebec",
    "ON" : "Ontario",
    "NT" : "Northwest Territories"
}



def getProvinceFullString( province:str ) -> str:
    if len( province ) == 2:
        return PROVINCE[province]
    else:
        return province

def getProvinceAbbreviation( province:str ) -> str:
    if len( province ) == 2:
        return province
    else:
        for k, v in PROVINCE.items( ):
            if v == province:
                return k
            
def checkParameterInput( input:str ) -> bool:
    result:bool = False

    for k, v in PROVINCE.items( ):
        if v == input or k == input:
            result = True
            break

    return result
