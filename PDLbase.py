from pyDatalog import pyDatalog as pd
import logging
logging.basicConfig(level=logging.INFO)
#       Data Descriptions 

pd.create_terms('repairs','owns')

#repairs(X,Y) means X can repair Y
+repairs('john','bulb')
+repairs('jack','tv')
+repairs('john','fan')
+repairs('james','ac')

+owns('alice','fan')
+owns('bob','bulb')
+owns('kevin','clock')

pd.create_terms('local','area')
+area('john','north')
+area('jack','south')
+area('james','north')

+area('alice','north')
+area('bob','south')
+area('kevin','north')

pd.create_terms('X','Y','Z')

local(X,Y) <= area(X,Z) & area(Y,Z)
#          Queries 

def inpData(query):
    if query[0] == '+':
        pd.load("""{0} """.format(query))
    else:
        pd.load("""+{0} """.format(query))
    print("""+{0} """.format(query))
    return query + " added to assertions"
    
def GetQuery(query):
    print(pd.ask(query).answers)
    return(pd.ask(query).answers)

def getLog(query):
    pd.pyEngine.Logging = True
    print(pd.ask(query))
    pd.pyEngine.Logging = False
    
    
#inpData("owns('saki','fan')")

getLog("owns('saki',X)")
