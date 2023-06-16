from pets import *

pet_dict = {
    "dog": Dog,
    "cat": Cat,
    "rodent": Rodent,
    "reptile": Reptile,
    "exotic": Exotic,
    "bird": Bird,
}


def main():
    my_pets = []
    print("Welcome to the Adoption Center!")
    print(
        "We currently have dogs, cats, rodents, reptiles, exotic animals and birds up for adoption."
    )

    while True:
        choice = (
            input(
                "\n What kind of animal do you want to adopt (dog/ cat/ rodent/ reptile/ exotic/ bird): "
            )
            .strip()
            .lower()
        )
        if choice not in pet_dict:
            print("Please choose an available species!")
            continue
        name = input("What is the name of your new pet? ")
        pet = pet_dict[choice].create_pet(choice, name)
        my_pets.append(pet)
        print(pet.adoption_message)
        print("Please take good care of your new pet!")
        pet.speak()
        pet.pet_pet()
        print("\n You own:", "; ".join(map(str, my_pets)))
        choice = input("Adopt another pet (Y) or leave (any key)?: ")
        if choice == "y":
            continue
        else:
            quit("Goodbye!")


if __name__ == "__main__":
    main()
