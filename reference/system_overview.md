<!-- system_overview.md -->
HRD_Final/  
├── README.md  
├── LICENSE  
├── .gitignore  
├── docs/                     # 제출용 한글 문서
│   ├── 프로젝트_기술서_3차_2조.hwp  
│   ├── HRD_프로젝트 계획서_3차_2조.hwp  
│   └── 프로젝트 요약서.hwp   
├── reference/                 # 내부 시스템 문서  
│   ├── reference.md           # 시스템 구성 문서  
│   ├── structure.md           # Mermaid 다이어그램  
│   └── database.md            # DB 스키마 상세  
├── images/                    # 시각 자료
│   ├── assets/                # 문서용 자료  
│   └── resources/             # 코드에서 참조 이미지  
├── src/                       # 실행 코드  
│   ├── game_start.sh  
│   └── main.py  
└── tests/                     # 테스트/ML/서버/웹  
    ├── server/  
    │   ├── app.py  
    │   ├── run_server.sh  
    │   ├── requirements.txt  
    │   ├── api_reference.json  
    │   └── utils/  
    │       ├── auth.py  
    │       ├── blur_face.py  
    │       ├── error_handler.py  
    │       └── image_processor.py  
    ├── notebook/  
    │   ├── fashion_train.ipynb  
    │   ├── pose_analysis.ipynb  
    │   ├── models/  
    │   │   └── model_latest.pt  
    │   └── dataset/  
    │       ├── clothes/  
    │       └── users/  
    └── application/  
        ├── index.html  
        ├── script.js  
        └── styles.css  
  

<!-- 모든 md 파일은 관리자에게 문의 후 수정하시오 -->