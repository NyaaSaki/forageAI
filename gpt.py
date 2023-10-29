import openai
import context
gptlog = []
gptlog = context.GetContext
key = open("key","r").read()

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