# FROMEATS

# 서비스 소개

![](./metadata_description/1.png)
![](./metadata_description/2.png)
![](./metadata_description/3.png)
![](./metadata_description/4.png)
![](./metadata_description/5.png)
![](./metadata_description/6.png)
![](./metadata_description/7.png)
![](./metadata_description/8.png)
![](./metadata_description/9.png)
![](./metadata_description/10.png)
![](./metadata_description/11.png)
![](./metadata_description/12.png)
![](./metadata_description/13.png)


## How to Run

### Sub1

```sh
cd sub1
pip install -r requirements.txt
python parse.py
python analyze.py
python visualize.py
```

### Sub 2

**Backend**

```sh
cd sub2/backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve
```
