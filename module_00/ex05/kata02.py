kata = (2019, 10, 25, 30, 30)

def main():
    nb1 = '0' + str(kata[1]) if kata[1] <= 9 else str(kata[1])
    nb2 = '0' + str(kata[2]) if kata[2] <= 9 else str(kata[2])
    nb3 = '0' + str(kata[3]) if kata[3] <= 9 else str(kata[3])
    nb4 = '0' + str(kata[4]) if kata[4] <= 9 else str(kata[4])
    final_str = nb1 + '/' + nb2  + '/' + str(kata[0])  + ' ' + nb3  + ':' + nb4
    print(final_str)

if __name__ == "__main__":
    main()