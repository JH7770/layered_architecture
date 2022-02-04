# layered_architecture
Flask Backend layered architecture pattern

```
├── README.md
├── app.py
├── requirements.txt
├── config.py
├── common
│   ├── __init__.py
│   └── db.py
├── model
│   ├── __init__.py
│   ├── model_a.py
│   └── model_b.py
├── router
│   ├── __init__.py
│   ├── router_a.py
│   └── router_b.py
└── services
    ├── __init__.py
    ├── service_a.py
    └── service_b.py
    
```

### /common
공통으로 사용하는 모듈 정의
* db.py : 데이터베이스 관련 함수 정의

### /router
Presentation Layer

### /services
Business Layer


### /model
Persistence Layer

