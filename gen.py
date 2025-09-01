from openai import  OpenAI


API=  "AIzaSyBzxxo2L-6zL5Gt9wq6v0IvmH-8aQJnxbo"
base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"

Model ="gemini-2.0-flash-exp"


client = OpenAI(api_key=API,base_url=base_url)


def create_completion(input):

    prompt = f"you are a smart ai answer me as a doctor when I ask this: {input}"


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





