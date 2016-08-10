import os
import psycopg2


def get_input():
    os.system('clear')
    print("Would you like to: ")
    print("1.) Search current Panthers players")
    print("2.) Add new player")
    key_stroke = input("Type 1 or 2 for your choice  ")
    if key_stroke in ['1', '2']:
        return int(key_stroke)
    else:
        get_input


def add_new_player():
    os.system('clear')
    con = psycopg2.connect("dbname=panthers2 user=richardt.brownjr.")
    cur = con.cursor()
    name = input("Name of new Panther player: ")
    numb = input("Number for {} ".format(name))
    position = input("{} position ".format(name))
    new_age = input("{}'s age: ".format(name))
    new_rushing = input("Yards Rushing: ")
    new_receiving = input("Yards Receving: ")
    td = input("number of touch downs ")
    cur.execute("""INSERT INTO panthers2 (Num, Name, Age, Pos, YRushing, YReceiving,TD) VALUES (%s, %s, %s, %s, %s, %s, %s)""", (name, numb, position, new_age, new_rushing, new_receiving, td))
    con.commit()
    cur.close()
    con.close()


def search_players():
    os.system('clear')
    con = psycopg2.connect("dbname=panthers2 user=richardt.brownjr.")
    cur = con.cursor()
    pname = input("Name of Panther player you want to find in database? ")
    cur.execute("SELECT * FROM panthers2 WHERE Name ILIKE %(name)s", {'name': "%" + pname.replace(' ',"%") + "%"})
    print(" Num,     Name,       Age,  Pos,   YRushing,  YReceiving,  TD")
    print (cur.fetchone())
    con.commit()
    cur.close()
    con.close()


def main():
    # con = psycopg2.connect("dbname=panthers2 user=richardt.brownjr.")
    # cur = con.cursor()
    key_stroke = get_input()
    if key_stroke == 2:
        add_new_player()
    if key_stroke == 1:
        search_players()
    # con.commit()
    # cur.close()
    # con.close()

if __name__ == '__main__':
    main()
