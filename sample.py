import xml.etree.ElementTree as et

tree = et.parse('Input.xml')

root = tree.getroot()
groups = tree.findall('GRUP')


def find_grup_for_dial(id,dial_grup_list):
    for dial_grup in dial_grup_list:
        label = dial_grup.get("label")
        label_to_match = "0x"+id
        if(label == label_to_match):
            return dial_grup
    return None

global_variables = None 
keywords= None 
dialogues= None 
for group in groups:
    if(group.get('label') == 'GLOB'):
        global_variables = group
    elif(group.get('label') == 'KYWD'):
        keywords = group
    elif(group.get('label') == 'DIAL'):
        dialogues = group

dial_grup_mapping_list = []
count_not_found = 0
if(dialogues!=None):
    print(dialogues)
    dial_group_list = dialogues.findall('GRUP')
    dial_dial_list = dialogues.findall('DIAL')

    
    for dial_dial in dial_dial_list:
        id = dial_dial.get("id")
        dial_grup = find_grup_for_dial(id,dial_group_list)
        if(dial_grup != None):
            dial_grup_mapping_list.append([dial_dial,dial_grup])
        else:
            count_not_found+=1


print(f"count_found = {len(dial_grup_mapping_list)}")
print(f"count_not_found = {count_not_found}")
