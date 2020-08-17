# FROMEATS 

## 서비스 소개

![1](./meta_description/1.JPG)
![2](./meta_description/2.JPG)
![3](./meta_description/3.JPG)
![4](./meta_description/4.JPG)
![5](./meta_description/5.JPG)
![6](./meta_description/6.JPG)
![7](./meta_description/7.JPG)
![8](./meta_description/8.JPG)
![9](./meta_description/9.JPG)
![10](./meta_description/11.JPG)
![11](./meta_description/10.JPG)
![12](./meta_description/12.JPG)
![13](./meta_description/13.JPG)


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
