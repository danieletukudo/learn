from openai import  OpenAI


API=  "YOUR API KEY"
base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"

Model ="gemini-2.0-flash-exp"


client = OpenAI(api_key=API,base_url=base_url)
def create_completion(input):

    prompt = f"you are a smart do this: {input}"


    response = client.chat.completions.create(
        model=Model,
        messages=[

            {"role":"system",

             "content": "you are smart doctor respond well"},

             {

                 "role":"user",
                 "content": prompt
             } ] )
    return response.choices[0].message.content

create_completion("give me an html code I can use to send user text with formdata of object 'text' and then the the text ourput")





