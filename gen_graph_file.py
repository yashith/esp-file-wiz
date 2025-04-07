
import xml.etree.ElementTree as et
from Structs import Info
import networkx as nx

import dash
from dash import html, Output, Input, dcc
import dash_cytoscape as cyto

tree = et.parse('resources/approach.xml')

root = tree.getroot()
groups = tree.findall('GRUP')


#to get the maching pair of GRUP and DIAL
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



nodes = []
edges = []

def generate_graph_one_dial_branch(bname,nodes,edges,dial_grup_mapping_list):
    
    for dial_grup_map in dial_grup_mapping_list:
        # Generate for branch topic DIAL

        dial = dial_grup_map[0]   
        branch_name = dial.find("BNAM")
        dial_id = None
        # if (branch_name != None and branch_name.text == bname):
        if (branch_name != None):
            dial_id = dial.get("id")
            if(dial.find("FULL")!= None):
                dial_text = "[p]"+dial.find("FULL").text
            else:
                dial_text = "[p] NOT FOUND"
            new_node_dial = {'data':{'id':dial_id,'label':dial_text}}
            nodes.append(new_node_dial)
    
        #Generate for Grup -> Info
        grup = dial_grup_map[1] 
        info_list = grup.findall("INFO")
        for info in info_list:

            info_id = info.get("id")
            nam1_list = info.findall("NAM1")
            info_text = ""
            for nam1 in nam1_list:
                if nam1!=None : info_text = info_text +"\n" + nam1.text
            
            new_node_info = {'data':{'id':info_id,'label':info_text}}
            nodes.append(new_node_info)
            next_topics = info.findall("TCLT") 
            if next_topics != None and len(next_topics) != 0:
                if dial_id != None:
                    new_edge_dial_to_info = {'data': {'source': dial_id, 'target': info_id}}
                    edges.append(new_edge_dial_to_info)

                for next_topic in next_topics:
                    next_topic_id = next_topic.text
                    new_edge_info_to_next_topic = {'data': {'source': info_id, 'target': next_topic_id}}
                    edges.append(new_edge_info_to_next_topic)

generate_graph_one_dial_branch("079850fb",nodes,edges,dial_grup_mapping_list)




def validate_elements(nodes,edges):
    """
    Returns a cleaned list of elements where all edges reference existing nodes.
    """
    # Step 1: Get set of all valid node IDs
    node_ids = {el['data']['id'] for el in nodes}

    # Step 2: Filter edges that have valid source and target
    valid_edges = []
    for edge in edges:
        data = edge['data']
        if 'source' in data and 'target' in data:
            if data['source'] in node_ids and data['target'] in node_ids:
                valid_edges.append(edge)
            else:
                print(f"⚠️ Removed invalid edge: {data}")

    
    return nodes+valid_edges

# validate edges with non-existing nodes
final_elements = validate_elements(nodes,edges)



def dash_to_nx(elements):
    G = nx.Graph()
    for el in elements:
        data = el['data']
        if 'source' in data and 'target' in data:
            G.add_edge(data['source'], data['target'])
        else:
            G.add_node(data['id'], **data)
    return G

G = dash_to_nx(final_elements)
nx.write_graphml(G, 'approach.graphml')


################################################# Graph Generation ############################################
# app = dash.Dash(__name__)
#
# app.layout = html.Div([
#     cyto.Cytoscape(
#         id='cytoscape',
#         layout={'name': 'breadthfirst'},
#         style={'width': '100%', 'height': '1000px'},
#         elements=final_elements
#     ),
#     dcc.Interval(id='interval-update', interval=2000, n_intervals=0)  # Update every 2 seconds
# ])
#
# app.run(debug = True)

