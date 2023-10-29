import openai
import context
import kbcontext
gptlog = []
gptlog = context.GetContext
kblog = []
kblog = kbcontext.GetContext

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

    
