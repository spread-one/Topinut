project/
├── backend/                # Flask 백엔드
│   ├── app/                # Flask 애플리케이션 폴더
│   │   ├── __init__.py     # Flask 앱 초기화 파일
│   │   ├── routes.py       # API 라우팅
│   │   ├── models.py       # 데이터베이스 모델
│   │   ├── services.py     # 비즈니스 로직
│   │   └── utils.py        # 유틸리티 함수
│   ├── config.py           # Flask 설정 파일
│   ├── requirements.txt    # Python 의존성 파일
│   ├── run.py              # Flask 실행 스크립트
│   └── migrations/         # DB 마이그레이션 파일
│
├── frontend/               # React 프런트엔드
│   ├── public/             # 정적 파일 (HTML, Favicon 등)
│   │   └── index.html      # React 엔트리 HTML
│   ├── src/                # React 소스 파일
│   │   ├── components/     # React 컴포넌트
│   │   │   ├── Header.jsx  # 예: Header 컴포넌트
│   │   │   ├── Footer.jsx  # 예: Footer 컴포넌트
│   │   │   └── ErrorList.jsx  # 틀린 부분을 보여줄 컴포넌트
│   │   ├── pages/          # React 페이지 (라우팅 기준)
│   │   │   ├── Home.jsx    # 홈 페이지
│   │   │   └── Dashboard.jsx  # 학습 대시보드 페이지
│   │   ├── App.js          # React 최상위 컴포넌트
│   │   ├── index.js        # React 엔트리 파일
│   │   └── services/       # API 요청 파일 (Axios)
│   │       └── api.js      # API 호출 관련 코드
│   ├── package.json        # React 의존성 및 설정
│   └── webpack.config.js   # Webpack 설정 (선택적)
│
├── db/                     # MySQL 관련 설정
│   ├── schema.sql          # 초기 스키마 파일
│   ├── seed.sql            # 테스트용 더미 데이터
│   └── migrations/         # 마이그레이션 파일 (선택적)
│
├── .gitignore              # Git 무시 파일
├── .env     
├── README.md               # 프로젝트 설명 파일
└── docker-compose.yml      # Docker 설정 (선택적)
