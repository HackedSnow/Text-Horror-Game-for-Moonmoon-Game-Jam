from collections import OrderedDict
from player import Player
import world
import time 

def play():
    print(r""" 



    
 
 _   .-')                                  .-') _                   .-') _    
( '.( OO )_                               ( OO ) )                 (  OO) )   
 ,--.   ,--.).-'),-----.  .-'),-----. ,--./ ,--,' ,--.      ,-.-') /     '._  
 |   `.'   |( OO'  .-.  '( OO'  .-.  '|   \ |  |\ |  |.-')  |  |OO)|'--...__) 
 |         |/   |  | |  |/   |  | |  ||    \|  | )|  | OO ) |  |  \'--.  .--' 
 |  |'.'|  |\_) |  |\|  |\_) |  |\|  ||  .     |/ |  |`-' | |  |(_/   |  |    
 |  |   |  |  \ |  | |  |  \ |  | |  ||  |\    | (|  '---.',|  |_.'   |  |    
 |  |   |  |   `'  '-'  '   `'  '-'  '|  | \   |  |      |(_|  |      |  |    
 `--'   `--'     `-----'      `-----' `--'  `--'  `------'  `--'      `--'    

                                _  .-')     ('-.    .-')    .-') _    
                               ( \( -O )  _(  OO)  ( OO ). (  OO) )   
           ,------. .-'),-----. ,------. (,------.(_)---\_)/     '._  
        ('-| _.---'( OO'  .-.  '|   /`. ' |  .---'/    _ | |'--...__) 
        (OO|(_\    /   |  | |  ||  /  | | |  |    \  :` `. '--.  .--' 
        /  |  '--. \_) |  |\|  ||  |_.' |(|  '--.  '..`''.)   |  |    
        \_)|  .--'   \ |  | |  ||  .  '.' |  .--' .-._)   \   |  |    
          \|  |_)     `'  '-'  '|  |\  \  |  `---.\       /   |  |    
           `--'         `-----' `--' '--' `------' `-----'    `--'                                                     
                      
                                        _|_
                                         |
                                        / \
                                       //_\\
                                      //(_)\\
                                       |/^\| 
                             ,%%%%     // \\    ,@@@@@@@,
                           ,%%%%/%%%  //   \\ ,@@@\@@@@/@@,
                       @@@%%%\%%//%%%// === \\ @@\@@@/@@@@@
                      @@@@%%%%\%%%%%// =-=-= \\@@@@\@@@@@@;%#####,
                      @@@@%%%\%%/%%//   ===   \\@@@@@@/@@@%%%######,
                      @@@@@%%%%/%%//|         |\\@\\//@@%%%%%%#/####
                      '@@@@@%%\\/%~ |         | ~ @|| %\\//%%%#####;
                        @@\\//@||   |  __ __  |    || %%||%%'######
                         '@||  ||   | |  |  | |    ||   ||##\//####
                           ||  ||   | | -|- | |    ||   ||'#||###'
                           ||  ||   |_|__|__|_|    ||   ||  ||
                           ||  ||_/`  =======  `\__||_._||  ||
                         __||_/`      =======            `\_||___
                                         
           
                                   Moonlit Forest
                                   
                                   
                                   
        Special thanks to Phillip Johnson for his book "Make Your Own Python Text Adventure"
                                                                                                """)     

    time.sleep(1)
    print("Chased...")
    print("You head south to the Moonlit Woods.")
    time.sleep(1)
    print("Lost within the denseness.")
    print("Attacked...")
    print("You lose conciousness.")
    time.sleep(1)
    print("You awake surrounded by the dead bodies of your group.")
    print("You gather your self.")
    time.sleep(1)
    print("                       ")                                 
    world.parse_world_dsl()
    player=Player()
    while player.is_alive()and player.is_sane() and not player.victory:
        room=world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive()and player.is_sane() and not player.victory:
            choose_action(room,player)
        elif player.is_alive()and not player.is_sane() and not player.victory:
            print("You stagger. Your mind betrays you.")
            print("The beast consumes your heart.")
            print("Your eyes peer inward. Your innards reach towards your soul.")
            print("Consumed... Nothing left...")
            input("Press enter to exit")
        elif not player.is_alive():
            print("You have fallen. Unbind your soul and let the undgrowth take your corporeal body.")
            input("Press enter to exit")

        
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")  


    
def get_available_actions(room, player):
    actions = OrderedDict()
    print(" Choose an action:")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Inventory/Stats")
    if player.inventory:
        action_adder(actions, 'p', player.pick, "Select Weapon")
    if isinstance(room, world.BossTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")        
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")  
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    
    
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north (Up)")
        if world.tile_at(room.x, room.y + 1):                       
            action_adder(actions, 's', player.move_south, "Go south (Down)")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east (Right)")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west (Left)")
    if player.hp < player.fullhp:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))



    

play()