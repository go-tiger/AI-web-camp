## 주제.1

html 문서 앞에 script 태그 내에 js코드를 작성했고, 문서가 로드 되기 전에 script의 element를 가져오지 못한 상태에서 console.log로 디버그하여 개발자도구에 확인해보았을때는 왜 element를 가져와졌는지 이유에 대해서 알아보기.

HTML은 인터프리터 언어이기 때문에 위에서부터 아래로 순서대로 실행된다.

참고 코드

```
<!DOCTYPE html>
<html lang=“ko”>
<head>
    <meta charset=“UTF-8">
    <title>JavaScript DOM Element</title>
    <script>
        //HTML 태그 이름을 이용한 선택
        console.log(‘aaa’)
        var selectedItem = document.getElementsByTagName(“li”);     // 모든 <li> 요소를 선택함.
        console.log(selectedItem)
        console.log(selectedItem.length)
        for (var i = 0; i < selectedItem.length; i++) {
            selectedItem.item(i).style.color = “red”;   // 선택된 모든 요소의 텍스트 색상을 변경함.
            console.log(selectedItem.item(i));
        }
    </script>
</head>
<body>
    <h1>HTML 태그 이름을 이용한 선택</h1>
    <ul>
        <li>첫 번째 아이템이에요!</li>
        <li>두 번째 아이템이에요!</li>
        <li>세 번째 아이템이에요!</li>
        <li>네 번째 아이템이에요!</li>
        <li>다섯 번째 아이템이에요!</li>
    </ul>
    <script>
        var selectedItem = document.getElementsByTagName(“li”);     // 모든 <li> 요소를 선택함.
        for (var i = 0; i < selectedItem.length; i++) {
            selectedItem.item(i).style.color = “red”;   // 선택된 모든 요소의 텍스트 색상을 변경함.
        }
    </script>
</body>
</html>
```

참고 코드를 보면 head 다음에 js 코드가 작성되어 있다.

하지만 코드를 실행하고 개발자 도구를 열어보면

![img1](https://blog.kakaocdn.net/dn/bxV5he/btso7QUEwu6/83qkfUpEmw0HRZfErpg25k/img.png)

이것 처럼 li 요소가 body 안에 있는데 불어와져 있는걸 볼 수 있다..

왜일까??

![img2](https://blog.kakaocdn.net/dn/WoMdc/btspg2lnnVS/yKGMBq2hBhQrvcMxZsDro0/img.png)

브레이크 포인트를 걸어놓고 확인해 보자

새로 고침을 해보면 js 코드에서 브레이크를 걸어놔서 body가 안나온다

![img3](https://blog.kakaocdn.net/dn/b6qZun/btspfkfIAnw/ZlJFN2kDSMOTiECklqZcsK/img.png)
![img4](https://blog.kakaocdn.net/dn/Bc28Q/btspeGpAszi/7KrnWPuDS8GUehD9Y0OXLk/img.png)

분명이 11번째 줄 지났을때 개발자 도구에서는 <body>에 있는 요소들이 출력이 안된다

하지만 getElementsByTagName 메소드는 HTMLCollection 이다.

아래 [참고 링크](https://dev.to/theoluyi/queryselector-vs-getelementsbyclassname-nodelist-vs-htmlcollection-30gg) 처럼 HTMLCollection 는 실시간으로 반영된다.

핵심 포인트는

![img5](https://blog.kakaocdn.net/dn/q9gBy/btspd3MairT/ykfD8hUK9Jlr74X7nlXAR0/img.png)

이것 처럼 body 부분 로딩이 완료 되었을때 실시간 반영되어서 selectedItem 을 가져와서 개발자 도구에 실시간 반영된다.