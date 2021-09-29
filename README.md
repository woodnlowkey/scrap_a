# scrap_a

2021-09-27 amazon scraper project

개인 학습 프로젝트 계획

목표 : 저장용 아마존 검색 프로그램 제작
- 셀레니움과 뷰티풀숲의 활용 학습
- 데이터 활용 방안 모색 : 지도학습을 통해 상품 이미지의 특징을 학습시켜 판매자가 등록하는 이미지로 상세 카테고리를 태그하도록 만들 수 있습니다. 구매자는 원하는 상품의 자세한 특징을 설정하여 니즈를 충족하는 상품을 쉽게 찾을 수 있습니다.
- UI 편의성, 접근성, 예외처리 방법 학습

수행기간 : 2021. 09. 27 ~ 2021. 10. 8 (10일간) 예정

![시나리오1](https://user-images.githubusercontent.com/64139631/135197409-0781959f-31f8-4200-a21b-c78b87ec8537.png)
![시나리오2](https://user-images.githubusercontent.com/64139631/135197416-64143afe-0e07-4370-96ec-210e2d999a03.png)

![flowchart](https://user-images.githubusercontent.com/64139631/135197507-7c66df4d-38bb-4fcc-8047-3741ead8842d.png)

예외처리 : 제작단계 - 사용자 입력에 대한 부분 검토, 각 페이지 콘텐츠의 부재 검토

진행 과정 : 
- 1일차 >>> 계획 수립, 플로우차트 작성, 프로그램 프레임 구성, 함수 작성, 1차 테스트 (입력이 필요한 기능을 함수로 정의, 프로그램 동작 단계에 따라 지역변수로 진행해서 가독성을 향상시키고 필요하지 않은 메모리 사용 최소화, 데이터 셋 형태로 저장하여 누락되는 데이터를 보완)
- 2일차 >>> 동료를 대상으로 사용자 피드백 요청, 에러 확인 - 데이터 손실 : 문법적 오류 해결 / 두번째 검색 시 종료되는 현상 : 함수 내에서 전역변수를 선언하고 다음 함수를 반환값으로 호출하여 해결, 편의성 개선을 위한 수정 - 검색 결과의 저장 요청 갯수가 페이지상에 모자랄 때 계속 진행할 지를 묻는 메시지 출력, 사용자 접근성과 정확한 데이터 관리를 위한 수정 - 페이지상의 문제로 저장되지 않은 이미지의 번호 출력, 함수 설명과 주석 추가.
- 3일차 >>> 진행중

시연 :

느낀 점, 배운 점 : 전체 플로우차트와 시나리오 작성으로 제작 단계에서의 수정을 최소화하여 개발 기간을 단축할 수 있습니다. 데이터 수집의 상세한 목적이 있으면 활용도 높은 자동화 프로그램을 제작할 수 있습니다.
