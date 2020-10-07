##returns array of sentences

import wikipedia
wikipedia.set_lang("it")

def get_description(character_name):
    content = wikipedia.page(character_name)
    print('Character description downloaded')
    description = str(content.content).replace("\n"," ")
    description = description.replace('"',"'")
    return description

def replace_name(character_name,description):
    hint_list = character_name.split(" ")
    print('Removing '+character_name+' Wikipedia from description')
    for hint in hint_list:
        description = str(description).replace(hint,'XXXX')
    array_description = description.split(". ")
    print('Removing '+character_name+' Wikipedia from description.... COMPLETE',end='\r')
    return array_description

def get_wiki_hints(character_name):
    description = get_description(character_name)
    hint_list = replace_name(character_name,description)
    return hint_list

## replace_name('Silvio Berlusconi','il mio nome è Silvio non Mario. Vivo sulle montagne. Berlusconi si chiama anche Luca')

print(get_wiki_hints('Roberto Baggio'))