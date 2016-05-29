import places, Connection,datetime
name = int(raw_input("enter your name: "))
isdriver = raw_input("hi %s are you a driver or a passanger? " %(name))

if int(isdriver) == 1:
    print "available locations:"
    for x in places.getPlaces():
        print '%s '.ljust(5) %(x[0]), x[1]
    dest = int(raw_input("what is your destination?"))
    origin = int(raw_input("what is your origin?"))
    when = datetime.datetime.strptime( raw_input("when do you go ddmmyyyy hh24:mi ?"),'%d%m%Y %H%M')
    seats = int(raw_input("how many seats do you have?"))

    conn = Connection.getConnection()
    cur = conn.cursor()

    query = cur.mogrify("INSERT INTO nesiot(driver_id, origin_id, dest_id, taarich, num_seats) VALUES"\
                 " (%s,%s,%s,%s,%s);" ,(name,dest,origin,when,seats))
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
