from openai import OpenAI
client = OpenAI()

# Extracting the last message's content



class GPT():
    def __init__(self):
        pass

    def Generate():
        """ The generation function"""
        # Getting all the inputs from the user for us to use
        output =''
        booleen = True
        while booleen == True:
            harmonyormelody = input('Please select if you want harmony or melody')
            if harmonyormelody == 'harmony':
                harmonyormelody = 'chord progression'
                booleen = False 
            elif harmonyormelody == 'melody':
                harmonyormelody = 'melody'
                booleen = False 
            else:
                print('invalid input please try again')

        Genre = input('Please select your genre')
        key = input(f'Please select the key of your {harmonyormelody}')
        length = input('Please select the number of bars')



        my_msg = [
            {"role": "system", "content": f"You are music producer to create a {harmonyormelody}"},
            {"role": "user", "content": f"Please generate me a {harmonyormelody}, in the Genre of \
{Genre}, the key of {key}, and the length of {length}"}
         ]

        completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=my_msg
        )
        content = completion.choices[0].message[-1].content

        print(content)

    def Find_chordprogression():
        pass

    def suggestions():
        pass





if __name__ == '__main__':
    options = ['Generate','Find chord progression or melody', 'suggestions']
    a = GPT()
    a.Generate()


