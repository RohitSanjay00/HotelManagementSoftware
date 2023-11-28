CREATE DATABASE mydatabase;
USE mydatabase;
Show tables;


/***************************************************************** HOTEL ROOMS TABLE **************************************/
CREATE TABLE HotelRooms (
    RoomNumber INT,
    RoomType VARCHAR(255),
    RoomSize INT,
    NumberOfBeds INT,
    NumberOfRooms INT,
    TypeOfBeds VARCHAR(255),
    View VARCHAR(255),
    WiFiIncluded BOOLEAN,
    BreakfastIncluded BOOLEAN,
    MiniFridge BOOLEAN,
    Occupied BOOLEAN,
    PRIMARY KEY (RoomNumber)
);
ALTER TABLE HotelRooms
ADD Reserved BOOLEAN DEFAULT FALSE;

INSERT INTO HotelRooms VALUES (101, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (102, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (103, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (104, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (105, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (106, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (107, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (108, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (109, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (110, 'Regular', 250, 1, 1, 'Single Bed', 'City View', true, true, true, false);

INSERT INTO HotelRooms VALUES (201, 'Premium', 300, 2, 1, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (202, 'Premium', 300, 2, 1, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (203, 'Premium', 300, 2, 1, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (204, 'Premium', 300, 2, 1, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (205, 'Premium', 300, 2, 1, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (206, 'Premium', 300, 2, 2, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (207, 'Premium', 300, 2, 2, '2 Single Beds', 'Ocean View', true, true, true, false);
INSERT INTO HotelRooms VALUES (208, 'Premium', 300, 2, 2, '2 Single Beds', 'Ocean View', true, true, true, false);

INSERT INTO HotelRooms VALUES (301, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (302, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (303, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (304, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (305, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (306, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (307, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (308, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (309, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);
INSERT INTO HotelRooms VALUES (310, 'Suit', 550, 1, 1, '1 Queen Bed', 'Mountain View', true, true, true, false);


INSERT INTO HotelRooms VALUES (401, 'Premium Suit', 650, 2, 2, '2 Queen Beds', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (402, 'Premium Suit', 650, 2, 2, '2 Queen Beds', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (403, 'Premium Suit', 650, 2, 2, '2 Queen Beds', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (404, 'Premium Suit', 650, 2, 2, '2 Queen Beds', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (405, 'Premium Suit', 650, 2, 2, '2 Queen Beds', 'City View', true, true, true, false);
INSERT INTO HotelRooms VALUES (406, 'Premium Suit', 650, 2, 2, '2 Queen Beds', 'City View', true, true, true, false);

INSERT INTO HotelRooms VALUES (501, 'VIP Suit', 1000, 4, 1, '4 Queen Beds', 'Panoramic View', true, true, true, false);
INSERT INTO HotelRooms VALUES (502, 'VIP Suit', 1000, 4, 1, '4 Queen Beds', 'Panoramic View', true, true, true, false);
INSERT INTO HotelRooms VALUES (503, 'VIP Suit', 1000, 4, 1, '4 Queen Beds', 'Panoramic View', true, true, true, false);
INSERT INTO HotelRooms VALUES (504, 'VIP Suit', 1000, 4, 1, '4 Queen Beds', 'Panoramic View', true, true, true, false);
SET SQL_SAFE_UPDATES = 0;


/************************************************************* BOOKING INFORMATION TABLE**************************************************/

CREATE TABLE BookingDetails (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    EmailAddress VARCHAR(255) CHECK (EmailAddress LIKE '%_@__%.__%'),
    MobileNumber VARCHAR(15) CHECK (LENGTH(MobileNumber) >= 9),
    RoomNumber INT,
    RoomType VARCHAR(255),
    NumberOfGuests INT,
    FromDate DATE,
    ToDate DATE,
    NumberOfDays INT GENERATED ALWAYS AS (DATEDIFF(ToDate, FromDate)),
    Comments TEXT
);


/**************************************************************************** ADMIN LOGIN INFORMATION *****************************************************/
CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);


/************************************************************************ EVENT INFORMAITON TABLE***************************************************************************/
CREATE TABLE event (
    EventName VARCHAR(255),
    HostName VARCHAR(255),
    StartDate DATE,
    EndDate DATE,
    TotalDays INT
);


/************************************************************************** COMMANDS ***************************************************************************************/


SELECT * FROM HotelRooms;
UPDATE HotelRooms SET Occupied = False WHERE RoomNumber = 101;
UPDATE HotelRooms SET Reserved = false WHERE RoomNumber = 201;

SELECT * FROM BookingDetails;
INSERT INTO BookingDetails (FirstName, LastName, EmailAddress, MobileNumber, RoomNumber, RoomType, NumberOfGuests, FromDate, ToDate)
VALUES ('John', 'Doe', 'johndoe@email.com', '1234567890', 101, 'Deluxe', 2, '2023-11-27', '2023-12-28');
UPDATE HotelRooms SET Occupied = 0 WHERE RoomNumber = 102;
DELETE FROM BookingDetails;

SELECT * FROM event;
INSERT INTO event (EventName, HostName, StartDate, EndDate, TotalDays)
VALUES ('Party', 'John Doe', '2023-11-25', '2023-11-26', 1);
DELETE FROM event;

SELECT * FROM admins;




SELECT NumberOfDays FROM BookingDetails WHERE RoomNumber = 103;
















