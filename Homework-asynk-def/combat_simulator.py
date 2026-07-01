import asyncio
import time
import random

class Player:
    def __init__(self, name: str, hp: int, damage: int, attack_speed:float) -> None:
        self.name = name
        self. hp = hp
        self.damage = damage
        self.attack_speed = attack_speed
    
class Boss:
    def __init__(self, name: str, hp: int, damage:int, attack_speed:float) -> None:
        self.name = name
        self. hp = hp
        self.damage = damage
        self.attack_speed = attack_speed
        self.lock = asyncio.Lock()    


async def attack_boss(player, boss) -> None:
    """
    This func for attacking the boss on the attack speed
    loop stops if either the attacker or the main target reaches 0 health
    """
    
    while boss.hp > 0 and player.hp > 0:
        boss.hp -=player.damage
        print(f"Attack: {player.name} damage {boss.name} on {player.damage} HP \nBoss_hp: {boss.hp}")
        
        if boss.hp <= 0:
            print(f"Yeah! Boss is dead now. Congrats")
            break
        await asyncio.sleep(player.attack_speed)
        

async def boss_attack(boss, player_list: list) -> None:
    """
    This func for the boss to attack any player who is still alive
    loop stops when the main target dies or all targets are dead.
    """
    while boss.hp > 0:
        alive_players = []
        for current_player in player_list:
            if current_player.hp > 0:
                alive_players.append(current_player)
        
        if not alive_players:
            print(f"Oh no, all players are dead")
            break
        target_player = random.choice(alive_players)
        target_player.hp -= boss.damage
        print(f"{boss.name} choose {target_player.name} as a new victim")
        if target_player.hp <= 0:
            print(f"{target_player.name} dead after this much damage from boss")
        await asyncio.sleep(boss.attack_speed)
        
        
async def main() -> None:
    """
    The main func for getting players and boss, and running process at one time
    """
    
    boss = Boss(name="BIGBOSS-Morshynska", hp=1000, damage=50, attack_speed=2)
    player_1 = Player(name="Uru", hp=100, damage=20, attack_speed=1.5)
    player_2 = Player(name="Ram", hp=500,damage=50,attack_speed=3)
    player_3 = Player(name="Magicican", hp=300, damage=15,attack_speed=0.5)
    players = [player_1, player_2, player_3]
    
    print("The battle is start!")
    
    await asyncio.gather(
        boss_attack(boss, players),
        *[attack_boss(player, boss) for player in players]
    )
    
    print("The battle is over :)")\
        
asyncio.run(main())