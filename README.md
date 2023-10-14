# bag-inventory
Python script to keep track of inventory in 'bugout' or 'get home' bags

## Installation

You'll need to install panda and tabulate
```
pip install panda
pip install tabulate
```
Then, chmod +x and put it in your path somewhere.   Create your bag_inventory.csv in /tmp/ 

## Usage
Just run it by itself
```
$ bag_inventory.py 
Full Inventory:
+-----------------+----------+-------+--------+-------------+
|      item       | quantity |  bag  | pocket |  category   |
+-----------------+----------+-------+--------+-------------+
|   usb-c cord    |    1     | sling |  side  | electronics |
|   usb-c plug    |    1     | sling |  side  | electronics |
|  extra wallet   |    1     | sling | front  |  emergency  |
| firestarter kit |    1     | sling | inner  |  emergency  |
|   bic lighter   |    2     | sling |  top   |  emergency  |
|    paracord     |   50ft   | large |  side  |    tools    |
|    duct tape    |   10ft   | large | inner  |    tools    |
|       axe       |    1     | large |  main  |    tools    |
+-----------------+----------+-------+--------+-------------+

Items in small sling bag:
+-----------------+----------+-------+--------+-------------+
|      item       | quantity |  bag  | pocket |  category   |
+-----------------+----------+-------+--------+-------------+
|   usb-c cord    |    1     | sling |  side  | electronics |
|   usb-c plug    |    1     | sling |  side  | electronics |
|  extra wallet   |    1     | sling | front  |  emergency  |
| firestarter kit |    1     | sling | inner  |  emergency  |
|   bic lighter   |    2     | sling |  top   |  emergency  |
+-----------------+----------+-------+--------+-------------+

Items in large bag:
+-----------+----------+-------+--------+----------+
|   item    | quantity |  bag  | pocket | category |
+-----------+----------+-------+--------+----------+
| paracord  |   50ft   | large |  side  |  tools   |
| duct tape |   10ft   | large | inner  |  tools   |
|    axe    |    1     | large |  main  |  tools   |
+-----------+----------+-------+--------+----------+
```
Or specify a bag
```
$ bag_inventory.py sling
Items in sling bag:
+-----------------+----------+-------+--------+-------------+
|      item       | quantity |  bag  | pocket |  category   |
+-----------------+----------+-------+--------+-------------+
|   usb-c cord    |    1     | sling |  side  | electronics |
|   usb-c plug    |    1     | sling |  side  | electronics |
|  extra wallet   |    1     | sling | front  |  emergency  |
| firestarter kit |    1     | sling | inner  |  emergency  |
|   bic lighter   |    2     | sling |  top   |  emergency  |
+-----------------+----------+-------+--------+-------------+
```
