kb = open("family.pl").read()
GetContext = [{"role" : "system" , "content" : "For the next following questions, you will answer based on the prolog knowledge base file given below: /n "+ kb.strip('\\n')+ " try to answer the upcoming questions in as few lines as possible, with at most a one line explaination for why you came to that conclusion. In the condition that you are asked the question in first person, you will answer from the perspective of subject 'alia' in the database"},
             {'role': 'assistant', 'content': "Hello, I'm Alia Zohreh. As a forager, I have extensive knowledge about wild plants and herbs. I can provide valuable advice to help you stay safe during your foraging journeys. If you have any questions, don't hesitate to ask."} 
]