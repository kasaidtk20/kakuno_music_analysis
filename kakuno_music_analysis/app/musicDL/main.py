from .webcommand import Web
from .mp4_mp3 import mp4_mp3

test = False

def main():

    if test:
        web = Web()

        web.quit()
        
        web.test_url()
    
    else:
        web = Web()

        a = input()

        web.quit()

    web.download()

    mp3 = mp4_mp3()
    mp3.all('../../dataU')


    


if __name__ == "__main__":
    main()
