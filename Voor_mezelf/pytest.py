def process_payment(amount):
    print(f"Verwerken van betaling via iDEAL voor bedrag: {amount} EUR")
    # Voeg hier de code toe om de iDEAL-betaling te verwerken


def main():
    amount = float(input("Voer het te betalen bedrag in EUR in: "))
    process_payment(amount)


if __name__ == "__main__":
    main()
