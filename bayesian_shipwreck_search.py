import random


def show_map(sectors):
    map_str = ''
    for j, p in enumerate(sectors):
        map_str += f' {p:.4f} |'
        if (j + 1) % 3 == 0:
            map_str += '\n'
    print(map_str)

def main():
    # S1 = 0.2, S5 = 0.2, Sother = 0.6/7 ~ 0.086
    sectors = [0.2, 0.6/7, 0.6/7, 0.6/7, 0.2, 0.6/7, 0.6/7, 0.6/7, 0.6/7]
    print('\nInitial probabilities for shipwreck in each sector:')
    show_map(sectors)

    shipwreck_sector_i = 3
    sonar_effectiveness = 0.8
    while True:
        selected_sector = int(input('Which sector to search: '))
        i = selected_sector - 1

        if i == shipwreck_sector_i and random.random() < sonar_effectiveness:
            print('Found! Shipwreck was in sector', shipwreck_sector_i + 1)
            return

        # Update currently searched sector if search failed
        prior = (sectors[i] * (1 - sonar_effectiveness) + (1 - sectors[i]) * 1) # total p of failing in sector_i
        sectors[i] = sectors[i] * (1 - sonar_effectiveness) / prior
        
        # Update other sectors, based on the fact that in currently search sector there isn't shipwreck
        for j in range(len(sectors)):
            if j == i: # Omit currently searched sector
                continue
            # P(ship in sector_j | search failed in sector_i)
            sectors[j] = 1 * sectors[j] / prior

        show_map(sectors)

if __name__ == '__main__':
    main()