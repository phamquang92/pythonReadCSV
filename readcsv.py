import csv

class AgentState:
    firstname =""
    lastname =""
    id =""
    status =""

class AgentMLS(AgentState):
    mlsid = ""
    name =""
    create_date = ""

statelist = []
mlslist = []
##read AgentState
with open('C:/Users/Quang Pham/Desktop/csv/agentNY.csv', newline='') as csvfile:
     state_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in state_reader:
        agent_state = AgentState()
        agent_state.firstname = row[7]
        agent_state.lastname = row[8]
        agent_state.id = row[11]
        agent_state.status = row[25]
        statelist.append(agent_state)

##read AgentMLS
with open('C:/Users/Quang Pham/Desktop/csv/agentMLS.csv', newline='') as csvfile:
    mls_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in mls_reader:
        agent_mls = AgentMLS()
        agent_mls.name = row[3]
        agent_mls.create_date = row[0]
        agent_mls.id = row[2] 
        mlslist.append(agent_mls)

for stateid in statelist:
    for mlsid in mlslist:
        if (stateid.id == mlsid.id):
            print(mlsid.id)
