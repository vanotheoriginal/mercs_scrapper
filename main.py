from urllib.request import urlopen
from bs4 import BeautifulSoup
from emoji import emojize



maps = ['Forest Arena', 'Village', 'Ruins', 'Desert Raid', 'Field by the River', 'Mountain Village',
        'By the Rocks', 'Desert Farm', 'Village on the Hill', 'Widespread Ruins', 'Desert Village',
        'Desert Town', 'Old Village Ruins', 'Night Skirmish', 'Forest Hideout', 'Cavalry Training Ground',
        'Cold Reception', 'Tihr', 'Steppe Farm', 'Village on the Ruins', 'Boarding', 'Riot in Swadian City',
        'Fight for Mines', 'Canyon', 'The Arena', 'Thrifty Village', 'Two Banks of One River', 'Port Assault',
        'Village Defence', 'Nord Town', 'Dugan Gorge', 'Battle on Ice', 'Vaegir Village', 'Steppe Village',
        'Village with a Dam', 'Oasis', 'Sandstorm', 'Village with a Watchtower', 'Bariyye', 'Village Field',
        'Camp']


def __get_map_rotation(curr_map=None):

    rotation = ''
    counter = 1
    for i in maps:
        if i == curr_map:
            i = emojize(f':camel: {curr_map}')
        rotation = rotation + f'{counter}. ' + i + '\n'
        counter = counter + 1
    return rotation


def __get_info():

    html = urlopen('http://www.mbmerc.com/?q=servers')
    bsObj = BeautifulSoup(html.read())
    result = bsObj.find_all("td", class_="with_left_padding")[8:56]

    # counter = 0
    # for i in result:
    #     print(str(counter), i)
    #     counter = counter + 1
    # print(len(result), result[39])

    numbers = [10, 11, 14, 15, 18, 19, 2, 3, 38, 39, 42, 43]

    return [result[i].text for i in numbers]


def __organise():

    info = __get_info()
    server = f'Mercenaries_EU1   {info[0]}\t\t{info[1]}\n' \
             f'Mercenaries_EU2   {info[2]}\t\t{info[3]}\n' \
             f'Mercenaries_EU3   {info[4]}\t\t{info[5]}\n' \
             f'Mercenaries_CW1  {info[6]}\t\t{info[7]}\n' \
             f'Somewhatknown    {info[8]}\t\t{info[9]}\n' \
             f'Unknown                  {info[10]}\t\t{info[11]}\n'

    current_map = info[0]

    return server, current_map


def __update(num: int):
    server, current_map = __organise()
    rotation = __get_map_rotation(current_map)
    if num == 1:
        return server
    return rotation
