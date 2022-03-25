const clockContainer = document.querySelector(".js-clock"),
     clockTitle = clockContainer.querySelector('h1');
     clockdate = clockContainer.querySelector('h2')
//js-clock 클래스를 seletor지정 clockTile을 자식으로 지정


function getTime(){
    const date= new Date();//시계(날짜)출력 함수 값
    const week =new Array ('일','월','화','수','목','금','토');
    const minutes=date.getMinutes();//분
    const hour=date.getHours();//시간
    const seconds = date.getSeconds();//초
    const years= date.getFullYear();
    const days=date.getDate();
    const months=date.getMonth();
    const weeks = week[date.getDay()];
    clockTitle.innerText = `${hour<10 ? `0${hour}` : hour}:${minutes<10 ? `0${minutes}` : minutes}:${seconds< 10 ? `0${seconds}` : seconds}`;//?는 백쉼표(`)안에서 if를 나타냄 
    clockdate.innerText = `${years}.${months}.${days}.${weeks}`;

    //clockTitle안에 텍스트로 시간 :분:초 로 보여줘
}


function init(){
 getTime();
setInterval(getTime,1000);//setInterval(함수,밀리언초)로 실시간출력
}

init();


