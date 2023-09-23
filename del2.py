# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import random

# Define a class for a simple guessing game
class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess the number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.target_number:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.root.quit()
            elif guess < self.target_number:
                messagebox.showinfo("Try Again", "Try a higher number.")
            else:
                messagebox.showinfo("Try Again", "Try a lower number.")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

import random

# Define a Product class to represent items in the store
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_product(self):
        return f"{self.name} - ${self.price} ({self.stock} in stock)"

# Define a ShoppingCart class to manage the user's shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            return True
        else:
            return False

    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.stock += item[1]
                break

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

    def checkout(self):
        total = self.calculate_total()
        if total == 0:
            return "Your cart is empty. Add items before checking out."

        return f"Total: ${total}. Thank you for shopping with us!"

# Define a Store class to manage products and the shopping process
class Store:
    def __init__(self):
        self.products = []
        self.cart = ShoppingCart()

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        return "\n".join(product.display_product() for product in self.products)

# Create a store and populate it with products
store = Store()
product1 = Product("Laptop", 800, 10)
product2 = Product("Phone", 300, 15)
product3 = Product("Tablet", 200, 20)
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# Simulate a user's shopping experience
print("Welcome to Our E-Commerce Store!")
while True:
    print("\nAvailable Products:")
    print(store.display_products())

    choice = input("\nEnter 'add' to add a product to the cart, 'remove' to remove, 'checkout' to checkout, or 'exit' to exit: ").lower()

    if choice == 'add':
        product_name = input("Enter the name of the product you want to add: ")
        quantity = int(input("Enter the quantity you want to add: "))
        for product in store.products:
            if product.name.lower() == product_name.lower():
                if store.cart.add_to_cart(product, quantity):
                    print(f"{quantity} {product_name}(s) added to your cart.")
                else:
                    print(f"Sorry, there are not enough {product_name}(s) in stock.")
                break

    elif choice == 'remove':
        product_name = input("Enter the name of the product you want to remove: ")
        for product in store.products:
            if product.name.lower() == product_name.lower():
                store.cart.remove_from_cart(product)
                print(f"{product_name} removed from your cart.")
                break

    elif choice == 'checkout':
        print(store.cart.checkout())
        break

    elif choice == 'exit':
        break

    else:
        print("Invalid choice. Please enter 'add', 'remove', 'checkout', or 'exit'.")


import random

# Define a Player class to represent the game's character
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.gold = 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        enemy.take_damage(damage)

    def earn_gold(self, amount):
        self.gold += amount

    def display_stats(self):
        return f"{self.name}'s Stats - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Gold: {self.gold}"

# Define an Enemy class for the game's enemies
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        damage = random.randint(0, self.attack)
        player.take_damage(damage)

    def is_alive(self):
        return self.health > 0

    def display_stats(self):
        return f"{self.name}'s Stats - Health: {self.health}, Attack: {self.attack}"

# Define a function to simulate a battle between the player and an enemy
def battle(player, enemy):
    while player.health > 0 and enemy.is_alive():
        print(player.display_stats())
        print(enemy.display_stats())
        input("Press Enter to continue...")
        
        player.attack_enemy(enemy)
        enemy.attack_player(player)
        
        print(f"{player.name} attacks {enemy.name} for {player.attack} damage.")
        print(f"{enemy.name} attacks {player.name} for {enemy.attack} damage.")
        
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
        elif enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            player.earn_gold(random.randint(1, 10))
            break

# Main game loop
player_name = input("Enter your character's name: ")
player = Player(player_name)

while True:
    print("\n1. Explore\n2. Check Inventory\n3. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        enemy_name = random.choice(["Goblin", "Orc", "Dragon"])
        enemy_health = random.randint(10, 50)
        enemy_attack = random.randint(5, 15)
        enemy = Enemy(enemy_name, enemy_health, enemy_attack)
        print(f"A wild {enemy_name} appears!\n")
        
        battle(player, enemy)
    
    elif choice == '2':
        print(player.display_stats())
    
    elif choice == '3':
        print("Thanks for playing!")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
