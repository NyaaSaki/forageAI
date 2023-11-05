import openai
import context
import kbcontext
import PDLbase as dl
import pdlcontext


gptlog = []
gptlog = context.GetContext
kblog = []
kblog = kbcontext.GetContext
dllog = []
dllog = pdlcontext.AskContext


key = open("key","r").read()
knowledge = open("family.pl").read()

openai.api_key = key
def req(content,model = "gpt-3.5-turbo"):
    gptlog.append(
        {
            "role": "user", "content" : content
        }
    )
    response = openai.ChatCompletion.create(
        model = model,
        messages = gptlog
    )
    gptlog.append(
        {
            "role": "assistant", "content" : response['choices'][0]['message']['content']
        }
    )
    return response['choices'][0]['message']['content'],response["usage"]["total_tokens"]

def query(content,cypher = False,model = "gpt-3.5-turbo"):
    if cypher:
        kblog.append(
        {
            "role": "user", "content" : "Can you convert the question ' " + content + " ' into a prolog query based on the knowledge base given before. only send the prolog query without any text before or after it, only send the query"
        }
    )
    else:
        kblog.append(
        {
            "role": "user", "content" : "answer the question ' " + content + " 'with the given instructions with context to the prolog knowledgebase given before. in one sentence"
        }
    )
    response = openai.ChatCompletion.create(
        model = model,
        messages = kblog
    )
    kblog.append(
        {
            "role": "assistant", "content" : response['choices'][0]['message']['content']
        }
    )
    return response['choices'][0]['message']['content'],response["usage"]["total_tokens"]
    
def remember(content):
        kblog.append(
        {
            "role": "system", "content" : content
        })
        return

    
def dlQuery(content,model = "gpt-3.5-turbo"):
    dllog.append(
        {
            "role": "user", "content" : "Can you convert the question ' " + content + " ' into a datalog query. do not start the query with a + .only send the Datalog query without any text before or after it, only send the query"
        })
    response = openai.ChatCompletion.create(
        model = model,
        messages = dllog
    )
    dllog.append(
        {
            "role": "assistant", "content" : response['choices'][0]['message']['content']
        }
    )
    query = response['choices'][0]['message']['content']
    
    print(query)
    try:
        ans = dl.GetQuery(query)
    except SyntaxError:
        ans = "There was an error : " + query
    except AttributeError:
        ans = "no answers found for query: " + query
        
        
    dllog.append(
        {
            "role": "user", "content" : "The reply to the query ' " + content + " ' was ' " + str(ans) + " '. Can you make this into a simple sentence reply? only give the sentence reply "
        })
    response = openai.ChatCompletion.create(
        model = model,
        messages = dllog
    )
    reply = response['choices'][0]['message']['content']
    
    return query,reply,response["usage"]["total_tokens"]
    
    
def dlRemember(content,model = "gpt-3.5-turbo"):
    dllog.append(
        {
            "role": "user", "content" : "Can you convert the assertion ' " + content + " ' into a datalog code clause for the file given before. only send the Datalog clause code without any text before or after it, only send the code"
        })
    response = openai.ChatCompletion.create(
        model = model,
        messages = dllog
    )
    dllog.append(
        {
            "role": "assistant", "content" : response['choices'][0]['message']['content']
        }
    )
    query = response['choices'][0]['message']['content']
    print(query)
    
    try:
        ans = dl.inpData(query)
    except SyntaxError:
        ans = "There was an error : " + query
    except AttributeError:
        ans = "Invalid assersion : " + query
        
    return query,ans,response["usage"]["total_tokens"]
