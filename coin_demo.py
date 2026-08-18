import coin # custom module

def main():
    # Create an object from the coin class
    my_coin = coin.Coin()

    # Create variables to store head and tail count
    head_count = 0
    tail_count = 0

    for count in range(1000000):
        # Toss the coin
        my_coin.toss()

        # Increment count varable depending on sideup
        if my_coin.get_sideup() == 'Heads':
            head_count += 1
        else:
            tail_count += 1

    print(f'Heads: {head_count}\nTails: {tail_count}')

if __name__ == '__main__':
    main()