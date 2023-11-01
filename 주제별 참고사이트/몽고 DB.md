# 몽고 DB



> ### 몽고 DB 특징 소개

- 몽고 DB 현업자가 나와서 몽고 DB의 특징 등을 유튜버분과 잘 설명해줌.
  
  - [개발자가 NoSQL 몽고DB 좋아하는 이유 [토크아이티 세미남268] - YouTube](https://youtu.be/WCzBiv-neDA?si=cmC82KfPPzNLvPJd) 
  
  - [글로벌 클라우드 서비스에 NoSQL 몽고DB 아틀라스가 좋은 5가지 이유 [토크아이티 세미남269] - YouTube](https://youtu.be/kpXA5YLkCqo?si=T1G8EGn3-Co5jBgE)
  
  - 전반적으로 좋은 영상이고, 몽고 DB 특징 파악하기 좋다.

- 몽고 DB와 MySQL 비교
  
  - [MongoDB와 MySQL 누가 더 빠를까? - YouTube](https://youtu.be/3axR2Onz1nU?si=ig3W5KgMZakEgyuf)
  
  - 결론적으로는 Update는 MySQL이 더 빠르다는 특징, 그 외적으로 대용량 데이터를 읽거나 삽입할 때에는 MongoDB가 더 좋을 확률이 높다는 결과를 알려줌.
  
  - 영상 내부에 속도 비교 실험 출처 참고해서 하면 좋을 듯
  
  - 추가적으로 다른 자료, 비교 등을 찾아보면 좋지 않을까 생각이 든다ㅏ.

- 몽고 DB Document 최대 크기가 16MB
  
  - https://velog.io/@redjen/mongodb의-16mb-악마



> ### 이를 읽으면서 생각이 든 설계 고려사항

- 현재 국회 입법 사항 저장해야할 데이터가 csv파일 기준 40mb가량 되고, 더 추가될 것으로 예상된다.
  
  - 이에, 데이터베이스의 다큐먼트 분산을 어떻게 처리해야 될 것인가에 대한 고민이 필수적이다.
  
  - 한 다큐먼트를 16MB 이상 담고 싶다면 특정 API를 사용하면 된다고 위 블로그 글에서 나와 있긴 한데, 조금 더 고려를 해봐야할 것이다.

- 데이터 스키마 설계 시에 Reference Document와 Embedded Document 방식을 사용하는데, 어떤 방식을 선택할 것인가.
  
  - 특징 비교하고 우리 서비스에 맞는 스키마 설계 방식을 가져가야할 것이다.
  
  - 해당 내용은 몽고 DB Document 최대 크기가 16MB 글에 존재한다.
  
  - - 전체 parent document의 필요 없이 대용량 데이터를 write 해야 하는 상황이라면 referenced document를 사용
    - 대부분의 데이터를 한 document에서 read 해야 하고, 그 곁다리로 관련 document가 존재한다면 embedded document를 사용
  
  - 일단 위의 내용을 바탕으로 한다면 embedded document를 사용하는 것이 옳아 보인다. 추가적으로, 해당 내용은 조금 더 조사가 필요해 보인다.

- 
