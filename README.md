# scrap_a

2021-09-27 amazon scraper project

개인 학습 프로젝트 계획

목표 : 저장용 아마존 검색 프로그램 제작
- 셀레니움과 뷰티풀숲의 활용 학습
- 데이터 활용 방안 모색
- UI 편의성, 접근성, 예외처리 방법 학습

수행기간 : 2021. 09. 27 ~ 2021. 10. 8 (10일간) 예정

> 시나리오 : 프로그램 실행
> ![캡처1](https://user-images.githubusercontent.com/64139631/134908439-8c471f42-02bb-4268-93ee-ab1e2eba2aac.PNG)
> 
> 저장 할 폴더 입력 > 메인 페이지, 검색어 입력 
> ![캡처2](https://user-images.githubusercontent.com/64139631/134908601-ed05b383-ae6c-4ae0-8a6f-2188b5646392.PNG)
> 
> 결과 카테고리 추출 
> ![캡처3](https://user-images.githubusercontent.com/64139631/134908678-e11850a8-cbc4-4bd1-89b6-deaf7cff5ab6.PNG)
> 
> 카테고리, 검색 할 갯수 입력 
> ![캡처4](https://user-images.githubusercontent.com/64139631/134908768-f67fcfad-7f49-458d-bf42-be3619c7107a.PNG)
> 
> 해당하는 페이지 검색 실행 
> ![캡처5](https://user-images.githubusercontent.com/64139631/134908812-8b922c78-a15d-451e-aa4b-5ad1b4af42f5.PNG)
> 
> 검색 결과 출력 > 저장 여부, 확장자 입력 
> ![캡처6](https://user-images.githubusercontent.com/64139631/134908859-15883908-7519-4b07-b932-efd160a005e9.PNG)
> 
> 저장 완료 출력 후 메인 페이지 > 검색어 입력 반복

흐름도 : ![flowchart](https://user-images.githubusercontent.com/64139631/134908282-2f69f0f2-bb76-49cb-8be4-d3a09f9f6249.PNG)

예외처리 : 제작단계 - 사용자 입력에 대한 부분 검토, 각 페이지 콘텐츠의 부재 검토

진행 과정 : 
> 1일차 >>> 계획 수립, 플로우차트 작성, 프로그램 프레임 구성, 함수 작성, 1차 테스트 (입력이 필요한 기능을 함수로 정의, 프로그램 동작 단계에 따라 지역변수로 진행해서 가독성을 향상시키고 필요하지 않은 메모리 사용 최소화, 데이터 셋 형태로 저장하여 누락되는 데이터를 보완)
> 2일차 >>> 동료를 대상으로 사용자 피드백 요청, 에러 확인 - 데이터 손실 : 문법적 오류 해결, 편의성 개선을 위한 수정 - 검색 결과의 저장 요청 갯수가 페이지상에 모자랄 때 계속 진행할 지를 묻는 메시지 출력, 사용자 접근성과 정확한 데이터 관리를 위한 수정 - 페이지상의 문제로 저장되지 않은 이미지의 번호 출력, 함수 설명과 주석 추가.
> 3일차 >>> 진행중

시연 :

느낀 점, 배운 점 :
