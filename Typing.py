import random
import time


def speedType():
    phrases = ['Fortnite is an online video game developed by Epic Games and released in 2017.',
               'A hamburger (also burger for short) is a sandwich consisting of one '
               'or more cooked patties of ground meat, '
               'usually beef, placed inside a sliced bread roll or bun. ',
               'Ancient humans were present in Germany at least 600,000 years ago. The first non-modern human fossil '
               '(the Neanderthal) was discovered in the Neander Valley.',
               'Both groups of people caused a loss of species and both altered their behaviour to a degree '
               'after realising their effect on indigenous flora and fauna.',
               "Peter Vernon's mother dies and he is adopted by a squatte"
               "r, Kingston, whose son, Philip, is Peter's age.",
               'The British Columbia Mountaineering Club (BCMC) is a mountaineering organization, based in '
               'Vancouver, British Columbia.',
               'Their morale was further bruised when faced with bowlers of dubious legality and unsympathetic umpires.',
               'Good-Bye is a collection of gekiga short stories by manga artist Yoshihiro Tatsumi.',
               'The adult Bolivian red howler has a well-built body that is capable of attaining a maximum body length.',
               'As winners, Chelsea took part in the 2012 UEFA Super Cup, losin'
               'g 4–1 to Atlético Madrid, the winners of the 2011–12 UEFA Europa League.',
               'Billson was born in Leicester, graduated from Oxford University, and died in Heathfield in Sussex.',
               'The Confirmation is a 2016 Canadian drama film starring Clive Owen, Jaeden Martell, and Maria Bello.',
               'The outbreak was first identified in Wuhan, China, in December 2019.',
               'Trulla dentipora is a neotropical polypore fungus in the family Stecche'
               'rinaceae, and the type species of the genus Trulla.', 'All Systems Down begins with a North Korean '
                'cyberattack that destroys infrastructure across '
                'Western nations, including banks, dams, '
                'and the power grid.', 'Vladimir Stolyarenko ('
                'born 1961) is a Russian banker, and was the '
                'president and chairman of the executive board of Evrofinance '
                'Mosnarbank between June '
                '2006 and 2012.', 'The 2013 Heineken Open was a tennis tournament played on outdo'
                'or hard courts. It was the 38th edition of the Heineken Open, and was p'
                'art of the ATP World Tour 250 series of the 2013 ATP World Tour.', 'ullycorbet is a civi'
                'l parish in the centre of '
                'Co. Monaghan, Ireland north of the town of Ballybay'


               ]
    num = int(input('How many typing rounds do you want: '))
    for i in range(num):
        print(f'Your phrase is:')
        write = phrases[random.randint(0, len(phrases) - 1)]
        print(write)
        input('press Enter to begin')
        start_time = time.time()
        typing = input('type here: ')
        timer = round(time.time() - start_time, 1)
        n1 = 60 / timer
        spaces = [s for s in typing if s == ' ']
        if len(write) < len(typing):
            typer = write
        elif len(write) == len(typing):
            typer = typing
        else:
            typer = typing
        space = len(spaces) + 1
        WPM = n1 * space
        counter, n = 0, 0
        for x in range(len(typer)):
            if write[n] == typing[n]:
                counter += 1
            n += 1
        acc = (counter / len(write))
        percentage = "{:.0%}".format(acc)
        print(f'{percentage} accuracy')
        print(f'WPM:{round(WPM)}')
        print(f'Time taken: {timer} seconds')


speedType()
