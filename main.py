import os
import random
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет'],
        'create_task': ['добавить задачу', 'создать заметку'],
        'play_music': ['музыку'],
        'stop_bot': ['стоп']
    }
}


def listen_command():    
    try:
        with speech_recognition.Microphone() as mic:
            #sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
        return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'




def greeting():    
    return 'Привет мой повелитель =) мяу'




def create_task():    
    print('Есть какие планы?')
    query = listen_command()
        
    with open('todo-list.txt', 'a') as file:
        file.write(f'❗️ {query}\n')
        
    return f'Задача {query} добавлена в todo-list!'



def play_music():    
    files = os.listdir('music')
    #random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open music/test.mp3')

    return f'Танцуем под {random_file.split("/")[-1]} 🔊🔊🔊'



def stop_bot():
    i = 0



i = 1

while i == 1:
    query = listen_command()
    
    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())



def main():
    query = listen_command()
    
    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())
        

#if __name__ == '__main__':
#    main()