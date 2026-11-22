import random

def attack(damage):
    print("You attacked the enemy!")
    return damage
def heal(health):
    print("You healed yourself!")
    health += 20
    if health > 100:
        health = 100
    return health
def escape():
    print("You escaped from the battle!")
def enemy_attack():
    print("Enemy is attacking you!")
    return 20
while True:
    player_health = 100
    enemy_health = 100
    print("\n===== MINI BATTLE GAME =====")
    while player_health> 0 and enemy_health>0:

        print("Your Health:", player_health)
        print("Enemy Health:", enemy_health)
        print("1. Attack")
        print("2. Heal")
        print("3. Escape")
        choice = input("Choose your action: ")

        if choice == "1":
            damage = random.randint(10, 20)
            damage = attack(damage)

            enemy_health -= damage
            print("You dealt", damage, "damage!")
            if enemy_health <= 0:
                enemy_health=0
                print("You defeated the enemy! You Won")
                break
            else:
                enemy_damage = enemy_attack()
                player_health -= enemy_damage
                print("Your health:", player_health)
        elif choice == "2":
            player_health = heal(player_health)
            print("Your health:", player_health)

        elif choice == "3":
            escape()
            break

        else:
            print("Invalid choice!")
        if player_health <= 0:
            print("Game Over! You Lost!")

    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
     print("Thank you for playing!")
     break
