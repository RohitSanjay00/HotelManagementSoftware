from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configure MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Appamon00$',
    'database': 'mydatabase',
}

conn = mysql.connector.connect(**db_config)

@app.route('/')
def login_page():
    return render_template('LoginPage.html')
@app.route('/events')
def events():
    # Add logic for Events Info page
    return render_template('EventInfo.html')
@app.route('/roominfo')
def roominfo():
    # Add logic for Room Info page
    return render_template('RoomInfo.html')
@app.route('/checkin')
def checkin():
    # Add logic for Check-In page
    return render_template('CheckIn.html')


################################################################ LOGIN PAGE ################################################################

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM admins WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()

    cursor.close()

    if user:
        # Authentication successful, redirect to dashboard
        return redirect(url_for('dashboard'))
    else:
        # Authentication failed
        return render_template('LoginPage.html', error='Invalid credentials')
    

################################################################# DASHBOARD PAGE ####################################################################

@app.route('/dashboard')
def dashboard():
    # Sample query to retrieve events for the current day
    cursor = conn.cursor(dictionary=True)
    today = datetime.now().date()
    cursor.execute('SELECT * FROM event WHERE StartDate = %s', (today,))
    events = cursor.fetchall()
    cursor.close()

    # Query to get all non-occupied rooms grouped by room type
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT RoomType, COUNT(*) AS NumberOfAvailableRooms FROM HotelRooms WHERE Occupied = FALSE GROUP BY RoomType')
    available_rooms = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM BookingDetails WHERE DATE(FromDate) = %s', (today,))
    bookings = cursor.fetchall()
    cursor.close()
    return render_template('dashboard.html', events=events, bookings=bookings, available_rooms=available_rooms)

@app.route('/upcoming_guests')
def upcoming_guests():
    # You can pass any necessary data to the template here
    return render_template('GuestList.html')
##################################################################### NEW GUEST LIST PAGE ############################################################################

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    # Retrieve form data
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    email = request.form['email']
    mobile_number = request.form['mobileNumber']
    room_type = request.form['roomType']
    from_date = request.form['fromDate']
    to_date = request.form['toDate']
    room_number = request.form['roomNumber']
    comments = request.form['comments']
    number_of_guests = request.form['numberOfGuests']

    # Insert reservation details into the database (BookingDetails table)
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO BookingDetails (FirstName, LastName, EmailAddress, MobileNumber, RoomType, FromDate, ToDate, RoomNumber, Comments, NumberOfGuests) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (first_name, last_name, email, mobile_number, room_type, from_date, to_date, room_number, comments, number_of_guests))

        # Update the Reserved column in the HotelRooms table to True
        cursor.execute('UPDATE HotelRooms SET Reserved = TRUE WHERE RoomNumber = %s', (room_number,))

    conn.commit()
    cursor.close()
    return redirect(url_for('checkin'))

@app.route('/get_available_rooms')
def get_available_rooms():
    room_type = request.args.get('roomType')
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT RoomNumber FROM HotelRooms WHERE RoomType = %s AND Reserved = FALSE', (room_type,))
    available_rooms = cursor.fetchall()
    cursor.close()

    return jsonify(available_rooms)

############################################### EVENTS FUNCTIONS #############################################################

@app.route('/get_events')
def get_events():
    # Retrieve upcoming events from the database
    cursor = conn.cursor(dictionary=True)
    current_date = datetime.now().strftime('%Y-%m-%d')
    query = f"SELECT * FROM event WHERE StartDate >= '{current_date}' ORDER BY StartDate"
    cursor.execute(query)
    events = cursor.fetchall()
    cursor.close()
    return jsonify(events)

@app.route('/create_event', methods=['POST'])
def create_event():
    try:
        # Add logic to insert a new event into the database
        cursor = conn.cursor()
        event_name = request.json.get('eventName')
        host_name = request.json.get('hostName')
        start_date = request.json.get('startDate')
        end_date = request.json.get('endDate')

        # Calculate the number of days between start_date and end_date
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        total_days = (end_date_obj - start_date_obj).days

        query = "INSERT INTO event (EventName, HostName, StartDate, EndDate, TotalDays) VALUES (%s, %s, %s, %s, %s)"
        values = (event_name, host_name, start_date, end_date, total_days)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()

        return jsonify({'message': 'Event created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/delete_event', methods=['POST'])
def delete_event():
    try:
        # Add logic to delete an event from the database
        cursor = conn.cursor()
        event_name = request.json.get('eventName')
        start_date = request.json.get('startDate')

        query = "DELETE FROM event WHERE EventName = %s AND StartDate = %s"
        values = (event_name, start_date)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()

        return jsonify({'message': 'Event deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/event_info')
def event_info():
    # You can pass any necessary data to the template here
    return render_template('EventInfo.html')

####################################################################### GUEST LIST #######################################################



@app.route('/guestlist')
def guestlist():
    # Fetch booking details from the database
    cursor = conn.cursor(dictionary=True)

    # Assuming you have a table named 'BookingDetails' with columns: BookingID, FirstName, LastName, EmailAddress, MobileNumber, RoomNumber, RoomType, NumberOfGuests, FromDate, ToDate, NumberOfDays, Comments
    query = "SELECT * FROM BookingDetails WHERE FromDate >= %s"
    today = datetime.now().strftime('%Y-%m-%d')
    cursor.execute(query, (today,))
    today_bookings = cursor.fetchall()
    cursor.close()
    return render_template('GuestList.html', today_bookings=today_bookings)

@app.route('/checkinout', methods=['POST'])
def checkinout():
    data = request.get_json()
    room_number = data['roomNumber']
    action = data['action']

    # Fetch room status from the database (Assuming 'HotelRooms' table)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Occupied, Reserved FROM HotelRooms WHERE RoomNumber = %s", (room_number,))
    result = cursor.fetchone()

    if result:
        occupied = result['Occupied']
        reserved = result['Reserved']

        if action == 'checkin':
            if not occupied and reserved:
                # Update the occupancy status to true if the room is not occupied and reserved
                cursor.execute("UPDATE HotelRooms SET Occupied = TRUE WHERE RoomNumber = %s", (room_number,))
                conn.commit()
                return "Checked In successfully for Room " + room_number
            else:
                return "Room " + room_number + " is either occupied or not reserved. Check-in not allowed."

        elif action == 'checkout':
            if occupied and reserved:
                
                # Update both occupancy and reservation status to false for Check Out
                cursor.execute("UPDATE HotelRooms SET Occupied = FALSE, Reserved = FALSE WHERE RoomNumber = %s", (room_number,))
                
                conn.commit()
                return "Checked Out successfully for Room " + room_number
            else:
                return "Room " + room_number + " is not occupied or not reserved. Check-out not allowed."

    return "Invalid request."


@app.route('/payment')
def payment():
    # Get the room number from the query parameters
    room_number = request.args.get('room_number')

    # Fetch price per night from HotelRooms table
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Price FROM HotelRooms WHERE RoomNumber = %s", (room_number,))
    price_result = cursor.fetchone()

    if price_result:
        price_per_night = price_result['Price']
    else:
        return "Price information not found for Room " + room_number

    # Fetch the number of days from BookingDetails table
    cursor.execute("SELECT * FROM BookingDetails WHERE RoomNumber = %s", (room_number,))
    number_of_days_result = cursor.fetchone()
    print(number_of_days_result)

    if number_of_days_result:
        number_of_days = number_of_days_result['NumberOfDays']
    else:
        return "Number of days information not found for Room " + room_number

    # Calculate total cost
    total_cost = price_per_night * number_of_days
    # Delete the entry from BookingDetails for Check Out
    cursor.execute("DELETE FROM BookingDetails WHERE RoomNumber = %s", (room_number,))
    conn.commit()
    
    return render_template('payment.html', room_number=room_number, price_per_night=price_per_night,
                           number_of_days=number_of_days, total_cost=total_cost)

@app.route('/paymentGateway')
def paymentGateway():
    return render_template('paymentGateway.html', )

if __name__ == '__main__':
    app.run(debug=True)
