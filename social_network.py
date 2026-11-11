class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        person1 = self.people.get(person1_name)
        person2 = self.people.get(person2_name)

        if person1 is None or person2 is None:
            missing_names = [
                name
                for name, person in (
                    (person1_name, person1),
                    (person2_name, person2),
                )
                if person is None
            ]
            if len(missing_names) == 1:
                print(
                    f"Friendship not created. {missing_names[0]} doesn't exist."
                )
            else:
                missing_list = " and ".join(missing_names)
                print(f"Friendship not created. {missing_list} don't exist.")
            return

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = ", ".join(friend.name for friend in person.friends)
            print(f"{person.name} is friends with: {friend_names}")


if __name__ == "__main__":
    network = SocialNetwork()

    for name in ("Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"):
        network.add_person(name)

    network.add_person("Alex")

    for person1, person2 in (
        ("Alex", "Jordan"),
        ("Alex", "Morgan"),
        ("Jordan", "Taylor"),
        ("Morgan", "Casey"),
        ("Taylor", "Riley"),
        ("Casey", "Riley"),
        ("Morgan", "Riley"),
        ("Alex", "Taylor"),
    ):
        network.add_friendship(person1, person2)

    network.add_friendship("Jordan", "Johnny")
    network.print_network()
