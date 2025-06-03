from openai import OpenAI
key = ("Your Key Here")
messages=[]


client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)
def completion(message):
    global messages
   
    messages.append(
        {
               "role": "user",
            "content": message
                
        }
    ),
    chat_completion= client.chat.completions.create(messages=messages,
                        model="gpt-4o"        
           )
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Sahota:{message['content']}")

if __name__ == "__main__":
    print(f"Sahota:Hi I am your assistant: ")
    while True:
                user_question =input("Ask me anything: ")
                print(f"Sahota:{user_question}")
                completion(user_question)