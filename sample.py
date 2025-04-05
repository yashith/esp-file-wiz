import xml.etree.ElementTree as et

tree = et.parse('Input.xml')

root = tree.getroot()
groups = tree.findall('GRUP')

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


if(dialogues!=None):
    dialogues.
    dial_group_list = dialogues.findall('GRUP')
    dial_dial_list = dialogues.findall('DIAL')
    
    for dial_dial in dial_group_list:
        id = dial_dial.get("id")


def find_grup_for_dial(id,dial_grup_list):
    for dial_grup in dial_grup_list:
        label = dial_grup.get("label")
        if(id = "0x")
