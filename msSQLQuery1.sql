
USE master;

create database [db.mssql-jidox];

USE [db.mssql-jidox];

drop database ['db.mssql-jidox'];
drop database [db.mssql-jidox];

SELECT name AS TableName FROM sys.tables;


select * from users_user;
select * from users_billingmodel;
select * from users_inventorymodel;

DELETE FROM users_user;
DELETE from users_billingmodel;
delete from users_inventorymodel


-- To Verify the Schema of a Table
SELECT * FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'users_inventory';


SELECT 
    *
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'users_billingmodel';

select * from users_user;

Billing record created: {'client_name': 'Test001', 'client_address': 'No 19, queens street, Ontario', 'billing_to': 'Diamond', 'service_type': 'Billable', 'bill_description': 'dsfsdf', 'ticket_id': '43252', 'emailed': 'on', 'invoice_no': '0100', 'invoice_date': '2025-01-29'}


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
