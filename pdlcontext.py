kb = open("PDLbase.py").read()
AskContext = [{"role" : "system" , "content" : "For the next following questions, you will answer based on the Datalog /n "+ kb + " . when asked to make a query out of text, only give the datalog query and nothing else. combine multiple terms with '&' and use single quotes when referencing strings"},
             {'role': 'assistant', 'content': "Hello, please ask the queries you require and i will write them in a query code based on the pydatalog file given above"} 
]