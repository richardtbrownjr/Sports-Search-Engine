import os
import psycopg2


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
    cur.execute("""INSERT INTO panthers2 (Num, Name, Pos, Age, YRushing, YReceiving,TD) VALUES (%s, %s, %s, %s, %s, %s, %s)""", (name, numb, position, new_age, new_rushing, new_receiving, td))
    con.commit()
    cur.close()
    con.close()


def search_players():
    os.system('clear')
    con = psycopg2.connect("dbname=panthers2 user=richardt.brownjr.")
    cur = con.cursor()
    pname = input("Name of Panther player you want to find in database? ")
    for row in cur:
        if pname == name:
            print(row)
    con.commit()
    cur.close()
    con.close()



def main():
    # con = psycopg2.connect("dbname=panthers2 user=richardt.brownjr.")
    # cur = con.cursor()
    #add_new_player()
    search_players()
    # con.commit()
    # cur.close()
    # con.close()

if __name__ == '__main__':
    main()
