import os
import random
import speech_recognition
import time

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
    os.system('clear')  
    try:
        with speech_recognition.Microphone() as mic:
            os.system('clear')
            sr.adjust_for_ambient_noise(source=mic, duration=1)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'




def greeting():    
    os.system('clear')
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
    global i
    i = 0



i = 1



def main():
    os.system('clear') 

    query = listen_command()
    
    for k, v in commands_dict['commands'].items():
        if query in v:
            os.system('clear') 
            print(globals()[k]())

    time.sleep(5)
    return 
        

while i == 1:
    os.system('clear') 
    main()



#if __name__ == '__main__':
#    main()