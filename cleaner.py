import json 

tags = {"POP_EST","POP_RANK","POP_YEAR","GDP_MD","GDP_YEAR","ECONOMY","INCOME_GRP","ADM0_DIFF","ADM0_TLC","ADM0_A3_US","ADM0_A3_FR","ADM0_A3_RU","ADM0_A3_ES","ADM0_A3_CN","ADM0_A3_TW","ADM0_A3_IN","ADM0_A3_NP","ADM0_A3_PK","ADM0_A3_DE","ADM0_A3_GB","ADM0_A3_BR","ADM0_A3_IL","ADM0_A3_PS","ADM0_A3_SA","ADM0_A3_EG","ADM0_A3_MA","ADM0_A3_PT","ADM0_A3_AR","ADM0_A3_JP","ADM0_A3_KO","ADM0_A3_VN","ADM0_A3_TR","ADM0_A3_ID","ADM0_A3_PL","ADM0_A3_GR","ADM0_A3_IT","ADM0_A3_NL","ADM0_A3_SE","ADM0_A3_BD","ADM0_A3_UA","WIKIDATAID","NAME_AR","NAME_BN","NAME_DE","NAME_ES","NAME_FA","NAME_FR","NAME_EL","NAME_HE","NAME_HI","NAME_HU","NAME_ID","NAME_IT","NAME_JA","NAME_KO","NAME_NL","NAME_PL","NAME_PT","NAME_RU","NAME_SV","NAME_TR","NAME_UK","NAME_UR","NAME_VI","NAME_ZH","NAME_ZHT","TLC_DIFF","FCLASS_TLC","FCLASS_US","FCLASS_FR","FCLASS_RU","FCLASS_ES","FCLASS_CN","FCLASS_TW","FCLASS_IN","FCLASS_NP","FCLASS_PK","FCLASS_DE","FCLASS_GB","FCLASS_BR","FCLASS_IL","FCLASS_PS","FCLASS_SA","FCLASS_EG","FCLASS_MA","FCLASS_PT","FCLASS_AR","FCLASS_JP","FCLASS_KO","FCLASS_VN","FCLASS_TR","FCLASS_ID","FCLASS_PL","FCLASS_GR","FCLASS_IT","FCLASS_NL","FCLASS_SE","FCLASS_BD","FCLASS_UA","FORMAL_FR","pop_max","pop_min","pop_other"}


def clean(file_name):
    with open(file_name,"r",encoding="utf-8") as f:
       data = json.load(f)
    for feature in data["features"]:
        for prop in list(feature["properties"]):
            if prop in tags:
                feature["properties"].pop(prop)
    with open("cleaned.json", "w", encoding="utf-8") as fp:
        json.dump(data,fp,separators=(",", ":"))
        """
        fp.write('{"type":"FeatureCollection", "features": [\n')
        for i, feature in enumerate(data["features"]):
            json.dump(feature, fp,separators=(",", ":"), ensure_ascii=False)
            if i < len(data["features"]) - 1:
                fp.write(",\n")  # Add a comma between features
        fp.write("]}")
        """
       
                

clean("ne_110m\\us.json")