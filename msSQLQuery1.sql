
USE master;

SELECT name FROM sys.databases;


create database [db.mssql-jidox];

USE [db.mssql-jidox1];

drop database [db.mssql-jidox];

SELECT name AS TableName FROM sys.tables;

create table users_stockinhand;

select * from users_user;
select * from users_billingmodel;

select * from users_inventorymodel;
select * from users_stockinhand;
select * from users_stockinmodel;
select * from users_stockoutmodel;


ALTER TABLE users_stockinmodel
DROP COLUMN stock_in_hand;


DELETE FROM users_user;
DELETE from users_billingmodel;
delete from users_inventorymodel
delete from users_stockinmodel;
delete from users_stockoutmodel;
delete from users_stockinhand;

DROP TABLE users_stockoutmodel; -- Drop the StockInHand table

CREATE TABLE users_stockinhand (
    id INT PRIMARY KEY IDENTITY(1,1),
    product_item NVARCHAR(255) UNIQUE,
    manufacturer NVARCHAR(255),
    total_stock_received INT DEFAULT 0,
    serial_no NVARCHAR(255) NULL,
    mac_product_no NVARCHAR(255) NULL,
    description TEXT NULL,
    received_from NVARCHAR(255) NULL,
    stock_in_date DATE,
    stock_in_hand INT DEFAULT 0
);








UPDATE users_billingmodel
SET invoice_no = NULL
WHERE invoice_no IS NOT NULL AND invoice_no != '';



-- To Verify the Schema of a Table
SELECT * FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'users_inventory';


SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE 
    TABLE_NAME = 'users_billingmodel';


INSERT INTO [dbo].[users_billingmodel] (
    [client_name],
    [client_address],
    [billing_to],
    [service_type],
    [bill_description],
    [ticket_id],
    [emailed],
      [invoice_no],
    [invoice_date]
)
VALUES (
    'Test001',
    'No 19, queens street, Ontario',
    'Diamond',
    'Billable',
    'dsfsdf',
    '43252',
    '1',
    '0100',
    '2025-01-29'
);
Billing record created: {'client_name': 'Test001', 'client_address': 'No 19, queens street, Ontario', 'billing_to': 'Diamond', 'service_type': 'Billable', 'bill_description': 'dsfsdf', 'ticket_id': '43252', 'emailed': '1', 'invoice_no': '0100', 'invoice_date': '2025-01-29'}
USE [db.mssql-jidox];  -- Switch to the correct database

INSERT INTO [dbo].[users_billingmodel] (
    [client_name],
    [client_address],
    [billing_to],
    [service_type],
    [bill_description],
    [ticket_id],
    [emailed],
    [comments],
    [invoice_no],
    [invoice_date]
)
VALUES (
    'Test001',  -- client_name (nvarchar(255), not null)
    'No 19, queens street, Ontario',  -- client_address (nvarchar, nullable)
    'Diamond',  -- billing_to (nvarchar, nullable)
    'Billable',  -- service_type (nvarchar, nullable)
    'dsfsdf',  -- bill_description (nvarchar, nullable)
    '43252',  -- ticket_id (nvarchar(50), nullable)
    1,  -- emailed (bit, assuming 'on' means TRUE; 1 for TRUE)
    NULL,  -- comments (nvarchar, nullable)
    '0100',  -- invoice_no (nvarchar(50), not null)
    '2025-01-29'  -- invoice_date (nvarchar(50), nullable)
);
