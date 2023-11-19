kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    module = '0' + str(kata[0]) if kata[0] <= 9 else str(kata[0])
    ex = '0' + str(kata[1]) if kata[1] <= 9 else str(kata[1])
    dec = f"{kata[2]:.2f}"
    f = f"{kata[3]:.2e}"
    f2 = f"{kata[4]:.2e}"
    print(f"module_{module}, ex_{ex} : {dec}, {f}, {f2}")

if __name__ == "__main__":
    main()