# layered_architecture
Flask를 이용한 백엔드 API의 Layered Architecture 프로젝트 샘플


## <a>프로젝트 구조</a>
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
* router_a.py : A 서비스에 대한 엔드포인트 정의
* router_b.py : B 서비스에 대한 엔드포인트 정의

### /services
Business Layer
* service_a.py : A 서비스에 대한 비즈니스 로직 정의
* service_b.py : B 서비스에 대한 비즈니스 로직 정의

### /model
Persistence Layer
* model_a.py : A 서비스에 대한 데이터 액세스
* model_b.py : B 서비스에 대한 데이터 액세스

## <a>Layered Architecuture</a>
요청이 Presentation Layer -> Business Layer -> Persistence Layer 순서로 처리되도록 
