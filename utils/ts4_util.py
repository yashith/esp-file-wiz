from xml.etree.ElementTree import Element

def get_master_list(root) -> list[str]:
    '''Takes root Element as a parameter and returns a list of master files'''
    tes4 = root.find("TES4")
    masters = tes4.findall("MAST")
    master_list:list[str] = []
    if(len(masters)>0):
        for master in masters:
            master_name = master.text if master.text != None else ""
            master_list.append(master_name)

    return master_list
            
        
