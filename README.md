# test_gm_interview

This is for interview purpose.

## Start Containerized database and application

```
docker compose up -d --build
```

## Test API server's access

```
curl http://localhost:8081/hello
```

## API: to create item in inventory database

```
curl -X POST http://localhost:8081/Items \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Wireless Mouse",
  "code": "WM12345",
  "category": "Electronics",
  "size": "small,medium",
  "unit_price": 25,
  "inventory": 150,
  "color": "black, white"
}
'
```


## Docker Database: to check items added

```
docker exec -it test_gm_interview-database-1 mysql -u root -p 
```
then entery password:
```
test_password
```
After that, enter to the database
```
use inventory;
```
Then select the table
```
SELECT * FROM inventory.item;
```

## API: to get all items

```
http://localhost:8081/Items
```

## API: to delete items
```
http://localhost:8081/Items/{:id}
```
* put the item's id from database table to delete it.