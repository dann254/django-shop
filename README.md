# Django-Shop
this is a sample django app for managing a shop

## Setting up
  1. clone this repo and `cd` into it.
  2. create a virtual environment `mkvirtualenv myenv`
  3. Install postgresql and create a database `createdb shop`
  4. create a .env file like
    ```
      workon myenv
      export DATABASE_URL="postgresql:///shop"
    ```
  5. activate the environment and export variables `source.env`
  6. run migrations `./manage.py migrate`
  7. start app `./manage.py runserver`
  8. visit the link http://127.0.0.1:8000/ on your browser.
  DONE!!

## endpoints

  1. `/` - home page
  2. `/manage/addstock/` - add items to stock or update items in stock
  3. `/manage/stock/` - view items in stock
  4. `/manage/reports/` - view purchase and sell reports.
  5. `/manage/sell` - sell stocked items
  6. `/manage/item/{id}/` - view specific items. links available in `/manage/stock/` on each item's row.
  7. `/manage/delete/{id}/` - Delete existing item.
  8. `/manage/update/{id}/` - update item price.
